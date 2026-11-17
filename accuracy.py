from ultralytics import YOLO

# Load the trained model
model = YOLO(r'D:\pothole_detection\runs\detect\train4\weights\best.pt')  # Path to the best model

# Evaluate the model on the validation dataset
results = model.val()  # Automatically uses validation data defined in pothole.yaml

# Print metrics
print(f"Precision: {results.metrics['precision']}")
print(f"Recall: {results.metrics['recall']}")
print(f"mAP@0.5: {results.metrics['map50']}")  # Mean Average Precision at IoU=0.5
print(f"mAP@0.5:0.95: {results.metrics['map']}")  # Mean Average Precision across IoU thresholds
