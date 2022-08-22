
"""

! unzip ./GD500.zip -d DB/datasets

icdar2015 文本检测数据集
标注格式: x1,y1,x2,y2,x3,y3,x4,y4,text

其中, x1,y1为左上角坐标,x2,y2为右上角坐标,x3,y3为右下角坐标,x4,y4为左下角坐标。 

### 表示text难以辨认。
"""

import math
import numpy as np
import cv2


if __name__ == "__main__":
    
    # 验证原版的文本标记框
    im = './train_images/IMG_0855.JPG'
    gt = './train_gts/IMG_0855.JPG.txt'

    # 验证自已生成的标记框
    # im = './GD500/train_images/IMG_0456.JPG'
    # gt = './GD500/train_gts/IMG_0456.JPG.txt'
    
    items = []
    reader = open(gt, 'r').readlines()
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
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    for i in range( len(items) ):
        poly = items[i]['poly']
        poly = np.array(poly)
        poly = poly.astype(np.int32)

        #cv2.fillPoly(img, pts=[ poly ], color=(0, 0, 255))  # 就是画线，从起点连到第二个点 ... 最后一个点连到第一个点
        cv2.polylines(img, [ poly ], isClosed = True, color = (0, 0, 255), thickness = 1) # 只画线，不填充

    #cv2.imwrite("poly.jpg", img)

    cv2.imshow("poly", img)
    cv2.waitKey()


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

dir_json = './json' # '/yingedu/www/ocr_server/data/json'
dir_img = './img' # '/yingedu/www/ocr_server/data/img'

train_list = []
train_list_txt_path = os.path.join( 'GD500', 'train_list.txt' )

# 生成500 张一模一样的图
for i in range(500):

    num_img = i


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

        img_name = "IMG_{:04d}.JPG".format(num_img)
        gt_txt_name = "{}.txt".format(img_name)
        gt_name = "IMG_{:04d}.gt".format(num_img)

        gt_txt_list = []

        train_list.append( img_name )
        # num_img += 1

        img_path = os.path.join( 'GD500', 'train_images', img_name )
        img_gt_txt_path = os.path.join( 'GD500', 'train_gts', gt_txt_name )
        img_gt_path = os.path.join( 'GD500', 'train_gts', gt_name )


        cv2.imwrite(img_path, img)

        wordsInfo = jsn['prism_wordsInfo']
        for j in range( len(wordsInfo) ):
            jo = wordsInfo[j]
            word = jo["word"]
            pos = jo["pos"] # 四个角的位置 # 左上、右上、右下、左下，当NeedRotate为true时，如果最外层的angle不为0，需要按照angle矫正图片后，坐标才准确
            x = int(pos[0]["x"]) # 左上
            y = int(pos[0]["y"])

            x2 = int(pos[2]["x"]) # 右下
            y2 = int(pos[2]["y"])

    
            lu = ( pos[0]['x'], pos[0]['y'] ) # left up  四个角顺时针方向数
            ru = ( pos[1]['x'], pos[1]['y'] )
            rd = ( pos[2]['x'], pos[2]['y'] )
            ld = ( pos[3]['x'], pos[3]['y'] )

            gt_txt_list.append( "{},{},{},{},{},{},{},{},{}".format(lu[0], lu[1], ru[0], ru[1], rd[0], rd[1], ld[0], ld[1], 0) )  # TD500 的 1 代表文本不可辨认, 0 是正常文本

            # 绘制矩形
            start_point = (x, y) # 矩形的左上角
  
            end_point = (x2, y2) # 矩形的右下角
  
            color = (0, 0, 255) # BGR
  
            thickness = 2
  
            img_color = cv2.rectangle(img_color, start_point, end_point, color, thickness)

            # 逐行画框
            # cv2.imshow("box", img_color)
            # cv2.waitKey(0)

            # 生成 TD500 格式的人工标记训练数据（用于训练DBNet）



            # "{:02d}".format(number)


            lastx_mini = 0  # 下一个字符x 坐标的下界（肯定不小于这个值）
            prew = 0 # 上一个字符的宽度
            words = ""
            charInfo = jo["charInfo"]

            for i in range( len(charInfo) ):
                joc = charInfo[i]
                c = joc["word"]
                cx = int(joc["x"])
                cy = int(joc["y"])
                cw = int(joc["w"])
                ch = int(joc["h"])

                # 绘制矩形
                start_point = (cx, cy) # 矩形的左上角
  
                end_point = (cx + cw, cy + ch) # 矩形的右下角
  
                color = (0, 0, 255) # BGR
  
                thickness = 2
  
                img_color = cv2.rectangle(img_color, start_point, end_point, color, thickness)
            
                # 逐字画框
                # cv2.imshow("box", img_color)
                # cv2.waitKey(0)

        gt_txt = '\n'.join(gt_txt_list)

        with open(img_gt_txt_path, "w") as fp:
            fp.write(gt_txt)
    
        with open(img_gt_path, "w") as fp:
            fp.write(gt_txt)


        #GD500/test_gts/gt_IMG_0000.txt

train_list_txt = '\n'.join( train_list )
with open(train_list_txt_path, "w") as fp:
    fp.write(train_list_txt)

a = 1

