import cv2
#This project uses opencv to detect eyes.
video_formats = ['mp4', 'mov', 'wmv', 'avi', 'flv', 'f4v', 'swf', 'mkv']
image_formats = ['jpg', 'png']
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
print("Eye Detection with OpenCV\n")
print("Enter the corresponding number you want to work with: \n 1. Image \n 2. Video")
format = int(input())

if format == 1: #checking the format
    path = input("Please give the exact file path to your image: ")
    extension = path[len(path)-3:]
    print(extension)
    if extension in image_formats:
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in eyes:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
        cv2.imshow('img', img)
        cv2.waitKey(0)
        
    else:
        print("Please give a image with the proper extension.")
    
elif format == 2:
    path = input("Please give the exact file path to your video: ")
    extension = path[len(path)-3:]
    print(extension)
    if extension in video_formats:
        cap = cv2.VideoCapture(path)
        while cap.isOpened():
            _, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in eyes:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
    else:
        print("Please give a video with the proper extension.")