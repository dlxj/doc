
# https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga107a78bf7cd25dec05fb4dfc5c9e765f
# https://www.programcreek.com/python/example/89340/cv2.connectedComponentsWithStats
# https://learnopencv.com/color-spaces-in-opencv-cpp-python/

import numpy as np
import cv2
import random


"""
虽然python 3 使用统一编码解决了中文字符串的问题, 但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来, 然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

if __name__ == '__main__':

    img = cv2.imdecode(np.fromfile('./small3.jpg', dtype=np.uint8), -1)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    num, labels, stats, centroids = cv2.connectedComponentsWithStats(img)

    Rows, Cols = img.shape

    color = []
    color.append([0, 0, 0]) # 背景色
    for i in range(num):
        color.append( [
            random.randint(0, 32767) % 256,
            random.randint(0, 32767) % 256,
            random.randint(0, 32767) % 256 
        ])

    src_color = np.zeros((Rows,Cols, 3), dtype=np.uint8)

    for x in range(Rows):
        for y in range(Cols):
            label = labels[x][y]  # 图像总共有 num 个连通块, labels 会告诉你每一个坐标属于哪一个连通块
                # color 总共分配了 num + 1 种随机颜色, 每一个连通块都能分到一个随机色 
            src_color[x][y] = color[label]  

    cv2.imshow("Perpesctive transform", src_color)
    cv2.waitKey()