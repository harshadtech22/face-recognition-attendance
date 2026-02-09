import cv2
import face_recognition
import os
from datetime import datetime

# --- Step 1: Load known faces ---
path = 'images'   # Folder with student images
known_encodings = []
known_names = []

for file in os.listdir('C:\project\images'):
    img = face_recognition.load_image_file(f"{path}/{file}")# type: ignore
    encoding = face_recognition.face_encodings(img)[0]
    known_encodings.append(encoding)
    known_names.append(os.path.splitext(file)[0])  # filename without extension

# --- Step 2: Function to mark attendance ---
def mark_attendance(name):
    now = datetime.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
    with open('attendance.csv', 'a') as f:
        f.write(f"{name},{dt_string}\n")

# --- Step 3: Start webcam ---
cap = cv2.VideoCapture(0)

print("Press 'q' to quit the program.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    faces = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, faces)

    # Compare with known faces
    for encoding, face in zip(encodings, faces):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]
            mark_attendance(name)

        # Draw rectangle and name
        top, right, bottom, left = face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show video
    cv2.imshow('Attendance System', frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()