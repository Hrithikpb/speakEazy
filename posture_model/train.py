import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from joblib import dump  # Import joblib for saving model and scaler

# Load data
with open('keypoints_data.json', 'r') as f:
    data = json.load(f)

# Function to preprocess keypoints
def preprocess_keypoints(keypoints, max_features=3238488):
    flattened = np.array(keypoints).flatten()
    if len(flattened) > max_features:
        flattened = flattened[:max_features]
    elif len(flattened) < max_features:
        flattened = np.pad(flattened, (0, max_features - len(flattened)), 'constant')
    return flattened

# Prepare the dataset
X = [preprocess_keypoints(sample['keypoints']) for sample in data]
y = [1 if sample['label'] == 'good' else 0 for sample in data]

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Normalize/Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model and scaler
dump(model, 'random_forest_model.joblib')
dump(scaler, 'scaler.joblib')

print("Model and scaler saved successfully. Training complete.")
