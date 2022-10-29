## Resizing the image
# library import
import cv2 as cv

img = cv.imread("resources/image.jpg")
img1 = cv.resize(img, (800,600))
cv.imshow("First Image", img)
cv.imshow("Second Image", img1)
cv.waitKey(0)
cv.destroyAllWindows
