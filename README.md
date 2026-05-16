# Real-Time Object Tracking System
-----------------------------------
-----------------------------------
A computer vision project designed for high-precision real-time detection and tracking of specific objects (e.g., pens and boxes) using the **RT-DETR** architecture.

## -- Overview
-----------------
This project leverages **RT-DETR (Real-Time Detection Transformer)** to track objects in live video streams. Unlike traditional CNN-based models, this transformer-based approach provides superior contextual understanding and robust tracking, making it highly effective even when objects are partially occluded or overlap with other scene elements.

## -- Why RT-DETR?
------------------
- **Global Context Awareness:** Uses self-attention mechanisms to understand the relationship between objects and the entire image context, resulting in superior detection robustness.
- **NMS-Free Pipeline:** Operates as a direct set-prediction model, eliminating the latency and complexity of traditional Non-Maximum Suppression (NMS).
- **Hybrid Efficiency:** Engineered to maintain high reasoning power while meeting the strict low-latency requirements of real-time applications.

## -- Features
----------------
- **Real-Time Inference:** Fast, transformer-based detection via the Ultralytics framework.
- **Persistent Tracking:** Employs BoT-SORT for maintaining object identities across frames.
- **Modular Design:** Easily extensible to support custom objects through fine-tuning.

## -- Installation
-------------------
Ensure you have Python 3.9+ installed.

```bash
# Clone the repository
git clone https://github.com/ensafusa/CodeAlpha_TrackIt.git

# Install dependencies
pip install ultralytics opencv-python
```
## -- How to Run
----------------
1. Connect your webcam.

2. Execute the tracking script:

```Bash
python tracker.py
```

3. Press q to exit the video feed.

## -- Configuration
-------------------
The tracker.py script can be tuned for your specific hardware and accuracy needs:

- **imgsz:** Controls input resolution (e.g., 640, 960, or 1280). Increase for better small-object detection.

- **conf:** Detection confidence threshold (0.0 to 1.0).

- **iou:** Intersection over Union threshold for tracking consistency.

## -- Roadmap
-------------
- **Fine-Tuning:** Collect and label a custom dataset for specialized object recognition.

- **Deployment:** Export model to OpenVINO/ONNX for further latency optimization.

- **Expanded Classes:** Update custom_data.yaml as the dataset grows.

## -- License
-------------
Author: Doha El IDRISSI

Developed as part of a CodeAlpha Internship project.
