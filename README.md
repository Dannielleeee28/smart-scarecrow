# 🌾 Smart Scarecrow System

A solar-powered, Raspberry Pi-based robotic scarecrow designed to **monitor rice maturity** using computer vision (YOLOv5) and **deter birds** through motion and sound, with real-time alerts via **GSM SMS notifications**.

## 📸 Features
- 📷 Real-time rice ripeness detection using a Raspberry Pi Camera and YOLOv5.
- 🔊 Continuous bird deterrent sound played through speaker.
- 🦅 Motion-activated bird scaring via PIR sensor + servo.
- 📩 SMS alerts when rice is ripe using SIM800L GSM module.
- ☀️ Powered by solar energy and a 12V battery setup.

## 🧠 Tech Stack
- Raspberry Pi 4B (64-bit)
- Raspberry Pi Camera Module 3
- YOLOv5 (`best.pt`) model trained via Roboflow
- SIM800L V2 GSM module
- PIR sensor + servo motor
- Python 3, OpenCV, PyTorch, Picamera2

## 🔁 How It Works
1. Camera captures images continuously.
2. Tries to load YOLOv5 model and detect "Ripe" rice.
3. If model fails, uses HSV-based fallback color detection.
4. Sends SMS alert if rice is mature.
5. Plays hawk sound continuously to scare birds.
6. Activates servo motion if PIR sensor detects movement.

## 🔧 Setup
Clone this repo and install requirements:

```bash
git clone https://github.com/Dannielleeee28/smart-scarecrow.git
cd smart-scarecrow
pip install -r requirements.txt
```

> Ensure Picamera2 is properly configured on Raspberry Pi OS 64-bit.

## 🪫 Power Supply
- Powered using a 12V 25Ah battery via 2 XL4015 buck converters
  - 5.2V for Raspberry Pi
  - 5.2V for GSM module

## 📬 Acknowledgments
- YOLOv5 by Ultralytics
- Roboflow for dataset training
- Raspberry Pi Foundation

---

*This project was built as a capstone requirement for Computer Engineering at the University of Perpetual Help System Laguna.*
