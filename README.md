# 🚧 Pothole Detection Using YOLOv8

## 📌 Project Overview

Road potholes are a major safety concern that can cause accidents, vehicle damage, and traffic disruptions.

This project focuses on detecting potholes from images and videos using **YOLOv8 (You Only Look Once)**, a deep learning-based object detection model.

The system identifies potholes in road scenes using computer vision and displays bounding boxes around detected potholes.

## 🎯 Objectives

- Detect potholes automatically using deep learning.
- Identify potholes from images and video streams.
- Apply YOLOv8 for real-time object detection.
- Reduce the need for manual road inspection.
- Explore computer vision applications for road safety.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Deep Learning:** YOLOv8
- **Computer Vision:** OpenCV
- **Libraries:** Ultralytics, NumPy
- **Development Environment:** VS Code / Jupyter Notebook

## 📂 Project Structure

```text
Pothole-Detection-YOLOv8/
│
├── train_yolo.py
├── inference.py
├── pothole_inference.py
├── pothole.yaml
├── yolov8s.pt
│
├── media/
│   ├── uploads/
│   └── detections/
│
├── runs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: The actual repository may contain additional files and folders. Generated training outputs and large videos may be excluded from Git.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aakashv34/Pothole-Detection-YOLOv8.git
```

### 2. Navigate to the Project Directory

```bash
cd Pothole-Detection-YOLOv8
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install ultralytics opencv-python numpy
```

If a `requirements.txt` file is available, you can install all listed dependencies using:

```bash
pip install -r requirements.txt
```

## 🚀 Model Training

The project uses YOLOv8 for pothole detection.

To train the model using the dataset configuration:

```bash
yolo detect train data=pothole.yaml model=yolov8s.pt epochs=50 imgsz=640
```

Update the dataset paths in `pothole.yaml` according to your local dataset location.

## 🔍 Detection and Inference

After training, use the trained model for prediction.

**Image Detection:**

```bash
yolo detect predict model=best.pt source=test.jpg
```

**Video Detection:**

```bash
yolo detect predict model=best.pt source=video.mp4
```


## 📊 Key Features

- Automated pothole detection.
- YOLOv8-based object detection.
- Image-based pothole identification.
- Video-based pothole detection.
- Bounding box visualization.
- Detection result generation.

## 🔮 Future Enhancements

- Develop a web-based interface for pothole detection.
- Integrate real-time webcam detection.
- Improve detection accuracy using additional training data.
- Implement GPS-based pothole location tracking.
- Develop a road condition monitoring system.

## 👨‍💻 Developer

**Aakash V Devan**

- GitHub: [Aakashv34](https://github.com/Aakashv34)
- Project: [Pothole Detection using YOLOv8](https://github.com/Aakashv34/Pothole-Detection-YOLOv8)
Live Video : [LinkdIN](https://lnkd.in/p/gmZ4bRrg)

---

⭐ If you find this project interesting, consider giving it a star!
