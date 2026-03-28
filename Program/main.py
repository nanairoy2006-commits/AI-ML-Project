# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_data.csv")

# Features and target
X = data[['study_hours', 'sleep_hours', 'attendance']]
y = data['marks']

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict using test data
predictions = model.predict(X_test)

print("Predicted Marks:", predictions)

# Take user input
study_hours = float(input("Enter study hours: "))
sleep_hours = float(input("Enter sleep hours: "))
attendance = float(input("Enter attendance (%): "))

# Predict result
result = model.predict([[study_hours, sleep_hours, attendance]])

print(f"Predicted Marks: {result[0]:.2f}")