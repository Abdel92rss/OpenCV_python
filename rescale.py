import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.75):
    # This function rescales the frame to a given scale (photos, videos, live video)
    width = int(frame.shape[1] * scale) # Get the width of the frame and multiply it by the scale
    height = int(frame.shape[0] * scale) # Get the height of the frame and multiply it by the scale
    dimensions = (width, height) # Create a tuple with the new dimensions

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # Resize the frame to the new dimensions using INTER_AREA interpolation



def changeRes(width, height):
    # This function changes the resolution of the live video (webcam)
    capture.set(3, width) # Set the width of the video capture object
    capture.set(4, height) # Set the height of the video capture object

capture = cv.VideoCapture('/Users/abdel9rss/Computing_vision/Resources/Videos/dog.mp4') # Read from a video file

while True:
    isTrue, frame = capture.read() # Read a frame from the video
    frame_resized = rescaleFrame(frame) # Rescale the frame to 50% of its original size
    #cv.imshow('Video', frame) # Display the original frame in a window
    cv.imshow('Video Resized', frame_resized) # Display the resized frame in a window

    if cv.waitKey(20) & 0xFF==ord('d'): # Wait for 20ms and check if 'd' key is pressed
        break


capture = cv.VideoCapture(0) # Read from the webcam (0 is the default camera, 1 is the second camera, etc.)
changeRes(640, 480) # Change the resolution of the webcam to 640x480


while True:
    isTrue, frame = capture.read() # Read a frame from the webcam
    cv.imshow('Webcam', frame) # Display the frame in a window

    if cv.waitKey(1) & 0xFF==ord('d'): # Wait for 20ms and check if 'd' key is pressed
        break


capture.release() # Release the video capture object
cv.destroyAllWindows() # Close all windows

