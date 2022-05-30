
################################################# decoders ##########################################################################
import torch
import torch.nn as nn


class BalanceCrossEntropyLoss(nn.Module):
    '''
    Balanced cross entropy loss.
    Shape:
        - Input: :math:`(N, 1, H, W)`
        - GT: :math:`(N, 1, H, W)`, same shape as the input
        - Mask: :math:`(N, H, W)`, same spatial shape as the input
        - Output: scalar.

    Examples::

        >>> m = nn.Sigmoid()
        >>> loss = nn.BCELoss()
        >>> input = torch.randn(3, requires_grad=True)
        >>> target = torch.empty(3).random_(2)
        >>> output = loss(m(input), target)
        >>> output.backward()
    '''

    def __init__(self, negative_ratio=3.0, eps=1e-6):
        super(BalanceCrossEntropyLoss, self).__init__()
        self.negative_ratio = negative_ratio
        self.eps = eps

    def forward(self,
                pred: torch.Tensor,
                gt: torch.Tensor,
                mask: torch.Tensor,
                return_origin=False):
        '''
        Args:
            pred: shape :math:`(N, 1, H, W)`, the prediction of network
            gt: shape :math:`(N, 1, H, W)`, the target
            mask: shape :math:`(N, H, W)`, the mask indicates positive regions
        '''
        positive = (gt[:,0,:,:] * mask).byte()
        negative = ((1 - gt[:,0,:,:]) * mask).byte()
        positive_count = int(positive.float().sum())
        negative_count = min(int(negative.float().sum()),
                            int(positive_count * self.negative_ratio))
        loss = nn.functional.binary_cross_entropy(
            pred, gt, reduction='none')[:, 0, :, :]
        positive_loss = loss * positive.float()
        negative_loss = loss * negative.float()
        negative_loss, _ = torch.topk(negative_loss.view(-1), negative_count)

        balance_loss = (positive_loss.sum() + negative_loss.sum()) /\
            (positive_count + negative_count + self.eps)

        if return_origin:
            return balance_loss, loss
        return balance_loss

import torch
import torch.nn as nn
import numpy as np
import cv2
from scipy import ndimage


class DiceLoss(nn.Module):
    '''
    Loss function from https://arxiv.org/abs/1707.03237,
    where iou computation is introduced heatmap manner to measure the
    diversity bwtween tow heatmaps.
    '''
    def __init__(self, eps=1e-6):
        super(DiceLoss, self).__init__()
        self.eps = eps

    def forward(self, pred: torch.Tensor, gt, mask, weights=None):
        '''
        pred: one or two heatmaps of shape (N, 1, H, W),
            the losses of tow heatmaps are added together.
        gt: (N, 1, H, W)
        mask: (N, H, W)
        '''
        assert pred.dim() == 4, pred.dim()
        return self._compute(pred, gt, mask, weights)

    def _compute(self, pred, gt, mask, weights):
        if pred.dim() == 4:
            pred = pred[:, 0, :, :]
            gt = gt[:, 0, :, :]
        assert pred.shape == gt.shape
        assert pred.shape == mask.shape
        if weights is not None:
            assert weights.shape == mask.shape
            mask = weights * mask

        intersection = (pred * gt * mask).sum()
        union = (pred * mask).sum() + (gt * mask).sum() + self.eps
        loss = 1 - 2.0 * intersection / union
        assert loss <= 1
        return loss


class LeakyDiceLoss(nn.Module):
    '''
    Variation from DiceLoss.
    The coverage and union are computed separately.
    '''
    def __init__(self, eps=1e-6, coverage_scale=5.0):
        super(LeakyDiceLoss, self).__init__()
        self.eps = eps
        self.coverage_scale = coverage_scale

    def forward(self, pred, gt, mask):
        if pred.dim() == 4:
            pred = pred[:, 0, :, :]
            gt = gt[:, 0, :, :]
        assert pred.shape == gt.shape
        assert pred.shape == mask.shape

        coverage = (pred * mask * gt).sum() / ((gt * mask).sum() + self.eps)
        assert coverage <= 1
        coverage = 1 - coverage
        excede = (pred * mask * gt).sum() / ((pred * mask).sum() + self.eps)
        assert excede <= 1
        excede = 1 - excede
        loss = coverage * self.coverage_scale + excede
        return loss, dict(coverage=coverage, excede=excede)


