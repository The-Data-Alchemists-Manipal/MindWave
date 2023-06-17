"""
@Disha Modi
"""

import  cv2
import numpy as np
img = cv2.imread('lena.png')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)

layer = gp[5] #upper level Gaussian Pyramid
cv2.imshow('upper level Gaussian Pyramid',layer)
lp = [layer]    #Laplacian Pyramid

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended) #subtracting the upper level Gaussian Pyramid from the lower level Gaussian Pyramid
    cv2.imshow(str(i),laplacian) #Laplacian Pyramid

cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
