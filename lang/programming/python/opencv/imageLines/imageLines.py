
import numpy as np
import cv2

def readImg(path):
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
    if (len(img.shape) > 2): # 1 个通道以上的是彩图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

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

    img_conv_removed = readImg('./img_conv_removed.jpg')

    # 膨胀加粗
    # rect_kernel2 = cv2.getStructuringElement(
    #     cv2.MORPH_RECT, (3, 3))  # 定义了20*2 大小的矩形核
    # img_conv_removed = cv2.dilate(img_conv_removed, rect_kernel2)

    # cv2.imshow("img_conv_removed", img_conv_removed)
    # cv2.waitKey()
    #img_conv_removed = cv2.bitwise_not(img_conv_removed, mask = None)  # 反色
    lines = cv2.HoughLinesP(
        img_conv_removed,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi/180,  # Angle resolution in radians
        threshold=50,  # Min number of votes for valid line
        minLineLength=10,  # Min allowed length of line
        maxLineGap=0  # Max allowed gap between line for joining them
    )

    img_color = cv2.cvtColor(img_conv_removed, cv2.COLOR_GRAY2BGR)
    for points in lines:
        # Extracted points nested in the list
        x1,y1,x2,y2=points[0]
        # Draw the lines joing the points
        # On the original image
        #cv2.line(img_origin, (x1,y1),(x2,y2),(0,0,255, 255), 2)  # 原图是四通道的BGRA(蓝绿红 + alpha 透明度)
        cv2.line(img_color, (x1,y1),(x2,y2),(0,0,255), 2)  # 看来无论原图怎么样，cv2 的三个通道顺序永远都是: BGR
    
    cv2.imshow("img_color", img_color)
    cv2.waitKey()

    img = cv2.imdecode(np.fromfile('./密密麻麻.bmp', dtype=np.uint8), -1)
    if (len(img.shape) > 2): # 1 个通道以上的是彩图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret, img = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY) # 二值化

    # 未反色前0 代表纯黑是前景色，255 代表纯白是背景色
    img = cv2.bitwise_not(img, mask = None)  # 反色

    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    img_removed = deleteSmallComponents(img)

    # 卷积, 只保留水平线
    kernel1 = np.array([ [1], [-1] ])
    img_conv = cv2.filter2D(src=img_removed, ddepth=-1, kernel=kernel1)

    img_conv_removed = deleteSmallComponents(img_conv)

    cv2.imwrite('img_conv_removed.jpg', img_conv_removed)

    # cv2.imshow("origin", img)
    # cv2.imshow("img_color", img_color)
    # cv2.imshow("img_removed", img_removed)
    cv2.imshow("img_conv", img_conv)
    cv2.imshow("img_conv_removed", img_conv_removed)
    cv2.waitKey()


