
import cv2
import numpy as np
  

image = cv2.imdecode(np.fromfile('./cleaned.jpg',dtype=np.uint8), -1)

# 卷积, 只保留水平线
kernel1 = np.array([ [1], [-1] ])
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
  
cv2.imshow('Original', image)
cv2.imshow('conv', img)
  
cv2.waitKey()

