#  Python Functions, Modules, Packages and Workspaces Usage Example
 
# Functions allow you to encapsulate logic, while modules and packages help structure your codebase.
# This script demonstrates how to define and use functions, modules, and packages in Python.  

# Import necessary modules  
import os
import sys
import logging
import _06_my_module
from _06_my_module_2 import square

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a simple function 
# This function takes a name as an argument and returns a greeting message.

# This is a simple function that greets a user by name.
# It demonstrates how to define a function, use parameters, and return a value.
def greet(name):
    """
    Function to greet a user by name.

    Args:
        name (str): The name of the user to greet.

    Returns:
        str: A greeting message.

    Raises:
        TypeError: If the provided name is not a string.

    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    if not isinstance(name, str):
        logger.error("The 'name' argument must be a string.")
        raise TypeError("The 'name' argument must be a string.")
    return f"Hello, {name}!"

# Example usage of the function
if __name__ == "__main__":
    try:
        logger.info("Executing _05_my_function.py as the main module.")
        logger.info("Calling greet() function.")
        # Call the greet function with a sample name
        user_name = "Alice"
        logger.info("Calling greet() with user_name: %s", user_name)
        # Call the greet function and print the result
        greeting = greet(user_name)
        print(greeting)  # Output: Hello, Alice!
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# Example usage of the module function
if __name__ == "__main__":
    try:
        logger.info("Executing _05_my_function.py as the main module.")
        # Call the function from the imported module
        logger.info("Calling _06_my_module.my_module_function() from _05_my_function.py.")
        result = _06_my_module.my_module_function()
        logger.info("Calling square() of _06_my_module_2 from _05_my_function.py.")
        square_result = square(5)
        logger.info("Square of 5 is: %s", square_result)
        print(result)  # Output: Module function executed successfully.
    except Exception as e:
        logger.error(f"An error occurred while calling the module function: {e}")