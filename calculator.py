"""
- datatype :int
- Arithmetic  (+-*/%)
- interactive mode
"""
numFlavor = input("what type are the numbers? ")

match numFlavor:
    case 'int':
        x = int(input("What's x? "))
        y = int(input("What's 7? "))
    case 'float':
        x = float(input("What's x? "))
        y = float(input("What's 7? "))

operation = input("What operation? ")
def switch(operation):
    if operation == "+":
        return x+y
    elif operation == "-":
        return x-y
    elif operation == "*":
        return x*y
    elif operation == "/":
        return x/y
    elif operation == "%":
        return x%y

print("result", switch(operation))