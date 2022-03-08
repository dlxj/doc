# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 计算透视变换参数矩阵
def cal_perspective_params(img, points):
    # 设置偏移点。如果设置为(0,0),表示透视结果只显示变换的部分（也就是画框的部分）
    offset_x = 100
    offset_y = 100
    img_size = (img.shape[1], img.shape[0])
    src = np.float32(points)
    # 透视变换的四个点
    dst = np.float32([[offset_x, offset_y], [img_size[0] - offset_x, offset_y],
                      [offset_x, img_size[1] - offset_y], [img_size[0] - offset_x, img_size[1] - offset_y]])
    # 透视矩阵
    M = cv2.getPerspectiveTransform(src, dst)
    print(M)
    # 透视逆矩阵
    M_inverse = cv2.getPerspectiveTransform(dst, src)
    print(M_inverse)
    return M, M_inverse

# 透视变换
def img_perspect_transform(img, M):
    img_size = (img.shape[1], img.shape[0])
    return cv2.warpPerspective(img, M, img_size)

def draw_line(img,p1,p2,p3,p4):
    points = [list(p1), list(p2), list(p3), list(p4)]
    # 画线
    img = cv2.line(img, p1, p2, (0, 0, 255), 3)
    img = cv2.line(img, p2, p4, (0, 0, 255), 3)
    img = cv2.line(img, p4, p3, (0, 0, 255), 3)
    img = cv2.line(img, p3, p1, (0, 0, 255), 3)
    return points,img

if __name__ == '__main__':
    # 观察图像像素大小，便于手动选点
    #img = cv2.imread('book.jpg')
    img = cv2.imread('m.bmp')
    plt.figure()
    plt.imshow(img)
    plt.show()
    cv2.waitKey(0)
    # 选取四个点，分别是左上、右上、左下、右下
    points, img = draw_line(img, (932, 318), (1809, 299), (972, 2645), (1849, 2622))
    cv2.imshow('test01',img)
    cv2.waitKey(0)
    cv2.imwrite('test01.png',img)
    M, M_inverse = cal_perspective_params(img, points)
    trasform_img = img_perspect_transform(img, M)
    # 观察透视图像像素大小
    plt.figure()
    plt.imshow(trasform_img)
    plt.show()
    cv2.imshow('test02.png',trasform_img)
    cv2.waitKey(0)
    cv2.imwrite('test02.png',trasform_img)
    
    