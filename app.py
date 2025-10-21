from flask import Flask, Response, render_template
import cv2
from camera import VideoCamera
from detection import SocialDistancingDetector
from utils import draw_boxes
from config import Config

app = Flask(__name__)

# Initialize video camera and detector
camera = VideoCamera(Config.CAMERA_ID)
detector = SocialDistancingDetector(
    Config.YOLO_WEIGHTS,
    Config.YOLO_CONFIG,
    Config.YOLO_CLASSES
)

def generate_frames():
    """
    Generator function that yields video frames for MJPEG streaming
    
    Yields:
        bytes: JPEG-encoded frame with multipart headers
    """
    while True:
        # Get frame from camera
        frame = camera.get_frame()
        if frame is None:
            break

        # Detect people and check social distancing
        outs, height, width = detector.detect_people(frame)
        boxes, centroids = detector.process_frame(
            frame, outs, width, height, 
            threshold=Config.CONFIDENCE_THRESHOLD
        )
        violations = detector.check_distancing(
            centroids, 
            threshold=Config.DISTANCE_THRESHOLD
        )

        # Draw bounding boxes and violations
        draw_boxes(frame, boxes, centroids, violations)
        
        # Add stats overlay
        cv2.putText(
            frame, 
            f"People: {len(centroids)} | Violations: {len(violations)}", 
            (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, 
            (255, 255, 255), 
            2
        )

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        # Yield frame in multipart format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/')
def index():
    """Main page route"""
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting Social Distancing Monitor...")
    print(f"Server running at http://{Config.HOST}:{Config.PORT}")
    print("Press Ctrl+C to stop")
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG,
        threaded=True
    )