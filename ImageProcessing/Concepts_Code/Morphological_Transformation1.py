"""
@Disha Modi
"""
#Morphological Transformations
# Morphological transformations are always applied on binary images only.
#Morphological transformations are some simple operations based on the image shape.

#Kernel : A kernel is formed from an image. The kernel is placed on top of the image pixels and the pixel values under the kernel are combined in some way to produce the filtered value.
#The kernel is then slid over the whole image to produce the filtered output.
#The size of the kernel determines the size of the neighborhood being considered.
#The shape of the kernel determines the kind of operation being done.
#The kernel is usually square but can be any shape.
#The kernel is usually smaller than the image.
#The kernel must be smaller than the image.
#The kernel must be an odd size.
#The kernel must be centered over the pixel that is being changed.
#The kernel must be symmetric.
#The kernel must contain all positive values.
#The sum of all the values in the kernel must be one.
#The kernel is usually square but can be any shape.

#It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation.
#Two basic morphological operators are Erosion and Dilation.
#Then its variant forms like Opening, Closing, Gradient etc also comes into play.

#Erosion : The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white).
#So what it does? The kernel slides through the image (as in 2D convolution).
#A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
#So what happens is that, all the pixels near boundary will be discarded depending upon the size of kernel.
#So the thickness or size of the foreground object decreases or simply white region decreases in the image.
#It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.
#Here, as an example, I would use a 5x5 kernel with full of ones. Let’s see it how it works:

#Dilation : It is just opposite of erosion. Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’.
#So it increases the white region in the image or size of foreground object increases.
#Normally, in cases like noise removal, erosion is followed by dilation.
#Because, erosion removes white noises, but it also shrinks our object.
#So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
#It is also useful in joining broken parts of an object.

#Opening : Opening is just another name of erosion followed by dilation.
#It is useful in removing noise, as we explained above.
#Here we use the function, cv2.morphologyEx()

#Closing : Closing is reverse of Opening, Dilation followed by Erosion.
#It is useful in closing small holes inside the foreground objects, or small black points on the object.
#Here we use the function, cv2.morphologyEx()

#Morphological Gradient : It is the difference between dilation and erosion of an image.
#The result will look like the outline of the object.
#It is useful in finding the outline of an object.
#Here we use the function, cv2.morphologyEx()

#Top Hat : It is the difference between input image and Opening of the image.
#Below example is done for a 9x9 kernel.
#Here we use the function, cv2.morphologyEx()

#Black Hat : It is the difference between the closing of the input image and input image.
#Here we use the function, cv2.morphologyEx()

#Structuring Element : It is used to define the nature of operation.
#It is just a kernel which we decide what kind of operation we want.

#Two types of structuring elements are available: Rectangular and Elliptical.


import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('smarties.jpg',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

#kernal = np.ones((5,5),np.uint8)
kernal = np.ones((5,5),np.uint8)

#Dilation : It increases the white region in the image or size of foreground object increases.
dilation = cv2.dilate(mask,kernal,iterations = 2) #iterations = 2 is the number of times you want to apply the dilation
#Erosion : It erodes away the boundaries of foreground object (Always try to keep foreground in white).
erosion = cv2.erode(mask,kernal,iterations = 1) #iterations = 1 is the number of times you want to apply the erosion
#Opening : Opening is just another name of erosion followed by dilation.
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) #MORPH_OPEN is the opening operation
#Closing : Closing is reverse of Opening, Dilation followed by Erosion.
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) #MORPH_CLOSE is the closing operation
#Morphological Gradient : It is the difference between dilation and erosion of an image.
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal) #MORPH_GRADIENT is the morphological gradient operation
#Top Hat : It is the difference between input image and Opening of the image.
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal) #MORPH_TOPHAT is the top hat operation
#Black Hat : It is the difference between the closing of the input image and input image.
bh = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernal) #MORPH_BLACKHAT is the black hat operation
# wh = cv2.morphologyEx(mask,cv2.MORPH_WHITEHAT,kernal)

titles = ['image','mask','dilation','erosion','opening','closing','mg','th','bh']
images = [img,mask,dilation,erosion,opening,closing,mg,th,bh]

for i in range(9):
    plt.subplot(2,5,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#cv2.imshow('image',img)
#cv2.imshow('mask',mask)
#cv2.imshow('dilation',dilation)
#cv2.imshow('erosion',erosion)
#cv2.imshow('opening',opening)
#cv2.imshow('closing',closing)
#cv2.imshow('mg',mg)
#cv2.imshow('th',th)
#cv2.imshow('bh',bh)

cv2.waitKey(0)
cv2.destroyAllWindows()

