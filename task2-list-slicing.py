# Task 2: Demonstrate List Slicing
# This program creates a list of numbers, extracts elements,
# reverses them, and demonstrates various list operations.

def demonstrate_list_slicing():
    """
    Function to demonstrate list slicing operations:
    1. Creates a list of numbers from 1 to 10
    2. Extracts the first five elements
    3. Reverses the extracted elements
    4. Prints both lists
    """
    # Create a list of numbers from 1 to 10
    numbers = list(range(1, 11))
    a=numbers.append(76)
    print(f"Original list: {a}")
    
    # Extract the first five elements
    first_five = numbers[:5]  # This is equivalent to numbers[0:5]
    print(f"First five elements: {first_five}")
    
    # Reverse the extracted elements
    reversed_five = first_five[::-1]
    print(f"Reversed first five: {reversed_five}")
    
    # Additional list slicing operations for demonstration
    print("\nAdditional list slicing examples:")
    print(f"Last five elements: {numbers[5:]}")
    print(f"Every other element: {numbers[::2]}")
    print(f"Every third element: {numbers[::3]}")
    print(f"Elements from index 2 to 7: {numbers[2:8]}")
    print(f"Last three elements: {numbers[-3:]}")
    print(f"All elements in reverse: {numbers[::-1]}")

def demonstrate_list_operations():
    """
    Function to demonstrate additional list operations
    beyond simple slicing
    """
    # Create the base list
    numbers = list(range(1, 11))
    
    print("\nAdditional List Operations:")
    print("-" * 30)
    
    # List comprehension example
    squares = [x**2 for x in numbers]
    print(f"Squares of numbers: {squares}")
    
    # Filtering with list comprehension
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")
    
    # Common list methods
    numbers_copy = numbers.copy()
    numbers_copy.append(11)
    print(f"After append: {numbers_copy}")
    
    numbers_copy.insert(0, 0)
    print(f"After insert at beginning: {numbers_copy}")
    
    numbers_copy.remove(5)
    print(f"After removing 5: {numbers_copy}")
    
    popped_value = numbers_copy.pop()
    print(f"Popped value: {popped_value}")
    print(f"After pop: {numbers_copy}")
    
    # Sorting examples
    random_numbers = [7, 2, 5, 1, 9, 3]
    random_numbers.sort()
    print(f"Sorted list: {random_numbers}")
    
    random_numbers.sort(reverse=True)
    print(f"Reverse sorted: {random_numbers}")

# Main program
if __name__ == "__main__":
    print("List Slicing Demonstration")
    print("=" * 30)
    
    # Demonstrate basic list slicing as required
    demonstrate_list_slicing()
    
    # Demonstrate additional list operations
    demonstrate_list_operations()
