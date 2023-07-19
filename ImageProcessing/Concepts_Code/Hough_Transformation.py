"""
@Disha Modi
"""

import cv2
import numpy as np
img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts the image to grayscale
#Canny edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize = 3) #detects the edges in the image
#Hough line transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 200) #detects the lines in the image

for line in lines:
    rho, theta = line[0] #rho is the distance from the origin and theta is the angle
    a = np.cos(theta) #cos(theta)
    b = np.sin(theta) #sin(theta)
    x0 = a * rho #x = a * rho
    y0 = b * rho #y = b * rho
    #x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b)) #x1 = x0 + 1000 * (-b)
    #y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a)) #y1 = y0 + 1000 * (a)
    #x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b)) #x2 = x0 - 1000 * (-b)
    #y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a)) #y2 = y0 - 1000 * (a)
    #draws the lines on the image
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Accumulator: A 2D array of size (rho x theta) is created and initialized to zero. Suppose you want the accuracy of angles to be 1 degree, you need 180 columns. For rho, the maximum distance possible is the diagonal length of the image. So taking one pixel accuracy, number of rows can be diagonal length of the image.
#cv.HoughLinesP(image, rho, theta, threshold, lines=None, srn=None, stn=None, min_theta=None, max_theta=None)
#image: 8-bit, single-channel binary source image. The image may be modified by the function.
#rho: Distance resolution of the accumulator in pixels.
#theta: Angle resolution of the accumulator in radians.
#threshold: Accumulator threshold parameter. Only those lines are returned that get enough votes ( > threshold ).
#lines: Output vector of lines. Each line is represented by a two-element vector (rho, theta) . rho is the distance from the coordinate origin (0,0) (top-left corner of the image). theta is the line rotation angle in radians ( 0 ~ vertical line, pi/2 ~ horizontal line ).
#srn: For the multi-scale Hough transform, it is a divisor for the distance resolution rho . The coarse accumulator distance resolution is rho and the accurate accumulator resolution is rho/srn . If both srn=0 and stn=0 , the classical Hough transform is used. Otherwise, both these parameters should be positive.
#stn: For the multi-scale Hough transform, it is a divisor for the distance resolution theta.
#min_theta: For standard and multi-scale Hough transform, minimum angle to check for lines. Must fall between 0 and max_theta.
#max_theta: For standard and multi-scale Hough transform, maximum angle to check for lines. Must fall between min_theta and CV_PI.
#The function implements the standard or standard multi-scale Hough transform algorithm for line detection.




