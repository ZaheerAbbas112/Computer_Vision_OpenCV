## Basic functions or manipulator in open cv

from ctypes import resize
import cv2 as cv
import numpy as np
img = cv.imread('resources/image.jpg')
img = cv.resize(img, (500,400))

# resize
resize_img = cv.resize(img, (500,400))

# gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blurred image
blurr_img = cv.GaussianBlur(img, (7,7), 0)

# edge detection
edge_img = cv.Canny(img, 53,53)

# thickness of lines
mat_kernel = np.ones((3,3), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel), (8,8), iterations=1)

# make thinner outline
ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)

# cropping (we will use numpy library not open cv)
print("The size of my image is:", img.shape)
cropped_img = img[0:350, 0:300] # height,width






# cv.imshow('Original', img)
# cv.imshow('Resized', resize_img)
# cv.imshow('Gray', gray_img)
# cv.imshow('Blurr', blurr_img)
# cv.imshow('Edge', edge_img)
# cv.imshow('Dilated', dilated_img)
# cv.imshow('Erosion', ero_img)
cv.imshow('cropped', cropped_img)


cv.waitKey(0)

cv.destroyAllwindows()