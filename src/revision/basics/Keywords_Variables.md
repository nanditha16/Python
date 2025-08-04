# Keywords and Variables:

### Keywords:

**Note**: Total number of keywords: 35
1. **False**:  
   - **Definition**: `False` is a Boolean value representing logical falsehood in Python.
   - **Usage**: Used in logical operations, conditionals, and as a return value to indicate failure or a negative result.
   - **Example**:
     ```python
     is_active = False
     if not is_active:
         print("Inactive")
     ```
2. **None**:  
   - **Definition**: `None` is a special constant representing the absence of a value or a null value.
   - **Usage**: Used to indicate no value, or that a variable is not set.
   - **Example**:
     ```python
     result = None
     if result is None:
         print("No result")
     ```
3. **True**:  
   - **Definition**: `True` is a Boolean value representing logical truth in Python.
   - **Usage**: Used in logical operations, conditionals, and as a return value to indicate success or a positive result.
   - **Example**:
     ```python
     is_valid = True
     if is_valid:
         print("Valid")
     ```
4. **and**:  
   - **Definition**: `and` is a logical operator used to combine conditional statements.
   - **Usage**: Returns `True` if both operands are true.
   - **Example**:
     ```python
     if is_valid and is_active:
         print("Both conditions are true")
     ```
5. **as**:  
   - **Definition**: `as` is used to create an alias while importing a module or in exception handling.
   - **Usage**: Assigns a new name to a module or exception.
   - **Example**:
     ```python
     import numpy as np
     try:
         1 / 0
     except ZeroDivisionError as e:
         print(e)
     ```
6. **assert**:  
   - **Definition**: `assert` is used for debugging purposes to test if a condition is true.
   - **Usage**: Raises an `AssertionError` if the condition is false.
   - **Example**:
     ```python
     assert 2 + 2 == 4
     ```
7. **async**:  
   - **Definition**: `async` is used to declare an asynchronous function.
   - **Usage**: Used with `def` to define a coroutine.
   - **Example**:
     ```python
     async def fetch_data():
         pass
     ```
8. **await**:  
   - **Definition**: `await` is used to pause the execution of an async function until a result is available.
   - **Usage**: Used inside async functions to wait for coroutines.
   - **Example**:
     ```python
     async def main():
         await fetch_data()
     ```
9. **break**:  
   - **Definition**: `break` is used to exit a loop prematurely.
   - **Usage**: Stops the nearest enclosing loop.
   - **Example**:
     ```python
     for i in range(5):
         if i == 3:
             break
     ```
10. **class**:  
    - **Definition**: `class` is used to define a new user-defined class.
    - **Usage**: Declares a class.
    - **Example**:
      ```python
      class MyClass:
          pass
      ```
11. **continue**:  
    - **Definition**: `continue` skips the rest of the code inside a loop for the current iteration.
    - **Usage**: Proceeds to the next iteration of the loop.
    - **Example**:
      ```python
      for i in range(5):
          if i == 2:
              continue
          print(i)
      ```
12. **def**:  
    - **Definition**: `def` is used to define a function.
    - **Usage**: Declares a function.
    - **Example**:
      ```python
      def greet():
          print("Hello")
      ```
13. **del**:  
    - **Definition**: `del` is used to delete objects.
    - **Usage**: Removes variables, list items, or dictionary entries.
    - **Example**:
      ```python
      x = [1, 2, 3]
      del x[0]
      ```
14. **elif**:  
    - **Definition**: `elif` is used in conditional statements as "else if".
    - **Usage**: Checks another condition if previous ones are false.
    - **Example**:
      ```python
      if x < 0:
          print("Negative")
      elif x == 0:
          print("Zero")
      ```
15. **else**:  
    - **Definition**: `else` is used in conditional and loop statements to specify a block of code to run if all previous conditions are false.
    - **Usage**: Executes when previous conditions are not met.
    - **Example**:
      ```python
      if x > 0:
          print("Positive")
      else:
          print("Not positive")
      ```
