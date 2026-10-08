import numpy as np
def calculate_total(row):
    """Calculate total marks for a student."""
    return (
        row["Python_Marks"]
        + row["Mathematics_Marks"]
        + row["English_Marks"]
    )


def calculate_average(row):
    """Calculate average marks for a student."""
    marks = np.array([
        row["Python_Marks"],
        row["Mathematics_Marks"],
        row["English_Marks"]
    ])
    return np.mean(marks)
    
    


def assign_grade(average):
    """Assign a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(average, attendance):
    """Determine whether a student has passed."""
    if average >= 50 and attendance >= 75:
        return "PASS"
    else:
        return "FAIL"