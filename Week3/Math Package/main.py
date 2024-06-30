from math_package.addition import add
from math_package.subtraction import subtract
from math_package.multiplication import multiply
from math_package.division import divide
from math_package.modulus import modulus
from math_package.exponentiation import power
from math_package.square_root import sqrt

# Basic arithmetic operations
result_add = add(5, 3)
result_subtract = subtract(10, 7)
result_multiply = multiply(6, 8)
result_divide = divide(20, 4)
result_modulus = modulus(15, 3)

# Advanced mathematical operations
result_power = power(2, 3)  # 2^3
result_sqrt = sqrt(16)  # √16

# Printing results
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Modulus: {result_modulus}")
print(f"Power: {result_power}")
print(f"Square Root: {result_sqrt}")
