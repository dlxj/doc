
# https://blog.csdn.net/jizhidexiaoming/article/details/124273621

import os.path
 
import cv2
import torch
 
from mmocr.apis.inference import model_inference
from mmocr.apis import init_detector
from mmocr.utils import revert_sync_batchnorm
from mmocr.datasets.pipelines.crop import crop_img
from mmocr.core.visualize import det_recog_show_result
 
textdet_models = {
            'DB_r18': {
                'config':
                'dbnet/dbnet_r18_fpnc_1200e_icdar2015.py',
                'ckpt':
                'dbnet/'
                'dbnet_r18_fpnc_sbn_1200e_icdar2015_20210329-ba3ab597.pth'
            },
            'DB_r50': {
                'config':
                'dbnet/dbnet_r50dcnv2_fpnc_1200e_icdar2015.py',
                'ckpt':
                'dbnet/'
                'dbnet_r50dcnv2_fpnc_sbn_1200e_icdar2015_20211025-9fe3b590.pth'
            },
            'DRRG': {
                'config':
                'drrg/drrg_r50_fpn_unet_1200e_ctw1500.py',
                'ckpt':
                'drrg/drrg_r50_fpn_unet_1200e_ctw1500_20211022-fb30b001.pth'
            },
            'FCE_IC15': {
                'config':
                'fcenet/fcenet_r50_fpn_1500e_icdar2015.py',
                'ckpt':
                'fcenet/fcenet_r50_fpn_1500e_icdar2015_20211022-daefb6ed.pth'
            },
            'FCE_CTW_DCNv2': {
                'config':
                'fcenet/fcenet_r50dcnv2_fpn_1500e_ctw1500.py',
                'ckpt':
                'fcenet/' +
                'fcenet_r50dcnv2_fpn_1500e_ctw1500_20211022-e326d7ec.pth'
            },
            'MaskRCNN_CTW': {
                'config':
                'maskrcnn/mask_rcnn_r50_fpn_160e_ctw1500.py',
                'ckpt':
                'maskrcnn/'
                'mask_rcnn_r50_fpn_160e_ctw1500_20210219-96497a76.pth'
            },
            'MaskRCNN_IC15': {
                'config':
                'maskrcnn/mask_rcnn_r50_fpn_160e_icdar2015.py',
                'ckpt':
                'maskrcnn/'
                'mask_rcnn_r50_fpn_160e_icdar2015_20210219-8eb340a3.pth'
            },
            'MaskRCNN_IC17': {
                'config':
                'maskrcnn/mask_rcnn_r50_fpn_160e_icdar2017.py',
                'ckpt':
                'maskrcnn/'
                'mask_rcnn_r50_fpn_160e_icdar2017_20210218-c6ec3ebb.pth'
            },
            'PANet_CTW': {
                'config':
                'panet/panet_r18_fpem_ffm_600e_ctw1500.py',
                'ckpt':
                'panet/'
                'panet_r18_fpem_ffm_sbn_600e_ctw1500_20210219-3b3a9aa3.pth'
            },
            'PANet_IC15': {
                'config':
                'panet/panet_r18_fpem_ffm_600e_icdar2015.py',
                'ckpt':
                'panet/'
                'panet_r18_fpem_ffm_sbn_600e_icdar2015_20210219-42dbe46a.pth'
            },
            'PS_CTW': {
                'config': 'psenet/psenet_r50_fpnf_600e_ctw1500.py',
                'ckpt':
                'psenet/psenet_r50_fpnf_600e_ctw1500_20210401-216fed50.pth'
            },
            'PS_IC15': {
                'config':
                'psenet/psenet_r50_fpnf_600e_icdar2015.py',
                'ckpt':
                'psenet/psenet_r50_fpnf_600e_icdar2015_pretrain-eefd8fe6.pth'
            },
            'TextSnake': {
                'config':
                'textsnake/textsnake_r50_fpn_unet_1200e_ctw1500.py',
                'ckpt':
                'textsnake/textsnake_r50_fpn_unet_1200e_ctw1500-27f65b64.pth'
            },
            'Tesseract': {}
        }
 
