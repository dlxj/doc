import os
import os.path
import cv2
import numpy as np
from math import cos,sin,pi
def rotate_angle(angle,image,center_xy,wh):
 
    (image_h, image_w) = image.shape[:2]
    cx, cy = image_w / 2, image_h / 2
    r_image=rotate_image(image, angle)
    x,y=center_xy
    r_center_xy=rotate_xy(x,y,angle,cx,cy)
    r_wh=rotate_wh(center_xy,wh,angle,cx,cy)
    return r_image,r_center_xy,r_wh
 
def rotate_image(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    (nW, nH)=(w,h)
 
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))
def rotate_wh(center_xy,wh,angle,cx,cy):
    '''angle = angle*pi/180
    print('angle,cos(angle)',angle,cos(angle))
    r_wh=np.abs(wh*cos(angle))'''
    s_x,s_y=center_xy-wh/2
    e_x,e_y=center_xy+wh/2
    r_s_x_s_y=rotate_xy(s_x,s_y,angle,cx,cy)
    r_s_x_e_y=rotate_xy(s_x,e_y,angle,cx,cy)
    r_e_x_s_y=rotate_xy(e_x,s_y,angle,cx,cy)
    r_e_x_e_y=rotate_xy(e_x,e_y,angle,cx,cy)
    r_x_y=np.array([r_s_x_s_y,r_s_x_e_y,r_e_x_s_y,r_e_x_e_y])
 
    min_xy=np.min(r_x_y,axis=0)
    max_xy=np.max(r_x_y,axis=0)
    return max_xy-min_xy
def rotate_xy(x,y,angle,cx,cy):
 
    """
    点(x,y) 绕(cx,cy)点旋转
    """
    angle = angle*pi/180
    x_new = (x-cx)*cos(angle) - (y-cy)*sin(angle)+cx
    y_new = (x-cx)*sin(angle) + (y-cy)*cos(angle)+cy
    return x_new,y_new
 
def save_image(image_path,image):
    cv2.imwrite(image_path,image)
    print('save image to path:',image_path)
 
 
 
image=cv2.imread('book.jpg')
image_rect=image*1
center_xy=np.array([150,250])
wh=np.array([100,50])
s_x,s_y=center_xy-wh/2
e_x,e_y=center_xy+wh/2
s_x,s_y,e_x,e_y=int(s_x),int(s_y),int(e_x),int(e_y)
cv2.rectangle(image, (s_x,s_y), (e_x,e_y), (0,255,255), 1)
 
angle=360
r_image,r_center_xy,r_wh=rotate_angle(angle,image,center_xy,wh)
 
s_x,s_y=r_center_xy-r_wh/2
e_x,e_y=r_center_xy+r_wh/2   
s_x,s_y,e_x,e_y=int(s_x),int(s_y),int(e_x),int(e_y)   
cv2.rectangle(r_image, (s_x,s_y), (e_x,e_y), (0,0,255), 1)
cv2.imwrite('rotaterotaterotaterotaterotaterotate.jpg', r_image)
