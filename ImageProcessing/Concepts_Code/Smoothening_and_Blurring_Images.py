"""
@Disha Modi
"""
#Smoothing Images
#Blurring Images

#There are various filters for blurring. I will explain four of them here.
#1. Averaging
#This is done by convolving the image with a normalized box filter. It simply takes the average of all the pixels under the kernel area and replaces the central element. This is done by the function cv2.blur() or cv2.boxFilter(). Check the docs for more details about the kernel. We should specify the width and height of kernel. A 3x3 normalized box filter would look like this:
#K = 1/9 * [[1,1,1],[1,1,1],[1,1,1]]
#2. Gaussian Filtering
#In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used. It is done with the function, cv2.GaussianBlur(). We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective in removing Gaussian noise from the image.
#If you want, you can create a Gaussian kernel with the function, cv2.getGaussianKernel().
#3. Median Filtering
#Here, the function cv2.medianBlur() computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value. This is highly effective against salt-and-pepper noise in the images. Interesting thing is that, in the above filters, central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.
#4. Bilateral Filtering
#cv2.bilateralFilter() is highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters. We already saw that gaussian filter takes the a neighbourhood around the pixel and find its gaussian weighted average. This gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost same intensity. It doesn't consider whether pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.

#GaussianFilter is using a different weight kernel in both the x and y direction. It is using a Gaussian distribution in both the x and y direction. The Gaussian distribution is a bell-shaped curve showing distribution of data. The Gaussian distribution is defined as:
#G(x) = 1/(sqrt(2*pi)*sigma) * exp(-x^2/(2*sigma^2))
#1/16[1 4 6 4 1
#     4 16 24 16 4
#     6 24 36 24 6
#     4 16 24 16 4
#     1 4  6 4 1]
#

#MedianFilter is something that replace each pixel's value with the median of it's neighbouring pixels. It is good when we are dealing with "salt and pepper" noise.
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('opencv.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25

#filter2D(name, depth, kernel)
dst = cv2.filter2D(img,-1,kernel) #filter2D is the function to convolve the kernel with an image

#blur(name, kernel size)
blur = cv2.blur(img,(5,5)) #blur is the function to blur the image

#GaussianBlur(name, kernel size, sigmaX)
gblur = cv2.GaussianBlur(img,(5,5),0) #GaussianBlur is the function to blur the image using Gaussian kernel

median = cv2.medianBlur(img,5) #medianBlur is the function to blur the image using median kernel

bilateralFilter = cv2.bilateralFilter(img,9,75,75) #bilateralFilter is the function to blur the image using bilateral filter

titles = ['image','2D Convolution','blur','GaussianBlur','medianBlur','bilateralFilter']

images = [img,dst,blur,gblur,median,bilateralFilter]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
