import ultralytics
from ultralytics import YOLO
import cv2
import numpy as np

# Load the trained YOLOv8 model
model_path = "D:/Projects/Bauch_Defect_Detection/yolodefect.pt"
try:
    model = YOLO(model_path)  # Ensure the model path is correct
    print(f"Model loaded successfully from: {model_path}")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Open webcam (0 for default, change if using external)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLOv8 inference on the frame
    results = model(frame, conf=0.1, task="detect")  # Use "detect" for bounding boxes

    # Loop through results and display detections
    for result in results:
        annotated_frame = result.plot()  # Overlay detections on frame

        # Display the frame with detections
        cv2.imshow("YOLOv8 Real-time Defect Detection", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