class InstanceDiceLoss(DiceLoss):
    '''
    DiceLoss normalized on each instance.
    Input:
        pred: (N, 1, H, W)
        gt: (N, 1, H, W)
        mask: (N, H, W)
    Note: This class assume that input tensors are on gpu,
        while cput computation is required to find union areas.
    '''
    REDUCTION = ['mean', 'sum', 'none']

    def __init__(self, threshold=0.3, iou_thresh=0.2, reduction=None,
                 max_regions=100, eps=1e-6):
        nn.Module.__init__(self)
        self.threshold = threshold
        self.iou_thresh = iou_thresh
        self.reduction = reduction
        if self.reduction is None:
            self.reduction = 'mean'
        assert self.reduction in self.REDUCTION
        self.max_regions = max_regions
        self.eps = eps

    def label(self, tensor_on_gpu, blur=None):
        '''
        Args:
            tensor_on_gpu: (N, 1, H, W)
            blur: Lambda. If exists, each instance will be blured using `blur`.
        '''
        tensor = tensor_on_gpu.cpu().detach().numpy()

        instance_maps = []
        instance_counts = []
        for batch_index in range(tensor_on_gpu.shape[0]):
            instance = tensor[batch_index]
            if blur is not None:
                instance = blur(instance)
            lable_map, instance_count = ndimage.label(instance[0])
            instance_count = min(self.max_regions, instance_count)
            instance_map = []
            for index in range(1, instance_count):
                instance = torch.from_numpy(
                        lable_map == index).to(tensor_on_gpu.device).type(torch.float32)
                instance_map.append(instance)
            instance_maps.append(instance_map)
        return instance_maps, instance_counts

    def iou(self, pred, gt):
        overlap = (pred * gt).sum()
        return max(overlap / pred.sum(), overlap / gt.sum())

    def replace_or_add(self, dest, value):
        if dest is None:
            return value
        if value is None:
            return dest
        return dest + value

    def forward(self, pred, gt, mask):
        # pred_label_maps: N, P, H, W, where P is the number of regions.
        torch.cuda.synchronize()
        pred_label_maps, _ = self.label(pred > self.threshold)
        gt_label_maps, _ = self.label(gt)

        losses = []
        for batch_index, gt_instance_maps in enumerate(gt_label_maps):
            pred_instance_maps = pred_label_maps[batch_index]
            if gt_instance_maps is None or pred_instance_maps is None:
                continue

            single_loss = None  # loss on a single image in a batch
            mask_not_matched = set(range(len(pred_instance_maps)))
            for gt_instance_map in gt_instance_maps:
                instance_loss = None  # loss on a specific gt region
                for instance_index, pred_instance_map in enumerate(pred_instance_maps):
                    if self.iou(pred_instance_map, gt_instance_map) > self.iou_thresh:
                        match_loss = self._compute(
                                pred[batch_index][0], gt[batch_index][0],
                                mask[batch_index] * (pred_instance_map + gt_instance_map > 0).type(torch.float32))
                        instance_loss = self.replace_or_add(instance_loss, match_loss)
                        if instance_index in mask_not_matched:
                            mask_not_matched.remove(instance_index)
                if instance_loss is None:
                    instance_loss = self._compute(
                            pred[batch_index][0], gt[batch_index][0],
                            mask[batch_index] * gt_instance_map)
                single_loss = self.replace_or_add(single_loss, instance_loss)

            '''Whether to compute single loss on instances which contrain no positive sample.
            if single_loss is None:
                single_loss = self._compute(
                        pred[batch_index][0], gt[batch_index][0],
                        mask[batch_index])
            '''

            for instance_index in mask_not_matched:
                single_loss = self.replace_or_add(
                        single_loss,
                        self._compute(
                            pred[batch_index][0], gt[batch_index][0],
                            mask[batch_index] * pred_instance_maps[instance_index]))

            if single_loss is not None:
                losses.append(single_loss)

        if self.reduction == 'none':
            loss = losses
        else:
            assert self.reduction in ['sum', 'mean']
            count = len(losses)
            loss = sum(losses)
            if self.reduction == 'mean':
                loss = loss / count
        return loss


