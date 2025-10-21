import cv2
import imutils

class VideoCamera:
    """Handles video capture and frame preprocessing"""
    
    def __init__(self, camera_id=0):
        """
        Initialize video camera
        
        Args:
            camera_id: Camera device ID (0 for default webcam)
        """
        self.cap = cv2.VideoCapture(camera_id)
        
        if not self.cap.isOpened():
            raise Exception(f"Could not open camera {camera_id}")
        
        # Set camera resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def __del__(self):
        """Release camera when object is destroyed"""
        if hasattr(self, 'cap'):
            self.cap.release()

    def get_frame(self):
        """
        Capture and return a single frame
        
        Returns:
            numpy.ndarray: Captured frame, or None if capture failed
        """
        ret, frame = self.cap.read()
        
        if not ret:
            return None
        
        # Resize frame for consistent processing
        frame = imutils.resize(frame, width=800)
        return frame