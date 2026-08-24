import cv2 as cv

# Read an image
img = cv.imread('/Users/abdel9rss/Computing_vision/Resources/Photos/cat.jpg')

# Display the image in a window (press x to close the window)
cv.imshow('Cat', img)
cv.waitKey(0)


img = cv.imread('/Users/abdel9rss/Computing_vision/Resources/Photos/cat_large.jpg')

#cv.imshow use the dimension of the monitor to display the image, if the image is larger than the monitor, it will be scaled down to fit the monitor size
cv.imshow('Cat Large', img) 
cv.waitKey(0)


# Read a video
capture = cv.VideoCapture(0) # Read from the webcam (0 is the default camera, 1 is the second camera, etc.)
capture = cv.VideoCapture('Videos/dog.mp4') # Read from a video file

while True:
    isTrue, frame = capture.read() # Read a frame from the video
    #isTrue is a boolean value that indicates if the frame was read successfully, frame is the actual frame that was read
    cv.imshow('Video', frame) # Display the frame in a window

    if cv.waitKey(20) & 0xFF==ord('d'): # Wait for 20ms and check if 'd' key is pressed
        break

#OxFF is a bitwise AND operator that is used to get the last 8 bits of the key pressed. This is necessary because cv.waitKey() returns a 32-bit integer, but we only want to check the last 8 bits (the ASCII value of the key pressed).
capture.release() # Release the video capture object
cv.destroyAllWindows() # Close all windows 

#All don't work because size of the image is 0,0, which means that the image was not read successfully. This can happen if the path to the image is incorrect or if the image file is corrupted.
#error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'