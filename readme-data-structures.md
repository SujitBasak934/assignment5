# Python Data Structures and Strings Assignment

This repository contains Python scripts that demonstrate data structures (dictionaries and lists) and string operations in Python.

## Task 1: Create a Dictionary of Student Marks

The `task1_student_marks.py` script demonstrates:
- Creating and using dictionaries in Python
- Accessing dictionary items using keys
- Handling cases where a key doesn't exist
- Basic user input and data retrieval

### Features:
- Creates a dictionary with student names as keys and their marks as values
- Displays all students in the database for reference
- Allows users to search for students by name
- Shows appropriate messages based on whether the student is found
- Provides grade interpretation based on marks
- Allows multiple searches without restarting the program

### Example Output:
```
Student Marks Lookup Program
==============================
Student Database:
------------------------------
John: 85
Emma: 92
Michael: 78
Sophia: 95
William: 88
Olivia: 90
James: 82
Ava: 91
Robert: 75
Isabella: 89
------------------------------

Enter a student's name to search: Emma

Student Found!
Mark for Emma: 92
Grade: A

Would you like to search for another student? (yes/no): yes
```

If the student doesn't exist:
```
Enter a student's name to search: David

Student 'David' not found in the database.
Please check the spelling or try another name.
```

## Task 2: Demonstrate List Slicing

The `task2_list_slicing.py` script demonstrates:
- Creating lists in Python
- Performing various list slicing operations
- Using negative indices and step values
- Additional list operations and methods

### Features:
- Creates a list of numbers from 1 to 10
- Extracts the first five elements using slicing
- Reverses the extracted elements using slicing syntax
- Shows various other slicing techniques for educational purposes
- Demonstrates additional list operations like comprehensions, filtering, and common methods

### Example Output:
```
List Slicing Demonstration
==============================
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
First five elements: [1, 2, 3, 4, 5]
Reversed first five: [5, 4, 3, 2, 1]

Additional list slicing examples:
Last five elements: [6, 7, 8, 9, 10]
Every other element: [1, 3, 5, 7, 9]
Every third element: [1, 4, 7, 10]
Elements from index 2 to 7: [3, 4, 5, 6, 7, 8]
Last three elements: [8, 9, 10]
All elements in reverse: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## How to Run

1. Make sure you have Python 3.x installed on your system
2. Download or clone this repository
3. Run the scripts using:

```
python task1_student_marks.py
python task2_list_slicing.py
```

## Key Concepts Demonstrated

- **Dictionaries**: Creating, accessing, and checking for keys
- **Lists**: Creation, slicing, and manipulation
- **String Handling**: Input processing and output formatting
- **User Interaction**: Taking user input and providing appropriate responses
- **Control Structures**: Using conditionals and loops for program flow
