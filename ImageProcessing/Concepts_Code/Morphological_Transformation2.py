"""
@Disha Modi
"""
#Morphological Transformations
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal = np.ones((5,5),np.uint8)

dilation = cv2.dilate(mask,kernal,iterations = 2) #iterations = 2 is the number of times you want to apply the dilation
erosion = cv2.erode(mask,kernal,iterations = 1) #iterations = 1 is the number of times you want to apply the erosion
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) #MORPH_OPEN is the opening operation
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) #MORPH_CLOSE is the closing operation
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal) #MORPH_GRADIENT is the morphological gradient operation
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal) #MORPH_TOPHAT is the top hat operation
bh = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernal) #MORPH_BLACKHAT is the black hat operation
# wh = cv2.morphologyEx(mask,cv2.MORPH_WHITEHAT,kernal)

titles = ['image','mask','dilation','erosion','opening','closing','mg','th','bh']
images = [img,mask,dilation,erosion,opening,closing,mg,th,bh]

for i in range(9):
    plt.subplot(2,5,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

