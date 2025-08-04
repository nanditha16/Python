# Note: This script demonstrates how to define and use functions, modules, and packages in Python.
# It also highlights the importance of organizing code for reusability and modularity.
# Python Functions, Modules, Packages and Workspaces Usage Example

# Import necessary modules
import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a module with a simple function to calculate the square of a number
# This function takes a number as an argument and returns its square.
def my_module_2_function():
    logger.info("This is a function in _06_my_module_2.")

def square(x):
    logger.info("This is a square function in _06_my_module_2.")
    return x ** 2
    
# It can define functions, classes, and variables that can be used in other Python scripts.
pi = 3.14159265

# Example usage of the module function
if __name__ == "__main__":
    logger.info("Executing _06_my_module_2.py as the main module.")
    logger.info("Calling my_module_2_function() and square(2).")
    # Call the functions defined in this module 
    my_module_2_function()
    print("Square of 2 is:", square(2))  # Output: Square of 2 is: 4

