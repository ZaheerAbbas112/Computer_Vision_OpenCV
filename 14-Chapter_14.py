## How to draw lines, and shapes in python

import cv2 as cv
import numpy as np

# Draw a canvas, 0 is for black, 1 is for white
img = np.zeros((600,600)) # black
img1 = np.ones((600,600))  # white

# print size
print("The size of our canvas is:", img.shape)
# print(img)
 # adding colors to the canvas
colored_img = np.zeros((600,600,3), np.uint8) # color channel addition

colored_img[:] = 255,0,255 # color complete image (color key:255,0,255)
colored_img[300:500, 100:500] = 255,0,190 # part of image to be colored

# adding line
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1] ), (255,0,0), 3) # croosed line
cv.line(colored_img,(100,100),(300,300), (255,255,50), 3) # part line

# adding rectangles
cv.rectangle(colored_img, (50,100) , (300,400), (300,300,255), 3) # draw
cv.rectangle(colored_img, (50,100) , (300,400), (300,300,255), cv.FILLED) # fill

# adding circle
cv.circle(colored_img, (500,200), 50, (255,100,0), 5) # draw circle
cv.circle(colored_img, (500,200), 50, (255,100,0), cv.FILLED) # filled circle

# adding text
cv.putText(colored_img, "Python ka chilla with baba Aamar", (30,50), cv.FONT_HERSHEY_DUPLEX, 1, (255,255,0), 2 )


# cv.imshow('Black', img)
# cv.imshow('White', img1)
cv.imshow('Colored', colored_img)
cv.waitKey(0)

cv.destroyAllwindows()