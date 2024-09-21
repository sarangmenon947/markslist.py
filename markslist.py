import random

# Predefined list of student names
students = [
    "Arun", "Deeksh", "Sarang", "Renuka", "Priya",
    "Karan", "Meera", "Vikram", "Tanvi", "Rajesh",
    "Sneha", "Anil", "Pooja", "Ravi", "Nisha",
    "Amit", "Kavya", "Siddharth", "Neha", "Rohan"
]

# Generate 20 random marks between 0 and 100
marks = [random.randint(0, 100) for _ in range(20)]

# Combine student names with their respective marks
student_scores = list(zip(students, marks))

# Initialize lists for different categories
low_marks = []    # Marks <= 30
medium_marks = [] # Marks between 31 and 69
high_marks = []   # Marks >= 70

# Categorize the marks into the respective lists
for student, mark in student_scores:
    if mark <= 30:
        low_marks.append((student, mark))
    elif 31 <= mark <= 69:
        medium_marks.append((student, mark))
    else:
        high_marks.append((student, mark))

# Print the results
print("Student Scores:")
for student, score in student_scores:
    print(f"{student}: {score}")

print("\nMarks <= 30:")
for student, score in low_marks:
    print(f"{student}: {score}")

print("\nMarks between 31 and 69:")
for student, score in medium_marks:
    print(f"{student}: {score}")

print("\nMarks >= 70:")
for student, score in high_marks:
    print(f"{student}: {score}")
