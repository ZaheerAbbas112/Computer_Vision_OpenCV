
## Reading and displying an image
# library import
import cv2 as cv

img = cv.imread("resources/ds.jpg")
img = cv.resize(img, (650,180))

cv.imshow('ds',img)
cv.waitKey(0)
