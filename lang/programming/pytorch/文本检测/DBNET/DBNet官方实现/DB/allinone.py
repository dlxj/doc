
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


import sys

import torch
import torch.nn as nn


class SegDetectorLossBuilder():
    '''
    Build loss functions for SegDetector.
    Details about the built functions:
        Input:
            pred: A dict which contains predictions.
                thresh: The threshold prediction
                binary: The text segmentation prediction.
                thresh_binary: Value produced by `step_function(binary - thresh)`.
            batch:
                gt: Text regions bitmap gt.
                mask: Ignore mask,
                    pexels where value is 1 indicates no contribution to loss.
                thresh_mask: Mask indicates regions cared by thresh supervision.
                thresh_map: Threshold gt.
        Return:
            (loss, metrics).
            loss: A scalar loss value.
            metrics: A dict contraining partial loss values.
    '''

    def __init__(self, loss_class, *args, **kwargs):
        self.loss_class = loss_class
        self.loss_args = args
        self.loss_kwargs = kwargs

    def build(self):
        return getattr(sys.modules[__name__], self.loss_class)(*self.loss_args, **self.loss_kwargs)


class DiceLoss(nn.Module):
    '''
    DiceLoss on binary.
    For SegDetector without adaptive module.
    '''

    def __init__(self, eps=1e-6):
        super(DiceLoss, self).__init__()
        # from .dice_loss import DiceLoss as Loss
        self.loss = DiceLoss(eps)

    def forward(self, pred, batch):
        loss = self.loss(pred['binary'], batch['gt'], batch['mask'])
        return loss, dict(dice_loss=loss)


class BalanceBCELoss(nn.Module):
    '''
    DiceLoss on binary.
    For SegDetector without adaptive module.
    '''

    def __init__(self, eps=1e-6):
        super(BalanceBCELoss, self).__init__()
        from .balance_cross_entropy_loss import BalanceCrossEntropyLoss
        self.loss = BalanceCrossEntropyLoss()

    def forward(self, pred, batch):
        loss = self.loss(pred['binary'], batch['gt'], batch['mask'])
        return loss, dict(dice_loss=loss)


class AdaptiveDiceLoss(nn.Module):
    '''
    Integration of DiceLoss on both binary
        prediction and thresh prediction.
    '''

    def __init__(self, eps=1e-6):
        super(AdaptiveDiceLoss, self).__init__()
        from .dice_loss import DiceLoss
        self.main_loss = DiceLoss(eps)
        self.thresh_loss = DiceLoss(eps)

    def forward(self, pred, batch):
        assert isinstance(pred, dict)
        assert 'binary' in pred
        assert 'thresh_binary' in pred

        binary = pred['binary']
        thresh_binary = pred['thresh_binary']
        gt = batch['gt']
        mask = batch['mask']
        main_loss = self.main_loss(binary, gt, mask)
        thresh_loss = self.thresh_loss(thresh_binary, gt, mask)
        loss = main_loss + thresh_loss
        return loss, dict(main_loss=main_loss, thresh_loss=thresh_loss)


class AdaptiveInstanceDiceLoss(nn.Module):
    '''
    InstanceDiceLoss on both binary and thresh_bianry.
    '''

    def __init__(self, iou_thresh=0.2, thresh=0.3):
        super(AdaptiveInstanceDiceLoss, self).__init__()
        from .dice_loss import InstanceDiceLoss, DiceLoss
        self.main_loss = DiceLoss()
        self.main_instance_loss = InstanceDiceLoss()
        self.thresh_loss = DiceLoss()
        self.thresh_instance_loss = InstanceDiceLoss()
        self.weights = nn.ParameterDict(dict(
            main=nn.Parameter(torch.ones(1)),
            thresh=nn.Parameter(torch.ones(1)),
            main_instance=nn.Parameter(torch.ones(1)),
            thresh_instance=nn.Parameter(torch.ones(1))))

    def partial_loss(self, weight, loss):
        return loss / weight + torch.log(torch.sqrt(weight))

    def forward(self, pred, batch):
        main_loss = self.main_loss(pred['binary'], batch['gt'], batch['mask'])
        thresh_loss = self.thresh_loss(pred['thresh_binary'], batch['gt'], batch['mask'])
        main_instance_loss = self.main_instance_loss(
            pred['binary'], batch['gt'], batch['mask'])
        thresh_instance_loss = self.thresh_instance_loss(
            pred['thresh_binary'], batch['gt'], batch['mask'])
        loss = self.partial_loss(self.weights['main'], main_loss) \
               + self.partial_loss(self.weights['thresh'], thresh_loss) \
               + self.partial_loss(self.weights['main_instance'], main_instance_loss) \
               + self.partial_loss(self.weights['thresh_instance'], thresh_instance_loss)
        metrics = dict(
            main_loss=main_loss,
            thresh_loss=thresh_loss,
            main_instance_loss=main_instance_loss,
            thresh_instance_loss=thresh_instance_loss)
        metrics.update(self.weights)
        return loss, metrics


class L1DiceLoss(nn.Module):
    '''
    L1Loss on thresh, DiceLoss on thresh_binary and binary.
    '''

    def __init__(self, eps=1e-6, l1_scale=10):
        super(L1DiceLoss, self).__init__()
        self.dice_loss = AdaptiveDiceLoss(eps=eps)
        from .l1_loss import MaskL1Loss
        self.l1_loss = MaskL1Loss()
        self.l1_scale = l1_scale

    def forward(self, pred, batch):
        dice_loss, metrics = self.dice_loss(pred, batch)
        l1_loss, l1_metric = self.l1_loss(
            pred['thresh'], batch['thresh_map'], batch['thresh_mask'])

        loss = dice_loss + self.l1_scale * l1_loss
        metrics.update(**l1_metric)
        return loss, metrics


class FullL1DiceLoss(L1DiceLoss):
    '''
    L1loss on thresh, pixels with topk losses in non-text regions are also counted.
    DiceLoss on thresh_binary and binary.
    '''

    def __init__(self, eps=1e-6, l1_scale=10):
        nn.Module.__init__(self)
        self.dice_loss = AdaptiveDiceLoss(eps=eps)
        from .l1_loss import BalanceL1Loss
        self.l1_loss = BalanceL1Loss()
        self.l1_scale = l1_scale


class L1BalanceCELoss(nn.Module):
    '''
    Balanced CrossEntropy Loss on `binary`,
    MaskL1Loss on `thresh`,
    DiceLoss on `thresh_binary`.
    Note: The meaning of inputs can be figured out in `SegDetectorLossBuilder`.
    '''

    def __init__(self, eps=1e-6, l1_scale=10, bce_scale=5):
        super(L1BalanceCELoss, self).__init__()
        from .dice_loss import DiceLoss
        from .l1_loss import MaskL1Loss
        from .balance_cross_entropy_loss import BalanceCrossEntropyLoss
        self.dice_loss = DiceLoss(eps=eps)
        self.l1_loss = MaskL1Loss()
        self.bce_loss = BalanceCrossEntropyLoss()

        self.l1_scale = l1_scale
        self.bce_scale = bce_scale

    def forward(self, pred, batch):
        bce_loss = self.bce_loss(pred['binary'], batch['gt'], batch['mask'])
        metrics = dict(bce_loss=bce_loss)
        if 'thresh' in pred:
            l1_loss, l1_metric = self.l1_loss(pred['thresh'], batch['thresh_map'], batch['thresh_mask'])
            dice_loss = self.dice_loss(pred['thresh_binary'], batch['gt'], batch['mask'])
            metrics['thresh_loss'] = dice_loss
            loss = dice_loss + self.l1_scale * l1_loss + bce_loss * self.bce_scale
            metrics.update(**l1_metric)
        else:
            loss = bce_loss
        return loss, metrics


class L1BCEMiningLoss(nn.Module):
    '''
    Basicly the same with L1BalanceCELoss, where the bce loss map is used as
        attention weigts for DiceLoss
    '''

    def __init__(self, eps=1e-6, l1_scale=10, bce_scale=5):
        super(L1BCEMiningLoss, self).__init__()
        from .dice_loss import DiceLoss
        from .l1_loss import MaskL1Loss
        from .balance_cross_entropy_loss import BalanceCrossEntropyLoss
        self.dice_loss = DiceLoss(eps=eps)
        self.l1_loss = MaskL1Loss()
        self.bce_loss = BalanceCrossEntropyLoss()

        self.l1_scale = l1_scale
        self.bce_scale = bce_scale

    def forward(self, pred, batch):
        bce_loss, bce_map = self.bce_loss(pred['binary'], batch['gt'], batch['mask'],
                                          return_origin=True)
        l1_loss, l1_metric = self.l1_loss(pred['thresh'], batch['thresh_map'], batch['thresh_mask'])
        bce_map = (bce_map - bce_map.min()) / (bce_map.max() - bce_map.min())
        dice_loss = self.dice_loss(
            pred['thresh_binary'], batch['gt'],
            batch['mask'], weights=bce_map + 1)
        metrics = dict(bce_loss=bce_loss)
        metrics['thresh_loss'] = dice_loss
        loss = dice_loss + self.l1_scale * l1_loss + bce_loss * self.bce_scale
        metrics.update(**l1_metric)
        return loss, metrics


