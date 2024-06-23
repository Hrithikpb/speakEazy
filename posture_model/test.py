import cv2
import mediapipe as mp
import numpy as np
import os
import openai
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from joblib import load  # Used for loading model and scaler

# Load environment variables and API key
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')



model = load('random_forest_model.joblib')
scaler = load('scaler.joblib')

def analyze_posture(frame, holistic):
    """Analyzes the posture by processing a video frame."""
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    if results.pose_landmarks:
        keypoints = np.array([[lm.x, lm.y, lm.z, lm.visibility] for lm in results.pose_landmarks.landmark]).flatten()
        keypoints = scaler.transform([keypoints])  # Normalize features
        prediction = model.predict(keypoints)
        return 'good' if prediction[0] == 1 else 'bad'
    return 'unknown'

def generate_feedback(posture):
    """Generates feedback using OpenAI's GPT-4 based on the detected posture."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Check OpenAI for the correct GPT-4 model identifier
            messages=[{"role": "system", "content": "You are a public speaking coach."},
                      {"role": "user", "content": f"The posture detected is {posture}. Please provide feedback."}],
            max_tokens=150
        )
        feedback = response.choices[0].message.content.strip()
        return feedback
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error in generating feedback."

# Process a video file
cap = cv2.VideoCapture('./testing/video1.mp4')
with mp.solutions.holistic.Holistic() as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        posture = analyze_posture(frame, holistic)
        feedback = generate_feedback(posture)
        print(feedback)

cap.release()
