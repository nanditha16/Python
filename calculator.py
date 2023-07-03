"""
- datatype :int, float
- Arithmetic  (+-*/%)
- interactive mode
"""
numFlavor = input("what type are the numbers? [int, float] ")

if numFlavor not in ('int', 'float'):
    print("Invalid number type. Please select 'int' or 'float'.")
    exit(1)

match numFlavor:
    case 'int':
        try:
            x = int(input("What's x? "))
            y = int(input("What's y? "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            exit(1)
    case 'float':
        try:
            x = float(input("What's x? "))
            y = float(input("What's y? "))
        except ValueError:
            print("Invalid input. Please enter valid floats.")
            exit(1)

operation = input("What operation? [+-*/%]")
def switch(operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        try:
            if y == 0:
                raise ZeroDivisionError
            return x / y
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            exit(1)
    elif operation == "%":
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

print("Result:", switch(operation))