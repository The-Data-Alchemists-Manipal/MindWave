import matplotlib.pylab as plt
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = (255)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img,lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img,(x1,y1),(x2,y2),(255,0,0),thickness=3)
    img = cv2.addWeighted(img,0.8,blank_image,1,0.0)

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts the image to grayscale

height = gray.shape[0];
width = gray.shape[1];

region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts the image to grayscale
cropped_image = region_of_interest(gray,np.array([region_of_interest_vertices], np.int32),) 
canny = cv2.Canny(gray,100,200)
lines = cv2.HoughLinesP(cropped_image,
                        rho = 6,
                        theta = np.pi/60,
                        line = np.array([]),
                        minLineLength=40,
                        maxLineGap=25) #detects the lines in the image

plt.imshow(canny)
plt.show()
