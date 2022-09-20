
# 7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on data.7z data/

"""

conda install numpy opencv-python==4.6.0.66 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

"""

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


img_root = 'all_data'

if not os.path.exists('data'):
    os.makedirs('data/img')
    os.makedirs('data/json')

root_img1 = './data/img' # 'xx/www/ocr_server/data/img'
root_json1 = './data/json' # 'xx/www/ocr_server/data/json'


root_img2 = './data/img' # 'yy/www/ocr_server/data/img'
root_json2 = './data/json' # 'yy/www/ocr_server/data/json'

dic_shape = {}

g_count = 0

for root, dirs, files in os.walk( root_json2 ):
    
    if g_count >= 5000:
        break
    
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

            # cv2.imshow('img', img)
            # cv2.waitKey(0)

        if len(img.shape) != 3:  # 转彩图
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # DBNet 原版只能处理彩图，这里转一下


        # 把相同分辨率的图全部放一起
        
        h, w = img.shape[0:2]
        sp = f'{w}x{h}'

        if sp != '2115x3046':
            continue

        p1 = os.path.join(img_root, sp, 'data/img')
        p2 = os.path.join(img_root, sp, 'data/json')

        if not os.path.exists(p1):
            os.makedirs(p1)

        if not os.path.exists(p2):
            os.makedirs(p2)

        dst1 =  os.path.join(p1, os.path.basename(img_path))
        dst2 =  os.path.join(p2, os.path.basename(json_path))

        shutil.copyfile(img_path, dst1)
        shutil.copyfile(json_path, dst2)

        g_count += 1

        if g_count >= 5000:
            break

print('done.')