import cv2
import mediapipe as mp
import copy

def connect(lista,i,j):
     stpoint=(int(lista[i].x*w)+200,int(lista[i].y*h))
     endpoint=(int(lista[j].x*w)+200,int(lista[j].y*h))
     return cv2.line(img,stpoint,endpoint,(255,0,0),5)

cap=cv2.VideoCapture(0)
mppose=mp.solutions.pose
pose=mppose.Pose()
while True:
    success,img=cap.read()
    imgreal=copy.copy(img)
    positionslist=[]
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgrgb)
    if results.pose_landmarks:
        positions=enumerate(results.pose_landmarks.landmark)
        for id,lm in positions:
            positionslist.append(lm)
            h,w,c=img.shape
            cx,cy=int(lm.x*w)+200,int(lm.y*h)
            # cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
        img=connect(positionslist, 0, 4)
        img = connect(positionslist, 0, 1)
        img = connect(positionslist, 1, 2)
        img = connect(positionslist, 5, 4)
        img = connect(positionslist, 10, 9)
        img = connect(positionslist,12,11 )
        img = connect(positionslist,24,23 )
        img = connect(positionslist,26,24 )
        img = connect(positionslist,23,25 )
        img = connect(positionslist,28,26 )
        img = connect(positionslist,27,25 )
        img = connect(positionslist,32,28 )
        img = connect(positionslist,30,28 )
        img = connect(positionslist,27,31 )
        img = connect(positionslist,27,29 )
        img = connect(positionslist,11,13 )
        img = connect(positionslist,13,15 )
        img = connect(positionslist,15,21 )
        img = connect(positionslist,15,19 )
        img = connect(positionslist,15,17 )
        img = connect(positionslist,17,19 )
        img = connect(positionslist,12,14 )
        img = connect(positionslist,14,16 )
        img = connect(positionslist,16,22 )
        img = connect(positionslist,16,18 )
        img = connect(positionslist,18,20 )
        img = connect(positionslist,20,16 )
        img = connect(positionslist,12,24 )
        img = connect(positionslist,11,23 )
        img = connect(positionslist, 2, 3)
        img = connect(positionslist, 5, 6)
        img = connect(positionslist, 8, 6)
        img = connect(positionslist, 3, 7)




        cv2.circle(img,(int(positionslist[5].x*w)+200,int(positionslist[5].y*h)),10,(255,0,255),cv2.FILLED)
        cv2.circle(img, (int(positionslist[2].x * w) + 200, int(positionslist[2].y * h)), 10, (255, 0, 255), cv2.FILLED)









    #cv2.namedWindow("input",cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("input",700,800)
    #cv2.moveWindow("input",0,0)
    cv2.namedWindow("output",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("output",1400,1000)
    #cv2.moveWindow("output",710,0)
    #cv2.imshow("input",imgreal)
    cv2.imshow("output",img)
    cv2.waitKey(1)