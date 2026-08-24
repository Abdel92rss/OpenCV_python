import cv2 as cv 
import numpy as np  

img = cv.imread('/Users/abdel9rss/Computing_vision/Resources/Photos/cat.jpg')
cv.imshow('Cat', img)
#Dimension 
dimensions = img.shape
#print(dimensions)

#Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.COLOR_BGR2GRAY convert BGR2GRAY

cv.imshow('Gray', gray)


img = cv.imread('/Users/abdel9rss/Computing_vision/Resources/Photos/park.jpg')
#Blur 
# Applique un flou gaussien sur l'image source 'img'
# - img : L'image d'entrée (matrice NumPy).
# - size : La taille de la matrice de convolution / noyau gaussien (ksize).
# - sigmaX (implicite ici, mis à 0 si omit) : Écart-type du noyau selon l'axe X.
# - cv.BORDER_DEFAULT : Mode de gestion des bordures de l'image lors du filtrage (padding).
size = (5,5)
blurred_img = cv.GaussianBlur(img, size, cv.BORDER_DEFAULT)
cv.imshow('Blur', blurred_img)


#Edge cascade 
canny = cv.Canny(blurred_img,125,175)
cv.imshow('Canny', canny)

#Dilated image

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)
#It performs a morphological dilation: it expands or "thickens" the white areas (foreground pixels) of a binary image, particularly after edge detection like Canny.

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('eroded', eroded)

#Resize 
rezided = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', rezided)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)
