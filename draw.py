import numpy as np
import cv2 as cv


blank = np.zeros((500, 500, 3), dtype='uint8') #blank image 
#unit8 means 0-255 values for each pixel in the image
#3 channels for RGB 


blank[:] = 0, 0, 255 #fill the image with red color
#bgr values for green is (0, 255, 0)
#bgr values for red is (0, 0, 255)

cv.imshow('Red', blank) #show the image
cv.waitKey(0)

#square 
blank = np.zeros((500, 500, 3), dtype='uint8') #blank image
blank[200:300, 200:300] = 0, 255, 0 #draw a green square in the image
cv.imshow('Green Square', blank) #show the image
cv.waitKey(0)

#rectangle
blank = np.zeros((500, 500, 3), dtype='uint8') #blank image
pt1 = (0,0) #top left corner
# Note on coordinates in OpenCV / NumPy:
# - In OpenCV functions (like cv2.rectangle), points are specified as (x, y),
#   where x is the horizontal axis (column) and y is the vertical axis (row).
# - In NumPy array indexing blank[y, x], the first index corresponds to the vertical axis (y / row)
#   and the second index corresponds to the horizontal axis (x / column).
pt2 = (250, 250) #center of the image
color = (255, 0, 0) #blue color in BGR
cv.rectangle(blank, pt1, pt2, color, thickness=cv.FILLED) #draw a blue rectangle in the image
#cv.FILLED means fill the rectangle with color, if you want to draw only the border of the rectangle, you can use thickness=2 or any other value
pt2 = (blank.shape[1]//2, blank.shape[0]//2) #center of the image
color = (0, 255, 0) #green color in BGR
cv.rectangle(blank, pt1, pt2, color, thickness=cv.FILLED) #draw a green rectangle in the image with thickness of 5 pixels
cv.imshow('Green Rectangle', blank) #show the image
cv.waitKey(0)


#circle
blank = np.zeros((500, 500, 3), dtype='uint8') #blank image
pt1 = (250, 250) #center of the image
radius = 50 #radius of the circle
color = (0, 0, 255) #red color in BGR
cv.circle(blank, pt1, radius, color, thickness=cv.FILLED) #draw a red circle in the image
cv.imshow('Red Circle', blank) #show the image
cv.waitKey(0)   

#line
pt1 = (0, 0) #top left corner
pt2 = (500, 500) #bottom right corner
color = (255, 255, 0) #cyan color in BGR
cv.line(blank, pt1, pt2, color, thickness=3) #draw a cyan line in the image with thickness of 3 pixels
cv.imshow('Cyan Line', blank) #show the image
cv.waitKey(0)   

#text
text = 'Hello World' #text to be written on the image
pt1 = (blank.shape[1]//2, blank.shape[0]//2) #position of the debut of the text, in this case, it is the center of the image
cv.putText(blank, text, pt1, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) #write the text on the image
#cv.FONT_HERSHEY_SIMPLEX is the font type, 1 is the font scale, (255, 255, 255) is the color of the text in BGR, 2 is the thickness of the text
cv.imshow('Text', blank) #show the image
cv.waitKey(0)



