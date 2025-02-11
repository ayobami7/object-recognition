# app.py
from flask import Flask, Response, render_template
import cv2
from camera import VideoCamera
from detection import SocialDistancingDetector
from utils import draw_boxes

app = Flask(__name__)

# Initialize video camera and detector
camera = VideoCamera()
detector = SocialDistancingDetector("yolov3.weights", "yolov3.cfg", "coco.names")

def generate_frames():
    while True:
        frame = camera.get_frame()
        if frame is None: 
            break

        # Detect people and check social distancing
        outs, height, width = detector.detect_people(frame)
        boxes, centroids = detector.process_frame(frame, outs, width, height)
        violations = detector.check_distancing(centroids)

        # Draw bounding boxes and violations
        draw_boxes(frame, boxes, centroids, violations)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)