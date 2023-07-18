"""
@Name : Disha Modi
"""

###################################### VIRTUAL QUIZ STEPS ##############################################
#   1. Import the required libraries
#   2. Create a HandDetector object
#   3. Create MCQ_Questions class that will be used for updating the question and the options
#   4. Check for hands
#   5. Check if answer is clicked
#   6. Check for correct answer
#   7. Check if anymore questions exists
#   8. Display the score
#   9. Display the progress bar
########################################################################################################

import csv
import time
import cv2
import numpy as np
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0, maxHands=2)
# MCQ Options
class MCQ_Questions():
    def __init__(self,data):
        self.question = data[0]
        self.c1 = data[1]
        self.c2 = data[2]
        self.c3 = data[3]
        self.c4 = data[4]
        self.answer = int(data[5])

        self.userAns = None

    #Update the question and options
    def update(self,cursor,bboxes):
        for x,bbox in enumerate(bboxes):
            x1,y1,x2,y2 = bbox
            if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                self.userAns = x+1
                cv2.rectangle(self.img,(x1,y1),(x2,y2),(0,255,0),cv2.FILLED)



#Import CSV file data
pathCSV = "Quiz.csv"
with open(pathCSV, newline = '\n') as f:
    reader = csv.reader(f)
    dataset = list(reader)[1:]
print(len(dataset))

#Creating object for each question
mcqList = []
for q in dataset:
    mcqList.append(MCQ_Questions(q))    #Creating list of objects

print("Total Questions: ",len(mcqList))
      
currentQuestion = 0
totalQuestions = len(dataset)

print(len(mcqList))
print(totalQuestions)

while True:
    success, img = cap.read()
    # img = cv2.flip(img, 1)
    hands = detector.findHands(img)
    #If there are questions left
    if currentQuestion<totalQuestions:
        mcq = mcqList[0];

        # Displaying the question
        img, bbox = cvzone.putTextRect(img, mcq.question, [100, 100], 2, 2, offset=20, border=2)
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [100, 250], 2, 2, offset=20, border=2)
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [400, 250], 2, 2, offset=20, border=2)
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [100, 400], 2, 2, offset=20, border=2)
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [400, 400], 2, 2, offset=20, border=2)


        if hands:
            lmList = hands[0]['lmList']
            # print(lmList)
            # print(lmList[8])
            # print(lmList[4])
            #Cursor
            cursor = lmList[8]
            length,info,img = detector.findDistance(lmList[8],lmList[12],img)
            print(length)
            if length<30:
                #If clicked, update the question on screen
                mcq.update(cursor,[bbox1,bbox2,bbox3,bbox4])
                print(mcq.userAns)
                
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    currentQuestion += 1
                    # mcq = mcqList[currentQuestion%totalQuestions]
    else :
        #If no questions left, calculate the score and display it
        score = 0
        for mcq in mcqList:
            if mcq.answer == mcq.userAns:
                score += 1
        score = round((score/totalQuestions)*100,2)
        img,_ = cvzone.putTextRect(img,f'Quiz Completed',[150,100],2,2,offset=20,border=2)
        img,_ = cvzone.putTextRect(img,f'Your Score: {score}%',[700,100],2,2,offset=20,border=2)

    #Draw progress bar
    barValue = 150 + (950//totalQuestions)*currentQuestion
    cv2.rectangle(img,(150,600),(barValue,650),(0,255,0),cv2.FILLED)
    cv2.rectangle(img,(150,600),(1100,650),(255,0,255),cv2.FILLED)
    img,_=cvzone.putTextRect(img,f'{(round(currentQuestion/totalQuestions)*100)}%',[1130,635],2,2,offset=20,border=2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)