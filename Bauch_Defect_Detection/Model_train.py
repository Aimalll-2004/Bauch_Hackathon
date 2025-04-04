from ultralytics import YOLO

# Load the YOLOv8 model (it can be a pre-trained model, or we will train it from scratch)
model = YOLO("yolov8n.pt")  # You can change "yolov8n.pt" to "yolov8s.pt" or "yolov8m.pt" based on the size you want.

# Dataset path (Roboflow dataset)
data_path = 'D:/Projects/Bauch_Defect_Detection/dataset/data.yaml'  # Replace this with your dataset YAML file path.

# Train the model
model.train(data=data_path, epochs=50, imgsz=640)  # Change epochs and image size based on your need

# Save the model after training
model.save("D:/Projects/Bauch_Defect_Detection/yolodefect.pt")
