#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
echo "=== Starting build process ==="
echo "Python version: $(python --version)"

# Upgrade pip and build tools
echo "=== Upgrading pip and build tools ==="
pip install --upgrade pip setuptools wheel

pip install -r requirements.txt

# Download YOLO files if not present
if [ ! -f yolov3.weights ]; then
    echo "Downloading YOLOv3 weights..."
    wget https://pjreddie.com/files/yolov3.weights
fi

if [ ! -f yolov3.cfg ]; then
    echo "Downloading YOLOv3 config..."
    wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
fi

if [ ! -f coco.names ]; then
    echo "Downloading COCO names..."
    wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
fi