textrecog_models = {
            'CRNN': {
                'config': 'crnn/crnn_academic_dataset.py',
                'ckpt': 'crnn/crnn_academic-a723a1c5.pth'
            },
            'SAR': {
                'config': 'sar/sar_r31_parallel_decoder_academic.py',
                'ckpt': 'sar/sar_r31_parallel_decoder_academic-dba3a4a3.pth'
            },
            'SAR_CN': {
                'config':
                'sar/sar_r31_parallel_decoder_chinese.py',
                'ckpt':
                'sar/sar_r31_parallel_decoder_chineseocr_20210507-b4be8214.pth'
            },
            'NRTR_1/16-1/8': {
                'config': 'nrtr/nrtr_r31_1by16_1by8_academic.py',
                'ckpt':
                'nrtr/nrtr_r31_1by16_1by8_academic_20211124-f60cebf4.pth'
            },
            'NRTR_1/8-1/4': {
                'config': 'nrtr/nrtr_r31_1by8_1by4_academic.py',
                'ckpt':
                'nrtr/nrtr_r31_1by8_1by4_academic_20211123-e1fdb322.pth'
            },
            'RobustScanner': {
                'config': 'robust_scanner/robustscanner_r31_academic.py',
                'ckpt': 'robustscanner/robustscanner_r31_academic-5f05874f.pth'
            },
            'SATRN': {
                'config': 'satrn/satrn_academic.py',
                'ckpt': 'satrn/satrn_academic_20211009-cb8b1580.pth'
            },
            'SATRN_sm': {
                'config': 'satrn/satrn_small.py',
                'ckpt': 'satrn/satrn_small_20211009-2cf13355.pth'
            },
            'ABINet': {
                'config': 'abinet/abinet_academic.py',
                'ckpt': 'abinet/abinet_academic-f718abf6.pth'
            },
            'SEG': {
                'config': 'seg/seg_r31_1by16_fpnocr_academic.py',
                'ckpt': 'seg/seg_r31_1by16_fpnocr_academic-72235b11.pth'
            },
            'CRNN_TPS': {
                'config': 'tps/crnn_tps_academic_dataset.py',
                'ckpt': 'tps/crnn_tps_academic_dataset_20210510-d221a905.pth'
            },
            'Tesseract': {}
        }
 
 
def single_inference(model, arrays, batch_mode, batch_size=0):
    def inference(m, a, **kwargs):
        return model_inference(m, a, **kwargs)
 
    result = []
    if batch_mode:
        if batch_size == 0:
            result = inference(model, arrays, batch_mode=True)
        else:
            n = batch_size
            arr_chunks = [
                arrays[i:i + n] for i in range(0, len(arrays), n)
            ]
            for chunk in arr_chunks:
                result.extend(inference(model, chunk, batch_mode=True))
    else:
        for arr in arrays:
            result.append(inference(model, arr, batch_mode=False))
    return result
 
 
