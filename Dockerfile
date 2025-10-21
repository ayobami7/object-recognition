FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Download YOLO files
RUN wget -q https://pjreddie.com/media/files/yolov3.weights && 
    # wget -q https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg && \
    # wget -q https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

# Expose port
EXPOSE 10000

# Run with gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT app:app