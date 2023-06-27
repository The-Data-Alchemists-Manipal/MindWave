# Ultralytics Model for Drowziness Detection


Ultralytics YOLOv8 is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. YOLOv8 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection and tracking, instance segmentation, image classification and pose estimation tasks.


- [ Ultralytics Model Repo ]
- [Notebook Link]


## Prerequisites 
#### Installations
- [ Ultralytics Model Repo ]
- [PyTorch Installation]
- [COCO classes]
- [LabellImg]




Note : I am using google Colab so me accessing webcam will be different in Jupyter Notebook. You can refer to the following code for Jupyter Notebook.

```
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```


## Training

For Training you need to use your own dataset and annotate it. 
I used Teachable Machine to collect Images and annotate it with the help of labelImg.

Keep the collected images under 'data' directory in 'images' folder
and Keep the labelled images under 'data' directory in 'label' folder

Clone LabelImg
```
!git clone https://github.com/tzutalin/labelImg
!pip install pyqt5 lxml --upgrade
!cd labelImg && pyrcc5 -o libs/resources.py resources.qrc
```

Run LabelImg
```
python labelImg.py

```

Open the Image directory. You can use 'A' or 'D' for jumping to different images.

To annotate press 'W' and hold 'Left Click Mouse button' and draw a box where u want to annotate

Remember : To change you Directory to label folder first

## Create Dataset.yaml

I will attach my Dataset.yaml file.

After creating labels. You will find a classes file over there. Open it up and copy the classes from there and paste in the required section of Dataset.yaml file.

The Dataset.yaml file must be present in the yolov5 folder.

## Load Model

Now your result of the model will be saved into runs/train/exp(some number it will show).

load the model 

```
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp10/weights/last.pt', force_reload=True)

```
The path must be the saved model path /weights/last.pt



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Ultralytics Model Repo]: <https://github.com/ultralytics/ultralytics>
   [PyTorch Installation]: <https://pytorch.org/get-started/locally/>
   [COCO classes]: <https://gist.github.com/AruniRC/7b3dadd004da04c80198557db5da4bda>
   [LabellImg]: <https://github.com/heartexlabs/labelImg>
   [Notebook Link]: <https://github.com/Mochoye/MindWave/blob/mochoye/Deep%20Learning/Drowziness%20Detection/algorithm_dataset.ipynb>
 
