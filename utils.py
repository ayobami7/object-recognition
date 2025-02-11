import cv2

def draw_boxes(frame, boxes, centroids, violations):
    for i, (box, centroid) in enumerate(zip(boxes, centroids)):
        color = (0, 255, 0) if i not in violations else (0, 0, 255)
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.circle(frame, centroid, 5, color, -1)