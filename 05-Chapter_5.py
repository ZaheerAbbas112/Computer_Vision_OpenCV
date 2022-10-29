## Saving an image or Writing an image

import cv2 as cv
from cv2 import imshow
from cv2 import imwrite
img = cv.imread("resources/image.jpg")
img1 = cv.resize(img, (300,200))
gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127,255, cv.THRESH_BINARY)

# resize the binary image
binary = cv.resize(binary, (100,300))

imwrite('resources/image_gray.png', gray)
imwrite('resources/image_bw.png', binary)
# cv.waitKey(0)
# cv.destroyAllWindows()