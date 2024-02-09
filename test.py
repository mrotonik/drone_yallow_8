import cvzone
from ultralytics import YOLO
import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default camera
facemodel = YOLO('yolov8n-drone.pt')  # Ensure the model is intended for your specific detection task

while cap.isOpened():
    rt, frame = cap.read()
    if not rt:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (1020, 720))
    mainframe = frame.copy()

    detection_result = facemodel.predict(frame)
    for info in detection_result:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            h, w = y2-y1, x2-x1

            cvzone.cornerRect(frame, [x1, y1, w, h], l=9, rt=3)
            cvzone.cornerRect(mainframe, [x1, y1, w, h], l=9, rt=3)

            face = frame[y1:y1+h, x1:x1+w]
            face = cv2.blur(face, (30, 30))
            frame[y1:y1+h, x1:x1+w] = face

    allFeeds = cvzone.stackImages([mainframe, frame], 2, 0.70)
    cv2.imshow('frame', mainframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
