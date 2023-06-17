"""
@Disha Modi
"""
#Contours are the boundaries of a shape with same intensity. 
#It stores the (x,y) coordinates of the boundary of a shape.
#Contours are a useful tool for shape analysis and object detection and recognition.
#For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.

#Contours
#cv2.findContours(image, Retrieval Mode, Approximation Method)
#Returns -> image, contours, hierarchy
#Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
#Hierarchy is the optional output vector containing information about the image topology.
#It has as many elements as the number of contours.
#For each i-th contour contours[i], the elements hierarchy[i][0] , hiearchy[i][1] , hiearchy[i][2] , and hiearchy[i][3]
#are set to 0-based indices in contours of the next and previous contours at the same hierarchical level,
#the first child contour and the parent contour, respectively.
#If for the contour i there are no next, previous, parent, or nested contours, the corresponding elements of hierarchy[i] will be negative.

import cv2
import numpy as np

img = cv2.imread('opencv.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#To draw all the contours in an image:
cv2.drawContours(img, contours, -1, (0,255,0), 3)


#To draw an individual contour, say 4th contour:
cv2.drawContours(img, contours, 3, (0,255,0), 3)
print(str(len(contours)))
#But most of the time, below method will be useful:
# cnt = contours[4]
# cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
print(contours[0])
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
