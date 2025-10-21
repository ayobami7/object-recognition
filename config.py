class Config:
    """Configuration settings for the social distancing monitor"""
    
    # Camera settings
    CAMERA_ID = 0
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480
    DISPLAY_WIDTH = 800
    
    # YOLO settings
    YOLO_WEIGHTS = "yolov3.weights"
    YOLO_CONFIG = "yolov3.cfg"
    YOLO_CLASSES = "coco.names"
    CONFIDENCE_THRESHOLD = 0.5
    
    # Social distancing settings
    DISTANCE_THRESHOLD = 100  # pixels 
    
    # Flask settings
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
