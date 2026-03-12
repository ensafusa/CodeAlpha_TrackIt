import cv2
from ultralytics import YOLO

model = YOLO("rtdetr-l.pt")
#model.train(data="custom_data.yaml", epochs=50, imgsz=640)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model.track(frame, persist=True, tracker="botsort.yaml", imgsz=960, conf=0.3, iou=0.5, agnostic_nms=True)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Real-Time Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()