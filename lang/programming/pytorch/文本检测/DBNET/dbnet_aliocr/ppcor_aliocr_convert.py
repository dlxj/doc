
"""

PPOCRLabel --lang ch  # 启动标注工具

cp autodl-tmp/train_data.zip . && \
unzip train_data.zip -d PaddleOCR

# https://github.com/PaddlePaddle/PaddleOCR/blob/static/doc/doc_ch/FAQ.md

# 7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on data.7z data/

新建文件夹 train_data, 要标注的图片全部放在里面

新建 train_data/Label.txt 内容如下
行中用 \t 分隔 , points 的标记顺序是 左上 右上  右下 左下
train_data/0093.bmp	[{"transcription":"参考答案及解析","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]
train_data/0094.bmp	[{"transcription":"其他内容","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]


给 PaddleOCR 用，前面是坐标和图片都变换；这里图像不变，坐标不变


将阿里OCR 的识别结果（图片和标注）转换成 icdar2015 格式 (注意：它的文本是含 utf8 bom 的)

给 mmocr 训练用。格式是 icdar2015 的格式，文件夹的组织方式是按照 mmocr 的要求创建的

"""


"""

! unzip ./GD500.zip -d DB/datasets

icdar2015 文本检测数据集
标注格式: x1,y1,x2,y2,x3,y3,x4,y4,text

其中, x1,y1为左上角坐标,x2,y2为右上角坐标,x3,y3为右下角坐标,x4,y4为左下角坐标。

# 表示text难以辨认。
"""




import random
from pathlib import Path
import os
import shutil
import glob
import base64
from importlib.resources import path
import math
import numpy as np
import cv2
import json
import decimal
import datetime
from pickletools import uint8
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)


def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()


def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json


def parse(s):
    return json.loads(s, strict=False)

# convert dict to string


def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


