
import numpy as np
import cv2

if __name__ == '__main__':

    img = cv2.imdecode(np.fromfile('../卷积(只保留水平线)/cleaned.jpg', dtype=np.uint8), -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret, img = cv2.threshold(img, 185, 255, cv2.THRESH_BINARY) # 二值化

    # 前提假设：原图是纯白表示空白像素；反色后纯黑表示空白像素
    #img = cv2.bitwise_not(img, mask = None)  # 反色

    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img_removed = img.copy()

    num, labels, stats, centroids = cv2.connectedComponentsWithStats(img)

    rows, cols = img.shape

    for x in range(cols):
        for y in range(rows):
            label = labels[y][x]
            left, up, w, h, area = stats[label]
            if (area < 20):
                cv2.rectangle(img_color, pt1=(left, up), pt2=(left+w,up+h), color=(255,0,0), thickness=1)
                img_removed[y][x] = 0


    cv2.imshow("origin", img)
    cv2.imshow("img_color", img_color)
    cv2.imshow("img_removed", img_removed)
    cv2.waitKey()


