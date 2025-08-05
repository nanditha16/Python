import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function to demonstrate arithmetic operations : +, -, *, /, %, //, **
def arithmetic_operations(a, b):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        a (int or float): First number.
        b (int or float): Second number.
    
    Returns:
        dict: A dictionary containing the results of the operations.
    """
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else 'Division by zero error',
        'modulus': a % b if b != 0 else 'Division by zero error',
        'floor_division': a // b if b != 0 else 'Division by zero error',
        'exponentiation': a ** b
    }
    
# Define a function to demonstrate assignment operations :
def assignment_operations():
    """
    Demonstrate assignment operations using various operators.
    
    Returns:
        dict: A dictionary containing the results of the assignment operations.
    """
    x = 10
    x += 5  # x is now 15
    x -= 3  # x is now 12
    x *= 2  # x is now 24
    x /= 4  # x is now 6.0
    # x %= 3  # x is now 0.0
    return {
        'x': x,
        'x_after_addition': x + 5,
        'x_after_subtraction': x - 3,
        'x_after_multiplication': x * 2,
        'x_after_division': x / 4
    }

# Define a function to demonstrate relational/comparison operators  :
def relational_comparison_operations(a, b):
    """
    Perform relational/comparison operations on two numbers.
    
    Args:
        a (int or float): First number.
        b (int or float): Second number.
    
    Returns:
        dict: A dictionary containing the results of the operations.
    """
    return {
        'equal': a == b, # Check if equal output False
        'not_equal': a != b, # Check if not equal output True
        'greater_than': a > b, # Check if greater than output True
        'less_than': a < b, # Check if less than output False
        'greater_than_equal': a >= b, # Check if greater than or equal output True
        'less_than_equal': a <= b # Check if less than or equal output False
    }
 
# Define a function to demonstrate logical operators:
def logical_operations(x, y):
    """
    Perform logical operations on two boolean values.
    
    Args:
        x (bool): First boolean value.
        y (bool): Second boolean value.
    
    Returns:
        dict: A dictionary containing the results of the logical operations.
    """
    return {
        'and': x and y, # Check if both are True output False
        'or': x or y,   # Check if either is True output True
        'not_x': not x,  # Check if x is False output False
        'not_y': not y   # Check if y is False output True
    }

# Define a function to demonstrate identity operators
def identity_operations(a, b):
    """
    Perform identity operations on two objects.
    
    Args:
        a: First object.
        b: Second object.
    
    Returns:
        dict: A dictionary containing the results of the identity operations.
    """
    return {
        'is': a is b, # Check if both refer to the same object 
        'is_not': a is not b # Check if both do not refer to the same object 
    }

# Define a function to demonstrate membership operators
def membership_operations(a, b):
    """
    Perform membership operations to check if 'a' is in 'b' and not in 'b'.

    Args:
        a: Element to check.
        b: Collection (like list, tuple, string, etc.).

    Returns:
        dict: A dictionary containing the results of the membership operations.
    """
    return {
        'in': a in b, # checks if 'a' is a member of 'b'. 
        'not_in': a not in b # checks if 'a' is not a member of 'b'.
    }

# Define a function to demonstrate bitwise operators
def bitwise_operations(a, b):
    """
    Perform bitwise operations on two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        dict: A dictionary containing the results of the bitwise operations.
    """
    return {
        'and': a & b, 
        'or': a | b,
        'xor': a ^ b,
        'not_a': ~a,
        'left_shift_a': a << 1,
        'right_shift_a': a >> 1
    }

# Define a function to demonstrate precedence operators
def precedence_operations():
    """
    Demonstrate operator precedence in Python expressions.

    Returns:
        dict: A dictionary showing results of expressions with different operator precedence.
    """
    a = 2 + 3 * 4      # Multiplication has higher precedence than addition
    b = (2 + 3) * 4    # Parentheses change the order
    c = 2 ** 3 ** 2    # Exponentiation is right-associative
    d = 100 / 10 * 2   # Left to right for operators with same precedence
    e = 5 + 4 > 7 and 2 < 5  # Comparison and logical operators
    return {
        '2 + 3 * 4': a,  
        '(2 + 3) * 4': b,
        '2 ** 3 ** 2': c,
        '100 / 10 * 2': d,
        '5 + 4 > 7 and 2 < 5': e
    }


# Demonstrate test and demonstrate operator usage
if __name__ == "__main__":
    # Call the arithmetic operations function to demonstrate usage
    arith_result = arithmetic_operations(10, 5)
    logger.info(f"Arithmetic operations result for 10 and 5: {arith_result}")
    # Output: Arithmetic operations result for 10 and 5: {'addition': 15, 'subtraction': 5, 'multiplication': 50, 'division': 2.0, 'modulus': 0, 'floor_division': 2, 'exponentiation': 100000}

    # Call the assignment operations function to demonstrate usage
    assignment_result = assignment_operations()
    logger.info(f"Assignment operations result: {assignment_result}")
    # Output: Assignment operations result: {'x': 6.0, 'x_after_addition': 11.0, 'x_after_subtraction': 3.0, 'x_after_multiplication': 12.0, 'x_after_division': 1.5}

    # Call the relational/comparison operations function to demonstrate usage
    relational_result = relational_comparison_operations(10, 5)
    logger.info(f"Relational operations result for 10 and 5: {relational_result}")
    # Output: Relational operations result for 10 and 5: {'equal': False, 'not_equal': True, 'greater_than': True, 'less_than': False, 'greater_than_equal': True, 'less_than_equal': False}

    # Call the logical operations function to demonstrate usage
    logical_result = logical_operations(True, False)
    logger.info(f"Logical operations result for True and False: {logical_result}")
    # Output: Logical operations result for True and False: {'and': False, 'or': True, 'not_x': False, 'not_y': True}

    # Call the identity operations function to demonstrate usage
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    identity_result = identity_operations(x, z)
    identity_result2 = identity_operations(x, y)
    logger.info(f"Identity operations result for two lists: {identity_result}")
    logger.info(f"Identity operations result for two lists: {identity_result2}")
    # Output: Identity operations result for two lists: {'is': False, 'is_not': True}
    # Output: Identity operations result for two lists: {'is': True, 'is_not': False}

    # Call the membership operations function to demonstrate usage
    membership_result = membership_operations(3, [1, 2, 3, 4, 5])
    logger.info(f"Membership operations result for 3 in [1, 2, 3, 4, 5]: {membership_result}")
    # Output: Membership operations result for 3 in [1, 2, 3, 4, 5]: {'in': True, 'not_in': False}

    # Call the bitwise operations function to demonstrate usage
    bitwise_result = bitwise_operations(5, 3)
    logger.info(f"Bitwise operations result for 5 and 3: {bitwise_result}")
    # Output: Bitwise operations result for 5 and 3: {'and': 1, 'or': 7, 'xor': 6, 'not_a': -6, 'left_shift_a': 10, 'right_shift_a': 2}

    # Call the precedence operations function to demonstrate usage
    precedence_result = precedence_operations()
    logger.info(f"Precedence operations result: {precedence_result}")
    # Output: Precedence operations result: {'2 + 3 * 4': 14, '(2 + 3) * 4': 20, '2 ** 3 ** 2': 512, '100 / 10 * 2': 20.0, '5 + 4 > 7 and 2 < 5': True}

