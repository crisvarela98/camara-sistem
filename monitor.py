import cv2
import datetime
from utils.motion_detector import MotionDetector

cap = cv2.VideoCapture(0)  # webcam (para IP usar URL)

detector = MotionDetector()

recording = False
out = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    motion = detector.detect(frame)

    if motion and not recording:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recordings/event_{timestamp}.avi"

        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(filename, fourcc, 20.0, (frame.shape[1], frame.shape[0]))

        recording = True
        print("Movimiento detectado - grabando:", filename)

    if recording:
        out.write(frame)

    cv2.imshow("Camera Monitor", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()

if out:
    out.release()

cv2.destroyAllWindows()