import torch
import torch.nn as nn


class MaskL1Loss(nn.Module):
    def __init__(self):
        super(MaskL1Loss, self).__init__()

    def forward(self, pred: torch.Tensor, gt, mask):
        mask_sum = mask.sum()
        if mask_sum.item() == 0:
            return mask_sum, dict(l1_loss=mask_sum)
        else:
            loss = (torch.abs(pred[:, 0] - gt) * mask).sum() / mask_sum
            return loss, dict(l1_loss=loss)


class BalanceL1Loss(nn.Module):
    def __init__(self, negative_ratio=3.):
        super(BalanceL1Loss, self).__init__()
        self.negative_ratio = negative_ratio

    def forward(self, pred: torch.Tensor, gt, mask):
        '''
        Args:
            pred: (N, 1, H, W).
            gt: (N, H, W).
            mask: (N, H, W).
        '''
        loss = torch.abs(pred[:, 0] - gt)
        positive = loss * mask
        negative = loss * (1 - mask)
        positive_count = int(mask.sum())
        negative_count = min(
                int((1 - mask).sum()),
                int(positive_count * self.negative_ratio))
        negative_loss, _ = torch.topk(negative.view(-1), negative_count)
        negative_loss = negative_loss.sum() / negative_count
        positive_loss = positive.sum() / positive_count
        return positive_loss + negative_loss,\
            dict(l1_loss=positive_loss, nge_l1_loss=negative_loss)


import torch
import torch.nn as nn
import torch.nn.functional as F

