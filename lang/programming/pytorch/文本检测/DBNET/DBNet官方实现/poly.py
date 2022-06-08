

"""
显示人工标记的区域
"""

import numpy as np
import math
import cv2

if __name__ == "__main__":
    
    im = './TD_TR/TD500/train_images/IMG_0855.JPG'
    gt = './TD_TR/TD500/train_gts/IMG_0855.JPG.txt'
    
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

    cv2.imshow("origin", img)
    cv2.waitKey()