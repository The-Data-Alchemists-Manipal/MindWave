import cv2
import numpy as np
from flask import Flask, Response, render_template

app = Flask(__name__)

camera = cv2.VideoCapture(0)

def color_intensify(img,in_b,in_g,in_r):
    b,g,r=cv2.split(img)
    increased_b = np.clip(b*in_b, 0, 255).astype(np.uint8)
    increased_g = np.clip(g*in_g, 0, 255).astype(np.uint8)
    increased_r = np.clip(r*in_r, 0, 255).astype(np.uint8)
    modified_image = cv2.merge((increased_b, increased_g, increased_r))
    return modified_image

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_gray_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_red_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = color_intensify(frame,1,1,5)
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_red_frames2():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = color_intensify(frame,1,5,1)
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_green_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = color_intensify(frame,1,5,1)
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_blue_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = color_intensify(frame,5,1,1)
            ret,buffer=cv2.imencode('.jpg',np.array(frame))
            frame=buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def thresh(img,max_val,thresh,convert_type):
    _,img=cv2.threshold(img,thresh,max_val,convert_type)
    return img

def generate_binary():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = thresh(gray, 255, 100, cv2.THRESH_BINARY)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_thresholded_color():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = thresh(frame, 255, 100, cv2.THRESH_BINARY)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    return Response(generate_gray_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed3():
    return Response(generate_red_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed4():
    return Response(generate_green_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed4')
def video_feed5():
    return Response(generate_blue_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed5')
def video_feed6():
    return Response(generate_binary(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed6')
def video_feed7():
    return Response(generate_thresholded_color(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