class PSS_Loss(nn.Module):

    def __init__(self, cls_loss):
        super(PSS_Loss, self).__init__()
        self.eps = 1e-6
        self.criterion = eval('self.' + cls_loss + '_loss')

    def dice_loss(self, pred, gt, m):
        intersection = torch.sum(pred*gt*m)
        union = torch.sum(pred*m) + torch.sum(gt*m) + self.eps
        loss = 1 - 2.0*intersection/union
        if loss > 1:
            print(intersection, union)
        return loss

    def dice_ohnm_loss(self, pred, gt, m):
        pos_index = (gt == 1) * (m == 1)
        neg_index = (gt == 0) * (m == 1)
        pos_num = pos_index.float().sum().item()
        neg_num = neg_index.float().sum().item()
        if pos_num == 0 or neg_num < pos_num*3.0:
            return self.dice_loss(pred, gt, m)
        else:
            neg_num = int(pos_num*3)
            pos_pred = pred[pos_index]
            neg_pred = pred[neg_index]
            neg_sort, _ = torch.sort(neg_pred, descending=True)
            sampled_neg_pred = neg_sort[:neg_num]
            pos_gt = pos_pred.clone()
            pos_gt.data.fill_(1.0)
            pos_gt = pos_gt.detach()
            neg_gt = sampled_neg_pred.clone()
            neg_gt.data.fill_(0)
            neg_gt = neg_gt.detach()
            tpred = torch.cat((pos_pred, sampled_neg_pred))
            tgt = torch.cat((pos_gt, neg_gt))
            intersection = torch.sum(tpred * tgt)
            union = torch.sum(tpred) + torch.sum(gt) + self.eps
            loss = 1 - 2.0 * intersection / union
        return loss

    def focal_loss(self, pred, gt, m, alpha=0.25, gamma=0.6):
        pos_mask = (gt == 1).float()
        neg_mask = (gt == 0).float()
        mask = alpha*pos_mask * \
            torch.pow(1-pred.data, gamma)+(1-alpha) * \
            neg_mask*torch.pow(pred.data, gamma)
        l = F.binary_cross_entropy(pred, gt, weight=mask, reduction='none')
        loss = torch.sum(l*m)/(self.eps+m.sum())
        loss *= 10
        return loss

    def wbce_orig_loss(self, pred, gt, m):
        n, h, w = pred.size()
        assert (torch.max(gt) == 1)
        pos_neg_p = pred[m.byte()]
        pos_neg_t = gt[m.byte()]
        pos_mask = (pos_neg_t == 1).squeeze()
        w = pos_mask.float() * (1 - pos_mask).sum().item() + \
            (1 - pos_mask).float() * pos_mask.sum().item()
        w = w / (pos_mask.size(0))
        loss = F.binary_cross_entropy(pos_neg_p, pos_neg_t, w, reduction='sum')
        return loss

    def wbce_loss(self, pred, gt, m):
        pos_mask = (gt == 1).float()*m
        neg_mask = (gt == 0).float()*m
        # mask=(pos_mask*neg_mask.sum()+neg_mask*pos_mask.sum())/m.sum()
        # loss=torch.sum(l)
        mask = pos_mask * neg_mask.sum() / pos_mask.sum() + neg_mask
        l = F.binary_cross_entropy(pred, gt, weight=mask, reduction='none')
        loss = torch.sum(l)/(m.sum()+self.eps)
        return loss

    def bce_loss(self, pred, gt, m):
        l = F.binary_cross_entropy(pred, gt, weight=m, reduction='sum')
        loss = l/(m.sum()+self.eps)
        return loss

    def dice_bce_loss(self, pred, gt, m):
        return (self.dice_loss(pred, gt, m) + self.bce_loss(pred, gt, m)) / 2.0

    def dice_ohnm_bce_loss(self, pred, gt, m):
        return (self.dice_ohnm_loss(pred, gt, m) + self.bce_loss(pred, gt, m)) / 2.0

    def forward(self, pred, gt, mask, gt_type='shrink'):
        if gt_type == 'shrink':
            loss = self.get_loss(pred, gt, mask)
            return loss
        elif gt_type == 'pss':
            loss = self.get_loss(pred, gt[:, :4, :, :], mask)
            g_g = gt[:, 4, :, :]
            g_p, _ = torch.max(pred, 1)
            loss += self.criterion(g_p, g_g, mask)
            return loss
        elif gt_type == 'both':
            pss_loss = self.get_loss(pred[:, :4, :, :], gt[:, :4, :, :], mask)
            g_g = gt[:, 4, :, :]
            g_p, _ = torch.max(pred, 1)
            pss_loss += self.criterion(g_p, g_g, mask)
            shrink_loss = self.criterion(
                pred[:, 4, :, :], gt[:, 5, :, :], mask)
            return pss_loss, shrink_loss
        else:
            return NotImplementedError('gt_type [%s] is not implemented', gt_type)

    def get_loss(self, pred, gt, mask):
        loss = torch.tensor(0.)
        for ind in range(pred.size(1)):
            loss += self.criterion(pred[:, ind, :, :], gt[:, ind, :, :], mask)
        return loss


import torch
import torch.nn as nn
import torch.nn.functional as F

