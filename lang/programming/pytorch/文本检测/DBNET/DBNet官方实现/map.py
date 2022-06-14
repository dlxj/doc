
# 制作概率图
# probability map, w*h*1 , 代表像素点是文本的概率

import numpy as np
import math
import cv2
from collections import OrderedDict
from shapely.geometry import Polygon
import pyclipper

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
                (-1, 2)) #.tolist()
        else:
            num_points = math.floor((len(line) - 1) / 2) * 2
            poly = np.array(list(map(float, line[:num_points]))).reshape(
                (-1, 2)) #.tolist()
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
        #cv2.polylines(img, [ poly ], isClosed = True, color = (0, 0, 255), thickness = 1) # 只画线，不填充


    #cv2.imwrite("poly.jpg", img)

    # cv2.imshow("origin", img)
    # cv2.waitKey()

    min_text_size = 8
    shrink_ratio = 0.4

    h, w = img.shape[:2]

    gt = np.zeros((1, h, w), dtype=np.float32)
    mask = np.ones((h, w), dtype=np.float32)

    for i in range(len(items)):
        polygon = items[i]['poly']
        height = max(polygon[:, 1]) - min(polygon[:, 1])
        width = max(polygon[:, 0]) - min(polygon[:, 0])
        polygon_shape = Polygon(polygon)
        distance = polygon_shape.area * \
            (1 - np.power(shrink_ratio, 2)) / polygon_shape.length
        subject = [tuple(l) for l in polygon]
        padding = pyclipper.PyclipperOffset()
        padding.AddPath(subject, pyclipper.JT_ROUND,
           pyclipper.ET_CLOSEDPOLYGON)
        shrinked = padding.Execute(-distance)
        if shrinked == []:
            cv2.fillPoly(mask, polygon.astype(
            np.int32)[np.newaxis, :, :], 0)
            items[i]['ignore'] = True
            continue
        shrinked = np.array(shrinked[0]).reshape(-1, 2)
        cv2.fillPoly(gt[0], [shrinked.astype(np.int32)], 1)

        cv2.polylines(img, [ shrinked ], isClosed = True, color = (0, 0, 255), thickness = 1)


    cv2.imshow("概率图", gt[0])
    cv2.imshow("缩小后的文本区域", img)
    cv2.waitKey()