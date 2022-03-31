
import numpy as np
import cv2

def deleteSmallComponents(img):
    """
        注意：图片必须已反色
            未反色前0 代表纯黑是前景色, 255 代表纯白是背景色
    """
    img_removed = img.copy()

    num, labels, stats, centroids = cv2.connectedComponentsWithStats(img)

    rows, cols = img.shape

    for x in range(cols):
        for y in range(rows):
            label = labels[y][x]
            left, up, w, h, area = stats[label]
            if (area < 10):  # 面积小于10 像素的移除(反色后0 代表空白)
                cv2.rectangle(img_color, pt1=(left, up), pt2=(left+w,up+h), color=(255,0,0), thickness=1)
                img_removed[y][x] = 0
    
    return img_removed

if __name__ == '__main__':

    img = cv2.imdecode(np.fromfile('./密密麻麻.bmp', dtype=np.uint8), -1)
    if (len(img.shape) > 2): # 1 个通道以上的是彩图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret, img = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY) # 二值化

    # 未反色前0 代表纯黑是前景色，255 代表纯白是背景色
    img = cv2.bitwise_not(img, mask = None)  # 反色

    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # img_removed = img.copy()

    # num, labels, stats, centroids = cv2.connectedComponentsWithStats(img)

    # rows, cols = img.shape

    # for x in range(cols):
    #     for y in range(rows):
    #         label = labels[y][x]
    #         left, up, w, h, area = stats[label]
    #         if (area < 10):  # 面积小于10 像素的移除(反色后0 代表空白)
    #             cv2.rectangle(img_color, pt1=(left, up), pt2=(left+w,up+h), color=(255,0,0), thickness=1)
    #             img_removed[y][x] = 0

    img_removed = deleteSmallComponents(img)

    # 卷积, 只保留水平线
    kernel1 = np.array([ [1], [-1] ])
    img_conv = cv2.filter2D(src=img_removed, ddepth=-1, kernel=kernel1)

    img_conv_removed = deleteSmallComponents(img_conv)

    # cv2.imshow("origin", img)
    # cv2.imshow("img_color", img_color)
    # cv2.imshow("img_removed", img_removed)
    cv2.imshow("img_conv", img_conv)
    cv2.imshow("img_conv_removed", img_conv_removed)
    cv2.waitKey()


