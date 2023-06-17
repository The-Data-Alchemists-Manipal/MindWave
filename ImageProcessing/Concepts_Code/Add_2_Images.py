"""
@Disha Modi
"""
import cv2
import numpy as np

img = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv.png')
#BOTH IMAGES SHOULD BE OF SAME SIZE
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

final = cv2.add(img,img2)
#addWeighted() is used to blend two images
#addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
#Gamma is taken as zero by default 
#alpha and beta are weights given to the images
final2 = cv2.addWeighted(img,0.8,img2,0.2,0)
cv2.imshow('image',final)
cv2.imshow('image2',final2)
cv2.waitKey(0)
cv2.destroyAllWindows()