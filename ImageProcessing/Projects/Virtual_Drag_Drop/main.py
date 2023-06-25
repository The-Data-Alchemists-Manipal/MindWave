"""
@Disha Modi
"""

# print("Hello Everyone, This is my contribution to MindWave")

# TASK LIST :
# Change the color of the rectangle, if the finger is inside the rectangle
# Check if cursor clicked ot not
# Use two fingers to drag and drop the rectangle
# Use class to create multiple rectangles
# Enable multiple rectangles to be dragged and dropped

import cv2
import cvzone
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 728)
detector = HandDetector(detectionCon=1)  # detectionCon is the confidence level, for strict detection, keep it high
print(detector)
colorRect = (255, 0, 255)  # purple color
cx, cy, w, h = 100, 100, 200, 200  # coordinates of the rectangle


class DragRectangle():
    def __init__(self, posCenter, size=None):
        if size is None:
            size = [200, 200]
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size
        # If the index fingertip is inside the rectangle, change the position of the rectangle to the cursor position
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            # colorRect = (0,255,0)                       # green color
            # cx,cy = cursor                # change the coordinates of the rectangle to the cursor coordinates for the rectangle to follow the cursor
            self.posCenter = cursor


rectangles = []
for x in range(5):
    rectangles.append(DragRectangle([x * 250 + 250, 150]))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)  # bboxInfo is the bounding box info, it contains the coordinates of the bounding box

    # Change the color of the rectangle, if the finger is inside the rectangle
    if lmList:

        l, _, _ = detector.findDistance(8, 12, img,
                                        draw=False)  # 8 and 12 are the indices of the tip of the index finger and the tip of the middle finger respectively
        print(l)
        if l < 30:
            # lmList[8] = (lmList[8][0]+20,lmList[8][1]+20)    # adding 20 to the x and y coordinates of the tip of the index finger
            # lmList[8] gives the coordinates of the tip of the index finger, from mediapipe
            cursor = lmList[8]
            for rectangle in rectangles:
                rectangle.update(cursor)

    # For solid rectangle
    # for rectangle in rectangles:
    #     cx,cy = rectangle.posCenter
    #     w,h = rectangle.size
    #     cv2.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),(255,0,255),cv2.FILLED)
    #     cvzone.cornerRect(img,(cx-w//2,cy-h//2,w,h),20,rt=8) # rt is the radius of the corner rectangle

    ##Transparency
    imgNew = np.zeros_like(img, np.uint8)  # creates a black image of the same size as the original image
    for rectangle in rectangles:
        cx, cy = rectangle.posCenter
        w, h = rectangle.size
        cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), (255, 0, 255), cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20,
                          rt=8)  # rt is the radius of the corner rectangle
    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    cv2.imshow("Image", out)
    # cv2.imshow("image",img)
    cv2.waitKey(1)
