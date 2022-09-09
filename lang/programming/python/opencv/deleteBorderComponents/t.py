import cv2
import numpy as np

# read image
# img = cv2.imread('lungs.jpg')
img = cv2.imread('5.jpg')

h, w = img.shape[:2]

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# add 1 pixel white border all around
pad = cv2.copyMakeBorder(gray, 1,1,1,1, cv2.BORDER_CONSTANT, value=255)
h, w = pad.shape

# create zeros mask 2 pixels larger in each dimension
mask = np.zeros([h + 2, w + 2], np.uint8)

# floodfill outer white border with black
img_floodfill = cv2.floodFill(pad, mask, (0,0), 0, (5), (0), flags=8)[1]

# remove border
img_floodfill = img_floodfill[1:h-1, 1:w-1]    

# save cropped image
cv2.imwrite('lungs_floodfilled.png',img_floodfill)

# show the images
cv2.imshow("img_floodfill", img_floodfill)
cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# import numpy as np
# img = cv2.imread('5.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)[1]
# cv2.bitwise_not(thresh, thresh)
# kernel = np.ones((7,7),np.uint8)
# kernel2 = np.ones((3,3),np.uint8)
# marker = thresh.copy()
# marker[1:-1,1:-1]=0
# while True:
#     tmp=marker.copy()
#     marker=cv2.dilate(marker, kernel2)
#     marker=cv2.min(thresh, marker)
#     difference = cv2.subtract(marker, tmp)
#     if cv2.countNonZero(difference) == 0:
#         break

# mask=cv2.bitwise_not(marker)
# mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
# out=cv2.bitwise_and(img, mask_color)
# cv2.imwrite('out.png', out)
# cv2.imshow('result', out )
# cv2.waitKey(0) # waits until a key is pressed
# cv2.destroyAllWindows()