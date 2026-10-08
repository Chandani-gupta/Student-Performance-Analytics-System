import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    assign_grade,
    check_pass_fail
)

df = pd.read_csv("student.csv")
print("\nDATASET INFORMATION")
print("Number of students:", len(df))
print("Number of columns:", len(df.columns))
print("Columns:", list(df.columns))
df["Total_Marks"] = df.apply(calculate_total, axis=1)

df["Average_Marks"] = df.apply(calculate_average, axis=1)

df["Grade"] = df["Average_Marks"].apply(assign_grade)

df["Result"] = df.apply(
    lambda row: check_pass_fail(
        row["Average_Marks"],
        row["Attendance"]
    ),
    axis=1
)
print(df)
print("\nSUBJECT-WISE ANALYSIS")

print("Python Average:", np.mean(df["Python_Marks"]))
print("Mathematics Average:", np.mean(df["Mathematics_Marks"]))
print("English Average:", np.mean(df["English_Marks"]))
highest_student = df.loc[df["Average_Marks"].idxmax()]
lowest_student = df.loc[df["Average_Marks"].idxmin()]

print("\nHIGHEST PERFORMER")
print("Student_ID:", highest_student["Student_ID"])
print("Name:", highest_student["Name"])
print("Average_Marks:", highest_student["Average_Marks"])
print("Grade:", highest_student["Grade"])
print("\nLOWEST PERFORMER")
print("Student_ID:", lowest_student["Student_ID"])
print("Name:", lowest_student["Name"])
print("Average_Marks:", lowest_student["Average_Marks"])
print("Grade:", lowest_student["Grade"])
print("\nCLASS SUMMARY")

print("Total Students:", len(df))

print("Passed Students:", (df["Result"] == "PASS").sum())

print("Failed Students:", (df["Result"] == "FAIL").sum())

print("Overall Class Average:", np.mean(df["Average_Marks"]))
print("\nBEST SUBJECT")

subject_averages = {
    "Python": np.mean(df["Python_Marks"]),
    "Mathematics": np.mean(df["Mathematics_Marks"]),
    "English": np.mean(df["English_Marks"])
}

for subject, average in subject_averages.items():
    print(subject, "Average:", round(average, 2))

best_subject = max(subject_averages, key=subject_averages.get)

print("Best Subject:", best_subject)
print("\nTOP PERFORMERS")

top_students = df.sort_values("Average_Marks", ascending=False).head(3)

print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]])