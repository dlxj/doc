import torch
import torch.nn as nn

#交叉 除以 合并
def get_dice_loss(gt_score, pred_score):
	inter = torch.sum(gt_score * pred_score) #交叉（交集）
	union = torch.sum(gt_score) + torch.sum(pred_score) + 1e-5 #合并（并集）
	return 1. - (2 * inter / union) #0-1之间的损失


def get_geo_loss(gt_geo, pred_geo):
	d1_gt, d2_gt, d3_gt, d4_gt, angle_gt = torch.split(gt_geo, 1, 1)
	d1_pred, d2_pred, d3_pred, d4_pred, angle_pred = torch.split(pred_geo, 1, 1)
	area_gt = (d1_gt + d2_gt) * (d3_gt + d4_gt) #标签面积
	area_pred = (d1_pred + d2_pred) * (d3_pred + d4_pred) #预测面积
	#相交面积（交集）v
	w_union = torch.min(d3_gt, d3_pred) + torch.min(d4_gt, d4_pred)
	h_union = torch.min(d1_gt, d1_pred) + torch.min(d2_gt, d2_pred)
	area_intersect = w_union * h_union
	#合并面积（并集）
	area_union = area_gt + area_pred - area_intersect
	#计算面积loss（交集/并集）
	iou_loss_map = -torch.log((area_intersect + 1.0)/(area_union + 1.0))
	#计算angle loss
	angle_loss_map = 1. - torch.cos(angle_pred - angle_gt)
	return iou_loss_map, angle_loss_map


class Loss(nn.Module):
	def __init__(self, weight_angle=10):
		super(Loss, self).__init__()
		self.weight_angle = weight_angle

	def forward(self, gt_score, pred_score, gt_geo, pred_geo, ignored_map):
		#图像中不存在目标直接返回0
		if torch.sum(gt_score) < 1:
			return torch.sum(pred_score + pred_geo) * 0
		#score loss 采用Dice方式计算，没有采用log熵计算，为了防止样本不均衡问题
		classify_loss = get_dice_loss(gt_score, pred_score*(1-ignored_map))
		#geo loss采用Iou方式计算（计算每个像素点的loss）
		iou_loss_map, angle_loss_map = get_geo_loss(gt_geo, pred_geo)
		#计算一整张图的loss，angle_loss_map*gt_score去除不是目标点的像素（感觉这句话应该放在前面减少计算量，放在这里没有减少计算loss的计算量）
		angle_loss = torch.sum(angle_loss_map*gt_score) / torch.sum(gt_score)
		iou_loss = torch.sum(iou_loss_map*gt_score) / torch.sum(gt_score)
		geo_loss = self.weight_angle * angle_loss + iou_loss#这里的权重设置为1
		print('classify loss is {:.8f}, angle loss is {:.8f}, iou loss is {:.8f}'.format(classify_loss, angle_loss, iou_loss))
		return geo_loss + classify_loss
