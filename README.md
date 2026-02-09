# Face Recognition Attendance System 📸

## 📌 Overview
This is an automated **Attendance System** built using Python. It leverages machine learning to detect faces in real-time via a webcam, compares them against a database of known faces, and automatically logs the attendance (Name, Date, Time) into a CSV file.

## 🚀 Features
- **Real-time Detection:** Detects faces instantly using OpenCV.
- **High Accuracy:** Uses the `face_recognition` library (based on dlib) for precise matching.
- **Automated Logging:** Saves attendance data to `attendance.csv` automatically.
- **Dynamic Loading:** Automatically loads and encodes all images found in the `images/` folder.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:**
  - `opencv-python` (Video capture and processing)
  - `face_recognition` (Face detection and encoding)
  - `numpy` (Data handling)
  - `os` & `datetime` (System operations)

## 📂 Project Structure
```text
Face-Recognition-Attendance/
│
├── images/                  # Folder containing student photos
│   ├── harshad.jpg          # (Filename becomes the user's name)
│   ├── amit.jpg
│   └── ...
│
├── main.py                  # The main Python script
├── attendance.csv           # Auto-generated attendance log
└── README.md                # Project documentation
🏃‍♂️ Usage
Run the main script:

Bash

python main.py

The webcam will start.

When a known face is detected, it will draw a green box and display the name.

Press 'q' to exit the program.

📊 Output
The system generates an attendance.csv file that looks like this:

Code snippet

Harshad,2026-02-09 10:30:15
Amit,2026-02-09 10:35:00
👨‍💻 Author
Harshad Prasad

CSE (AIML) Student
