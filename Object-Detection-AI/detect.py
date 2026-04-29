from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 20

# Save output video
out = cv2.VideoWriter(
    "output_detection.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (frame_width, frame_height)
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Write frame to video
    out.write(annotated_frame)

    # Show live output
    cv2.imshow("Detection Recording", annotated_frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
