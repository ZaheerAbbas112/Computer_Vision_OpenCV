## How to change the perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread("resources/warp.jpg")
print(img.shape)

#  defining points
point1 = np.float32([[78,251], [380,126], [201,467], [504,277]])
width = 532
height = 594
point2 = np.float32([[0,0], [width,0], [0,height], [width, height]])

matrix = cv. getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))

cv.imshow('Original', img)
cv.imshow('Transformed', out_img)
cv.imwrite('resources/warp_perspective.png', out_img)









cv.waitKey(0)
cv.destroyAllWindows