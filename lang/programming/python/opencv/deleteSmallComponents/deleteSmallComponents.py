

from tokenize import String
import numpy as np
import cv2

if __name__ == '__main__':

    img = cv2.imdecode(np.fromfile('D:/GitHub/doc/lang/programming/python/opencv/deleteSmallComponents/booktitle.png', dtype=np.uint8), -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY) # 二值化

    # 前提假设：原图是纯白表示空白像素；反色后纯黑表示空白像素
    img = cv2.bitwise_not(img, mask = None)  # 反色

    num, labels, stats, centroids = cv2.connectedComponentsWithStats(img)

    Rows, Cols = img.shape

    

    a = 1

    # ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
