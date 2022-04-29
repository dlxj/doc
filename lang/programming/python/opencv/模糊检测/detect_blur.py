# detect_blur.py
# https://yanshilin.xyz/%e4%bd%bf%e7%94%a8opencv%e5%af%b9%e6%89%8b%e6%9c%ba%e4%b8%ad%e7%85%a7%e7%89%87%e8%bf%9b%e8%a1%8c%e6%a8%a1%e7%b3%8a%e6%a3%80%e6%b5%8b/
# import the necessary packages
from imutils import paths
import argparse
import cv2
import numpy as np

def variance_of_laplacian(image):
  # compute the Laplacian of the image and then return the focus
  # measure, which is simply the variance of the Laplacian
  return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=False, default=r"D:\GitHub\doc\lang\programming\python\opencv\模糊检测",
  help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
  help="focus measures that fall below this value will be considered 'blurry'")

args = vars(ap.parse_args())


# loop over the input images
for imagePath in paths.list_images(args["images"]):
  # load the image, convert it to grayscale, and compute the
  # focus measure of the image using the Variance of Laplacian
  # method

  """
  虽然python 3 使用统一编码解决了中文字符串的问题, 但在使用opencv中imread函数读取中文路径图像文件时仍会报错
  此时可借助于numpy 先将文件数据读取出来, 然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
  """
  image = cv2.imdecode(np.fromfile(imagePath, dtype=np.uint8), -1)

  # image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  fm = variance_of_laplacian(gray)
  text = "Not Blurry"
  # if the focus measure is less than the supplied threshold,
  # then the image should be considered "blurry"
  if fm < args["threshold"]:
    text = "Blurry"
  # show the image
  cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
  cv2.imshow("Image", image)
  key = cv2.waitKey(0)