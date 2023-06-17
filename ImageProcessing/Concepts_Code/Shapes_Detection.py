"""
@Disha Modi
"""

import cv2
import numpy as np

img = cv2.imread('shapes.png')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True) #approximates the contour to a polygon
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5) #draws the contours
    x = approx.ravel()[0] #x coordinate of the shape
    y = approx.ravel()[1]
    if len(approx) == 3: #if the shape has 3 sides
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0)) #puts text on the image
    elif len(approx) == 4: #if the shape has 4 sides
        cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0)) #puts text on the image
    elif len(approx) == 5: #if the shape has 5 sides
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0)) #puts text on the image
    elif len(approx) == 10: #if the shape has 10 sides
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0)) #puts text on the image

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
