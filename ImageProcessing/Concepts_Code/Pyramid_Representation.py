"""
@Disha Modi
"""
# Image Pyramids
# Image pyramids are used to create images of different resolutions. It is used in image blending, image resizing,
# edge detection, etc.
# There are two types of image pyramids:
# 1. Gaussian Pyramid
# 2. Laplacian Pyramid

# Gaussian pyramid is used to downsample the image. It is used to reduce the size of the image. It is used in image
# blending and image resizing.

# Laplacian pyramid is used to reconstruct the image from the lower resolution image. It is used in image compression.

# cv2.pyrDown(src, dst, dstsize)
# cv2.pyrUp(src, dst, dstsize)
# src: source image
# dst: destination image
# dstsize: size of the destination image
# dstsize is the size of the output image. It is optional. If dstsize is not specified, the size of the output image is
# calculated as:
# dstsize = (src.cols/2, src.rows/2)

# The size of the output image is half the size of the input image.
# The size of the output image is calculated as:
# dstsize = (src.cols*2, src.rows*2)

#We loose some information when we downsample the image. So, we cannot reconstruct the original image from the
#downsampled image. So, we use Laplacian pyramid to reconstruct the image from the downsampled image.
#Laplacian pyramid is formed from the Gaussian pyramid. It is formed by the difference between the Gaussian pyramid
#and the expanded version of its upper level in Gaussian pyramid. The expanded version of the upper level is resized
#to the size of the current level in the Gaussian pyramid. The difference between the two is the Laplacian pyramid.


import cv2
import numpy as np

img = cv2.imread('lena.png')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr1 = cv2.pyrUp(lr2)

cv2.imshow('Original Image', img)
cv2.imshow('PyrDown1 Image', lr1)
cv2.imshow('PyrDown2 Image', lr2)
cv2.imshow('PyrUp1 Image', hr1)

cv2.waitKey(0)
cv2.destroyAllWindows()
