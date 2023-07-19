"""
@Disha Modi
"""

import cv2
import numpy as np

def nothing(x):
    print(x)


img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
switch = '0 : OFF \n1 : ON' #switch is the name of the trackbar
cv2.createTrackbar(switch,'image',0,1,nothing) #0 is the default value, 1 is the max value, nothing is the function that will be called everytime the trackbar value changes
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break      
#Trackbar is used to change the color of the image
#getTrackbarPos() is used to get the current position of the trackbar
#setTrackbarPos() is used to set the position of the trackbar
#cv2.getTrackbarPos('B','image') will return the current position of the trackbar named 'B' in the window named 'image'
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
        #img[:] = [b,g,r] #this will change the color of the image to the color of the trackbar
    else:
        img[:] = [b,g,r]  

cv2.destroyAllWindows()