16. **except**:  
    - **Definition**: `except` is used to catch and handle exceptions.
    - **Usage**: Specifies a block of code to run if an error occurs in the try block.
    - **Example**:
      ```python
      try:
          1 / 0
      except ZeroDivisionError:
          print("Cannot divide by zero")
      ```
17. **finally**:  
    - **Definition**: `finally` is used to define a block of code that will be executed no matter what, after try and except blocks.
    - **Usage**: Ensures code runs after try/except.
    - **Example**:
      ```python
      try:
          x = 1
      finally:
          print("Always runs")
      ```
18. **for**:  
    - **Definition**: `for` is used to create a for loop.
    - **Usage**: Iterates over a sequence.
    - **Example**:
      ```python
      for i in range(3):
          print(i)
      ```
19. **from**:  
    - **Definition**: `from` is used to import specific parts of a module.
    - **Usage**: Imports specific attributes or functions.
    - **Example**:
      ```python
      from math import sqrt
      ```
20. **global**:  
    - **Definition**: `global` is used to declare that a variable inside a function is global.
    - **Usage**: Modifies a global variable inside a function.
    - **Example**:
      ```python
      x = 0
      def set_global():
          global x
          x = 5
      ```
21. **if**:  
    - **Definition**: `if` is used to make a conditional statement.
    - **Usage**: Executes a block of code if a condition is true.
    - **Example**:
      ```python
      if x > 0:
          print("Positive")
      ```
22. **import**:  
    - **Definition**: `import` is used to import modules.
    - **Usage**: Brings in external modules.
    - **Example**:
      ```python
      import sys
      ```
23. **in**:  
    - **Definition**: `in` is used to check if a value exists within an iterable.
    - **Usage**: Tests membership.
    - **Example**:
      ```python
      if 2 in [1, 2, 3]:
          print("Found")
      ```
24. **is**:  
    - **Definition**: `is` tests object identity.
    - **Usage**: Checks if two variables point to the same object.
    - **Example**:
      ```python
      a = b = []
      print(a is b)
      ```
25. **lambda**:  
    - **Definition**: `lambda` is used to create anonymous functions.
    - **Usage**: Defines small, unnamed functions.
    - **Example**:
      ```python
      square = lambda x: x * x
      print(square(3))
      ```
26. **nonlocal**:  
    - **Definition**: `nonlocal` is used to declare that a variable inside a nested function is not local to that function.
    - **Usage**: Modifies a variable in the nearest enclosing scope.
    - **Example**:
      ```python
      def outer():
          x = 1
          def inner():
              nonlocal x
              x = 2
      ```
27. **not**:  
    - **Definition**: `not` is a logical operator that inverts the truth value.
    - **Usage**: Returns `True` if the operand is false.
    - **Example**:
      ```python
      if not False:
          print("True")
      ```
28. **or**:  
    - **Definition**: `or` is a logical operator used to combine conditional statements.
    - **Usage**: Returns `True` if at least one operand is true.
    - **Example**:
      ```python
      if x < 0 or x > 10:
          print("Out of range")
      ```
29. **pass**:  
    - **Definition**: `pass` is a null statement; it does nothing.
    - **Usage**: Used as a placeholder.
    - **Example**:
      ```python
      def func():
          pass
      ```
30. **raise**:  
    - **Definition**: `raise` is used to raise an exception.
    - **Usage**: Triggers an exception.
    - **Example**:
      ```python
      raise ValueError("Invalid value")
      ```
31. **return**:  
    - **Definition**: `return` is used to exit a function and return a value.
    - **Usage**: Sends a result back from a function.
    - **Example**:
      ```python
      def add(a, b):
          return a + b
      ```
32. **try**:  
    - **Definition**: `try` is used to specify exception handling blocks.
    - **Usage**: Wraps code that may raise exceptions.
    - **Example**:
      ```python
      try:
          x = 1 / 0
      except ZeroDivisionError:
          print("Error")
      ```
33. **while**:  
    - **Definition**: `while` is used to create a while loop.
    - **Usage**: Repeats a block of code while a condition is true.
    - **Example**:
      ```python
      i = 0
      while i < 3:
          print(i)
          i += 1
      ```
