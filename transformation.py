import numpy as np 
import cv2 as cv 

#Translation 
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

#-x --> Left
#-y --> Up
#x --> Right
#y --> Down

img = cv.imread('/Users/abdel9rss/Computing_vision/Resources/Photos/park.jpg')

translated = translate(img,100,100)
cv.imshow('translated', translated)

# Rotation 
def rotate(img, angle, rotPoint=None):
    # Get the image height and width
    height, width = img.shape[:2]

    # Use the image center as the rotation point if none is provided
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # Create the rotation matrix
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Keep the original image dimensions
    dimensions = (width, height)

    # Rotate and return the image
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -90)
cv.imshow('Rotated', rotated)

#Flipping 
flip = cv.flip(img, -1)
# 0  : Vertical flip (around the x-axis)
# 1  : Horizontal flip (around the y-axis)
# -1 : Both axes flip (combined horizontal and vertical)
cv.imshow('flip',flip)



cv.waitKey(0)
    

