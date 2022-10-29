## Image into Black & White image

import cv2 as cv
from cv2 import cvtColor
img = cv.imread("resources/image.jpg")
img1 = cv.resize(img, (300,200))
gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray, 127,255, cv.THRESH_BINARY)
cv.imshow('original', img1)
cv.imshow('gray', gray)
cv.imshow('Black and White', binary)
cv.waitKey(0)
cv.destroyAllWindows()
