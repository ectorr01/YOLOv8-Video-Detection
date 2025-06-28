# 📌 README: Count Unique People in a Video using YOLOv8

## 🎯 Objective

This script analyzes a video using the **YOLOv8** model with built-in **object tracking**, detects people, and prints the total number of **unique individuals** identified by their unique tracking IDs.

Ideal for applications like crowd counting, person tracking, or video analytics.

---

## 🧰 Requirements

Make sure to install the required library:

```bash
pip install ultralytics
```

- `ultralytics`: provides the YOLOv8 model and tracking tools.

---

## 📁 Project Structure

```
yolo-person-tracking/
│
├── yolov8s.pt             # Pre-trained YOLOv8 model (optional, can be downloaded automatically)
├── sample.mp4             # Input video to analyze
└── track_people.py        # Main tracking script
```

---

## ⚙️ Setup

1. Download your input video and name it `sample.mp4`.
2. Place it in the same folder as the script.
3. If you don't have the `yolov8s.pt` model, download it from:
   👉 [https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s.pt](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s.pt)

> Note: You can use `YOLO("yolov8s")` instead to automatically download the model on first run.

---

## ▶️ Run the Script

Run the script using:

```bash
python track_people.py
```

---

## 🖥 Output

The script:
- Displays the video with bounding boxes and tracking IDs in real-time.
- Prints the total number of **unique people** detected during the video.

Example output:

```
Unique people found in the video: 5
```
---

## ✅ Features

- Lightweight and fast.
- No web interface or server needed.
- Ideal for quick testing or integration into other projects.

---

## 🔚 Notes

- Tracking is handled internally by YOLO using ByteTrack.
- For best results, avoid overly crowded scenes or fast camera movements.
- You can extend this code to export data to CSV, draw counts on screen, or save processed frames.
