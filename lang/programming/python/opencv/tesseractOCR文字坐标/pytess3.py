import pytesseract
import cv2
from pytesseract import Output

img = cv2.imread('7001.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (text,x,y,w,h) = (d['text'][i],d['left'][i],d['top'][i],d['width'][i],d['height'][i])
    cv2.rectangle(img, (x,y), (x+w,y+h) , (0,255,0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)