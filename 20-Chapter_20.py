## Split your video into frames or image sequence

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('resources/video1.mkv')

frameNr = 0

while(True):
    ret, frame = cap.read()
    if ret:
        cv.imwrite(f'resources/frames/frame_{frameNr}.png', frame)
    else:
        break
    frameNr = frameNr+1
cap.release()
