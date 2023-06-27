# -*- coding: utf-8 -*-
"""
@author: Disha Modi
"""
#print("Hello World")
import cv2
# Load an image using 'imread' specifying the path to image
img = cv2.imread('lena.png',-1)
cv2.imshow('image',img)
cv2.namedWindow('First demo') # Create a named window
# Wait for a key to be pressed to close window
k = cv2.waitKey(0) & 0xFF == ord('q')
# Wait for a key to be pressed to close window
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # wait for 's' key to save and exit
    cv2.imwrite('/lena_copy.png',img) # save image to PNG file
    cv2.destroyAllWindows() # close all openCV windows