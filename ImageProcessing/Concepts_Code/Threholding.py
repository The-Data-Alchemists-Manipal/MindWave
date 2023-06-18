"""
@Disha Modi
"""
import cv2
import numpy as np
#Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided.
#In thresholding, each pixel value is compared with the threshold value.
#If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255).
#cv2.threshold() function is used to apply the thresholding. The first argument is the source image, which should be a grayscale image.
#The second argument is the threshold value which is used to classify the pixel values.
#The third argument is the maximum value which is assigned to pixel values exceeding the threshold.
#OpenCV provides different types of thresholding which is given by the fourth parameter of the function.
#cv2.THRESH_BINARY
#cv2.THRESH_BINARY_INV
#cv2.THRESH_TRUNC
#cv2.THRESH_TOZERO
#cv2.THRESH_TOZERO_INV
#cv2.adaptiveThreshold() function is used to apply the adaptive thresholding. The first argument is the source image, which should be a grayscale image.
#The second argument is the maximum value which is assigned to pixel values exceeding the threshold.
#The third argument is the adaptive method. It determines how thresholding value is calculated.
#cv2.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
#The fourth argument is the threshold type. It is used to specify the thresholding type.

#Difference between threhsholding and adaptive thresholding: https://stackoverflow.com/questions/15341550/opencv-adaptive-threshold-vs-threshold    


img = cv2.imread('gradient.png')
#Is it necessary to convert the image to grayscale before applying thresholding? Yes, it is necessary to convert the image to grayscale before applying thresholding. 
#If the image is not in grayscale, then the cv2.threshold() function will throw an error.
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)  # 50 is the threshold value. 255 is the max value. cv2.THRESH_BINARY is the threshold type. 
_,th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# th6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# th7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)
# cv2.imshow('th6', th6)
# cv2.imshow('th7', th7)


cv2.waitKey(0)
cv2.destroyAllWindows()
