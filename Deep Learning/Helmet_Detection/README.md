# Helmet Detection with YOLO

This Python script performs real-time object detection using the YOLO (You Only Look Once) deep learning model. It utilizes OpenCV to read frames from a video stream (e.g., webcam) or an input video file, performs object detection, draws bounding boxes and class labels on the detected objects, and saves the output video with annotations.

## Requirements

- Python 3
- OpenCV
- Numpy
- argparse
- pyttsx3 (for text-to-speech output)

## Usage

```bash
python Helmet_Detection.py --output output/video.avi --yolo yolo-coco
```
## YOLO Model
The script uses the YOLO model trained on the COCO dataset. The class labels and corresponding confidence scores are displayed on the detected objects.

## Output
The script will display a real-time video feed with object detections and output the processed video with bounding boxes and class labels to the specified output file.