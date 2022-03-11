# Importing Required Libraries
import cv2
import numpy as np
  
  
# The Below function is a modified version of the
# conventional way to rotate an image without
# cropping/cutting sides.
def ModifiedWay(rotateImage, angle):
    
    # Taking image height and width
    imgHeight, imgWidth = rotateImage.shape[0], rotateImage.shape[1]
  
    # Computing the centre x,y coordinates
    # of an image
    centreY, centreX = imgHeight//2, imgWidth//2
  
    # Computing 2D rotation Matrix to rotate an image
    rotationMatrix = cv2.getRotationMatrix2D((centreY, centreX), angle, 1.0)
  
    # Now will take out sin and cos values from rotationMatrix
    # Also used numpy absolute function to make positive value
    cosofRotationMatrix = np.abs(rotationMatrix[0][0])
    sinofRotationMatrix = np.abs(rotationMatrix[0][1])
  
    # Now will compute new height & width of
    # an image so that we can use it in
    # warpAffine function to prevent cropping of image sides
    newImageHeight = int((imgHeight * sinofRotationMatrix) +
                         (imgWidth * cosofRotationMatrix))
    newImageWidth = int((imgHeight * cosofRotationMatrix) +
                        (imgWidth * sinofRotationMatrix))
  
    # After computing the new height & width of an image
    # we also need to update the values of rotation matrix
    rotationMatrix[0][2] += (newImageWidth/2) - centreX
    rotationMatrix[1][2] += (newImageHeight/2) - centreY
  
    # Now, we will perform actual image rotation
    rotatingimage = cv2.warpAffine(
        rotateImage, rotationMatrix, (newImageWidth, newImageHeight))
  
    return rotatingimage
  
  
# Driver Code
# Loading an Image from Disk
Image = cv2.imread("rotate_src.jpg", 1)
  
  
# Performing 40 degree rotation
ModifiedVersionRotation = ModifiedWay(Image, 40)
  
# Display image on Screen
cv2.imshow("Original Image", Image)
  
# Display rotated image on Screen
cv2.imshow("Modified Version Rotation", ModifiedVersionRotation)
  
  
# To hold the GUI screen and control until it is detected
# the input for closing it, Once it is closed
# control will be released
cv2.waitKey(0)
  
# To destroy and remove all created GUI windows from
#screen and memory
cv2.destroyAllWindows()