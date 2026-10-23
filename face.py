import cv2
from fer import FER

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
sdsd
if not cap.isOpened():
    print("❌ Camera not found")
    exit()

# ================= EMOTION DETECTOR =================
detector = FER(mtcnn=False)  # 🔥 IMPORTANT: OFF MTCNN

print("Press SPACE to quit")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    frame = cv2.resize(frame, (640, 480))

    # ================= DETECT EMOTIONS =================
    results = detector.detect_emotions(frame)

    if results:
        for result in results:
            x, y, w, h = result["box"]
            emotions = result["emotions"]

            dominant_emotion = max(emotions, key=emotions.get)
            score = emotions[dominant_emotion]

            # Draw face box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Label
            label = f"{dominant_emotion} ({score:.2f})"
            cv2.putText(
                frame,
                label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    cv2.putText(frame, "Press SPACE to quit", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == 32:  # SPACE
        break

cap.release()
cv2.destroyAllWindows()
