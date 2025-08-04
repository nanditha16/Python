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

# Define a module with a simple function
def my_module_function():
    logger.info("This is a function in _06_my_module.") 
    return "Module function executed successfully."
# This function can be used in other Python scripts to demonstrate module usage.   