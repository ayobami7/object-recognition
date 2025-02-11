import cv2
import numpy as np
from scipy.spatial import distance as dist

class SocialDistancingDetector:
    def __init__(self, weights_path, config_path, classes_path):
        self.net = cv2.dnn.readNet(weights_path, config_path)
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        with open(classes_path, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

    def detect_people(self, frame):
        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)
        return outs, height, width

    def process_frame(self, frame, outs, width, height, threshold=0.5):
        boxes = []
        centroids = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > threshold and class_id == 0:  # Class ID 0 is for "person"
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    centroids.append((center_x, center_y))
        return boxes, centroids

    def check_distancing(self, centroids, threshold=100):
        violations = set()
        for i in range(len(centroids)):
            for j in range(i + 1, len(centroids)):
                if dist.euclidean(centroids[i], centroids[j]) < threshold:
                    violations.add(i)
                    violations.add(j)
        return violations