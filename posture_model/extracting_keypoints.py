import cv2
import mediapipe as mp
import numpy as np
import json
import os

def extract_keypoints_from_video(video_path, label):
    cap = cv2.VideoCapture(video_path)
    keypoints_data = []

    with mp.solutions.holistic.Holistic() as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)

            if results.pose_landmarks:
                keypoints = np.array([[lm.x, lm.y, lm.z, lm.visibility] for lm in results.pose_landmarks.landmark])
                keypoints = keypoints.flatten()
                print(keypoints)
                keypoints_data.append(keypoints.tolist())

    cap.release()
    return {'label': label, 'keypoints': keypoints_data}

def main():
    data = []
    for label in ['good', 'bad']:
        directory = f'./training/{label}/'
        for filename in os.listdir(directory):
            if filename.endswith('.mp4'):
                video_path = os.path.join(directory, filename)
                video_data = extract_keypoints_from_video(video_path, label)
                data.append(video_data)

    with open('keypoints_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
