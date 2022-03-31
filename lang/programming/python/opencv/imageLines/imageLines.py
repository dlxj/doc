
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

# def lines(path):
#     imgData = np.fromfile(path, dtype=np.uint8)
#     img_origin = cv2.imdecode(imgData, -1)
#     img_rgb = cv2.cvtColor(np.asarray(img_origin), cv2.COLOR_BGRA2RGB)

#     # 转灰度图
#     img_gray = cv2.cvtColor(np.asarray(img_rgb), cv2.COLOR_BGR2GRAY)   #cv2.COLOR_RGB2BGR
#     print(type(img_gray))

#     w = img_gray.shape[0]
#     h = img_gray.shape[1]

#     # slice 子矩阵，既剪裁图像
#     img_crop = img_gray[0:w-30, 0:h-70]

#     # 二值化
#     ret, img_binary = cv2.threshold(img_crop, 92, 255, cv2.THRESH_BINARY_INV)
#     # imshow("1:二值操作", binaryImage)

#     # 开操作(将文字这些密集的“孔洞”给腐蚀掉，仅留下直线)
#     rect_kernel = cv2.getStructuringElement(
#         cv2.MORPH_RECT, (20, 2))  # 定义了20*2 大小的矩形核
#     img_opening = cv2.morphologyEx(img_binary, cv2.MORPH_OPEN, rect_kernel)

#     # 膨胀加粗
#     rect_kernel2 = cv2.getStructuringElement(
#         cv2.MORPH_RECT, (3, 3))  # 定义了20*2 大小的矩形核
#     img_dilate = cv2.dilate(img_opening, rect_kernel2)

#     #edges = cv2.Canny(img_dilate,50,150,apertureSize=3)


#     # Apply HoughLinesP method to
#     # to directly obtain line end points
#     lines = cv2.HoughLinesP(
#         img_dilate,  # Input edge image
#         1,  # Distance resolution in pixels
#         np.pi/180,  # Angle resolution in radians
#         threshold=30,  # Min number of votes for valid line
#         minLineLength=20,  # Min allowed length of line
#         maxLineGap=0  # Max allowed gap between line for joining them
#         )

#     #img_color = cv2.cvtColor(img_origin, cv2.COLOR_BGR2RGB)


#     for points in lines:
#       # Extracted points nested in the list
#       x1,y1,x2,y2=points[0]
#       # Draw the lines joing the points
#       # On the original image
#       #cv2.line(img_origin, (x1,y1),(x2,y2),(0,0,255, 255), 2)  # 原图是四通道的BGRA(蓝绿红 + alpha 透明度)
#       cv2.line(img_rgb, (x1,y1),(x2,y2),(0,0,255), 2)  # 看来无论原图怎么样，cv2 的三个通道顺序永远都是: BGR
      

#     cv2.imshow("origin", img_origin)
#     cv2.imshow("croped", img_crop)
#     cv2.imshow("binary", img_binary)
#     cv2.imshow("opening", img_opening)
#     cv2.imshow("dilate", img_dilate)  
#     cv2.imshow("result", img_rgb)

#     cv2.waitKey(0)

if __name__ == '__main__':

    """
        图片的左上角是坐标原点, x 轴向右是正方向, y 轴向下是正方向 
    """

    #lines('./img_conv_removed.jpg')

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

        x1,y1,x2,y2=points[0]

        cv2.line(img_color, (x1,y1),(x2,y2),(0,0,255), 2)  # 看来无论原图怎么样，cv2 的三个通道顺序永远都是: BGR
    
    #cv2.line(img_color, (0,500),(500,500),(0,0,255), 2)

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


