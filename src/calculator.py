"""
- datatype :int, float
- Arithmetic  (+-*/%)
- interactive mode
"""
import sys
import os

# Ensure the parent directory is in sys.path so 'utility' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing get_input from utility.library
# This assumes that the utility/library.py file is in the parent directory of src/calculator.py
# Add an empty __init__.py file to your utility folder. This makes it a Python package and allows for proper imports.
from utility.library import get_positive_number
from utility.library import get_input

def calculator_check(operationcheck, x, y): 
    """
    Performs a basic arithmetic operation on two numbers.

    Args:
        operationcheck (str): The operation to perform. Supported values are '+', '-', '*', '/', '%'.
        x (float or int): The first operand.
        y (float or int): The second operand.

    Returns:
        float or int: The result of the arithmetic operation.

    Raises:
        SystemExit: If division or modulo by zero is attempted, or if an unsupported operation is provided.

    Side Effects:
        Prints an error message and exits the program if division/modulo by zero is attempted or if the operation is unsupported.
    """
    if operationcheck == "+":
        return x + y
    elif operationcheck == "-":
        return x - y
    elif operationcheck == "*":
        return x * y
    elif operationcheck == "/":
        try:
            if y == 0:
                raise ZeroDivisionError
            return x / y
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            exit(1)
    elif operationcheck == "%":
        try:
            if y == 0:
                raise ZeroDivisionError
            return x % y
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            exit(1)
    else:
        print("Unsupported operation. Please select one of '+', '-', '*', '/', '%'.")
        exit(1)


def main():
    num_flavor = input("what type are the numbers? [int, float] ")

    if num_flavor not in ('int', 'float'):
        print("Invalid number type. Please select 'int' or 'float'.")
        exit(1)

    match num_flavor:
        case 'int':
            try:
                x = int(get_input("What's x? "))
                y = int(get_input("What's y? "))
            except ValueError:
                print("Invalid input. Please enter valid integers.")
                exit(1)
        case 'float':
            try:
                x = float(get_input("What's x? "))
                y = float(get_input("What's y? "))
            except ValueError:
                print("Invalid input. Please enter valid floats.")
                exit(1)

    operation = get_input("What operation? [+-*/%]")

    result = round(calculator_check(operation, x, y), 3)
    # adding , for readability like 1,000
    print(f"{result:,}")


"""
Main starts here
"""
if __name__ == "__main__":
    main()
