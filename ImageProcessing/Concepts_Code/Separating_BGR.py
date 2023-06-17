"""
@Disha Modi
"""
import cv2
import numpy as np
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorimage = np.zeros((512,512,3),np.uint8)
        #Generates the new image with the color selected having the same dimensions as the original image
        #2 ways to do this
        #1. mycolorimage[:] = [blue,green,red]
        #2. mycolorimage[:] = img[x,y]
        mycolorimage[:] = [blue,green,red]
        #New window to display the color selected
        cv2.imshow('color',mycolorimage)

img = cv2.imread('lena.png',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