class ScaleChannelAttention(nn.Module):
    def __init__(self, in_planes, out_planes, num_features, init_weight=True):
        super(ScaleChannelAttention, self).__init__()
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        print(self.avgpool)
        self.fc1 = nn.Conv2d(in_planes, out_planes, 1, bias=False)
        self.bn = nn.BatchNorm2d(out_planes)
        self.fc2 = nn.Conv2d(out_planes, num_features, 1, bias=False)
        if init_weight:
            self._initialize_weights()

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            if isinstance(m ,nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, x):
        global_x = self.avgpool(x)
        global_x = self.fc1(global_x)
        global_x = F.relu(self.bn(global_x))
        global_x = self.fc2(global_x)
        global_x = F.softmax(global_x, 1)
        return global_x

class ScaleChannelSpatialAttention(nn.Module):
    def __init__(self, in_planes, out_planes, num_features, init_weight=True):
        super(ScaleChannelSpatialAttention, self).__init__()
        self.channel_wise = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(in_planes, out_planes , 1, bias=False),
            # nn.BatchNorm2d(out_planes),
            nn.ReLU(),
            nn.Conv2d(out_planes, in_planes, 1, bias=False)
        )
        self.spatial_wise = nn.Sequential(
            #Nx1xHxW
            nn.Conv2d(1, 1, 3, bias=False, padding=1),
            nn.ReLU(),
            nn.Conv2d(1, 1, 1, bias=False),
            nn.Sigmoid()
        )
        self.attention_wise = nn.Sequential(
            nn.Conv2d(in_planes, num_features, 1, bias=False),
            nn.Sigmoid()
        )
        if init_weight:
            self._initialize_weights()

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            if isinstance(m ,nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, x):
        # global_x = self.avgpool(x)
        #shape Nx4x1x1
        global_x = self.channel_wise(x).sigmoid()
        #shape: NxCxHxW
        global_x = global_x + x
        #shape:Nx1xHxW
        x = torch.mean(global_x, dim=1, keepdim=True)
        global_x = self.spatial_wise(x) + global_x
        global_x = self.attention_wise(global_x)
        return global_x

class ScaleSpatialAttention(nn.Module):
    def __init__(self, in_planes, out_planes, num_features, init_weight=True):
        super(ScaleSpatialAttention, self).__init__()
        self.spatial_wise = nn.Sequential(
            #Nx1xHxW
            nn.Conv2d(1, 1, 3, bias=False, padding=1),
            nn.ReLU(),
            nn.Conv2d(1, 1, 1, bias=False),
            nn.Sigmoid() 
        )
        self.attention_wise = nn.Sequential(
            nn.Conv2d(in_planes, num_features, 1, bias=False),
            nn.Sigmoid()
        )
        if init_weight:
            self._initialize_weights()

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            if isinstance(m ,nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, x):
        global_x = torch.mean(x, dim=1, keepdim=True)
        global_x = self.spatial_wise(global_x) + x
        global_x = self.attention_wise(global_x)
        return global_x

