
"""

将阿里OCR 的识别结果（图片和标注）转换成 icdar2015 格式 (注意：它的文本是含 utf8 bom 的)

给 mmocr 训练用。格式是 icdar2015 的格式，文件夹的组织方式是按照 mmocr 的要求创建的

"""


"""

! unzip ./GD500.zip -d DB/datasets

icdar2015 文本检测数据集
标注格式: x1,y1,x2,y2,x3,y3,x4,y4,text

其中, x1,y1为左上角坐标,x2,y2为右上角坐标,x3,y3为右下角坐标,x4,y4为左下角坐标。 

### 表示text难以辨认。
"""

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
    return json.loads(s, strict=False )

# convert dict to string
def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


import base64
import numpy as np
import cv2

import glob
import os
from pathlib import Path

import random


if __name__ == "__main__":
    
    # 验证原版的文本标记框
    # im = './train_images/img_1.jpg'
    # gt = './train_gts/gt_img_1.txt'

    # 验证自已生成的标记框
    im = './icdar2015_aliocr/imgs/training/img_1.jpg'
    gt = './icdar2015_aliocr/annotations/training/gt_img_1.txt'

    if os.path.exists( gt ):

        items = []
        reader = open(gt, 'r', encoding='utf-8-sig').readlines()
        for line in reader:
            item = {}
            parts = line.strip().split(',')
            label = parts[-1]
            if 'TD' in gt and label == '1':
                label = '###'
            line = [i.strip('\ufeff').strip('\xef\xbb\xbf') for i in parts]
            if 'icdar' in gt:
                poly = np.array(list(map(float, line[:8]))).reshape(
                    (-1, 2)).tolist()
            else:
                num_points = math.floor((len(line) - 1) / 2) * 2
                poly = np.array(list(map(float, line[:num_points]))).reshape(
                    (-1, 2)).tolist()
            item['poly'] = poly
            item['text'] = label
            item['points'] = poly  # 多边形是用一个个的点表示的，起点连接第二个点，第二个连接第三个 ... 最后一点连接起点，构成一个闭合的区域
            item['ignore'] = True if label == '###' else False  # 此标记表示文字模糊不可辨认，文本框的标记是不可靠的
            items.append( item )

        img = cv2.imdecode(np.fromfile(im, dtype=np.uint8), -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # DBNet 原版代码只能处理彩图，所以统一处理成彩图
    
        for i in range( len(items) ):
            poly = items[i]['poly']
            poly = np.array(poly)
            poly = poly.astype(np.int32)

            #cv2.fillPoly(img, pts=[ poly ], color=(0, 0, 255))  

            b = random.randint(0, 255) # 用来生成[a,b]之间的随意整数，包括两个边界值。
            g = random.randint(0, 255)
            r = random.randint(0, 255)

            cv2.polylines(img, [ poly ], isClosed = True, color = (b, g, r), thickness = 1) # 只画线，不填充  # 就是画线，从起点连到第二个点 ... 最后一个点连到第一个点

        #cv2.imwrite("poly.jpg", img)

        # cv2.imshow("poly", img)
        # cv2.waitKey()


    # 开始转换

    out_dir = 'icdar2015_aliocr'

    # https://help.aliyun.com/document_detail/294540.html 阿里云ocr结果字段定义
        # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换

    dir_json = './data/json' # '/yingedu/www/ocr_server/data/json'
    dir_img = './data/img' # '/yingedu/www/ocr_server/data/img'

    train_list = []
    train_list_txt_path = os.path.join( out_dir, 'train_list.txt' )




    json_paths = glob.glob('{}/*.json'.format(dir_json), recursive=True)
        
    for json_path in json_paths:

        base = Path(json_path).stem

        img_path = os.path.join(dir_img, '{}.txt'.format(base) )

        if not os.path.exists(img_path): # 没有相应的图片，可能被删除了
            continue

        jsn = load_json(json_path)

        with open(img_path, "r", encoding="utf-8") as fp:
            imgdata = fp.read()
            imgdata = base64.b64decode(imgdata)
            imgdata = np.frombuffer(imgdata, np.uint8)
            img = cv2.imdecode(imgdata, cv2.IMREAD_UNCHANGED)

            # cv2.imshow('img', img)
            # cv2.waitKey(0)

        if len(img.shape) != 3:  # 转彩图
            img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # DBNet 原版只能处理彩图，这里转一下

        else:
            img_color = img.copy()


        # 生成1000 张一模一样的图
        for i in range(1, 1000+1):

            num_img = i

            img_name = "img_{}.jpg".format(num_img)
            gt_name = "gt_img_{}.txt".format(num_img)

            gt_txt_list = []

            train_list.append( img_name )
            # num_img += 1

            img_path = os.path.join( out_dir, 'imgs', 'training', img_name )
            img_gt_path = os.path.join( out_dir, 'annotations', 'training', gt_name )

            cv2.imwrite(img_path, img)

            wordsInfo = jsn['prism_wordsInfo']
            for j in range( len(wordsInfo) ):
                jo = wordsInfo[j]
                word = jo["word"]
                angle = jo['angle'] # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换
                word_x = jo['x']
                word_y = jo['y']
                word_width = jo['width']
                word_height = jo['height']

                if abs(angle) == 90 or abs(angle) == 270:
                    word_width = jo['height']
                    word_height = jo['width']
                elif angle != 0:

                    # 变换前画出绿框，方便追踪点的前后变化
                    img_color = cv2.rectangle(img_color, (word_x, word_y), (word_x + word_width, word_y + word_height), (0, 255, 0), 2)  # 矩形的左上角, 矩形的右下角


                    # 获取图像的维度，并计算中心
                    (h, w) = img_color.shape[:2]
                    (cX, cY) = (w // 2, h // 2)

                    # - (cX,cY): 旋转的中心点坐标
                    # - 180: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
                    # - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
                    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)  # 1° = π/180弧度   1 弧度 =  180 / 3.1415926   // 0.0190033 是Mathematica 算出来的弧度，先转换成角度  // -0.0190033 * (180 / 3.1415926)
                    img_color = cv2.warpAffine(img_color, M, (w, h))

                    cv2.imshow("after trans", img_color)
                    cv2.waitKey(0)

                    # https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html  # 原理
                        # https://stackoverflow.com/questions/30327659/how-can-i-remap-a-point-after-an-image-rotation # How can I remap a point after an image rotation?
                            # 如何得到移动后的坐标点



                    # points
                    points = np.array([[word_x,  word_y],
                        [175., 0.],
                        [105., 200.],
                        [105., 215.],
                    ])
                    # add ones
                    ones = np.ones(shape=(len(points), 1))

                    points_ones = np.hstack([points, ones])

                    # transform points
                    transformed_points = M.dot(points_ones.T).T

                    word_x, word_y = transformed_points[0]
                    word_x, word_y = np.round([word_x, word_y], decimals=0).astype(np.int32)

                    img_color = cv2.rectangle(img_color, (word_x, word_y), (word_x + word_width, word_y + word_height), (0, 0, 255), 2)  # 矩形的左上角, 矩形的右下角
                    # img_color = cv2.rectangle(img_color, (word_x, word_y), (word_x + word_width, word_y + word_height), (0, 0, 255), 2)  # 矩形的左上角, 矩形的右下角
                    cv2.imshow("box", img_color)
                    cv2.waitKey(0)

                pos = jo["pos"] # 四个角的位置 # 左上、右上、右下、左下，当NeedRotate为true时，如果最外层的angle不为0，需要按照angle矫正图片后，坐标才准确
                x = int(pos[0]["x"]) # 左上
                y = int(pos[0]["y"])

                x2 = int(pos[2]["x"]) # 右下
                y2 = int(pos[2]["y"])

    
                lu = ( pos[0]['x'], pos[0]['y'] ) # left up  四个角顺时针方向数
                ru = ( pos[1]['x'], pos[1]['y'] )
                rd = ( pos[2]['x'], pos[2]['y'] )
                ld = ( pos[3]['x'], pos[3]['y'] )

                # 生成 icdar2015 格式的人工标记训练数据（用于训练 mmocr）
                #gt_txt_list.append( "{},{},{},{},{},{},{},{},{}".format(lu[0], lu[1], ru[0], ru[1], rd[0], rd[1], ld[0], ld[1], word) )

                # 绘制矩形
                start_point = (x, y) # 矩形的左上角
  
                end_point = (x2, y2) # 矩形的右下角
  
                color = (0, 0, 255) # BGR
  
                thickness = 2
  

                # 逐行画框
                # img_color = cv2.rectangle(img_color, start_point, end_point, color, thickness)
                # cv2.imshow("box", img_color)
                # cv2.waitKey(0)


                lastx_mini = 0  # 下一个字符x 坐标的下界（肯定不小于这个值）
                prew = 0 # 上一个字符的宽度
                words = ""
                charInfo = jo["charInfo"]

                min_cx = 9999   # 最小左上角
                min_cy = 9999

                max_cxcw = -1   # 最大右下角
                max_cych = -1

                for i in range( len(charInfo) ):
                    joc = charInfo[i]
                    c = joc["word"]
                    cx = int(joc["x"])
                    cy = int(joc["y"])
                    cw = int(joc["w"])
                    ch = int(joc["h"])

                    if cx < min_cx:
                        min_cx = cx
                    if cy < min_cy:
                        min_cy = cy

                    if cx + cw > max_cxcw:
                        max_cxcw = cx + cw

                    if cy + ch > max_cych:
                        max_cych = cy + ch

                    # 绘制矩形
                    start_point = (cx, cy) # 矩形的左上角
  
                    end_point = (cx + cw, cy + ch) # 矩形的右下角
  
                    color = (0, 0, 255) # BGR
  
                    thickness = 2
  
            
                    # 逐字画框
                    img_color = cv2.rectangle(img_color, start_point, end_point, color, thickness)
                    # cv2.imshow("box", img_color)
                    # cv2.waitKey(0)

                # 这个框更准一些
                img_color = cv2.rectangle(img_color, (min_cx, min_cy), (max_cxcw, max_cych), (0, 255, 0), thickness)
                # cv2.imshow("box", img_color)
                # cv2.waitKey(0)

                # fix me: 如果上面的行框的左边要比这里更左，那就以行框的左边为准
                    # 因为发现单个字的框会有漏字的现想

                gt_txt_list.append( "{},{},{},{},{},{},{},{},{}".format(min_cx, min_cy, max_cxcw, min_cy, max_cxcw, max_cych, min_cx, max_cych, word) )


            gt_txt = '\n'.join(gt_txt_list)

            with open(img_gt_path, "w", encoding='utf-8-sig') as fp:
                fp.write(gt_txt)
