"""
@Disha Modi
"""
import cv2
import numpy as np

#Trackbar is a GUI component which is used to change the value of the image dynamically
#Trackbar is used to change the value of the image threshold

def nothing(x):
    print(x)

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B','image',0,255,nothing)

while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break
    # else:
    #     b = cv2.getTrackbarPos('B','image')
    #     img[:] = [b,b,b]
cv2.destroyAllWindows()