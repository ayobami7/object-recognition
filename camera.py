import cv2
import imutils

class VideoCamera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Use 0 for default webcam
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        frame = imutils.resize(frame, width=800)
        return frame