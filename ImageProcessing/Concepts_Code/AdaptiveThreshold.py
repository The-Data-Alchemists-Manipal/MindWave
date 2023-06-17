"""
@Disha Modi
"""
import cv2
import numpy as np
#Difference between threshold and adaptive threshold is that in threshold, we have to give a value of threshold
#whereas in adaptive threshold, the threshold value is calculated for smaller regions and therefore, there will be
#different threshold values for different regions. It gives better results for images with varying illumination.
#There are two types of adaptive thresholding:
#1. Adaptive Mean Thresholding
#2. Adaptive Gaussian Thresholding
#In adaptive mean thresholding, the threshold value is the mean of the neighbourhood area.
#In adaptive gaussian thresholding, the threshold value is the weighted sum of neighbourhood values where weights are
#a gaussian window.
#cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
#src: source image
#maxValue: maximum value that can be assigned to a pixel
#adaptiveMethod: adaptive method to use. 
img = cv2.imread('gradient.png', 0)
_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
