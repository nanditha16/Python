   # In-Built

1. **Numeric Data Types:**
   - **int**: Represents integers (whole numbers). Example: `x = 5`
   - **float**: Represents floating-point numbers (numbers with decimal points). Example: `y = 3.14`
   - **complex**: Represents complex numbers. Example: `z = 2 + 3j`

2. **Sequence Types:**
   - **str**: Represents strings (sequences of characters). Example: `text = "Hello, World"`
   - **list**: Represents lists (ordered, mutable sequences). Example: `my_list = [1, 2, 3]`
   - **tuple**: Represents tuples (ordered, immutable sequences). Example: `my_tuple = (1, 2, 3)`

3. **Mapping Type:**
   - **dict**: Represents dictionaries (key-value pairs). Example: `my_dict = {'name': 'John', 'age': 30}`

4. **Set Types:**
   - **set**: Represents sets (unordered collections of unique elements). Example: `my_set = {1, 2, 3}`
   - **frozenset**: Represents immutable sets. Example: `my_frozenset = frozenset([1, 2, 3])`

5. **Boolean Type:**
   - **bool**: Represents Boolean values (`True` or `False`). Example: `is_valid = True`

6. **Binary Types:**
   - **bytes**: Represents immutable sequences of bytes. Example: `data = b'Hello'`
   - **bytearray**: Represents mutable sequences of bytes. Example: `data = bytearray(b'Hello')`

7. **None Type:**
   - **NoneType**: Represents the `None` object, which is used to indicate the absence of a value or a null value.

8. **Custom Data Types:**
   - You can also define your custom data types using classes and objects.

   # Strings

**1. String Data Type in Python:**

- In Python, a string is a sequence of characters, enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.
- Strings are immutable, meaning you cannot change the characters within a string directly. Instead, you create new strings.
- You can access individual characters in a string using indexing, e.g., `my_string[0]` will give you the first character.
- Strings support various built-in methods, such as `len()`, `upper()`, `lower()`, `strip()`, `replace()`, and more, for manipulation.

**2. String Manipulation and Formatting:**

- Concatenation: You can combine strings using the `+` operator.
- Substrings: Use slicing to extract portions of a string, e.g., `my_string[2:5]` will extract characters from the 2nd to the 4th position.
- String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and `str.format()`.
- Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
- String methods: Python provides many built-in methods for string manipulation, such as `split()`, `join()`, and `startswith()`.


# Numberic Data Type

**1. Numeric Data Types in Python (int, float):**

- Python supports two primary numeric data types: `int` for integers and `float` for floating-point numbers.
- Integers are whole numbers, and floats can represent both whole and fractional numbers.
- You can perform arithmetic operations on these types, including addition, subtraction, multiplication, division, and more.
- Be aware of potential issues with floating-point precision, which can lead to small inaccuracies in calculations.
- Python also provides built-in functions for mathematical operations, such as `abs()`, `round()`, and `math` module for advanced functions.

# Regex

