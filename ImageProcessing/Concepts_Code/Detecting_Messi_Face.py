"""
@Disha Modi
"""
# Path: Detecting_messi_face.py

import cv2
import numpy as np

img = cv2.imread('messi.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts the image to grayscale
template = cv2.imread('messi_face.jpg', 0) #converts the template to grayscale

result = cv2.matchTemplate(imgGrey, template, cv2.TM_CCOEFF_NORMED) #compares the template with the image
loc = np.where(result >= 0.7) #returns the coordinates of the template in the image

#draws a rectangle around the template
#*loc[::-1] is used to reverse the coordinates
#pt[0] + 50 and pt[1] + 50 are the coordinates of the bottom right corner of the rectangle
for pt in zip(*loc[::-1]): #draws a rectangle around the template
    cv2.rectangle(img, pt, (pt[0] + 50, pt[1] + 50), (0, 0, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
