import pytesseract
import cv2
from pytesseract import Output

img = cv2.imread('7001.jpg')
height = img.shape[0]
width = img.shape[1]

d = pytesseract.image_to_boxes(img, output_type=Output.DICT)
n_boxes = len(d['char'])
for i in range(n_boxes):
    (text,x1,y2,x2,y1) = (d['char'][i],d['left'][i],d['top'][i],d['right'][i],d['bottom'][i])
    cv2.rectangle(img, (x1,height-y1), (x2,height-y2) , (0,255,0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)