**1. Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
- Examples of regex usage: matching emails, phone numbers, or extracting data from text.
- `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.


   # arguments and environment variables 

- arguments are passed to the script via the command line, allowing for dynamic input.
   - os is used to manipulate the file system, such as checking if a directory exists.
- environment variables can be accessed and modified, allowing for configuration of the script's behavior.
   - sys is used to manipulate the Python runtime environment, such as modifying the import path.  


   # Python operators 

## Introduction

Operators in Python are fundamental building blocks that allow you to manipulate data and perform computations.
They are special symbols or keywords that are used to perform operations on variables and values. 
Python supports a wide range of operators, categorized into several types.


Here is a brief overview of the main types of operators in Python:

1. **Arithmetic Operators:** These operators are used for performing basic mathematical operations such as addition, subtraction, multiplication, division, and more. 

### List of Arithmetic Operators
   1. **Addition (+):** Adds two numbers.
   2. **Subtraction (-):** Subtracts the right operand from the left operand.
   3. **Multiplication (*):** Multiplies two numbers.
   4. **Division (/):** Divides the left operand by the right operand (results in a floating-point number).
   5. **Floor Division (//):** Divides the left operand by the right operand and rounds down to the nearest whole number.
   6. **Modulus (%):** Returns the remainder of the division of the left operand by the right operand.
   7. **Exponentiation (**):** Raises the left operand to the power of the right operand.

### Examples
   arithmetic_operations(10, 5)


2. **Assignment Operators:** Assignment operators are used to assign values to variables. They include the equal sign (=) and various compound assignment operators that perform an operation on the variable while assigning a value.

### List of Assignment Operators
   1. **Basic Assignment (=):** Assigns a value to a variable.
   2. **Addition Assignment (+=):** Adds the right operand to the left operand and assigns the result to the left operand.
   3. **Subtraction Assignment (-=):** Subtracts the right operand from the left operand and assigns the result to the left operand.
   4. **Multiplication Assignment (*=):** Multiplies the left operand by the right operand and assigns the result to the left operand.
   5. **Division Assignment (/=):** Divides the left operand by the right operand and assigns the result to the left operand.
   6. **Floor Division Assignment (//=):** Performs floor division on the left operand and assigns the result to the left operand.
   7. **Modulus Assignment (%=):** Calculates the modulus of the left operand and assigns the result to the left operand.
   8. **Exponentiation Assignment (**=):** Raises the left operand to the power of the right operand and assigns the result to the left operand.

### Examples
   assignment_operations()


3. **Comparison/Relational Operators:** They are used to compare two values and determine the relationship between them. These operators return a Boolean result(`True` or `False`).

### List of Comparison/Relational Operators
   1. **Equal to (==):** Checks if two values are equal.
   2. **Not equal to (!=):** Checks if two values are not equal.
   3. **Greater than (>):** Checks if the left operand is greater than the right operand.
   4. **Less than (<):** Checks if the left operand is less than the right operand.
   5. **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand.
   6. **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand.

### Examples
   relational_comparison_operations(10, 5)


4. **Logical Operators:** Logical operators are used to combine and manipulate Boolean values. These operators allow you to perform logical operations such as AND, OR, and NOT.

### List of Logical Operators
   1. **AND (and):** Returns `True` if both operands are `True`.
   2. **OR (or):** Returns `True` if at least one of the operands is `True`.
   3. **NOT (not):** Returns the opposite Boolean value of the operand.

### Examples
   logical_operations(True, False)


5. **Identity Operators:** Identity operators are used to check if two variables point to the same object in memory. It is used to compare the memory locations of two objects to determine if they are the same object or not. The two identity operators are "is" and "is not."

### List of Identity Operators
   1. **is:** Returns `True` if both operands refer to the same object.
   2. **is not:** Returns `True` if both operands refer to different objects.

### Examples
   identity_operations([1, 2, 3], [1, 2, 3])


6. **Membership Operators:** Membership operators are used to check if a value is present in a sequence or collection, such as a list, tuple, or string. The membership operators are "in" and "not in."

### List of Membership Operators
   1. **in:** Returns `True` if the left operand is found in the sequence on the right.
   2. **not in:** Returns `True` if the left operand is not found in the sequence on the right.

### Examples
   membership_operations(3, [1, 2, 3, 4, 5])


7. **Bitwise Operators:** Bitwise operators are used to perform operations on individual bits of binary numbers.  These operators include bitwise AND, OR, XOR, and more.

### List of Bitwise Operators
   1. **Bitwise AND (&):** Performs a bitwise AND operation on the binary representations of the operands.
   2. **Bitwise OR (|):** Performs a bitwise OR operation.
   3. **Bitwise XOR (^):** Performs a bitwise XOR operation.
   4. **Bitwise NOT (~):** Flips the bits of the operand (bitwise NOT operation), changing 0 to 1 and 1 to 0.
   5. **Left Shift (<<):** Shifts the bits to the left by a specified number of positions.
   6. **Right Shift (>>):** Shifts the bits to the right.

## Examples
   bitwise_operations(5, 3)

>>>>>>>>>>>>>>>>>>>>>
8. **Precedence of Operations:** Operators in Python have different levels of precedence, which determine the order in which operations are performed in an expression. Operators with higher precedence are evaluated first.

## Examples
   - multiplication and division have higher precedence than addition and subtraction. 
