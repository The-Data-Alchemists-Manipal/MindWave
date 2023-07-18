"""
@ Disha Modi
"""
#Line, Circle, Rectangle, Text

import cv2
import numpy as np
# img = cv2.imread('lena.png',1)

#Create a black image with 3 channels having 512x512 dimension
#We need to use unit8 to specify the data type
#We can't use any other data type
img = np.zeros([512,512,3],np.uint8)
#BGR is the sequence of color and not RGB
#line(img,starting point,ending point,color,thickness,linetype)
img = cv2.line(img,(0,0),(255,255),(255,0,0),5) # draw a line on the image
#circle(img,center,radius,color,thickness,linetype)
img = cv2.circle(img,(143,255),63,(0,255,0),-1) # draw a circle on the image
#rectangle(img,upper left corner,lower right corner,color,thickness,linetype)

#Thickness of -1 px will fill the rectangle with the color
#Thickness of 1 px will draw the rectangle with the color
#Thickness of 5 px will draw the rectangle with the color
#Thickness of 0 px will draw the rectangle with the color
#Thickness of -10 px will fill the rectangle with the color

img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),-10) # draw a rectangle on the image
#putText(img,text,starting point,font,font size,color,thickness,linetype)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),10,cv2.LINE_8) # put text on the image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()