class L1LeakyDiceLoss(nn.Module):
    '''
    LeakyDiceLoss on binary,
    MaskL1Loss on thresh,
    DiceLoss on thresh_binary.
    '''

    def __init__(self, eps=1e-6, coverage_scale=5, l1_scale=10):
        super(L1LeakyDiceLoss, self).__init__()
        from .dice_loss import DiceLoss, LeakyDiceLoss
        from .l1_loss import MaskL1Loss
        self.main_loss = LeakyDiceLoss(coverage_scale=coverage_scale)
        self.l1_loss = MaskL1Loss()
        self.thresh_loss = DiceLoss(eps=eps)

        self.l1_scale = l1_scale

    def forward(self, pred, batch):
        main_loss, metrics = self.main_loss(pred['binary'], batch['gt'], batch['mask'])
        thresh_loss = self.thresh_loss(pred['thresh_binary'], batch['gt'], batch['mask'])
        l1_loss, l1_metric = self.l1_loss(
            pred['thresh'], batch['thresh_map'], batch['thresh_mask'])
        metrics.update(**l1_metric, thresh_loss=thresh_loss)
        loss = main_loss + thresh_loss + l1_loss * self.l1_scale
        return loss, metrics


from collections import OrderedDict

import torch
import torch.nn as nn
BatchNorm2d = nn.BatchNorm2d