def det_recog_kie_inference(det_model, recog_model, kie_model=None, imgs=None, batch_mode=False, recog_batch_size=0):
    end2end_res = []  # 所有图片的重要结果备份
 
    # 1， 定位（1orbatch）
    det_result = single_inference(det_model, imgs, batch_mode=batch_mode, batch_size=0)
    bboxes_list = [res['boundary_result'] for res in det_result]
 
    # 2, 识别（1orbatch）
    for img, bboxes in zip(imgs, bboxes_list):
        img_e2e_res = {}
        img_e2e_res['result'] = []  # 一张图片中检测到的所有文本位置，和内容
 
        box_imgs = []
        for bbox in bboxes:
            box_res = {}
            box_res['box'] = [round(x) for x in bbox[:-1]]  # 前8个是位置
            box_res['box_score'] = float(bbox[-1])  # 最后一个是概率
            box = bbox[:8]
            if len(bbox) > 9:  # 多边形bbox不止8个位置，返回的是轮廓点集合（xy,xy,...）
                min_x = min(bbox[0:-1:2])  # 从第一个开始到最后一个，间隔为2，找最小的x
                min_y = min(bbox[1:-1:2])  # 从第二个开始到最后一个，间隔为2，找最小的y
                max_x = max(bbox[0:-1:2])
                max_y = max(bbox[1:-1:2])
                box = [   # 最小外接矩形。
                    min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y
                ]
            # 2，裁剪
            box_img = crop_img(img, box)
            if batch_mode:
                box_imgs.append(box_img)  # 先打包成batch
            else:
                # 3，识别
                recog_result = model_inference(recog_model, box_img)
                text = recog_result['text']  # 文本内容
                text_score = recog_result['score']  # 概率
                if isinstance(text_score, list):
                    text_score = sum(text_score) / max(1, len(text))
                box_res['text'] = text
                box_res['text_score'] = text_score
            img_e2e_res['result'].append(box_res)
 
        if batch_mode:
            recog_results = single_inference(recog_model, box_imgs, True, recog_batch_size)
            for i, recog_result in enumerate(recog_results):
                text = recog_result['text']
                text_score = recog_result['score']
                if isinstance(text_score, (list, tuple)):
                    text_score = sum(text_score) / max(1, len(text))
                img_e2e_res['result'][i]['text'] = text
                img_e2e_res['result'][i]['text_score'] = text_score
        end2end_res.append(img_e2e_res)
    return end2end_res
 
 
# Post processing function for end2end ocr
def det_recog_pp(arrays, result, outputs=[None], imshow=True):
    final_results = []
    for arr, output, det_recog_result in zip(arrays, outputs, result):
        if output or imshow:
            res_img = det_recog_show_result(arr, det_recog_result, out_file=output)
            if imshow:
                cv2.namedWindow("inference results", cv2.WINDOW_NORMAL), cv2.imshow("inference results", res_img)
                cv2.waitKey()
                # mmcv.imshow(res_img, 'inference results')
 
 
if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
 
    img_dir = r"./demo"
    img_name_list = os.listdir(img_dir)
    img_name_list = [ 'demo_text_ocr.jpg' ]
    for img_name in img_name_list:
        # img
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (640, 640))
        # detection
        config_dir = r'./configs'
        td = "DB_r50"
        #det_ckpt = r"D:\code\python\mmocr\tools\work_dirs\dbnet_r50_0415\epoch_80.pth"
        det_config = os.path.join(config_dir, "textdet/", textdet_models[td]['config'])
        if True or (not det_ckpt):
            det_ckpt = 'https://download.openmmlab.com/mmocr/textdet/' + textdet_models[td]['ckpt']
        detect_model = init_detector(det_config, det_ckpt, device=device)
        detect_model = revert_sync_batchnorm(detect_model)
 
        # recognition
        tr = "SEG"
        recog_ckpt = None
        recog_config = os.path.join(config_dir, "textrecog/", textrecog_models[tr]['config'])
        if True or (not recog_ckpt):
            recog_ckpt = 'https://download.openmmlab.com/mmocr/' + 'textrecog/' + textrecog_models[tr]['ckpt']
        recog_model = init_detector(recog_config, recog_ckpt, device=device)
        recog_model = revert_sync_batchnorm(recog_model)
 
        # Attribute check
        for model in list(filter(None, [recog_model, detect_model])):
            if hasattr(model, 'module'):
                model = model.module
 
        det_recog_result = det_recog_kie_inference(
            detect_model, recog_model, kie_model=None, imgs=[img], batch_mode=False)
        det_recog_pp([img], det_recog_result, outputs=['./result.jpg'], imshow=False)
 