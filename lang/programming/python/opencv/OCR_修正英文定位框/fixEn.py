
# https://ocrapi-advanced.taobao.com/ocrservice/advanced

import numpy as np
import cv2
import hashlib

import json
import decimal
import datetime

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


def md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def read_string(path):
    with open(path, "r", encoding='UTF-8') as f:
        return f.read()

def paiban(ali_result, points = None): # p1 左上角x, y 坐标, p2 右下角 x, y 坐标
    
    # 图片的左上角坐标，右下角坐标

    p1 = None
    p2 = None

    weight = int(ali_result["width"])
    height = int(ali_result["height"])

    if points == None:
        p1 = { 'X': 0, 'Y': 0 }
        p2 = { 'X': weight, 'Y': height }
    else:
        p1 = points.p1
        p2 = points.p2


    result = ""

    lastY = 999999

    firstX = 0

    wordsInfo = ali_result['prism_wordsInfo']

    leftest = 999999
    #
    # 先找出最左边的字符x 坐标
    #
    for j in range( len(wordsInfo) ):
        jo = wordsInfo[j]
        charInfo = jo["charInfo"]
        for i in range( len(charInfo) ):
            joc = charInfo[i]
            c = joc["word"]
            cx = int( joc["x"] )
            cy = int( joc["y"] )
            cw = int( joc["w"] )
            if cx < leftest:
                leftest = cx

    for j in range( len(wordsInfo) ):
        jo = wordsInfo[j]
        word = jo["word"]
        pos = jo["pos"] # 四个角的位置
        x = int(pos[0]["x"]) # 左上
        y = int(pos[0]["y"])
        #
        # 处理同一行的字符要不要加空格（一个字符一个字符的检查x 坐标，确定它们之间是不是有空格）
        #
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

            #
            # 只要指定矩形范围内的字符
            #
            if cx < p1['X'] or cx > p2['X']:
                continue
                    

            if cy < p1['Y'] or cy > p2['Y']:
                continue
            
            if j == 0:
                # 记录第一个字符的x 坐标
                firstX = cx

            if i == 0:
                #
                # 首字符缩进
                #
                if y - lastY >= 50 or j == 0:  # Y 坐标相差太大的不是同一行
                    ns = int( (cx - leftest) / 50.0 )
                    for k in range(ns): 
                        words += " "
                    
            if cx - lastx_mini < 40: # 如果这个字符的x 坐标和坐标下界的宽度相差不多，那么中间没有空格
                words = words + c
            else:
                if i == 0:
                    words = words + c
                else:
                    words = words + "  " + c

            prew = cw
            lastx_mini = cx + cw         


        #
        # 处理可能不是可一行的文本之间要不要加入换行
        #
        if y - lastY < 50: # Y 坐标相差不大的是同一行
            if result == "":
                result += words
            else:
                result += "  " + words
            
        else:
            # 换行
            result = result + "\n" + words
        
        lastY = y

    return result

if __name__ == '__main__':

    path = './10101.jpg'

    m5 = md5(path)

    path_ali_result = './data/json/{}.json'.format(m5)

    ali_result =read_string(path_ali_result)

    ali_result = parse(ali_result)

    text = paiban(ali_result)

    print(text)

    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("orgin", img)
    cv2.waitKey()

    print('ok.')

