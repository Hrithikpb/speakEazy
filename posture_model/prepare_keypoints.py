from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import json
import numpy as np

# Load keypoints data from JSON
with open('keypoints_data.json', 'r') as file:
    keypoints_data = json.load(file)

# Prepare the dataset
X = []  # Feature vectors
y = []  # Labels: 1 for good, 0 for bad

for item in keypoints_data:
    for keypoints in item['keypoints']:
        if len(keypoints) != 0:  # Ensure the keypoints list is not empty
            X.append(keypoints)
            y.append(1 if item['label'] == 'good' else 0)

X = np.array(X)
y = np.array(y)

# Normalize/Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
