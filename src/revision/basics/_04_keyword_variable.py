# Keywords:
# This script lists all the keywords in Python.
# Note: This list is based on Python 3.10. The keywords may change in future versions.
# To see the current list of keywords, you can use the `keyword` module.
import keyword

print("Here is a list of Python keywords:")
print(keyword.kwlist)

# Output the list of keywords
print(f"Total number of keywords: {len(keyword.kwlist)}")

# You can also check if a string is a keyword using `keyword.iskeyword()`
test_string = "if"
if keyword.iskeyword(test_string):
    print(f'"{test_string}" is a keyword in Python.') #Output: "if" is a keyword in Python.
else:
    print(f'"{test_string}" is not a keyword in Python.')

# Example of using a keyword in a variable assignment
# Note: Using keywords as variable names will raise a SyntaxError.
# For example, the following line would raise an error:
# if = 5  # This will raise a SyntaxError

# Instead, use a different name for the variable
my_variable = 5 # This is a valid variable assignment

# Variables:

# Here are some examples of valid variable names:
x = 10  # An integer variable
y = 3.14  # A float variable
name = "Alice"  # A string variable
is_active = True  # A boolean variable
# Note: Variable names can include letters, numbers, and underscores.
# Note: Variable names cannot start with a number and cannot be a keyword.
user_age = 30  # A variable name with underscores

# Variable Scope:
# 1. Local Scope: 
def my_function():
    local_var = "I am local"
    print(local_var)
# Trying to access a local variable outside its scope will raise an error
# print(local_var)  # This will raise a NameError

# 2. Global Scope:
global_var = "I am global"

def another_function():
    print(global_var)  # This will work

# 3. Nonlocal Scope: 
def outer_function():
    nonlocal_var = "I am nonlocal"
    
    def inner_function():
        print(nonlocal_var)  # This will work
    inner_function()
    
my_function()
another_function()
outer_function()

### Variable Naming Conventions and Best Practices:
# 1. Use descriptive names:
user_age = 25  
# 2. Use underscores to separate words:
first_name = "John" 
camelCaseVariable = "This is camelCase" 
PascalCaseVariable = "This is PascalCase"
# 3. loop counters:
print("Using 'i' in Loop Example ")
for i in range(5):
    print(i)  # Using 'i' as a loop counter is acceptable
# 4. No keywords/reserved words:
# Example of a keyword used incorrectly:
# if = 10  # This will raise a SyntaxError
# Instead, use a different name:
if_condition = 10  # This is a valid variable name
# 5. Use Lowercase letters:
my_variable = "Hello"  # Instead of using uppercase letters
# 6. Use meaningful names:
counter = 0  # Instead of using vague names like a or b
# 7. No special characters or spaces:
# Example of an invalid variable name:
# my-variable = 10  # This will raise a SyntaxError
# Instead, use underscores:
my_variable = 10  # This is a valid variable name
# 8. Consistency:
# Example of consistent naming:
user_name = "Alice"
user_age = 30  # Both variables use snake_case naming convention
# 9. Use comments:
# Example of a variable with a comment:
user_age = 25  # Age of the user in years
# 10. Use constants: 
PI = 3.14159  # Value of Pi, which is a constant
# 11. Use plural names for collections:
user_names = ["Alice", "Bob", "Charlie"]  # A list of user names
# 12. Use singular names for individual items:
user_name = "Alice"  # A single user's name
# 13. Use descriptive names for functions and methods:
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return 3.14 * radius ** 2  # Using a descriptive function name
# 14. Use prefixes or suffixes to indicate the type of variable:
is_active = True  # Using 'is_' prefix for boolean variables
# 15. Use camelCase for class names:
class UserProfile:
    """A class representing a user profile."""
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Using camelCase for class names
# 16. Use snake_case for function and variable names:
def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b  # Using snake_case for function names

