
# 7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on data.7z data/

import os, hashlib, shutil
from pathlib import Path
import numpy as np
import cv2
import base64


def md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# m = md5('0861.jpg')

img_dir = '黑白'

if not os.path.exists('data'):
    os.makedirs('data/img')
    os.makedirs('data/json')

root_img1 = './data/img' # 'xx/www/ocr_server/data/img'
root_json1 = './data/json' # 'xx/www/ocr_server/data/json'


root_img2 = './data/img' # 'yy/www/ocr_server/data/img'
root_json2 = './data/json' # 'yy/www/ocr_server/data/json'


for root, dirs, files in os.walk( root_json2 ):
    for name in files:

        json_path = os.path.join( root_json2, name )

        m = Path(json_path).stem

        img_path1 = os.path.join(root_img1, f'{m}.txt')
        img_path2 = os.path.join(root_img2, f'{m}.txt')

        img_path = ''

        if os.path.exists(img_path1):
            img_path = img_path1
        elif os.path.exists(img_path2):
            img_path = img_path2
        else:
            print(f'image {name} not exists!!!')
            continue
        
        with open(img_path, "r", encoding="utf-8") as fp:
            imgdata = fp.read()
            imgdata = base64.b64decode(imgdata)
            imgdata = np.frombuffer(imgdata, np.uint8)
            img = cv2.imdecode(imgdata, cv2.IMREAD_UNCHANGED)

            cv2.imshow('img', img)
            cv2.waitKey(0)

        if len(img.shape) != 3:  # 转彩图
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # DBNet 原版只能处理彩图，这里转一下




        json_path1 = os.path.join(root_json1, f'{m}.json')
        json_path2 = os.path.join(root_json2, f'{m}.json')

        img_path = ''
        json_path = ''

        if os.path.exists(img_path1):
            img_path = img_path1
        elif os.path.exists(img_path2):
            img_path = img_path2
        else:
            print(f'image {name} not exists!!!')
            continue
        
        if os.path.exists(json_path1):
            json_path = json_path1
        elif os.path.exists(json_path2):
            json_path = json_path2
        else:
            print(f'json {name} not exists ###')
            continue

        

        shutil.copyfile(img_path, f'data/img/{os.path.basename(img_path)}')
        shutil.copyfile(json_path, f'data/json/{os.path.basename(json_path)}')

print('done.')