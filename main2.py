import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset: avg_intensity and on/off (0 for off, 1 for on)
data = {
    'avg_intensity': [50, 100, 150, 200, 250, 300, 350, 400],
    'on_off': [1, 1, 1, 0, 0, 0, 0, 0]  # Example labels (1 = light on, 0 = light off)
}

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Features and labels
X = df[['avg_intensity']]  # Features
y = df['on_off']  # Target labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Example: Predict whether to turn the light on/off for a given avg_intensity value
avg_intensity_value = 175  # Example intensity value
prediction = model.predict([[avg_intensity_value]])

if prediction == 1:
    print(f"For avg_intensity {avg_intensity_value}, light should be ON.")
else:
    print(f"For avg_intensity {avg_intensity_value}, light should be OFF.")
