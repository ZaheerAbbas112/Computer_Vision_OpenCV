## Resolution of cam

import cv2 as cv
import numpy as np

# capture your camera
cap = cv.VideoCapture(0)

# resolution (HD:1280*720)
cap.set(3,1280) # 3 for width
cap.set(4,720)  # 4 for height

def hd_resolution():
    cap.set(3,1280)
    cap.set(4,720)

def sd_resolution():
 cap.set(3,640)
 cap.set(4,480)

def fhd_resolution():
 cap.set(3,1920)
 cap.set(4,1080)


# hd_resolution()
# sd_resolution()
# fhd_resolution()




while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Camera", frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()








cv.waitKey(0)

cv.destroyAllwindows()