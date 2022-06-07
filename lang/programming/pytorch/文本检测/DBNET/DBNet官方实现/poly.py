

"""
显示人工标记的区域
"""

import numpy as np
import math

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