def transform(points, M):
    # points 算出四个点变换后移动到哪里了
    # points = np.array([[word_x,  word_y],              # 左上
    #                    [word_x + word_width, word_y],                 # 右上
    #                    [word_x + word_width, word_y + word_height],  # 右下
    #                    [word_x, word_y + word_height],  # 左下
    #                    ])
    # add ones
    ones = np.ones(shape=(len(points), 1))

    points_ones = np.hstack([points, ones])

    # transform points
    transformed_points = M.dot(points_ones.T).T

    transformed_points_int = np.round(
        transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

    return transformed_points_int


def cutPoly(img, pts):
    # img = cv2.imdecode(np.fromfile('./t.png', dtype=np.uint8), -1)
    # pts = np.array([[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]])

    # (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    croped = img[y:y+h, x:x+w].copy()

    # (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    # (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    # (4) add the white background
    bg = np.ones_like(croped, np.uint8)*255
    cv2.bitwise_not(bg, bg, mask=mask)
    dst2 = bg + dst

    # cv2.imwrite("croped.png", croped)
    # cv2.imwrite("mask.png", mask)
    # cv2.imwrite("dst.png", dst)
    # cv2.imwrite("dst2.png", dst2)

    return dst2


if __name__ == "__main__":

    root = 'train_data'
    tmp = 'tmp'
    label_path = os.path.join(root, 'Label.txt')
    
    key_path = os.path.join(root, 'keys.txt')

    fileState_path = os.path.join(root, 'fileState.txt')

    if os.path.exists(root):
        shutil.rmtree(root)
        # os.rmdir(root)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)

    if not os.path.exists(root):
        os.makedirs(root)

    if not os.path.exists(tmp):
        os.makedirs(tmp)

    label = ''
    keys = ''
    states = ''


    dic_words = {}  # 所有词

    # 开始转换

    # https://help.aliyun.com/document_detail/294540.html 阿里云ocr结果字段定义
    # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换

    dir_json = './data/json'  # '/yingedu/www/ocr_server/data/json'
    dir_img = './data/img'  # '/yingedu/www/ocr_server/data/img'

    g_count = 1
    g_count2 = 1


    json_paths = glob.glob('{}/*.json'.format(dir_json), recursive=False)

    for json_path in json_paths:

        arr = []

        base = Path(json_path).stem

        # if base == '0bf0383ece9a533683e615bf57525812':
        #     continue

        img_path = os.path.join(dir_img, '{}.txt'.format(base))

        if not os.path.exists(img_path):  # 没有相应的图片，可能被删除了
            print(f'Warnnig: no image {img_path}')
            continue

        jsn = load_json(json_path)

        if not ('prism_wordsInfo' in jsn):
            print(f'Warning: no charater in {img_path}')
            continue

        with open(img_path, "r", encoding="utf-8") as fp:
            imgdata = fp.read()
            imgdata = base64.b64decode(imgdata)
            imgdata = np.frombuffer(imgdata, np.uint8)
            img = cv2.imdecode(imgdata, cv2.IMREAD_UNCHANGED)

            # cv2.imshow('img', img)
            # cv2.waitKey(0)

        if len(img.shape) != 3:  # 转彩图
            img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # DBNet 原版只能处理彩图，这里转一下

        else:
            img_color = img.copy()

        img_color_origin = img_color.copy()
        img_color_origin2 = img_color.copy()

        name = f'{g_count}.jpg'
        dst_img_path = f'{root}/{name}'
        states += f'G:\\train_data\\{name}\t1\n'
        g_count += 1

        cv2.imwrite(dst_img_path, img)

        wordsInfo = jsn['prism_wordsInfo']
        for j in range(len(wordsInfo)):
            jo = wordsInfo[j]
            word = jo["word"]

            for w in list(word):
                if not (w in dic_words):
                    dic_words[w] = True

            # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换
            angle = jo['angle']

            img_color = img_color_origin.copy()

            word_x = jo['x']
            word_y = jo['y']
            word_width = jo['width']
            word_height = jo['height']

            if abs(angle) == 90 or abs(angle) == 270:
                word_width = jo['height']
                word_height = jo['width']
            elif angle != 0:

                # 变换前画出绿框，方便追踪点的前后变化
                # img_color = cv2.rectangle(img_color, (word_x, word_y), (
                #     word_x + word_width, word_y + word_height), (0, 255, 0), 2)  # 矩形的左上角, 矩形的右下角

                # cv2.imshow("green", img_color)
                # cv2.waitKey(0)

                # 变换前的多边形蓝框
                points = np.array([
                    [word_x,  word_y],                             # 左上
                    [word_x + word_width, word_y],                 # 右上
                    [word_x + word_width, word_y + word_height],  # 右下
                    [word_x, word_y + word_height],                # 左下
                ])

                # # cv2.fillPoly(img_color, pts=[points], color=(255, 0, 0)) # 填充
                # cv2.polylines(img_color, [points], isClosed=True, color=(
                #     255, 0, 0), thickness=1)  # 只画线，不填充

                # cv2.imshow("polys", img_color)
                # cv2.waitKey(0)

                # 获取图像的维度，并计算中心
                (h, w) = img_color.shape[:2]
                (cX, cY) = (w // 2, h // 2)

                # - (cX,cY): 旋转的中心点坐标
                # - 180: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
                # - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
                # 1° = π/180弧度   1 弧度 =  180 / 3.1415926   // 0.0190033 是Mathematica 算出来的弧度，先转换成角度  // -0.0190033 * (180 / 3.1415926)
                M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
                img_color = cv2.warpAffine(img_color, M, (w, h))
                img_color_transform = img_color.copy()

                # cv2.imshow("after trans", img_color)
                # cv2.waitKey(0)

                # https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html  # 原理
                # https://stackoverflow.com/questions/30327659/how-can-i-remap-a-point-after-an-image-rotation # How can I remap a point after an image rotation?
                # 如何得到移动后的坐标点

                # points 算出四个点变换后移动到哪里了
                points = np.array([[word_x,  word_y],              # 左上
                                   # 右上
                                   [word_x + word_width, word_y],
                                   [word_x + word_width, word_y + \
                                       word_height],  # 右下
                                   [word_x, word_y + word_height],  # 左下
                                   ])
                # add ones
                ones = np.ones(shape=(len(points), 1))

                points_ones = np.hstack([points, ones])

                # transform points
                transformed_points = M.dot(points_ones.T).T

                transformed_points_int = np.round(
                    transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

                # cv2.polylines(img_color, [transformed_points_int], isClosed=True, color=(
                #     0, 0, 255), thickness=2)  # 画转换后的点

                # cv2.polylines(img_color_origin, [points], isClosed=True, color=(
                #     random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

                # cv2.imshow("orgin", img_color_origin)
                # cv2.waitKey(0)

            # 四个角的位置 # 左上、右上、右下、左下，当NeedRotate为true时，如果最外层的angle不为0，需要按照angle矫正图片后，坐标才准确（错，经验证不需要）
            pos = jo["pos"]
            x = int(pos[0]["x"])  # 左上
            y = int(pos[0]["y"])

            x2 = int(pos[2]["x"])  # 右下
            y2 = int(pos[2]["y"])

            lu = [pos[0]['x'], pos[0]['y']]  # left up  四个角顺时针方向数
            ru = [pos[1]['x'], pos[1]['y']]
            rd = [pos[2]['x'], pos[2]['y']]
            ld = [pos[3]['x'], pos[3]['y']]

            # 生成 icdar2015 格式的人工标记训练数据（用于训练 mmocr）
            # gt_txt_list.append( "{},{},{},{},{},{},{},{},{}".format(lu[0], lu[1], ru[0], ru[1], rd[0], rd[1], ld[0], ld[1], word) )

            # 绘制矩形
            start_point = (x, y)  # 矩形的左上角

            end_point = (x2, y2)  # 矩形的右下角

            color = (0, 0, 255)  # BGR

            thickness = 2

            # 逐行画框
            # img_color_origin2 = cv2.rectangle(img_color_origin2, start_point, end_point, color, thickness)
            # cv2.imshow("box", img_color_origin2)

            # cv2.waitKey(0)

            points = [lu, ru, rd, ld]

            points0 = np.array([[word_x,  word_y],              # 左上
                                  # 右上
                                  [word_x + word_width, word_y],
                                    [word_x + word_width, word_y + \
                                     word_height],  # 右下
                                    [word_x, word_y + word_height],  # 左下
                                  ])
            points1 = np.array([lu, ru, rd, ld])

            if not (abs(angle) == 90 or abs(angle) == 270) and angle != 0:
                points = transform(points, M)
            else:
                points = np.array(points)

            ps3 = np.array(
                [
                    [min(points[0][0], points1[0][0]), min(
                        points[0][1], points1[0][1])],  # 左上(取最两者中最小的)

                    [max(points[1][0], points1[1][0]), min(
                        points[1][1], points1[1][1])],  # 右上

                    [max(points[2][0], points1[2][0]), max(
                        points[2][1], points1[2][1])],  # 右下

                    [min(points[3][0], points1[3][0]), max(
                        points[3][1], points1[3][1])]  # 左下
                ]
            )

            img_cuted = cutPoly(img, points1)
            cv2.imwrite(f'./tmp/{g_count2}.jpg', img_cuted)
            with open(f'./tmp/{g_count2}.txt', 'w', encoding='utf-8') as f:
                f.write(word)
            g_count2 += 1

            # cv2.polylines(img_color_origin, [points], isClosed=True, color=(   # 多边形，框得比较全
            #     100, 0, 255), thickness=2)  # 只画线，不填充

            
            arr.append( {"transcription":f"{word}","points":[lu, ru, rd, ld],"difficult":False} )


            cv2.polylines(img_color_origin, [points1], isClosed=True, color=(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

            # cv2.polylines(img_color_origin, [ps3], isClosed=True, color=(255, 0, 0), thickness=2)

            # cv2.imshow("orgin", img_color_origin)
            # cv2.waitKey(0)

            # break


        arr_str = string(arr)
        line = f'{dst_img_path}\t{arr_str}\n'
        label += line

        print( f'{g_count - 1} / {len(json_paths)} task done.' )

    ks = list( dic_words.keys() )

    keys = '\n'.join(ks)

    with open(label_path, "w", encoding='utf-8') as fp:
        fp.write(label)

    with open(key_path, "w", encoding='utf-8') as fp:
        fp.write(keys)

    with open(fileState_path, "w", encoding='utf-8') as fp:
        fp.write(states)

    print('all task done.')
