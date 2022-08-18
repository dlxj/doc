
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

    json = load_json(json_path)

    with open(img_path, "r", encoding="utf-8") as fp:
        imgdata = fp.read()
        imgdata = base64.b64decode(imgdata)
        imgdata = np.frombuffer(imgdata, np.uint8)
        img = cv2.imdecode(imgdata, cv2.IMREAD_UNCHANGED)

    cv2.imshow('img', img)
    cv2.waitKey(0)

    a = 1

