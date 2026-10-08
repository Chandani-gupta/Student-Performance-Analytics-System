Student Performance Analytics System

Project Description

The Student Performance Analytics System is a Python-based mini project developed to analyze student academic performance using a CSV dataset.

The system reads student details and marks from "student.csv", performs calculations using Pandas and NumPy, and displays useful performance analysis.

Features

- Displays dataset information
- Calculates total marks for each student
- Calculates average marks
- Assigns grades based on average marks
- Determines PASS/FAIL based on average marks and attendance
- Calculates subject-wise averages
- Identifies the highest performer
- Identifies the lowest performer
- Displays total number of students
- Displays passed and failed students
- Calculates overall class average
- Identifies the best subject
- Displays the top 3 performers

Technologies Used

- Python
- Pandas
- NumPy
- CSV Dataset

Project Structure

Student-Performance-Analytics-System/
│
├── main.py
├── functions.py
├── student.csv
├── README.md
└── venv/

Files Description

"main.py"

Contains the main program logic. It reads the CSV file, performs analysis, and displays the results.

"functions.py"

Contains the functions used for:

- Calculating total marks
- Calculating average marks
- Assigning grades
- Checking PASS/FAIL

"student.csv"

Contains the student information, including:

- Student ID
- Name
- Department
- Python Marks
- Mathematics Marks
- English Marks
- Attendance

Analysis Performed

The system generates:

1. Dataset information
2. Student-wise performance
3. Subject-wise average marks
4. Highest performer
5. Lowest performer
6. Class summary
7. Best subject
8. Top 3 performers

How to Run

Install the required libraries:

pip install pandas numpy

Run the project:

python main.py

Output

The program displays the calculated student performance data and analytical results directly in the terminal.

Project Status

Completed features: Student performance calculation and basic academic analytics.