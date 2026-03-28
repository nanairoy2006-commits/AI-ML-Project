# AI-ML-Project
Student Performance Predictor

This project uses a Machine Learning model to predict student marks based on study habits such as study hours, sleep hours, and attendance. It is a simple implementation of Linear Regression using Python.

Technologies Used
Python
pandas
numpy
scikit-learn
matplotlib (optional)
Project Structure
Student Marks Predictor/
│
├── main.py                # Main Python script
├── student_data.csv       # Dataset file
├── README.md              # Documentation
Setup and Installation Guide

Follow the steps below to set up and run the project on your system.

Step 1: Install Python
Go to https://www.python.org/downloads/
Download and install the latest version of Python
During installation, enable the option "Add Python to PATH"

To verify installation, open a terminal or command prompt and run:

python --version
Step 2: Install a Code Editor (Optional)

You may use any editor, but Visual Studio Code is recommended.

Download from https://code.visualstudio.com/
Install it
Install the Python extension inside the editor
Step 3: Get the Project Files

Option A: Download manually

Download the project folder and extract it

Option B: Clone using Git

git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
Step 4: Create a Virtual Environment (Recommended)

Create a virtual environment:

python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
Step 5: Install Dependencies

Install required libraries using pip:

pip install pandas numpy scikit-learn matplotlib
Step 6: Prepare Dataset

Create a file named student_data.csv in the project folder with the following content:

study_hours,sleep_hours,attendance,marks
2,6,60,50
3,7,65,55
4,6,70,60
5,7,75,65
6,8,80,70
7,7,85,75
8,8,90,85
9,6,95,90
10,7,98,95

Ensure:

The file is saved with .csv extension
It is located in the same directory as main.py
The file is not empty
Step 7: Run the Project

Navigate to the project folder in terminal and run:

python main.py
Step 8: Provide Input

The program will ask for:

Study hours
Sleep hours
Attendance percentage

Example:

Enter study hours: 6
Enter sleep hours: 7
Enter attendance (%): 80
Step 9: Output

The program will display predicted marks:

Predicted Marks: 72.45
How the Project Works
The dataset is loaded using pandas
Input features (study hours, sleep hours, attendance) are separated from the target (marks)
The data is split into training and testing sets
A Linear Regression model is trained on the training data
The model learns relationships between input features and marks
The user provides new input values
The trained model predicts the output marks
Troubleshooting
Error: No columns to parse from file
Ensure the CSV file is not empty
Verify correct formatting
Save the file properly
ModuleNotFoundError

Install missing libraries:

pip install pandas numpy scikit-learn
FileNotFoundError
Ensure student_data.csv is in the same folder as main.py
Check file name spelling
Future Improvements
Add a graphical user interface
Deploy as a web application
Use advanced machine learning models
Include more input features
Conclusion

This project demonstrates how machine learning can be used to predict student performance based on simple input parameters. It provides a basic understanding of supervised learning and regression techniques.

Student:

Soumyadipta Roy
Registration Number: 25BHI10111
