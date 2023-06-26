"""
@Disha Modi
"""

import cv2
import numpy as np

img = cv2.imread('messi.jpg')
print(img.shape)
print(img.size)
print(img.dtype)

#To determine b,g,r of img
b,g,r = cv2.split(img)
print(b)    #Array matrix

#To merge the b,g,r colors
img = cv2.merge((b,g,r))

ball = img[100:160, 180:240]

img[0:60,0:60] = ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
