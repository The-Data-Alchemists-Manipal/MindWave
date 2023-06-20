"""
@Disha Modi
"""

#Image Blending using Pyramids
#Image blending is used to join two images of the same size. It is used in seamless cloning, watermarking, etc.
#We can blend two images using the following formula:
#dst = (1-alpha)*img1 + alpha*img2
#where alpha is the weight of the first image.

#We can blend two images using the following steps:
#1. Load the two images
#2. Find the Gaussian pyramids for the two images
#3. From the Gaussian pyramids, find their Laplacian pyramids
#4. Now, join the left half of the first image and the right half of the second image in each level of the Laplacian
#pyramid
#5. Finally, from this joint image pyramids, reconstruct the original image.


import cv2
import numpy as np
apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')
print(apple.shape)
print(orange.shape)
apple = cv2.resize(apple, (512, 512))
orange = cv2.resize(orange, (512, 512))

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#Generate Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    # cv2.imshow(str(i),apple_copy)

#Generate Laplacian Pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)
    # cv2.imshow(str(i),laplacian)

#Generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
    # cv2.imshow(str(i),orange_copy)

#Generate Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)
    # cv2.imshow(str(i),laplacian)

#Add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
#Zip function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    #HSTACK function stacks images horizontally 
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    # cv2.imshow(str(n),laplacian)

#Reconstruct the original image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)
    # cv2.imshow(str(i),apple_orange_reconstruct)



cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.imshow('Apple_Orange', apple_orange)
cv2.imshow('Apple_Orange_Reconstruct', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