class ScaleFeatureSelection(nn.Module):
    def __init__(self, in_channels, inter_channels , out_features_num=4, attention_type='scale_spatial'):
        super(ScaleFeatureSelection, self).__init__()
        self.in_channels=in_channels
        self.inter_channels = inter_channels
        self.out_features_num = out_features_num
        self.conv = nn.Conv2d(in_channels, inter_channels, 3, padding=1)
        self.type = attention_type
        if self.type == 'scale_spatial':
            self.enhanced_attention = ScaleSpatialAttention(inter_channels, inter_channels//4, out_features_num)
        elif self.type == 'scale_channel_spatial':
            self.enhanced_attention = ScaleChannelSpatialAttention(inter_channels, inter_channels // 4, out_features_num)
        elif self.type == 'scale_channel':
            self.enhanced_attention = ScaleChannelAttention(inter_channels, inter_channels//2, out_features_num)

    def _initialize_weights(self, m):
        classname = m.__class__.__name__
        if classname.find('Conv') != -1:
            nn.init.kaiming_normal_(m.weight.data)
        elif classname.find('BatchNorm') != -1:
            m.weight.data.fill_(1.)
            m.bias.data.fill_(1e-4)
    def forward(self, concat_x, features_list):
        concat_x = self.conv(concat_x)
        score = self.enhanced_attention(concat_x)
        assert len(features_list) == self.out_features_num
        if self.type not in ['scale_channel_spatial', 'scale_spatial']:
            shape = features_list[0].shape[2:]
            score = F.interpolate(score, size=shape, mode='bilinear')
        x = []
        for i in range(self.out_features_num):
            x.append(score[:, i:i+1] * features_list[i])
        return torch.cat(x, dim=1)


from collections import OrderedDict
import pdb
import torch
import torch.nn as nn
# from .feature_attention import ScaleFeatureSelection
BatchNorm2d = nn.BatchNorm2d


class SegSpatialScaleDetector(nn.Module):
    def __init__(self,
                 in_channels=[64, 128, 256, 512],
                 inner_channels=256, k=10,
                 bias=False, adaptive=False, smooth=False, serial=False,fpn=True, attention_type='scale_spatial',
                 *args, **kwargs):
        '''
        bias: Whether conv layers have bias or not.
        adaptive: Whether to use adaptive threshold training or not.
        smooth: If true, use bilinear instead of deconv.
        serial: If true, thresh prediction will combine segmentation result as input.
        '''
        super(SegSpatialScaleDetector, self).__init__()
        self.k = k
        self.serial = serial
        self.fpn = fpn
        self.up5 = nn.Upsample(scale_factor=2, mode='nearest')
        self.up4 = nn.Upsample(scale_factor=2, mode='nearest')
        self.up3 = nn.Upsample(scale_factor=2, mode='nearest')

        self.in5 = nn.Conv2d(in_channels[-1], inner_channels, 1, bias=bias)
        self.in4 = nn.Conv2d(in_channels[-2], inner_channels, 1, bias=bias)
        self.in3 = nn.Conv2d(in_channels[-3], inner_channels, 1, bias=bias)
        self.in2 = nn.Conv2d(in_channels[-4], inner_channels, 1, bias=bias)

        if self.fpn:
            self.out5 = nn.Sequential(
                nn.Conv2d(inner_channels, inner_channels // 4, 3, padding=1, bias=bias),
                nn.Upsample(scale_factor=8, mode='nearest'))
            self.out4 = nn.Sequential(
                nn.Conv2d(inner_channels, inner_channels // 4, 3, padding=1, bias=bias),
                nn.Upsample(scale_factor=4, mode='nearest'))
            self.out3 = nn.Sequential(
                nn.Conv2d(inner_channels, inner_channels // 4, 3, padding=1, bias=bias),
                nn.Upsample(scale_factor=2, mode='nearest'))
            self.out2 = nn.Conv2d(inner_channels, inner_channels//4, 3, padding=1, bias=bias)
            self.out5.apply(self.weights_init)
            self.out4.apply(self.weights_init)
            self.out3.apply(self.weights_init)
            self.out2.apply(self.weights_init)

            self.concat_attention = ScaleFeatureSelection(inner_channels, inner_channels//4, attention_type=attention_type)
            self.binarize = nn.Sequential(
                nn.Conv2d(inner_channels, inner_channels // 4, 3, bias=bias, padding=1),
                BatchNorm2d(inner_channels//4),
                nn.ReLU(inplace=True),
                nn.ConvTranspose2d(inner_channels//4, inner_channels//4, 2, 2),
                BatchNorm2d(inner_channels//4),
                nn.ReLU(inplace=True),
                nn.ConvTranspose2d(inner_channels//4, 1, 2, 2),
                nn.Sigmoid())
        else:
            self.concat_attention = ScaleFeatureSelection(inner_channels, inner_channels//4, )
            self.binarize = nn.Sequential(
                nn.Conv2d(inner_channels, inner_channels // 4, 3, bias=bias, padding=1),
                BatchNorm2d(inner_channels//4),
                nn.ReLU(inplace=True),
                nn.ConvTranspose2d(inner_channels//4, inner_channels//4, 2, 2),
                BatchNorm2d(inner_channels//4),
                nn.ReLU(inplace=True),
                nn.ConvTranspose2d(inner_channels//4, 1, 2, 2),
                nn.Sigmoid())

        self.binarize.apply(self.weights_init)
        self.adaptive = adaptive
        if adaptive:
            self.thresh = self._init_thresh(
                    inner_channels, serial=serial, smooth=smooth, bias=bias)
            self.thresh.apply(self.weights_init)

        self.in5.apply(self.weights_init)
        self.in4.apply(self.weights_init)
        self.in3.apply(self.weights_init)
        self.in2.apply(self.weights_init)

    def weights_init(self, m):
        classname = m.__class__.__name__
        if classname.find('Conv') != -1:
            nn.init.kaiming_normal_(m.weight.data)
        elif classname.find('BatchNorm') != -1:
            m.weight.data.fill_(1.)
            m.bias.data.fill_(1e-4)

    def _init_thresh(self, inner_channels,
                     serial=False, smooth=False, bias=False):
        in_channels = inner_channels
        if serial:
            in_channels += 1
        self.thresh = nn.Sequential(
            nn.Conv2d(in_channels, inner_channels //
                      4, 3, padding=1, bias=bias),
            BatchNorm2d(inner_channels//4),
            nn.ReLU(inplace=True),
            self._init_upsample(inner_channels // 4, inner_channels//4, smooth=smooth, bias=bias),
            BatchNorm2d(inner_channels//4),
            nn.ReLU(inplace=True),
            self._init_upsample(inner_channels // 4, 1, smooth=smooth, bias=bias),
            nn.Sigmoid())
        return self.thresh

    def _init_upsample(self,
                       in_channels, out_channels,
                       smooth=False, bias=False):
        if smooth:
            inter_out_channels = out_channels
            if out_channels == 1:
                inter_out_channels = in_channels
            module_list = [
                    nn.Upsample(scale_factor=2, mode='nearest'),
                    nn.Conv2d(in_channels, inter_out_channels, 3, 1, 1, bias=bias)]
            if out_channels == 1:
                module_list.append(
                    nn.Conv2d(in_channels, out_channels,
                              kernel_size=1, stride=1, padding=1, bias=True))

            return nn.Sequential(module_list)
        else:
            return nn.ConvTranspose2d(in_channels, out_channels, 2, 2)

    def forward(self, features, gt=None, masks=None, training=False):
        c2, c3, c4, c5 = features
        in5 = self.in5(c5)
        in4 = self.in4(c4)
        in3 = self.in3(c3)
        in2 = self.in2(c2)

        out4 = self.up5(in5) + in4  # 1/16
        out3 = self.up4(out4) + in3  # 1/8
        out2 = self.up3(out3) + in2  # 1/4
        p5 = self.out5(in5)
        p4 = self.out4(out4)
        p3 = self.out3(out3)
        p2 = self.out2(out2)

        fuse = torch.cat((p5, p4, p3, p2), 1)
        fuse = self.concat_attention(fuse, [p5, p4, p3, p2])
        # this is the pred module, not binarization module; 
        # We do not correct the name due to the trained model.
        binary = self.binarize(fuse)
        if self.training:
            result = OrderedDict(binary=binary)
        else:
            return binary
        if self.adaptive and self.training:
            if self.serial:
                fuse = torch.cat(
                        (fuse, nn.functional.interpolate(
                            binary, fuse.shape[2:])), 1)
            thresh = self.thresh(fuse)
            thresh_binary = self.step_function(binary, thresh)
            result.update(thresh=thresh, thresh_binary=thresh_binary)
        return result

    def step_function(self, x, y):
        return torch.reciprocal(1 + torch.exp(-self.k * (x - y)))

if __name__ == "__main__":
    print('hi,,,')