# Task 1: Create a Dictionary of Student Marks
# This program creates a dictionary of student names and marks,
# allows users to search for a student, and displays their marks.

def create_student_dictionary():
    """
    Creates a dictionary of student names and their marks.
    
    Returns:
        dict: A dictionary with student names as keys and marks as values
    """
    # Create a dictionary with student names and marks
    students = {
        "John": 85,
        "Emma": 92,
        "Michael": 78,
        "Sophia": 95,
        "William": 88,
        "Olivia": 90,
        "James": 82,
        "Ava": 91,
        "Robert": 75,
        "Isabella": 89
    }
    
    return students

def search_student_marks():
    """
    Main function that:
    1. Creates a student dictionary
    2. Takes user input for a student name
    3. Displays the marks if the student exists in the dictionary
    4. Shows a message if the student doesn't exist
    """
    # Get the student dictionary
    students = create_student_dictionary()
    
    # Display all students in the dictionary
    print("Student Database:")
    print("-" * 30)
    for student, mark in students.items():
        print(f"{student}: {mark}")
    print("-" * 30)
    
    # Get user input for student name
    student_name = input("\nEnter a student's name to search: ")
    
    # Check if the student exists in the dictionary
    if student_name in students:
        # Display the student's marks
        print(f"\nStudent Found!")
        print(f"Mark for {student_name}: {students[student_name]}")
        
        # Provide grade interpretation
        mark = students[student_name]
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"Grade: {grade}")
        
    else:
        # Display message if student not found
        print(f"\nStudent '{student_name}' not found in the database.")
        print("Please check the spelling or try another name.")

# Main program
if __name__ == "__main__":
    print("Student Marks Lookup Program")
    print("=" * 30)
    
    # Run the main function
    search_student_marks()
    
    # Allow multiple searches
    while True:
        another_search = input("\nWould you like to search for another student? (yes/no): ")
        if another_search.lower() not in ["yes", "y"]:
            print("Thank you for using the Student Marks Lookup Program!")
            break
        search_student_marks()
