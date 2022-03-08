

import numpy as np
import cv2
import base64

"""
虽然python 3 使用统一编码解决了中文字符串的问题，但在使用opencv中imread函数读取中文路径图像文件时仍会报错
此时可借助于numpy 先将文件数据读取出来，然后使用opencv中imdecode函数将其解码成图像数据。此方法对python 2 和3均使用。
"""

# https://www.yisu.com/zixun/317058.html
    # 直线检测

if __name__ == '__main__':

    np_array = np.fromfile('./密密麻麻.bmp', dtype=np.uint8)
    img = cv2.imdecode(np_array, -1)
    # bytes = img.tobytes()  # 转字节数组  # 或者使用img.tostring()，两者是等价的
        # 注意了：得到的bytes数据并不等价于open(file,"rb")数据

    # 把img 对象编码为jpg 格式
    success, encoded_image = cv2.imencode(".jpg", img) 
    # 将数组转为bytes
    bytes = encoded_image.tobytes() # 等价于tostring() 

    b64 = base64.b64encode(bytes).decode('ascii')  # base64字符串

    bytes2 = base64.b64decode(b64)  # 编码解码以后是否还正确

    with open("密密麻麻_base64.txt", "w") as fp:
        fp.write(b64)
    
    with open("yyyyyyyyyyyyy.jpg", "wb") as fp:
        fp.write(bytes2)  # 成功，我们自已写的 bytes

    cv2.imwrite('./ttttttttttttttttttt.jpg', img)  # 成功，opencv 保存 img 对象



    
    
