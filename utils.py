import cv2

def draw_boxes(frame, boxes, centroids, violations):
    """
    Draw bounding boxes and centroids on frame
    
    Args:
        frame: Input image (modified in-place)
        boxes: List of [x, y, w, h] bounding boxes
        centroids: List of (x, y) centroid tuples
        violations: Set of indices for people violating distancing
    """
    for i, (box, centroid) in enumerate(zip(boxes, centroids)):
        # Green for safe, red for violation
        color = (0, 255, 0) if i not in violations else (0, 0, 255)
        
        # Draw bounding box
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        
        # Draw centroid
        cv2.circle(frame, centroid, 5, color, -1)