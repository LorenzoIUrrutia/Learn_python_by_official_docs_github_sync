""" 4.2.1_Python_NUM_FUNC_ABS """

# ----------

abs() # Absolute value of a number.

# ----------

# Integer absolute value
print(abs(-42))  # Output: 42
print(abs(42))   # Output: 42

# Float absolute value
print(abs(-3.14))  # Output: 3.14
print(abs(3.14))   # Output: 3.14

# Complex number absolute value
print(abs(3 + 4j))  # Output: 5.0 (sqrt(3^2 + 4^2))
print(abs(-3 - 4j))  # Output: 5.0 (sqrt(3^2 + 4^2)) 

# ----------
# ----------    

""" (FOOTNOTE) """
abs() # As a function, it returns the absolute value of a number.
# Assigning an absolute value to a variable     
#  Can be used with integers, floats, and complex numbers.
#   It returns the absolute value, which is always a non-negative number.
        
my_abs = abs(-42)  # Creates a variable with value 42
print(my_abs)  # Output: 42

# ---------
