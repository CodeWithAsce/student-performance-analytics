
import pandas as pd
import numpy as np
from pathlib import Path

# Load student dataset
df = pd.read_csv(Path(__file__).parent / "students.csv")

# Calculate total and average marks
subjects = ["Python", "Maths", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Assign grades
def calculate_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

# Display analysis
print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
print(df.to_string(index=False))

print("\n===== CLASS SUMMARY =====")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", round(df["Average"].max(), 2))
print("Lowest Average:", round(df["Average"].min(), 2))
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

print("\n===== SUBJECT-WISE AVERAGE =====")
print(df[subjects].mean().round(2))

print("\n===== TOP PERFORMER =====")
top_student = df.loc[df["Average"].idxmax()]
print("Name:", top_student["Name"])
print("Average:", round(top_student["Average"], 2))
