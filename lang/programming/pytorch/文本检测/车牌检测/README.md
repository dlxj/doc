# license-plate-detect-recoginition-pytorch
- https://blog.csdn.net/nihate/article/details/115504611?spm=1001.2014.3001.5501
- https://github.com/hpc203/license-plate-detect-recoginition-pytorch

深度学习车牌检测与识别，检测结果包含车牌矩形框和4个角点，基于pytorch框架运行，
主程序是detect_rec_img.py，运行程序前需要确保您的机器安装了pytorch

车牌识别模块，可以更换成crnn网络做识别，也可以更换到传统图像处理方法分割字符后逐个字符识别，
在这个车牌检测和识别系统里，我觉得最重要的是前面的车牌检测与矫正模块，因为如果前面没做好，
那么后面输入到车牌识别模块里的图片是一个倾斜的车牌，这时候输出结果就出错了。

对于车牌检测，也可以使用图像分割的思想，例如使用UNet语义分割网络，分割出车牌，
二值化然后查找连通域，计算4个顶点
