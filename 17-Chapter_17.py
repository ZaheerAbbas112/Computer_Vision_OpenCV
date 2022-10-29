## Joining two images

import cv2 as cv
import numpy as np

img1 = cv.imread("resources/image.jpg")
img1 = cv.resize(img1, (500,300))
img2 = cv.imread("resources/image_gray.png")
img2 = cv.resize(img2, (500,300))


# stacking same image
# 1- Horizontal stack
hor_img = np.hstack((img1, img2))

# 2- Vertical stack
ver_stack = np.vstack((img1, img2))




# cv.imshow('Horizontal', hor_img)
cv.imshow('Vertical', ver_stack)
cv.waitKey(0)
cv.destroyAllWindows()