"""
@Disha Modi
"""
#Image Gradients
#Image gradients are used to find edges in the image. It is the directional change in the intensity or color in an image.
# There are two types of image gradients:
#1. SobelX and SobelY
#2. Laplacian
#SobelX and SobelY are used to find horizontal and vertical edges respectively. Laplacian is used to find both
#horizontal and vertical edges.
#Laplacian is more sensitive to noise.
#Laplacian is a second derivative of the image.
#Sobel is a first derivative of the image.


#SobelX = cv2.Sobel(src, ddepth, dx, dy, ksize)
#SobelY = cv2.Sobel(src, ddepth, dx, dy, ksize)
#Laplacian = cv2.Laplacian(src, ddepth)
#src: source image
#ddepth: depth of the destination image
#dx: order of the derivative x
#dy: order of the derivative y
#ksize: size of the kernel
#ddepth: depth of the destination image

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3) #ksize = 3 is the size of the kernel
lap = np.uint8(np.absolute(lap)) #absolute value of laplacian

#cv2.CV_64F is the depth of the destination image. It is 64 bit float. It is used to avoid overflow. 
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #1 is the order of the derivative x
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) #1 is the order of the derivative y
#sobelX and sobelY are 64 bit float images. We need to convert them to 8 bit unsigned integers before we can display them.
#We can do this by taking the absolute value of sobelX and sobelY and then converting them to 8 bit unsigned integers.
#Why we need 8 bit images only? Because we can only display 8 bit images.
sobelX = np.uint8(np.absolute(sobelX)) #absolute value of sobelX
sobelY = np.uint8(np.absolute(sobelY)) #absolute value of sobelY
sobelCombined = cv2.bitwise_or(sobelX, sobelY) #combining sobelX and sobelY

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
