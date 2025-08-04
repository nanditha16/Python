# This file demonstrates basic NUmeric operations in Python.


# Numeric types in Python# Python has several numeric types: int, float, and complex.
# - int: Integer type
# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1) # Output: Integer Division: 2

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2) # Output: Modulus (Remainder): 0

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3) # Output: Absolute Value: 7

# - float: Floating-point type
# Floating-point variables
float1 = 10.5
float2 = 5.2

# Floating-point Division
result4 = float1 / float2
print("Floating-point Division:", result4) # Output: Floating-point Division: 2.019230769230769

# Floating-point Division with Floor
result4_floor = float1 // float2
print("Floating-point Division with Floor:", result4_floor) # Output: Floating-point Division with Floor: 2.0

# Floating-point Absolute Value
result4_abs = abs(float1)
print("Floating-point Absolute Value:", result4_abs) # Output: Floating-point Absolute Value: 10.5

# Floating-point Absolute Value with Negative
result4_neg_abs = abs(-float1)
print("Floating-point Absolute Value with Negative:", result4_neg_abs)

# Floating-point Modulus
result5 = float1 % float2
print("Floating-point Modulus:", result5) # Output: Floating-point Modulus: 0.09999999999999964

# - complex: Complex number type
complex1 = 2 + 3j
complex2 = 1 - 1j

# Complex Addition
result6 = complex1 + complex2
print("Complex Addition:", result6) # Output: Complex Addition: (3+2j)

# Complex Subtraction
result7 = complex1 - complex2
print("Complex Subtraction:", result7) # Output: Complex Subtraction: (1+4j)

# Complex Multiplication
result8 = complex1 * complex2
print("Complex Multiplication:", result8) # Output: Complex Multiplication: (5+1j)

# Complex Division
result9 = complex1 / complex2
print("Complex Division:", result9) # Output: Complex Division: (0.5+2.5j)
# Complex Division with Floor
# Note: Complex numbers do not support floor division directly.
# Complex Division with Floor
# result9_floor = complex1 // complex2
# print("Complex Division with Floor:", result9_floor)
# Complex numbers do not support floor division directly, so we skip that.

# Complex Conjugate
result10 = complex1.conjugate()
print("Complex Conjugate:", result10) # Output: Complex Conjugate: (2-3j)
# Complex Conjugate with Negative
result10_neg = complex1.conjugate()
print("Complex Conjugate with Negative:", result10_neg) # Output: Complex Conjugate with Negative: (2-3j)

# Complex Absolute Value
result11 = abs(complex1)
print("Complex Absolute Value:", result11) # Output: Complex Absolute Value: 3.605551275463989
# Complex Absolute Value with Negative
result11_neg = abs(-complex1)
print("Complex Absolute Value with Negative:", result11_neg) # Output: Complex Absolute Value with Negative: 3.605551275463989

# Complex Modulus
result12 = abs(complex1) % abs(complex2)
print("Complex Modulus:", result12) # Output: Complex Modulus: 0.7771241507177988

# Complex Modulus with Negative
result12_neg = abs(-complex1) % abs(-complex2)
print("Complex Modulus with Negative:", result12_neg) # Output: Complex Modulus with Negative: 0.7771241507177988
# Note: Complex numbers do not support modulus directly, so we use absolute values for demonstration.

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5) # Output: Rounded: 3.14
# Rounding with Negative
result5_neg = round(-3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded with Negative:", result5_neg) # Output: Rounded with Negative: -3.14
# Rounding with Floor
result5_floor = round(3.14159265359, 0)  # Rounds to nearest integer
print("Rounded with Floor:", result5_floor) # Output: Rounded with Floor: 3.0
# Rounding with Floor and Negative
result5_floor_neg = round(-3.14159265359, 0)  # Rounds to nearest integer
print("Rounded with Floor and Negative:", result5_floor_neg) # Output: Rounded with Floor and Negative: -3.0
# Rounding with Ceiling
result5_ceiling = round(3.14159265359, 0)  # Rounds to nearest integer
print("Rounded with Ceiling:", result5_ceiling) # Output: Rounded with Ceiling: 3.0
# Rounding with Ceiling and Negative
result5_ceiling_neg = round(-3.14159265359, 0)  # Rounds to nearest integer
print("Rounded with Ceiling and Negative:", result5_ceiling_neg) # Output: Rounded with Ceiling and Negative: -3.0

# Rounding with Truncation
result5_trunc = int(3.14159265359)  # Truncates to integer
print("Rounded with Truncation:", result5_trunc) # Output: Rounded with Truncation: 3
# Rounding with Truncation and Negative
result5_trunc_neg = int(-3.14159265359)  # Truncates to integer
print("Rounded with Truncation and Negative:", result5_trunc_neg) # Output: Rounded with Truncation and Negative: -3

# Rounding with Custom Function
# Note: The custom rounding function is a simple implementation and may not handle all edge cases.
def custom_round(value, decimals=0):
    multiplier = 10 ** decimals
    return int(value * multiplier + 0.5) / multiplier
result5_custom = custom_round(3.14159265359, 2)  # Custom rounding to 2 decimal places
print("Rounded with Custom Function:", result5_custom) # Output: Rounded with Custom Function: 3.14
# Rounding with Custom Function and Negative
result5_custom_neg = custom_round(-3.14159265359, 2)  # Custom rounding to 2 decimal places
print("Rounded with Custom Function and Negative:", result5_custom_neg) # Output: Rounded with Custom Function and Negative: -3.13
# Rounding with Custom Function and Floor
result5_custom_floor = custom_round(3.14159265359, 0)  # Custom rounding to nearest integer
print("Rounded with Custom Function and Floor:", result5_custom_floor) # Output: Rounded with Custom Function and Floor: 3.0
# Rounding with Custom Function and Floor and Negative
result5_custom_floor_neg = custom_round(-3.14159265359, 0)  # Custom rounding to nearest integer
print("Rounded with Custom Function and Floor and Negative:", result5_custom_floor_neg) # Output: Rounded with Custom Function and Floor and Negative: -2.0
# Rounding with Custom Function and Ceiling
result5_custom_ceiling = custom_round(3.14159265359, 0)  # Custom rounding to nearest integer
print("Rounded with Custom Function and Ceiling:", result5_custom_ceiling) # Output: Rounded with Custom Function and Ceiling: 3.0
# Rounding with Custom Function and Ceiling and Negative
result5_custom_ceiling_neg = custom_round(-3.14159265359, 0)  # Custom rounding to nearest integer
print("Rounded with Custom Function and Ceiling and Negative:", result5_custom_ceiling_neg) # Output: Rounded with Custom Function and Ceiling and Negative: -2.0
# Rounding with Custom Function and Truncation
result5_custom_trunc = custom_round(3.14159265359, 0)  # Custom rounding to integer
print("Rounded with Custom Function and Truncation:", result5_custom_trunc) # Output: Rounded with Custom Function and Truncation: 3.0
# Rounding with Custom Function and Truncation and Negative
result5_custom_trunc_neg = custom_round(-3.14159265359, 0)  # Custom rounding to integer
print("Rounded with Custom Function and Truncation and Negative:", result5_custom_trunc_neg) # Output: Rounded with Custom Function and Truncation and Negative: -2.0