34. **with**:  
    - **Definition**: `with` is used to wrap the execution of a block with methods defined by a context manager.
    - **Usage**: Manages resources like files.
    - **Example**:
      ```python
      with open("file.txt") as f:
          data = f.read()
      ```
35. **yield**:  
    - **Definition**: `yield` is used in a function to make it a generator.
    - **Usage**: Returns a value and pauses the function, saving its state for resumption.
    - **Example**:
      ```python
      def count():
          yield 1
          yield 2
      ```

**Note**: Avoid using keywords as variable names or identifiers to prevent syntax errors.
**Note**: Keywords are used to define the syntax and structure of the Python language.
**Note**: Keywords are case-sensitive and must be used exactly


### Variables:
**Note**: Variables are used to store data values.
**Note**: In Python, variables do not need to be declared with a specific type.
**Note**: You can simply assign a value to a variable, and Python will infer the type (Dynamic Type).
**Note**: Variable names can consist of letters, numbers, and underscores, 
**Note**: Variable cannot start with a number and cannot be a keyword.
**Note**: Variable names are case-sensitive, so `myVariable` and `myvariable` are considered different variables.
**Note**: You can use underscores to separate words in variable names for better readability.


### Variable Scope and Lifetime:
**Note**: Variables can have different scopes in Python:
1. **Local Scope**: 
    - Variables defined inside a function are local to that function 
    - Cannot access a local variable outside its scope will raise an error
2. **Global Scope**: 
    - Variables defined outside any function are global 
    - Can be accessed anywhere in the module.
3. **Nonlocal Scope**: 
    - Variables defined in an enclosing function 
    - Can be accessed in nested functions.


### Variable Naming Conventions and Best Practices:
1. **Use descriptive names**:
    - Variable names should be descriptive and indicate their purpose.
2. **Use underscores to separate words**:
    - Use lowercase letters and separate words with underscores (snake_case) for variable names.
    - Can also use camelCase or PascalCase but try not to.
3. **loop counters**:
    - Avoid using single character names except for loop counters.
4. **No keywords/reserved words**: 
    - Avoid using reserved words (keywords) for variable names.
    - Using keywords like 'if', 'for', 'while', etc. will raise a SyntaxError
5. **Use Lowercase letters **:
    - Use lowercase letters for variable names
6. **Use meaningful names**:
    - Use meaningful names that reflect the purpose of the variable
7. **No special characters or spaces**:
    - Avoid using special characters or spaces in variable names
    - Special characters like @, #, $, etc. are not allowed in variable names
    - hyphens (-) are not allowed in Python functions/variables/module names. 
    - Names must only contain letters, numbers, and underscores, and cannot start with a number.
8. **Consistency**:
    - Use consistent naming conventions throughout your code
    - Stick to a single naming convention (like snake_case) for all variable names
9. **Use comments**:
    - Use comments to explain the purpose of variables:
    - Comments can help clarify the purpose of a variable
10. **Use constants**:
    - Use constants for values that should not change:
    - Constants are typically defined in uppercase letters
11. **Use plural names**:
    - Use plural names for collections or lists:
12.  **Use singular names**:
    - Use singular names for individual items
13. Use descriptive names for functions and methods.
14. Use prefixes or suffixes to indicate the type of variable.
15. Use camelCase for class names.
16. Use snake_case for function and variable names.
17. Python function names cannot start with numbers. Function names (like variable and module names) must begin with a letter (a–z, A–Z) or an underscore (_), and can be followed by letters, digits (0–9), or underscores.

### Practice Exercises and Examples:

#### Example: Using Variables to Store and Manipulate Configuration Data in a DevOps Context
1. Example 01-devOps_usecase_config
**Security best practices**:
- Use environment variables for sensitive data (like DB credentials).
- Never log or print sensitive information.
- Always handle file and JSON errors.
- Avoid shell injection by using shlex or subprocess with argument lists.
- Mask sensitive data in outputs and logs.
- Validate all user and config inputs in production code.
