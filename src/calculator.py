"""
- datatype :int, float
- Arithmetic  (+-*/%)
- interactive mode
"""
from utility.library import get_input


def calculator_check(operationcheck, x, y):
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