class SegDetector(nn.Module):
    def __init__(self,
                 in_channels=[64, 128, 256, 512],
                 inner_channels=256, k=10,
                 bias=False, adaptive=False, smooth=False, serial=False,
                 *args, **kwargs):
        '''
        bias: Whether conv layers have bias or not.
        adaptive: Whether to use adaptive threshold training or not.
        smooth: If true, use bilinear instead of deconv.
        serial: If true, thresh prediction will combine segmentation result as input.
        '''
        super(SegDetector, self).__init__()
        self.k = k
        self.serial = serial
        self.up5 = nn.Upsample(scale_factor=2, mode='nearest')
        self.up4 = nn.Upsample(scale_factor=2, mode='nearest')
        self.up3 = nn.Upsample(scale_factor=2, mode='nearest')

        self.in5 = nn.Conv2d(in_channels[-1], inner_channels, 1, bias=bias)
        self.in4 = nn.Conv2d(in_channels[-2], inner_channels, 1, bias=bias)
        self.in3 = nn.Conv2d(in_channels[-3], inner_channels, 1, bias=bias)
        self.in2 = nn.Conv2d(in_channels[-4], inner_channels, 1, bias=bias)

        self.out5 = nn.Sequential(
            nn.Conv2d(inner_channels, inner_channels //
                      4, 3, padding=1, bias=bias),
            nn.Upsample(scale_factor=8, mode='nearest'))
        self.out4 = nn.Sequential(
            nn.Conv2d(inner_channels, inner_channels //
                      4, 3, padding=1, bias=bias),
            nn.Upsample(scale_factor=4, mode='nearest'))
        self.out3 = nn.Sequential(
            nn.Conv2d(inner_channels, inner_channels //
                      4, 3, padding=1, bias=bias),
            nn.Upsample(scale_factor=2, mode='nearest'))
        self.out2 = nn.Conv2d(
            inner_channels, inner_channels//4, 3, padding=1, bias=bias)

        self.binarize = nn.Sequential(
            nn.Conv2d(inner_channels, inner_channels //
                      4, 3, padding=1, bias=bias),
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
        self.out5.apply(self.weights_init)
        self.out4.apply(self.weights_init)
        self.out3.apply(self.weights_init)
        self.out2.apply(self.weights_init)

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


import torch
import torch.nn as nn
import torch.nn.functional as F


#from backbones.upsample_head import SimpleUpsampleHead
SimpleUpsampleHead = None

class SimpleDetectionDecoder(nn.Module):
    def __init__(self, feature_channel=256):
        nn.Module.__init__(self)

        self.feature_channel = feature_channel
        self.head_layer = self.create_head_layer()

        self.pred_layers = nn.ModuleDict(self.create_pred_layers())

    def create_head_layer(self):
        return SimpleUpsampleHead(
            self.feature_channel,
            [self.feature_channel, self.feature_channel // 2, self.feature_channel // 4]
        )

    def create_pred_layer(self, channels):
        return nn.Sequential(
            nn.Conv2d(self.feature_channel // 4, channels, kernel_size=1, stride=1, padding=0, bias=False),
        )

    def create_pred_layers(self):
        return {}

    def postprocess_pred(self, pred):
        return pred

    def calculate_losses(self, preds, label):
        raise NotImplementedError()

    def forward(self, input, label, meta, train):
        feature = self.head_layer(input)

        pred = {}
        for name, pred_layer in self.pred_layers.items():
            pred[name] = pred_layer(feature)

        if train:
            losses = self.calculate_losses(pred, label)
            pred = self.postprocess_pred(pred)
            loss = sum(losses.values())
            return loss, pred, losses
        else:
            pred = self.postprocess_pred(pred)
            return pred


class SimpleSegDecoder(SimpleDetectionDecoder):
    def create_pred_layers(self):
        return {
            'heatmap': self.create_pred_layer(1)
        }

    def postprocess_pred(self, pred):
        pred['heatmap'] = F.sigmoid(pred['heatmap'])
        return pred

    def calculate_losses(self, pred, label):
        heatmap = label['heatmap']
        heatmap_weight = label['heatmap_weight']

        heatmap_pred = pred['heatmap']

        heatmap_loss = F.binary_cross_entropy_with_logits(heatmap_pred, heatmap, reduction='none')
        heatmap_loss = (heatmap_loss * heatmap_weight).mean(dim=(1, 2, 3))

        return {
            'heatmap_loss': heatmap_loss,
        }


class SimpleEASTDecoder(SimpleDetectionDecoder):
    def __init__(self, feature_channels=256, densebox_ratio=1000.0, densebox_rescale_factor=512):
        SimpleDetectionDecoder.__init__(self, feature_channels)

        self.densebox_ratio = densebox_ratio
        self.densebox_rescale_factor = densebox_rescale_factor

    def create_pred_layers(self):
        return {
            'heatmap': self.create_pred_layer(1),
            'densebox': self.create_pred_layer(8),
        }

    def postprocess_pred(self, pred):
        pred['heatmap'] = F.sigmoid(pred['heatmap'])
        pred['densebox'] = pred['densebox'] * self.densebox_rescale_factor
        return pred

    def calculate_losses(self, pred, label):
        heatmap = label['heatmap']
        heatmap_weight = label['heatmap_weight']
        densebox = label['densebox'] / self.densebox_rescale_factor
        densebox_weight = label['densebox_weight']

        heatmap_pred = pred['heatmap']
        densebox_pred = pred['densebox']

        heatmap_loss = F.binary_cross_entropy_with_logits(heatmap_pred, heatmap, reduction='none')
        heatmap_loss = (heatmap_loss * heatmap_weight).mean(dim=(1, 2, 3))

        densebox_loss = F.mse_loss(densebox_pred, densebox, reduction='none')
        densebox_loss = (densebox_loss * densebox_weight).mean(dim=(1, 2, 3)) * self.densebox_ratio

        return {
            'heatmap_loss': heatmap_loss,
            'densebox_loss': densebox_loss,
        }


class SimpleTextsnakeDecoder(SimpleDetectionDecoder):
    def __init__(self, feature_channels=256, radius_ratio=10.0):
        SimpleDetectionDecoder.__init__(self, feature_channels)

        self.radius_ratio = radius_ratio

    def create_pred_layers(self):
        return {
            'heatmap': self.create_pred_layer(1),
            'radius': self.create_pred_layer(1),
        }

    def postprocess_pred(self, pred):
        pred['heatmap'] = F.sigmoid(pred['heatmap'])
        pred['radius'] = torch.exp(pred['radius'])
        return pred

    def calculate_losses(self, pred, label):
        heatmap = label['heatmap']
        heatmap_weight = label['heatmap_weight']
        radius = torch.log(label['radius'] + 1)
        radius_weight = label['radius_weight']

        heatmap_pred = pred['heatmap']
        radius_pred = pred['radius']

        heatmap_loss = F.binary_cross_entropy_with_logits(heatmap_pred, heatmap, reduction='none')
        heatmap_loss = (heatmap_loss * heatmap_weight).mean(dim=(1, 2, 3))

        radius_loss = F.smooth_l1_loss(radius_pred, radius, reduction='none')
        radius_loss = (radius_loss * radius_weight).mean(dim=(1, 2, 3)) * self.radius_ratio

        return {
            'heatmap_loss': heatmap_loss,
            'radius_loss': radius_loss,
        }


class SimpleMSRDecoder(SimpleDetectionDecoder):
    def __init__(self, feature_channels=256, offset_ratio=1000.0, offset_rescale_factor=512):
        SimpleDetectionDecoder.__init__(self, feature_channels)

        self.offset_ratio = offset_ratio
        self.offset_rescale_factor = offset_rescale_factor

    def create_pred_layers(self):
        return {
            'heatmap': self.create_pred_layer(1),
            'offset': self.create_pred_layer(2),
        }

    def postprocess_pred(self, pred):
        pred['heatmap'] = F.sigmoid(pred['heatmap'])
        pred['offset'] = pred['offset'] * self.offset_rescale_factor
        return pred

    def calculate_losses(self, pred, label):
        heatmap = label['heatmap']
        heatmap_weight = label['heatmap_weight']
        offset = label['offset'] / self.offset_rescale_factor
        offset_weight = label['offset_weight']

        heatmap_pred = pred['heatmap']
        offset_pred = pred['offset']

        heatmap_loss = F.binary_cross_entropy_with_logits(heatmap_pred, heatmap, reduction='none')
        heatmap_loss = (heatmap_loss * heatmap_weight).mean(dim=(1, 2, 3))
        offset_loss = F.mse_loss(offset_pred, offset, reduction='none')
        offset_loss = (offset_loss * offset_weight).mean(dim=(1, 2, 3)) * self.offset_ratio

        return {
            'heatmap_loss': heatmap_loss,
            'offset_loss': offset_loss,
        }


# https://github.com/kuan-wang/pytorch-mobilenet-v3
import torch
import torch.nn as nn
import torch.nn.functional as F


# __all__ = ['MobileNetV3', 'mobilenetv3']


def conv_bn(inp, oup, stride, conv_layer=nn.Conv2d, norm_layer=nn.BatchNorm2d, nlin_layer=nn.ReLU):
    return nn.Sequential(
        conv_layer(inp, oup, 3, stride, 1, bias=False),
        norm_layer(oup),
        nlin_layer(inplace=True)
    )


def conv_1x1_bn(inp, oup, conv_layer=nn.Conv2d, norm_layer=nn.BatchNorm2d, nlin_layer=nn.ReLU):
    return nn.Sequential(
        conv_layer(inp, oup, 1, 1, 0, bias=False),
        norm_layer(oup),
        nlin_layer(inplace=True)
    )


class Hswish(nn.Module):
    def __init__(self, inplace=True):
        super(Hswish, self).__init__()
        self.inplace = inplace

    def forward(self, x):
        return x * F.relu6(x + 3., inplace=self.inplace) / 6.


class Hsigmoid(nn.Module):
    def __init__(self, inplace=True):
        super(Hsigmoid, self).__init__()
        self.inplace = inplace

    def forward(self, x):
        return F.relu6(x + 3., inplace=self.inplace) / 6.


class SEModule(nn.Module):
    def __init__(self, channel, reduction=4):
        super(SEModule, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            Hsigmoid()
            # nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.avg_pool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y.expand_as(x)


class Identity(nn.Module):
    def __init__(self, channel):
        super(Identity, self).__init__()

    def forward(self, x):
        return x


def make_divisible(x, divisible_by=8):
    import numpy as np
    return int(np.ceil(x * 1. / divisible_by) * divisible_by)


class MobileBottleneck(nn.Module):
    def __init__(self, inp, oup, kernel, stride, exp, se=False, nl='RE'):
        super(MobileBottleneck, self).__init__()
        assert stride in [1, 2]
        assert kernel in [3, 5]
        padding = (kernel - 1) // 2
        self.use_res_connect = stride == 1 and inp == oup

        conv_layer = nn.Conv2d
        norm_layer = nn.BatchNorm2d
        if nl == 'RE':
            nlin_layer = nn.ReLU # or ReLU6
        elif nl == 'HS':
            nlin_layer = Hswish
        else:
            raise NotImplementedError
        if se:
            SELayer = SEModule
        else:
            SELayer = Identity

        self.conv = nn.Sequential(
            # pw
            conv_layer(inp, exp, 1, 1, 0, bias=False),
            norm_layer(exp),
            nlin_layer(inplace=True),
            # dw
            conv_layer(exp, exp, kernel, stride, padding, groups=exp, bias=False),
            norm_layer(exp),
            SELayer(exp),
            nlin_layer(inplace=True),
            # pw-linear
            conv_layer(exp, oup, 1, 1, 0, bias=False),
            norm_layer(oup),
        )

    def forward(self, x):
        if self.use_res_connect:
            return x + self.conv(x)
        else:
            return self.conv(x)


class MobileNetV3(nn.Module):
    def __init__(self, n_class=1000, input_size=224, dropout=0.8, mode='small', width_mult=1.0):
        super(MobileNetV3, self).__init__()
        input_channel = 16
        last_channel = 1280
        if mode == 'large':
            # refer to Table 1 in paper
            mobile_setting = [
                # k, exp, c,  se,     nl,  s,
                [3, 16,  16,  False, 'RE', 1],
                [3, 64,  24,  False, 'RE', 2],
                [3, 72,  24,  False, 'RE', 1],  # 3
                [5, 72,  40,  True,  'RE', 2],
                [5, 120, 40,  True,  'RE', 1],
                [5, 120, 40,  True,  'RE', 1],  # 6
                [3, 240, 80,  False, 'HS', 2],
                [3, 200, 80,  False, 'HS', 1],
                [3, 184, 80,  False, 'HS', 1],
                [3, 184, 80,  False, 'HS', 1],
                [3, 480, 112, True,  'HS', 1],
                [3, 672, 112, True,  'HS', 1],  # 12
                [5, 672, 160, True,  'HS', 2],
                [5, 960, 160, True,  'HS', 1],
                [5, 960, 160, True,  'HS', 1],
            ]
        elif mode == 'small':
            # refer to Table 2 in paper
            mobile_setting = [
                # k, exp, c,  se,     nl,  s,
                [3, 16,  16,  True,  'RE', 2],
                [3, 72,  24,  False, 'RE', 2],
                [3, 88,  24,  False, 'RE', 1],
                [5, 96,  40,  True,  'HS', 2],
                [5, 240, 40,  True,  'HS', 1],
                [5, 240, 40,  True,  'HS', 1],
                [5, 120, 48,  True,  'HS', 1],
                [5, 144, 48,  True,  'HS', 1],
                [5, 288, 96,  True,  'HS', 2],
                [5, 576, 96,  True,  'HS', 1],
                [5, 576, 96,  True,  'HS', 1],
            ]
        else:
            raise NotImplementedError

        # building first layer
        assert input_size % 32 == 0
        last_channel = make_divisible(last_channel * width_mult) if width_mult > 1.0 else last_channel
        self.features = nn.ModuleList([conv_bn(3, input_channel, 2, nlin_layer=Hswish)])   # start_idx = 0: Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same
        self.classifier = []

        # building mobile blocks
        for k, exp, c, se, nl, s in mobile_setting:
            output_channel = make_divisible(c * width_mult)
            exp_channel = make_divisible(exp * width_mult)
            self.features.append(MobileBottleneck(input_channel, output_channel, k, s, exp_channel, se, nl))
            input_channel = output_channel

        # building last several layers
        if mode == 'large':
            last_conv = make_divisible(960 * width_mult)
            self.features.append(conv_1x1_bn(input_channel, last_conv, nlin_layer=Hswish))  # 16
            self.features.append(nn.AdaptiveAvgPool2d(1))
            self.features.append(nn.Conv2d(last_conv, last_channel, 1, 1, 0))
            self.features.append(Hswish(inplace=True))
        elif mode == 'small':
            last_conv = make_divisible(576 * width_mult)
            self.features.append(conv_1x1_bn(input_channel, last_conv, nlin_layer=Hswish))
            # self.features.append(SEModule(last_conv))  # refer to paper Table2, but I think this is a mistake
            self.features.append(nn.AdaptiveAvgPool2d(1))
            self.features.append(nn.Conv2d(last_conv, last_channel, 1, 1, 0))
            self.features.append(Hswish(inplace=True))
        else:
            raise NotImplementedError

        # make it nn.Sequential
        #self.features = nn.Sequential(*self.features)  del for dbnet

        # building classifier
        self.classifier = nn.Sequential(
            nn.Dropout(p=dropout),    # refer to paper section 6
            nn.Linear(last_channel, n_class),
        )

        self._initialize_weights()

    def forward(self, x):
        '''x = self.features(x)
        x = x.mean(3).mean(2)
        x = self.classifier(x)
        return x'''
        x2, x3, x4, x5 = None, None, None, None
        for stage in range(17): # https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/ppocr/modeling/backbones/det_mobilenet_v3.py
            x = self.features[stage](x)
            if stage == 3:  # if s == 2 and start_idx > 3
                x2 = x
            elif stage == 6:
                x3 = x
            elif stage == 12:
                x4 = x
            elif stage == 16:
                x5 = x
        return x2, x3, x4, x5

    def _initialize_weights(self):
        # weight initialization
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out')
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.ones_(m.weight)
                nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                if m.bias is not None:
                    nn.init.zeros_(m.bias)


def mobilenet_v3_large(pretrained=False, **kwargs):
    model = MobileNetV3(mode='large', **kwargs)
    if pretrained:
        state_dict = torch.load('mobilenetv3_large.pth.tar')
        model.load_state_dict(state_dict, strict=True)
        # raise NotImplementedError
    return model

def mobilenet_v3_small(pretrained=False, **kwargs):
    model = MobileNetV3(mode='small', **kwargs)
    if pretrained:
        state_dict = torch.load('mobilenetv3_small_67.4.pth.tar')
        model.load_state_dict(state_dict, strict=True)
        # raise NotImplementedError
    return model


import torch.nn as nn
import math
import torch.utils.model_zoo as model_zoo
BatchNorm2d = nn.BatchNorm2d

# __all__ = ['ResNet', 'resnet18', 'resnet34', 'resnet50', 'resnet101',
#            'resnet152']


model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
}


def constant_init(module, constant, bias=0):
    nn.init.constant_(module.weight, constant)
    if hasattr(module, 'bias'):
        nn.init.constant_(module.bias, bias)


def conv3x3(in_planes, out_planes, stride=1):
    """3x3 convolution with padding"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)


class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsample=None, dcn=None):
        super(BasicBlock, self).__init__()
        self.with_dcn = dcn is not None
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace=True)
        self.with_modulated_dcn = False
        if self.with_dcn:
            fallback_on_stride = dcn.get('fallback_on_stride', False)
            self.with_modulated_dcn = dcn.get('modulated', False)
        # self.conv2 = conv3x3(planes, planes)
        if not self.with_dcn or fallback_on_stride:
            self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
                                   padding=1, bias=False)
        else:
            deformable_groups = dcn.get('deformable_groups', 1)
            if not self.with_modulated_dcn:
                from assets.ops.dcn import DeformConv
                conv_op = DeformConv
                offset_channels = 18
            else:
                from assets.ops.dcn import ModulatedDeformConv
                conv_op = ModulatedDeformConv
                offset_channels = 27
            self.conv2_offset = nn.Conv2d(
                planes,
                deformable_groups * offset_channels,
                kernel_size=3,
                padding=1)
            self.conv2 = conv_op(
                planes,
                planes,
                kernel_size=3,
                padding=1,
                deformable_groups=deformable_groups,
                bias=False)
        self.bn2 = BatchNorm2d(planes)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        # out = self.conv2(out)
        if not self.with_dcn:
            out = self.conv2(out)
        elif self.with_modulated_dcn:
            offset_mask = self.conv2_offset(out)
            offset = offset_mask[:, :18, :, :]
            mask = offset_mask[:, -9:, :, :].sigmoid()
            out = self.conv2(out, offset, mask)
        else:
            offset = self.conv2_offset(out)
            out = self.conv2(out, offset)
        out = self.bn2(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out


class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inplanes, planes, stride=1, downsample=None, dcn=None):
        super(Bottleneck, self).__init__()
        self.with_dcn = dcn is not None
        self.conv1 = nn.Conv2d(inplanes, planes, kernel_size=1, bias=False)
        self.bn1 = BatchNorm2d(planes)
        fallback_on_stride = False
        self.with_modulated_dcn = False
        if self.with_dcn:
            fallback_on_stride = dcn.get('fallback_on_stride', False)
            self.with_modulated_dcn = dcn.get('modulated', False)
        if not self.with_dcn or fallback_on_stride:
            self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
                                   stride=stride, padding=1, bias=False)
        else:
            deformable_groups = dcn.get('deformable_groups', 1)
            if not self.with_modulated_dcn:
                from assets.ops.dcn import DeformConv
                conv_op = DeformConv
                offset_channels = 18
            else:
                from assets.ops.dcn import ModulatedDeformConv
                conv_op = ModulatedDeformConv
                offset_channels = 27
            self.conv2_offset = nn.Conv2d(
                planes, deformable_groups * offset_channels,
                kernel_size=3,
                padding=1)
            self.conv2 = conv_op(
                planes, planes, kernel_size=3, padding=1, stride=stride,
                deformable_groups=deformable_groups, bias=False)
        self.bn2 = BatchNorm2d(planes)
        self.conv3 = nn.Conv2d(planes, planes * 4, kernel_size=1, bias=False)
        self.bn3 = BatchNorm2d(planes * 4)
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample
        self.stride = stride
        self.dcn = dcn
        self.with_dcn = dcn is not None

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        # out = self.conv2(out)
        if not self.with_dcn:
            out = self.conv2(out)
        elif self.with_modulated_dcn:
            offset_mask = self.conv2_offset(out)
            offset = offset_mask[:, :18, :, :]
            mask = offset_mask[:, -9:, :, :].sigmoid()
            out = self.conv2(out, offset, mask)
        else:
            offset = self.conv2_offset(out)
            out = self.conv2(out, offset)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out


class ResNet(nn.Module):
    def __init__(self, block, layers, num_classes=1000, 
                 dcn=None, stage_with_dcn=(False, False, False, False)):
        self.dcn = dcn
        self.stage_with_dcn = stage_with_dcn
        self.inplanes = 64
        super(ResNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3,
                               bias=False)
        self.bn1 = BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(
            block, 128, layers[1], stride=2, dcn=dcn)
        self.layer3 = self._make_layer(
            block, 256, layers[2], stride=2, dcn=dcn)
        self.layer4 = self._make_layer(
            block, 512, layers[3], stride=2, dcn=dcn)
        self.avgpool = nn.AvgPool2d(7, stride=1)
        self.fc = nn.Linear(512 * block.expansion, num_classes)
    
        self.smooth = nn.Conv2d(2048, 256, kernel_size=1, stride=1, padding=1)    

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
        if self.dcn is not None:
            for m in self.modules():
                if isinstance(m, Bottleneck) or isinstance(m, BasicBlock):
                    if hasattr(m, 'conv2_offset'):
                        constant_init(m.conv2_offset, 0)

    def _make_layer(self, block, planes, blocks, stride=1, dcn=None):
        downsample = None
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.inplanes, planes * block.expansion,
                          kernel_size=1, stride=stride, bias=False),
                BatchNorm2d(planes * block.expansion),
            )

        layers = []
        layers.append(block(self.inplanes, planes,
                            stride, downsample, dcn=dcn))
        self.inplanes = planes * block.expansion
        for i in range(1, blocks):
            layers.append(block(self.inplanes, planes, dcn=dcn))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x2 = self.layer1(x)
        x3 = self.layer2(x2)
        x4 = self.layer3(x3)
        x5 = self.layer4(x4)

        return x2, x3, x4, x5


def resnet18(pretrained=True, **kwargs):
    """Constructs a ResNet-18 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [2, 2, 2, 2], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet18']), strict=False)
    return model

def deformable_resnet18(pretrained=True, **kwargs):
    """Constructs a ResNet-18 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [2, 2, 2, 2],
                    dcn=dict(modulated=True,
                            deformable_groups=1,
                            fallback_on_stride=False),
                    stage_with_dcn=[False, True, True, True], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet18']), strict=False)
    return model


def resnet34(pretrained=True, **kwargs):
    """Constructs a ResNet-34 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [3, 4, 6, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet34']), strict=False)
    return model


def resnet50(pretrained=True, **kwargs):
    """Constructs a ResNet-50 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet50']), strict=False)
    return model


def deformable_resnet50(pretrained=True, **kwargs):
    """Constructs a ResNet-50 model with deformable conv.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 6, 3],
                   dcn=dict(modulated=True,
                            deformable_groups=1,
                            fallback_on_stride=False),
                   stage_with_dcn=[False, True, True, True],
                   **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet50']), strict=False)
    return model


def resnet101(pretrained=True, **kwargs):
    """Constructs a ResNet-101 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 23, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet101']), strict=False)
    return model


def resnet152(pretrained=True, **kwargs):
    """Constructs a ResNet-152 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 8, 36, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet152']), strict=False)
    return model

import importlib
from collections import OrderedDict

import anyconfig
import munch


class Config(object):
    def __init__(self):
        pass

    def load(self, conf):
        conf = anyconfig.load(conf)
        return munch.munchify(conf)

    def compile(self, conf, return_packages=False):
        packages = conf.get('package', [])
        defines = {}

        for path in conf.get('import', []):
            parent_conf = self.load(path)
            parent_packages, parent_defines = self.compile(
                parent_conf, return_packages=True)
            packages.extend(parent_packages)
            defines.update(parent_defines)

        modules = []
        for package in packages:
            module = importlib.import_module(package)
            modules.append(module)

        if isinstance(conf['define'], dict):
            conf['define'] = [conf['define']]

        for define in conf['define']:
            name = define.copy().pop('name')

            if not isinstance(name, str):
                raise RuntimeError('name must be str')

            defines[name] = self.compile_conf(define, defines, modules)

        if return_packages:
            return packages, defines
        else:
            return defines

    def compile_conf(self, conf, defines, modules):
        if isinstance(conf, (int, float)):
            return conf
        elif isinstance(conf, str):
            if conf.startswith('^'):
                return defines[conf[1:]]
            if conf.startswith('$'):
                return {'class': self.find_class_in_modules(conf[1:], modules)}
            return conf
        elif isinstance(conf, dict):
            if 'class' in conf:
                conf['class'] = self.find_class_in_modules(
                    conf['class'], modules)
            if 'base' in conf:
                base = conf.copy().pop('base')

                if not isinstance(base, str):
                    raise RuntimeError('base must be str')

                conf = {
                    **defines[base],
                    **conf,
                }
            return {key: self.compile_conf(value, defines, modules) for key, value in conf.items()}
        elif isinstance(conf, (list, tuple)):
            return [self.compile_conf(value, defines, modules) for value in conf]
        else:
            return conf

    def find_class_in_modules(self, cls, modules):
        if not isinstance(cls, str):
            raise RuntimeError('class name must be str')

        if cls.find('.') != -1:
            package, cls = cls.rsplit('.', 1)
            module = importlib.import_module(package)
            if hasattr(module, cls):
                return module.__name__ + '.' + cls

        for module in modules:
            if hasattr(module, cls):
                return module.__name__ + '.' + cls
        raise RuntimeError('class not found ' + cls)


class State:
    def __init__(self, autoload=True, default=None):
        self.autoload = autoload
        self.default = default


class StateMeta(type):
    def __new__(mcs, name, bases, attrs):
        current_states = []
        for key, value in attrs.items():
            if isinstance(value, State):
                current_states.append((key, value))

        current_states.sort(key=lambda x: x[0])
        attrs['states'] = OrderedDict(current_states)
        new_class = super(StateMeta, mcs).__new__(mcs, name, bases, attrs)

        # Walk through the MRO
        states = OrderedDict()
        for base in reversed(new_class.__mro__):
            if hasattr(base, 'states'):
                states.update(base.states)
        new_class.states = states

        for key, value in states.items():
            setattr(new_class, key, value.default)

        return new_class


class Configurable(metaclass=StateMeta):
    def __init__(self, *args, cmd={}, **kwargs):
        self.load_all(cmd=cmd, **kwargs)

    @staticmethod
    def construct_class_from_config(args):
        cls = Configurable.extract_class_from_args(args)
        return cls(**args)

    @staticmethod
    def extract_class_from_args(args):
        cls = args.copy().pop('class')
        package, cls = cls.rsplit('.', 1)
        module = importlib.import_module(package)
        cls = getattr(module, cls)
        return cls

    def load_all(self, **kwargs):
        for name, state in self.states.items():
            if state.autoload:
                self.load(name, **kwargs)

    def load(self, state_name, **kwargs):
        # FIXME: kwargs should be filtered
        # Args passed from command line
        cmd = kwargs.pop('cmd', dict())
        if state_name in kwargs:
            setattr(self, state_name, self.create_member_from_config(
                (kwargs[state_name], cmd)))
        else:
            setattr(self, state_name, self.states[state_name].default)

    def create_member_from_config(self, conf):
        args, cmd = conf
        if args is None or isinstance(args, (int, float, str)):
            return args
        elif isinstance(args, (list, tuple)):
            return [self.create_member_from_config((subargs, cmd)) for subargs in args]
        elif isinstance(args, dict):
            if 'class' in args:
                cls = self.extract_class_from_args(args)
                return cls(**args, cmd=cmd)
            return {key: self.create_member_from_config((subargs, cmd)) for key, subargs in args.items()}
        else:
            return args

    def dump(self):
        state = {}
        state['class'] = self.__class__.__module__ + \
            '.' + self.__class__.__name__
        for name, value in self.states.items():
            obj = getattr(self, name)
            state[name] = self.dump_obj(obj)
        return state

    def dump_obj(self, obj):
        if obj is None:
            return None
        elif hasattr(obj, 'dump'):
            return obj.dump()
        elif isinstance(obj, (int, float, str)):
            return obj
        elif isinstance(obj, (list, tuple)):
            return [self.dump_obj(value) for value in obj]
        elif isinstance(obj, dict):
            return {key: self.dump_obj(value) for key, value in obj.items()}
        else:
            return str(obj)


import os
import logging
import functools
import json
import time
from datetime import datetime

from tensorboardX import SummaryWriter
import yaml
import cv2
import numpy as np

# from concern.config import Configurable, State


class Logger(Configurable):
    SUMMARY_DIR_NAME = 'summaries'
    VISUALIZE_NAME = 'visualize'
    LOG_FILE_NAME = 'output.log'
    ARGS_FILE_NAME = 'args.log'
    METRICS_FILE_NAME = 'metrics.log'

    database_dir = State(default='./outputs/')
    log_dir = State(default='workspace')
    verbose = State(default=False)
    level = State(default='info')
    log_interval = State(default=100)

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

        self._make_storage()

        cmd = kwargs['cmd']
        self.name = cmd['name']
        self.log_dir = os.path.join(self.log_dir, self.name)
        try:
            self.verbose = cmd['verbose']
        except:
            print('verbose:', self.verbose)
        if self.verbose:
            print('Initializing log dir for', self.log_dir)

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        self.message_logger = self._init_message_logger()

        summary_path = os.path.join(self.log_dir, self.SUMMARY_DIR_NAME)
        self.tf_board_logger = SummaryWriter(summary_path)

        self.metrics_writer = open(os.path.join(
            self.log_dir, self.METRICS_FILE_NAME), 'at')

        self.timestamp = time.time()
        self.logged = -1
        self.speed = None
        self.eta_time = None

    def _make_storage(self):
        application = os.path.basename(os.getcwd())
        storage_dir = os.path.join(
            self.database_dir, self.log_dir, application)
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        if not os.path.exists(self.log_dir):
            os.symlink(storage_dir, self.log_dir)

    def save_dir(self, dir_name):
        return os.path.join(self.log_dir, dir_name)

    def _init_message_logger(self):
        message_logger = logging.getLogger('messages')
        message_logger.setLevel(
            logging.DEBUG if self.verbose else logging.INFO)
        formatter = logging.Formatter(
            '[%(levelname)s] [%(asctime)s] %(message)s')
        std_handler = logging.StreamHandler()
        std_handler.setLevel(message_logger.level)
        std_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(
            os.path.join(self.log_dir, self.LOG_FILE_NAME))
        file_handler.setLevel(message_logger.level)
        file_handler.setFormatter(formatter)

        message_logger.addHandler(std_handler)
        message_logger.addHandler(file_handler)
        return message_logger

    def report_time(self, name: str):
        if self.verbose:
            self.info(name + " time :" + str(time.time() - self.timestamp))
            self.timestamp = time.time()

    def report_eta(self, steps, total, epoch):
        self.logged = self.logged % total + 1
        steps = steps % total
        if self.eta_time is None:
            self.eta_time = time.time()
            speed = -1
        else:
            eta_time = time.time()
            speed = eta_time - self.eta_time
            if self.speed is not None:
                speed = ((self.logged - 1) * self.speed + speed) / self.logged
            self.speed = speed
            self.eta_time = eta_time

        seconds = (total - steps) * speed
        hours = seconds // 3600
        minutes = (seconds - (hours * 3600)) // 60
        seconds = seconds % 60

        print('%d/%d batches processed in epoch %d, ETA: %2d:%2d:%2d' %
              (steps, total, epoch,
               hours, minutes, seconds), end='\r')

    def args(self, parameters=None):
        if parameters is None:
            with open(os.path.join(self.log_dir, self.ARGS_FILE_NAME), 'rt') as reader:
                return yaml.load(reader.read())
        with open(os.path.join(self.log_dir, self.ARGS_FILE_NAME), 'wt') as writer:
            yaml.dump(parameters.dump(), writer)

    def metrics(self, epoch, steps, metrics_dict):
        results = {}
        for name, a in metrics_dict.items():
            results[name] = {'count': a.count, 'value': float(a.avg)}
            self.add_scalar('metrics/' + name, a.avg, steps)
        result_dict = {
            str(datetime.now()): {
                'epoch': epoch,
                'steps': steps,
                **results
            }
        }
        string_result = yaml.dump(result_dict)
        self.info(string_result)
        self.metrics_writer.write(string_result)
        self.metrics_writer.flush()

    def named_number(self, name, num=None, default=0):
        if num is None:
            return int(self.has_signal(name)) or default
        else:
            with open(os.path.join(self.log_dir, name), 'w') as writer:
                writer.write(str(num))
            return num

    epoch = functools.partialmethod(named_number, 'epoch')
    iter = functools.partialmethod(named_number, 'iter')

    def message(self, level, content):
        self.message_logger.__getattribute__(level)(content)

    def images(self, prefix, image_dict, step):
        for name, image in image_dict.items():
            self.add_image(prefix + '/' + name, image, step, dataformats='HWC')

    def merge_save_images(self, name, images):
        for i, image in enumerate(images):
            if i == 0:
                result = image
            else:
                result = np.concatenate([result, image], 0)
        cv2.imwrite(os.path.join(self.vis_dir(), name+'.jpg'), result)

    def vis_dir(self):
        vis_dir = os.path.join(self.log_dir, self.VISUALIZE_NAME)
        if not os.path.exists(vis_dir):
            os.mkdir(vis_dir)
        return vis_dir

    def save_image_dict(self, images, max_size=1024):
        for file_name, image in images.items():
            height, width = image.shape[:2]
            if height > width:
                actual_height = min(height, max_size)
                actual_width = int(round(actual_height * width / height))
            else:
                actual_width = min(width, max_size)
                actual_height = int(round(actual_width * height / width))
                image = cv2.resize(image, (actual_width, actual_height))
            cv2.imwrite(os.path.join(self.vis_dir(), file_name+'.jpg'), image)

    def __getattr__(self, name):
        message_levels = set(['debug', 'info', 'warning', 'error', 'critical'])
        if name == '__setstate__':
            raise AttributeError('haha')
        if name in message_levels:
            return functools.partial(self.message, name)
        elif hasattr(self.__dict__.get('tf_board_logger'), name):
            return self.tf_board_logger.__getattribute__(name)
        else:
            super()

# from concern.config import Configurable, State
import os
import torch


class Checkpoint(Configurable):
    start_epoch = State(default=0)
    start_iter = State(default=0)
    resume = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

        cmd = kwargs['cmd']
        if 'start_epoch' in cmd:
            self.start_epoch = cmd['start_epoch']
        if 'start_iter' in cmd:
            self.start_iter = cmd['start_iter']
        if 'resume' in cmd:
            self.resume = cmd['resume']

    def restore_model(self, model, device, logger):
        if self.resume is None:
            return

        if not os.path.exists(self.resume):
            self.logger.warning("Checkpoint not found: " +
                                self.resume)
            return

        logger.info("Resuming from " + self.resume)
        state_dict = torch.load(self.resume, map_location=device)
        model.load_state_dict(state_dict, strict=False)
        logger.info("Resumed from " + self.resume)

    def restore_counter(self):
        return self.start_epoch, self.start_iter


from bisect import bisect_right
import numpy as np
import torch.optim.lr_scheduler as lr_scheduler

# from concern.config import Configurable, State
# from concern.signal_monitor import SignalMonitor


class ConstantLearningRate(Configurable):
    lr = State(default=0.0001)

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

    def get_learning_rate(self, epoch, step):
        return self.lr


class FileMonitorLearningRate(Configurable):
    file_path = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

        self.monitor = SignalMonitor(self.file_path)

    def get_learning_rate(self, epoch, step):
        signal = self.monitor.get_signal()
        if signal is not None:
            return float(signal)
        return None


class PriorityLearningRate(Configurable):
    learning_rates = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

    def get_learning_rate(self, epoch, step):
        for learning_rate in self.learning_rates:
            lr = learning_rate.get_learning_rate(epoch, step)
            if lr is not None:
                return lr
        return None


class MultiStepLR(Configurable):
    lr = State()
    milestones = State(default=[])  # milestones must be sorted
    gamma = State(default=0.1)

    def __init__(self, cmd={}, **kwargs):
        self.load_all(**kwargs)
        self.lr = cmd.get('lr', self.lr)

    def get_learning_rate(self, epoch, step):
        return self.lr * self.gamma ** bisect_right(self.milestones, epoch)


class WarmupLR(Configurable):
    steps = State(default=4000)
    warmup_lr = State(default=1e-5)
    origin_lr = State()

    def __init__(self, cmd={}, **kwargs):
        self.load_all(**kwargs)

    def get_learning_rate(self, epoch, step):
        if epoch == 0 and step < self.steps:
            return self.warmup_lr
        return self.origin_lr.get_learning_rate(epoch, step)


class PiecewiseConstantLearningRate(Configurable):
    boundaries = State(default=[10000, 20000])
    values = State(default=[0.001, 0.0001, 0.00001])

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

    def get_learning_rate(self, epoch, step):
        for boundary, value in zip(self.boundaries, self.values[:-1]):
            if step < boundary:
                return value
        return self.values[-1]


class DecayLearningRate(Configurable):
    lr = State(default=0.007)
    epochs = State(default=1200)
    factor = State(default=0.9)

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

    def get_learning_rate(self, epoch, step=None):
        rate = np.power(1.0 - epoch / float(self.epochs + 1), self.factor)
        return rate * self.lr


class BuitlinLearningRate(Configurable):
    lr = State(default=0.001)
    klass = State(default='StepLR')
    args = State(default=[])
    kwargs = State(default={})

    def __init__(self, cmd={}, **kwargs):
        self.load_all(**kwargs)
        self.lr = cmd.get('lr', None) or self.lr
        self.scheduler = None

    def prepare(self, optimizer):
        self.scheduler = getattr(lr_scheduler, self.klass)(
            optimizer, *self.args, **self.kwargs)

    def get_learning_rate(self, epoch, step=None):
        if self.scheduler is None:
            raise 'learning rate not ready(prepared with optimizer) '
        self.scheduler.last_epoch = epoch
        # return value of gt_lr is a list,
        # where each element is the corresponding learning rate for a
        # paramater group.
        return self.scheduler.get_lr()[0]


import os

import torch

# from concern.config import Configurable, State
# from concern.signal_monitor import SignalMonitor


class ModelSaver(Configurable):
    dir_path = State()
    save_interval = State(default=1000)
    signal_path = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

        # BUG: signal path should not be global
        self.monitor = SignalMonitor(self.signal_path)

    def maybe_save_model(self, model, epoch, step, logger):
        if step % self.save_interval == 0 or self.monitor.get_signal() is not None:
            self.save_model(model, epoch, step)
            logger.report_time('Saving ')
            logger.iter(step)

    def save_model(self, model, epoch=None, step=None):
        if isinstance(model, dict):
            for name, net in model.items():
                checkpoint_name = self.make_checkpoint_name(name, epoch, step)
                self.save_checkpoint(net, checkpoint_name)
        else:
            checkpoint_name = self.make_checkpoint_name('model', epoch, step)
            self.save_checkpoint(model, checkpoint_name)

    def save_checkpoint(self, net, name):
        os.makedirs(self.dir_path, exist_ok=True)
        torch.save(net.state_dict(), os.path.join(self.dir_path, name))

    def make_checkpoint_name(self, name, epoch=None, step=None):
        if epoch is None or step is None:
            c_name = name + '_latest'
        else:
            c_name = '{}_epoch_{}_minibatch_{}'.format(name, epoch, step)
        return c_name


import torch

# from concern.config import Configurable, State


class OptimizerScheduler(Configurable):
    optimizer = State()
    optimizer_args = State(default={})
    learning_rate = State(autoload=False)

    def __init__(self, cmd={}, **kwargs):
        self.load_all(**kwargs)
        self.load('learning_rate', cmd=cmd, **kwargs)
        if 'lr' in cmd:
            self.optimizer_args['lr'] = cmd['lr']

    def create_optimizer(self, parameters):
        optimizer = getattr(torch.optim, self.optimizer)(
                parameters, **self.optimizer_args)
        if hasattr(self.learning_rate, 'prepare'):
            self.learning_rate.prepare(optimizer)
        return optimizer


import os
import subprocess
import shutil

import numpy as np
import json

# from concern import Logger, AverageMeter
# from concern.config import Configurable


class ICDARDetectionMeasurer(Configurable):
    def __init__(self, **kwargs):
        self.visualized = False

    def measure(self, batch, output):
        pairs = []
        for i in range(len(batch[-1])):
            pairs.append((batch[-1][i], output[i][0]))
        return pairs

    def validate_measure(self, batch, output):
        return self.measure(batch, output), [int(self.visualized)]

    def evaluate_measure(self, batch, output):
        return self.measure(batch, output), np.linspace(0, batch[0].shape[0]).tolist()

    def gather_measure(self, name, raw_metrics, logger: Logger):
        save_dir = os.path.join(logger.log_dir, name)
        shutil.rmtree(save_dir, ignore_errors=True)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        log_file_path = os.path.join(save_dir, name + '.log')
        count = 0
        for batch_pairs in raw_metrics:
            for _filename, boxes in batch_pairs:
                boxes = np.array(boxes).reshape(-1, 8).astype(np.int32)
                filename = 'res_' + _filename.replace('.jpg', '.txt')
                with open(os.path.join(save_dir, filename), 'wt') as f:
                    if len(boxes) == 0:
                        f.write('')
                    for box in boxes:
                        f.write(','.join(map(str, box)) + '\n')
                count += 1

        self.packing(save_dir)
        try:
            raw_out = subprocess.check_output(['python assets/ic15_eval/script.py -m=' + name
                                               + ' -g=assets/ic15_eval/gt.zip -s=' +
                                               os.path.join(save_dir, 'submit.zip') +
                                               '|tee -a ' + log_file_path],
                                              timeout=30, shell=True)
        except subprocess.TimeoutExpired:
            return {}
        raw_out = raw_out.decode().replace('Calculated!', '')
        dict_out = json.loads(raw_out)
        return {k: AverageMeter().update(v, n=count) for k, v in dict_out.items()}

    def packing(self, save_dir):
        pack_name = 'submit.zip'
        os.system(
            'zip -r -j -q ' +
            os.path.join(save_dir, pack_name) + ' ' + save_dir + '/*.txt')



import numpy as np

# from concern import Logger, AverageMeter
# from concern.config import Configurable
# from concern.icdar2015_eval.detection.iou import DetectionIoUEvaluator

DetectionIoUEvaluator = None

class QuadMeasurer(Configurable):
    def __init__(self, **kwargs):
        self.evaluator = DetectionIoUEvaluator()

    def measure(self, batch, output, is_output_polygon=False, box_thresh=0.6):
        '''
        batch: (image, polygons, ignore_tags
        batch: a dict produced by dataloaders.
            image: tensor of shape (N, C, H, W).
            polygons: tensor of shape (N, K, 4, 2), the polygons of objective regions.
            ignore_tags: tensor of shape (N, K), indicates whether a region is ignorable or not.
            shape: the original shape of images.
            filename: the original filenames of images.
        output: (polygons, ...)
        '''
        results = []
        gt_polyons_batch = batch['polygons']
        ignore_tags_batch = batch['ignore_tags']
        pred_polygons_batch = np.array(output[0])
        pred_scores_batch = np.array(output[1])
        for polygons, pred_polygons, pred_scores, ignore_tags in\
                zip(gt_polyons_batch, pred_polygons_batch, pred_scores_batch, ignore_tags_batch):
            gt = [dict(points=polygons[i], ignore=ignore_tags[i])
                  for i in range(len(polygons))]
            if is_output_polygon:
                pred = [dict(points=pred_polygons[i])
                        for i in range(len(pred_polygons))]
            else:
                pred = []
                # print(pred_polygons.shape)
                for i in range(pred_polygons.shape[0]):
                    if pred_scores[i] >= box_thresh:
                        # print(pred_polygons[i,:,:].tolist())
                        pred.append(dict(points=pred_polygons[i,:,:].tolist()))
                # pred = [dict(points=pred_polygons[i,:,:].tolist()) if pred_scores[i] >= box_thresh for i in range(pred_polygons.shape[0])]
            results.append(self.evaluator.evaluate_image(gt, pred))
        return results

    def validate_measure(self, batch, output, is_output_polygon=False, box_thresh=0.6):
        return self.measure(batch, output, is_output_polygon, box_thresh)

    def evaluate_measure(self, batch, output):
        return self.measure(batch, output),\
            np.linspace(0, batch['image'].shape[0]).tolist()

    def gather_measure(self, raw_metrics, logger: Logger):
        raw_metrics = [image_metrics
                       for batch_metrics in raw_metrics
                       for image_metrics in batch_metrics]

        result = self.evaluator.combine_results(raw_metrics)

        precision = AverageMeter()
        recall = AverageMeter()
        fmeasure = AverageMeter()

        precision.update(result['precision'], n=len(raw_metrics))
        recall.update(result['recall'], n=len(raw_metrics))
        fmeasure_score = 2 * precision.val * recall.val /\
            (precision.val + recall.val + 1e-8)
        fmeasure.update(fmeasure_score)

        return {
            'precision': precision,
            'recall': recall,
            'fmeasure': fmeasure
        }


# from concern.config import Configurable, State
# from concern.log import Logger
# from structure.builder import Builder
# from structure.representers import *
# from structure.measurers import *
# from structure.visualizers import *
from data.data_loader import *
from data import *
# from training.model_saver import ModelSaver
# from training.checkpoint import Checkpoint
# from training.optimizer_scheduler import OptimizerScheduler


class Structure(Configurable):
    builder = State()
    representer = State()
    measurer = State()
    visualizer = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)

    @property
    def model_name(self):
        return self.builder.model_name


class TrainSettings(Configurable):
    data_loader = State()
    model_saver = State()
    checkpoint = State()
    scheduler = State()
    epochs = State(default=10)

    def __init__(self, **kwargs):
        kwargs['cmd'].update(is_train=True)
        self.load_all(**kwargs)
        if 'epochs' in kwargs['cmd']:
            self.epochs = kwargs['cmd']['epochs']


class ValidationSettings(Configurable):
    data_loaders = State()
    visualize = State()
    interval = State(default=100)
    exempt = State(default=-1)

    def __init__(self, **kwargs):
        kwargs['cmd'].update(is_train=False)
        self.load_all(**kwargs)

        cmd = kwargs['cmd']
        self.visualize = cmd['visualize']


class EvaluationSettings(Configurable):
    data_loaders = State()
    visualize = State(default=True)
    resume = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)


class EvaluationSettings2(Configurable):
    structure = State()
    data_loaders = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)


class ShowSettings(Configurable):
    data_loader = State()
    representer = State()
    visualizer = State()

    def __init__(self, **kwargs):
        self.load_all(**kwargs)


class Experiment(Configurable):
    structure = State(autoload=False)
    train = State()
    validation = State(autoload=False)
    evaluation = State(autoload=False)
    logger = State(autoload=True)

    def __init__(self, **kwargs):
        self.load('structure', **kwargs)

        cmd = kwargs.get('cmd', {})
        if 'name' not in cmd:
            cmd['name'] = self.structure.model_name

        self.load_all(**kwargs)
        self.distributed = cmd.get('distributed', False)
        self.local_rank = cmd.get('local_rank', 0)

        if cmd.get('validate', False):
            self.load('validation', **kwargs)
        else:
            self.validation = None


import os

import torch
from tqdm import tqdm

# from experiment import Experiment
from data.data_loader import DistributedSampler


class Trainer:
    def __init__(self, experiment: Experiment):
        self.init_device()

        self.experiment = experiment
        self.structure = experiment.structure
        self.logger = experiment.logger
        self.model_saver = experiment.train.model_saver

        # FIXME: Hack the save model path into logger path
        self.model_saver.dir_path = self.logger.save_dir(
            self.model_saver.dir_path)
        self.current_lr = 0

        self.total = 0

    def init_device(self):
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')

    def init_model(self):
        model = self.structure.builder.build(
            self.device, self.experiment.distributed, self.experiment.local_rank)
        return model

    def update_learning_rate(self, optimizer, epoch, step):
        lr = self.experiment.train.scheduler.learning_rate.get_learning_rate(
            epoch, step)

        for group in optimizer.param_groups:
            group['lr'] = lr
        self.current_lr = lr

    def train(self):
        self.logger.report_time('Start')
        self.logger.args(self.experiment)
        model = self.init_model()
        train_data_loader = self.experiment.train.data_loader
        if self.experiment.validation:
            validation_loaders = self.experiment.validation.data_loaders

        self.steps = 0
        if self.experiment.train.checkpoint:
            self.experiment.train.checkpoint.restore_model(
                model, self.device, self.logger)
            epoch, iter_delta = self.experiment.train.checkpoint.restore_counter()
            self.steps = epoch * self.total + iter_delta

        # Init start epoch and iter
        optimizer = self.experiment.train.scheduler.create_optimizer(
            model.parameters())

        self.logger.report_time('Init')

        model.train()
        while True:
            self.logger.info('Training epoch ' + str(epoch))
            self.logger.epoch(epoch)
            self.total = len(train_data_loader)

            for batch in train_data_loader:
                self.update_learning_rate(optimizer, epoch, self.steps)

                self.logger.report_time("Data loading")

                if self.experiment.validation and\
                        self.steps % self.experiment.validation.interval == 0 and\
                        self.steps > self.experiment.validation.exempt:
                    self.validate(validation_loaders, model, epoch, self.steps)
                self.logger.report_time('Validating ')
                if self.logger.verbose:
                    torch.cuda.synchronize()

                self.train_step(model, optimizer, batch,
                                epoch=epoch, step=self.steps)
                if self.logger.verbose:
                    torch.cuda.synchronize()
                self.logger.report_time('Forwarding ')

                self.model_saver.maybe_save_model(
                    model, epoch, self.steps, self.logger)

                self.steps += 1
                self.logger.report_eta(self.steps, self.total, epoch)

            epoch += 1
            if epoch > self.experiment.train.epochs:
                self.model_saver.save_checkpoint(model, 'final')
                if self.experiment.validation:
                    self.validate(validation_loaders, model, epoch, self.steps)
                self.logger.info('Training done')
                break
            iter_delta = 0

    def train_step(self, model, optimizer, batch, epoch, step, **kwards):
        optimizer.zero_grad()

        results = model.forward(batch, training=True)
        if len(results) == 2:
            l, pred = results
            metrics = {}
        elif len(results) == 3:
            l, pred, metrics = results

        if isinstance(l, dict):
            line = []
            loss = torch.tensor(0.).cuda()
            for key, l_val in l.items():
                loss += l_val.mean()
                line.append('loss_{0}:{1:.4f}'.format(key, l_val.mean()))
        else:
            loss = l.mean()
        loss.backward()
        optimizer.step()

        if step % self.experiment.logger.log_interval == 0:
            if isinstance(l, dict):
                line = '\t'.join(line)
                log_info = '\t'.join(['step:{:6d}', 'epoch:{:3d}', '{}', 'lr:{:.4f}']).format(step, epoch, line, self.current_lr)
                self.logger.info(log_info)
            else:
                self.logger.info('step: %6d, epoch: %3d, loss: %.6f, lr: %f' % (
                    step, epoch, loss.item(), self.current_lr))
            self.logger.add_scalar('loss', loss, step)
            self.logger.add_scalar('learning_rate', self.current_lr, step)
            for name, metric in metrics.items():
                self.logger.add_scalar(name, metric.mean(), step)
                self.logger.info('%s: %6f' % (name, metric.mean()))

            self.logger.report_time('Logging')

    def validate(self, validation_loaders, model, epoch, step):
        all_matircs = {}
        model.eval()
        for name, loader in validation_loaders.items():
            if self.experiment.validation.visualize:
                metrics, vis_images = self.validate_step(
                    loader, model, True)
                self.logger.images(
                    os.path.join('vis', name), vis_images, step)
            else:
                metrics, vis_images = self.validate_step(loader, model, False)
            for _key, metric in metrics.items():
                key = name + '/' + _key
                if key in all_matircs:
                    all_matircs[key].update(metric.val, metric.count)
                else:
                    all_matircs[key] = metric

        for key, metric in all_matircs.items():
            self.logger.info('%s : %f (%d)' % (key, metric.avg, metric.count))
        self.logger.metrics(epoch, self.steps, all_matircs)
        model.train()
        return all_matircs

    def validate_step(self, data_loader, model, visualize=False):
        raw_metrics = []
        vis_images = dict()
        for i, batch in tqdm(enumerate(data_loader), total=len(data_loader)):
            pred = model.forward(batch, training=False)
            output = self.structure.representer.represent(batch, pred)
            raw_metric, interested = self.structure.measurer.validate_measure(
                batch, output)
            raw_metrics.append(raw_metric)

            if visualize and self.structure.visualizer:
                vis_image = self.structure.visualizer.visualize(
                    batch, output, interested)
                vis_images.update(vis_image)
        metrics = self.structure.measurer.gather_measure(
            raw_metrics, self.logger)
        return metrics, vis_images

    def to_np(self, x):
        return x.cpu().data.numpy()


#!python3
import argparse
import time

import torch
import yaml

# from trainer import Trainer
# tagged yaml objects
# from experiment import Structure, TrainSettings, ValidationSettings, Experiment
# from concern.log import Logger
from data.data_loader import DataLoader
from data.image_dataset import ImageDataset
# from training.checkpoint import Checkpoint
# from training.model_saver import ModelSaver
# from training.optimizer_scheduler import OptimizerScheduler
# from concern.config import Configurable, Config


def main():
    parser = argparse.ArgumentParser(description='Text Recognition Training')
    parser.add_argument('exp', type=str)
    parser.add_argument('--name', default='Experiment', type=str)
    parser.add_argument('--batch_size', type=int, help='Batch size for training')
    parser.add_argument('--resume', type=str, help='Resume from checkpoint')
    parser.add_argument('--epochs', type=int, help='Number of training epochs')
    parser.add_argument('--num_workers', type=int, help='Number of dataloader workers')
    parser.add_argument('--start_iter', type=int, help='Begin counting iterations starting from this value (should be used with resume)')
    parser.add_argument('--start_epoch', type=int, help='Begin counting epoch starting from this value (should be used with resume)')
    parser.add_argument('--max_size', type=int, help='max length of label')
    parser.add_argument('--lr', type=float, help='initial learning rate')
    parser.add_argument('--optimizer', type=str, help='The optimizer want to use')
    parser.add_argument('--thresh', type=float, help='The threshold to replace it in the representers')
    parser.add_argument('--verbose', action='store_true', help='show verbose info')
    parser.add_argument('--visualize', action='store_true', help='visualize maps in tensorboard')
    parser.add_argument('--force_reload', action='store_true', dest='force_reload', help='Force reload data meta')
    parser.add_argument('--no-force_reload', action='store_false', dest='force_reload', help='Force reload data meta')
    parser.add_argument('--validate', action='store_true', dest='validate', help='Validate during training')
    parser.add_argument('--no-validate', action='store_false', dest='validate', help='Validate during training')
    parser.add_argument('--print-config-only', action='store_true', help='print config without actual training')
    parser.add_argument('--debug', action='store_true', dest='debug', help='Run with debug mode, which hacks dataset num_samples to toy number')
    parser.add_argument('--no-debug', action='store_false', dest='debug', help='Run without debug mode')
    parser.add_argument('--benchmark', action='store_true', dest='benchmark', help='Open cudnn benchmark mode')
    parser.add_argument('--no-benchmark', action='store_false', dest='benchmark', help='Turn cudnn benchmark mode off')
    parser.add_argument('-d', '--distributed', action='store_true', dest='distributed', help='Use distributed training')
    parser.add_argument('--local_rank', dest='local_rank', default=0, type=int, help='Use distributed training')
    parser.add_argument('-g', '--num_gpus', dest='num_gpus', default=4, type=int, help='The number of accessible gpus')
    parser.set_defaults(debug=False)
    parser.set_defaults(benchmark=True)

    args = parser.parse_args()
    args = vars(args)
    args = {k: v for k, v in args.items() if v is not None}

    if args['distributed']:
        torch.cuda.set_device(args['local_rank'])
        torch.distributed.init_process_group(backend='nccl', init_method='env://')

    conf = Config()
    experiment_args = conf.compile(conf.load(args['exp']))['Experiment']
    experiment_args.update(cmd=args)
    experiment = Configurable.construct_class_from_config(experiment_args)

    if not args['print_config_only']:
        torch.backends.cudnn.benchmark = args['benchmark']
        trainer = Trainer(experiment)
        trainer.train()



if __name__ == '__main__':
    main()



"""

CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1

"""