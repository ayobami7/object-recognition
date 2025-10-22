import cv2
import numpy as np
from scipy.spatial import distance as dist
from ultralytics import YOLO

class SocialDistancingDetector:
    """Handles person detection using YOLOv3 and social distancing checks"""
    def __init__(self):
        # Load YOLOv8 model 
        self.model = YOLO('yolov8n.pt')  
    
    # def __init__(self, weights_path, config_path, classes_path):
    #     """
    #     Initialize YOLO detector
        
    #     Args:
    #         weights_path: Path to yolov3.weights
    #         config_path: Path to yolov3.cfg
    #         classes_path: Path to coco.names
    #     """
    #     self.net = cv2.dnn.readNet(weights_path, config_path)
    #     self.layer_names = self.net.getLayerNames()
        
    #     # Fix for different OpenCV versions
    #     unconnected = self.net.getUnconnectedOutLayers()
    #     if len(unconnected.shape) == 1:
    #         # OpenCV 4.5.4+
    #         self.output_layers = [self.layer_names[i - 1] for i in unconnected]
    #     else:
    #         # Older OpenCV versions
    #         self.output_layers = [self.layer_names[i[0] - 1] for i in unconnected]
        
    #     with open(classes_path, "r") as f:
    #         self.classes = [line.strip() for line in f.readlines()]

    def detect_people(self, frame):
        """
        Run YOLOv8 detection on frame
        
        Args:
            frame: Input image as numpy array
            
        Returns:
            tuple: (YOLO results, frame height, frame width)
        """
        height, width, _ = frame.shape
        
        # Run inference (class 0 = person in COCO dataset)
        results = self.model(frame, classes=[0], verbose=False)
        
        return results, height, width
    
    def process_frame(self, frame, results, width, height, threshold=0.5):
        """
        Process YOLOv8 results to extract person bounding boxes
        
        Args:
            frame: Input image
            results: YOLOv8 detection results
            width: Frame width
            height: Frame height
            threshold: Confidence threshold (default 0.5)
            
        Returns:
            tuple: (list of bounding boxes, list of centroids)
        """
        boxes = []
        centroids = []
        
        # YOLOv8 returns results in a list
        for result in results:
            # Access detection boxes
            if result.boxes is not None and len(result.boxes) > 0:
                for box in result.boxes:
                    # Get confidence
                    conf = float(box.conf[0])
                    
                    # Filter by confidence threshold
                    if conf > threshold:
                        # Get bounding box coordinates (xyxy format)
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        
                        # Convert to xywh format
                        x = int(x1)
                        y = int(y1)
                        w = int(x2 - x1)
                        h = int(y2 - y1)
                        
                        # Calculate centroid
                        center_x = int(x + w / 2)
                        center_y = int(y + h / 2)
                        
                        # Validate bounding box
                        if w > 0 and h > 0 and x >= 0 and y >= 0:
                            boxes.append([x, y, w, h])
                            centroids.append((center_x, center_y))
        
        return boxes, centroids
    
    def check_distancing(self, centroids, threshold=100):
        """
        Check for social distancing violations
        
        Args:
            centroids: List of (x, y) tuples representing person centers
            threshold: Minimum distance in pixels (default 100)
            
        Returns:
            set: Indices of people violating social distancing
        """
        violations = set()
        
        # Check all pairs of people
        for i in range(len(centroids)):
            for j in range(i + 1, len(centroids)):
                # Calculate Euclidean distance
                distance = dist.euclidean(centroids[i], centroids[j])
                
                # If too close, mark both as violators
                if distance < threshold:
                    violations.add(i)
                    violations.add(j)
        
        return violations