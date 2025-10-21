
# Social Distancing Monitoring System

![Social Distancing Monitor](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-orange)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)

A real-time social distancing monitoring system that uses **YOLOv3** for object detection and **Flask** for web-based streaming. The system detects people in a video stream, checks for social distancing violations, and displays the results in real-time on a web app.

---

## Features

- **Real-Time Monitoring**: Processes live video from a webcam or video file.
- **Social Distancing Detection**: Identifies people and checks if they are maintaining a safe distance.
- **Web Interface**: Streams the processed video to a web browser.
- **Modular Design**: Separates camera handling, detection logic, and web app for easy maintenance.
- **Customizable**: Adjust detection thresholds, video resolution, and more.

---

## Project Structure

```
social_distancing_monitor/
├── app.py                  # Main Flask application
├── camera.py               # Video capture handler
├── detection.py            # YOLO detection & distancing logic
├── utils.py                # Drawing utilities
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── .gitignore             
├── templates/
│   └── index.html         # Web interface
├── static/                # CSS/JS files
│   └── styles.css
├── yolov3.weights         # (237 MB)
├── yolov3.cfg             
└── coco.names             
```

---

## Requirements

- Python 3.7+
- OpenCV
- Flask
- NumPy
- SciPy
- imutils

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/social-distancing-monitor.git
   cd social-distancing-monitor
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv3 Files**:
   - Download the following files and place them in the project root:
     - `yolov3.weights`: [Download](https://pjreddie.com/files/yolov3.weights)
     - `yolov3.cfg`: [Download](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
     - `coco.names`: [Download](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

---

## Usage

1. **Run the Flask App**:
   ```bash
   python app.py
   ```

2. **Access the Web App**:
   - Open your browser and navigate to `http://localhost:5000`.
   - The web app will display the live video stream with social distancing violations highlighted.

3. **Adjust Settings**:
   - Modify the `threshold` values in `detection.py` to adjust the sensitivity of social distancing detection.
   - Change the video resolution in `camera.py` for better performance.

---

## Customization

- **Add Email Alerts**:
  Integrate an email notification system to send alerts when violations exceed a threshold.

- **Log Violations**:
  Save violation data to a database or file for further analysis.

- **Deploy to Cloud**:
  Use platforms like **Heroku**, **AWS**, or **Google Cloud** to deploy the web app.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **YOLOv3**: Object detection model by Joseph Redmon.
- **OpenCV**: Computer vision library.
- **Flask**: Lightweight web framework for Python.

---

