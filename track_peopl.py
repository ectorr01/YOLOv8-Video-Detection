from ultralytics import YOLO

# Load the pre-trained YOLO model
model = YOLO("yolov8s.pt")  # Use "yolov8s" to download the model automatically

# Perform tracking on the video
results = model.track(source="sample.mp4", show=True, classes=[0])  # Class 0 = persons

# Set to store unique person IDs
unique_person_ids = set()

# Loop through all frames
for result in results:
    boxes = result.boxes
    if boxes is not None and len(boxes) > 0:
        if hasattr(boxes, 'id') and hasattr(boxes, 'cls'):
            track_ids = boxes.id.tolist()
            class_ids = boxes.cls.tolist()

            # Only consider persons (class 0)
            for cls, track_id in zip(class_ids, track_ids):
                if int(cls) == 0:  # Class 0 = person
                    unique_person_ids.add(int(track_id))

# Print total number of unique people
print(f"Unique people found in the video: {len(unique_person_ids)}")
