
"""
@Disha Modi
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
#It is used 6 different types of thresholding

img = cv2.imread('gradient.png',0)
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #if pixel value is greater than threshold value, it is assigned one value (may be white), else it is assigned another value (may be black)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) #if pixel value is greater than threshold value, it is assigned one value (may be white), else it is assigned another value (may be black)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #if pixel value is greater than threshold value, it is assigned threshold value, else it is assigned pixel value
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) #if pixel value is greater than threshold value, it is assigned pixel value, else it is assigned zero
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) #if pixel value is greater than threshold value, it is assigned zero, else it is assigned pixel value

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    #It is used to plot multiple images in a single image window with Python, OpenCV and Matplotlib
    #Subplot(number of rows, number of columns, index number)
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
# plt.imshow(img,'gray')
# plt.title('Original Image')
# plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
