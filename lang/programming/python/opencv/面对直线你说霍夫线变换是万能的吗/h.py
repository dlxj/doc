
"""
https://mp.weixin.qq.com/s?__biz=MzA4ODgyMDg0MQ==&mid=100001057&idx=1&sn=ebfd3cf30ffb3a48909bd309fa59f82d&chksm=1025182727529131c5c63d02663bfc517b89c23f4884c4d49334fee27d12947b792e9b36643f#rd
面对直线，你说霍夫线变换是万能的吗

https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/?ref=gcse

doc\lang\programming\opencv summary.md

"""

import numpy as np
import cv2

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均适用。
"""

if __name__ == '__main__':

    imgData = np.fromfile('./填空题.png', dtype=np.uint8)
    img_origin = cv2.imdecode(imgData, -1)
    img_rgb = cv2.cvtColor(np.asarray(img_origin), cv2.COLOR_BGRA2RGB)

    # 转灰度图
    img_gray = cv2.cvtColor(np.asarray(img_origin), cv2.COLOR_BGR2GRAY)   #cv2.COLOR_RGB2BGR
    print(type(img_gray))

    w = img_gray.shape[0]
    h = img_gray.shape[1]

    # slice 子矩阵，既剪裁图像
    img_crop = img_gray[0:w-30, 0:h-70]

    # 二值化
    ret, img_binary = cv2.threshold(img_crop, 92, 255, cv2.THRESH_BINARY_INV)
    # imshow("1:二值操作", binaryImage)

    # 开操作(将文字这些密集的“孔洞”给腐蚀掉，仅留下直线)
    rect_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (20, 2))  # 定义了20*2 大小的矩形核
    img_opening = cv2.morphologyEx(img_binary, cv2.MORPH_OPEN, rect_kernel)

    # 膨胀加粗
    rect_kernel2 = cv2.getStructuringElement(
        cv2.MORPH_RECT, (3, 3))  # 定义了20*2 大小的矩形核
    img_dilate = cv2.dilate(img_opening, rect_kernel2)

    #edges = cv2.Canny(img_dilate,50,150,apertureSize=3)


    # Apply HoughLinesP method to
    # to directly obtain line end points
    lines = cv2.HoughLinesP(
        img_dilate,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi/180,  # Angle resolution in radians
        threshold=30,  # Min number of votes for valid line
        minLineLength=20,  # Min allowed length of line
        maxLineGap=0  # Max allowed gap between line for joining them
        )

    #img_color = cv2.cvtColor(img_origin, cv2.COLOR_BGR2RGB)


    for points in lines:
      # Extracted points nested in the list
      x1,y1,x2,y2=points[0]
      # Draw the lines joing the points
      # On the original image
      #cv2.line(img_origin, (x1,y1),(x2,y2),(0,0,255, 255), 2)  # 原图是四通道的BGRA(蓝绿红 + alpha 透明度)
      cv2.line(img_rgb, (x1,y1),(x2,y2),(0,0,255), 2)  # 看来无论原图怎么样，cv2 的三个通道顺序永远都是: BGR
      

    cv2.imshow("origin", img_origin)
    cv2.imshow("croped", img_crop)
    cv2.imshow("binary", img_binary)
    cv2.imshow("opening", img_opening)
    cv2.imshow("dilate", img_dilate)  
    cv2.imshow("result", img_rgb)

    cv2.waitKey(0)



    """

cpp origin


# include <iostream>
# include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
  Mat srcImage, dstImage, binaryImage;
  srcImage = imread("原图.png",0);  
  imshow("原图", srcImage);
  
  waitKey(0);
  return 0;
}

 //剪裁图片
  Mat roiImage = srcImage(Rect(0, 0, srcImage.cols - 70, srcImage.rows - 30));
  imshow("0:抠图操作", roiImage);

    //对图像进行二值化
  threshold(roiImage, binaryImage, 92, 255, THRESH_BINARY_INV );
  imshow("1:二值操作", binaryImage);


  Mat morhpImage;
  Mat kernel = getStructuringElement(MORPH_RECT, Size(20, 2), Point(-1, -1));//自定义一个核
  morphologyEx(binaryImage, morhpImage, MORPH_OPEN, kernel, Point(-1, -1));//开操作
  imshow("2:开操作", morhpImage);


  Mat dilateImage;
  kernel = getStructuringElement(MORPH_RECT, Size(3, 3), Point(-1, -1));
  dilate(morhpImage, dilateImage, kernel);
  imshow("3:膨胀操作", dilateImage);

  
  vector<Vec4i> lines;
  HoughLinesP(dilateImage, lines, 1, CV_PI / 180.0, 30, 20.0, 0);
  dstImage = srcImage.clone();
  cvtColor(dstImage, dstImage, COLOR_GRAY2BGR);
  for (size_t t = 0; t < lines.size(); t++) {
    Vec4i ln = lines[t];
    line(dstImage, Point(ln[0], ln[1]), Point(ln[2], ln[3]), Scalar(0, 0, 255), 2, 8, 0);
  }
  imshow("4:绘制直线", dstImage);

    """

