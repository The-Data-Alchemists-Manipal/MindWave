"""
@Disha Modi
"""
#Canny Edge Detection
#It is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.
#It was developed by John F. Canny in 1986.
#It is a multi-stage algorithm because it involves multiple steps.
#It is a very popular edge detection algorithm.
#It is also known as optimal edge detector.
#It is a very accurate edge detector.
#It is also very fast.
#It is used in many computer vision applications.

#It is a 5 step algorithm:
#1. Noise Reduction : Gaussian Filter is used to remove noise. It is a low pass filter. It removes high frequency content. It smooths the image. It is also known as Gaussian Blur.
#2. Gradient Calculation : It finds out the intensity gradient of the image. It is a high pass filter. It removes low frequency content. It is also known as Sobel Filter.
#3. Non-maximum Suppression : It is used to remove pixels that are not edges. It is used to thin out the edges. It is used to get rid of spurious response to edge detection. It is also known as thinning. It is also known as local maxima suppression. It is also known as non-maxima suppression. It is also known as local gradient maxima suppression. It is also known as edge thinning. 
#4. Double Threshold : It is used to find strong, weak and non-relevant pixels. It is used to find out which are all edges and which are not. It is used in the last step of the canny edge detection algorithm. It is also known as double thresholding. It is also known as hysteresis thresholding. It is also known as edge tracking by hysteresis.
#5. Edge Tracking by Hysteresis : It is used to find out which are all edges and which are not. It is used in the last step of the canny edge detection algorithm. It is also known as edge tracking. It is also known as hysteresis. It is also known as edge tracking by hysteresis.
#cv2.Canny(image, threshold1, threshold2)

#image: source image
#Hysteresis: It is a double thresholding technique.
#It is used to find out which are all edges and which are not.
#It is used in the last step of the canny edge detection algorithm.
#threshold1: first threshold for the hysteresis procedure
#threshold2: second threshold for the hysteresis procedure
#threshold1 and threshold2 are used in double thresholding.
#Double thresholding is used to find strong, weak and non-relevant pixels.
#Any gradient value larger than threshold2 is considered to be an edge pixel.
#Any gradient value smaller than threshold1 is considered to be a non-edge pixel.
#Any gradient value between threshold1 and threshold2 is considered to be a weak edge pixel.
#After double thresholding, we have to perform edge tracking by hysteresis.
#In edge tracking by hysteresis, we have to find out which are all edges and which are not.

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg', 0)
canny = cv2.Canny(img, 100, 200)
canny1 = cv2.Canny(img, 150, 300)

titles = ['image', 'canny','canny1']
images = [img, canny, canny1]

for i in range(3):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
