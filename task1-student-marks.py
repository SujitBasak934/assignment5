

# Creating a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74,
    "Eva": 88
}

# Asking user for input
student_name = input("Enter the student's name: ")

# Retrieving and displaying the marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found in the records.")
