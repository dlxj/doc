

import argparse
import cv2
# import imutils # pip install imutils
import numpy as np
import base64

imgData = np.fromfile('./密密麻麻.bmp', dtype=np.uint8)
image = cv2.imdecode(imgData, -1)
# image=cv2.imread('book.jpg')
# 获取图像的维度，并计算中心
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# - (cX,cY): 旋转的中心点坐标
# - 180: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
# - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
M = cv2.getRotationMatrix2D((cX, cY), -0.0190033 * (180 / 3.1415926), 1.0)  # 1° = π/180弧度   1 弧度 =  180 / 3.1415926   // 0.0190033 是Mathematica 算出来的弧度，先转换成角度
rotated = cv2.warpAffine(image, M, (w, h))

# 顺时针旋转33度，并保证图像旋转后完整~,确保整个图都在视野范围
# 使用imutils.rotata 一行代码实现旋转
# rotated = imutils.rotate_bound(image, 180)
cv2.imshow(f"Rotated by {-0.0190033 * (180 / 3.1415926)} Degrees", rotated)
cv2.waitKey(0)


# bytes = img.tobytes()  # 转字节数组  # 或者使用img.tostring()，两者是等价的
  # 注意了：得到的bytes数据并不等价于open(file,"rb")数据

# 把img 对象编码为jpg 格式
success, encoded_image = cv2.imencode(".jpg", rotated)
# 将数组转为bytes
bytes = encoded_image.tobytes()  # 等价于tostring()

b64 = base64.b64encode(bytes).decode('ascii')  # base64字符串

bytes2 = base64.b64decode(b64)  # 编码解码以后是否还正确

with open("密密麻麻_base64.txt", "w") as fp:
    fp.write(b64)

with open("yyyyyyyyyyyyy.jpg", "wb") as fp:
    fp.write(bytes2)  # 成功，我们自已写的 bytes

cv2.imwrite('./ttttttttttttttttttt.jpg', rotated)  # 成功，opencv 保存 img 对象


# 对图像进行旋转
# USAGE
# python opencv_rotate.py
# 导入必要的包
# 构建命令行参数及解析
# --image 图像路径
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="zly1.jpg",
                help="path to the input image")
args = vars(ap.parse_args())
# 从磁盘加载图像并展示
image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)
cv2.imshow("Original", image)
# 获取图像的维度，并计算中心
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
# 逆时针以图像中心旋转45度
# - (cX,cY): 旋转的中心点坐标
# - 45: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
# - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
# OpenCV不会自动为整个旋转图像分配空间，以适应帧。旋转完可能有部分丢失。如果您希望在旋转后使整个图像适合视图，则需要进行优化，使用imutils.rotate_bound.
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
# 逆时针以图像中心旋转-90度图像
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
# 以任意点作为中心旋转图像
M = cv2.getRotationMatrix2D((10, 10), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Arbitrary Point", rotated)
# 使用imutils.rotata 一行代码实现旋转
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
# 顺时针旋转33度，并保证图像旋转后完整~,确保整个图都在视野范围
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
