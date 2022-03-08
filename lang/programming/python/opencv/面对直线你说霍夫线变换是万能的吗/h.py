
"""
https://mp.weixin.qq.com/s?__biz=MzA4ODgyMDg0MQ==&mid=100001057&idx=1&sn=ebfd3cf30ffb3a48909bd309fa59f82d&chksm=1025182727529131c5c63d02663bfc517b89c23f4884c4d49334fee27d12947b792e9b36643f#rd
面对直线，你说霍夫线变换是万能的吗
"""

import numpy as np
import cv2

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

if __name__ == '__main__':

    imgData = np.fromfile('./填空题.png', dtype=np.uint8)
    img = cv2.imdecode(imgData, -1)

    w = img.shape[0]
    h = img.shape[1]

    # slice 子矩阵，既剪裁图像
    img_crop = img[ 0:w-30, 0:h-70]

    cv2.imshow("origin", img)
    cv2.imshow("croped", img_crop)
    cv2.waitKey(0)


    # img = cv2.mat_wrapper.Mat(img)

    #crop_img = img[0:y+h, 0:x+w]

    #img2 = img.crop((0, 0, 10, 10))  # (left, upper, right, lower)

    #img(cv2.Rect(0, 0, 10, 10))

    # 剪裁图片
    #Mat roiImage = srcImage(Rect(0, 0, srcImage.cols - 70, srcImage.rows - 30));
    #imshow("0:抠图操作", roiImage)






#include <iostream>
#include <opencv2/opencv.hpp>

# using namespace std;
# using namespace cv;

# int main()
# {
#   Mat srcImage, dstImage, binaryImage;
#   srcImage = imread("原图.png",0);  
#   imshow("原图", srcImage);
  
#   waitKey(0);
#   return 0;
# }


