"""
@Disha Modi
"""
import cv2
import numpy as np

#Matplot lib in OpenCV
from matplotlib import pyplot as plt

img = cv2.imread('lena.png',-1)
cv2.imshow('image',img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([]) #to hide tick values on X and Y axis
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

