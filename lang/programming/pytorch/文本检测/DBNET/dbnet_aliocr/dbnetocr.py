
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

# message = "Python is fun"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
# msg = base64.b64decode(base64_message).decode('ascii')

# print(base64_message)

import glob
import os
from pathlib import Path

dir_json = './json' # '/yingedu/www/ocr_server/data/json'
dir_img = './img' # '/yingedu/www/ocr_server/data/img'

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
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    wordsInfo = jsn['prism_wordsInfo']
    for j in range( len(wordsInfo) ):
        jo = wordsInfo[j]
        word = jo["word"]
        pos = jo["pos"] # 四个角的位置 # 左上、右上、右下、左下，当NeedRotate为true时，如果最外层的angle不为0，需要按照angle矫正图片后，坐标才准确
        x = int(pos[0]["x"]) # 左上
        y = int(pos[0]["y"])

        x2 = int(pos[2]["x"]) # 右下
        y2 = int(pos[2]["y"])

        
        # 绘制矩形
        start_point = (x, y) # 矩形的左上角
  
        end_point = (x2, y2) # 矩形的右下角
  
        color = (0, 0, 255) # BGR
  
        thickness = 2
  
        img = cv2.rectangle(img, start_point, end_point, color, thickness)

        # 逐行画框
        cv2.imshow("box", img)
        cv2.waitKey(0)


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
  
            img = cv2.rectangle(img, start_point, end_point, color, thickness)
            
            # 逐字画框
            cv2.imshow("box", img)
            cv2.waitKey(0)

    a = 1

