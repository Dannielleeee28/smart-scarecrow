# detect_rice.py
import torch
from picamera2 import Picamera2
import numpy as np
import cv2

MODEL_PATH = "best.pt"
CLASSES = ["Raw", "Ripe"]

def load_model():
    try:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH, force_reload=False)
        return model
    except Exception as e:
        print("Failed to load YOLO model. Falling back to color detection.", e)
        return None

def detect_rice_stage(model):
    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())
    picam2.start()
    frame = picam2.capture_array()
    picam2.close()

    if model:
        results = model(frame)
        labels = results.xyxyn[0][:, -1].numpy()
        if len(labels) == 0:
            return "Raw", 0
        ripe_count = np.sum(labels == CLASSES.index("Ripe"))
        maturity = int((ripe_count / len(labels)) * 100)
        return "Ripe", maturity
    else:
        # HSV fallback
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        ratio = (cv2.countNonZero(mask) / (frame.size / 3)) * 100
        return ("Ripe", int(ratio)) if ratio > 50 else ("Raw", int(ratio))
