import cv2
import mediapipe as mp
import numpy as np
import json  # Import the json module

# Initialize MediaPipe Holistic.
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic()

# Setup utility for drawing keypoints.
mp_drawing = mp.solutions.drawing_utils

# Load a video file
cap = cv2.VideoCapture('./training/good/tedtalk.mp4')

# List to store keypoints data
keypoints_data = []

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert the BGR image to RGB and process it with MediaPipe Holistic.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)

    # Extract keypoints and append to the list
    if results.pose_landmarks:
        # Flatten the landmarks into a single list
        pose = np.array([[lm.x, lm.y, lm.z, lm.visibility] for lm in results.pose_landmarks.landmark]).flatten()
        print (pose)
        keypoints_data.append(pose.tolist())

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # Draw the holistic annotations on the image.
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    # Other drawing functionalities as necessary

    # Show the image.
    cv2.imshow('MediaPipe Holistic - Detailed Pose and Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Optionally save keypoints data to a file
with open('keypoints_data.json', 'w') as f:
    json.dump(keypoints_data, f)
