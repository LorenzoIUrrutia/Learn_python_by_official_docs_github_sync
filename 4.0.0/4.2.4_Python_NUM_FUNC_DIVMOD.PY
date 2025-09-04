""" 4.2.4_Python_NUM_FUNC_DIVMOD """

divmod() # Returns the quotient and remainder of dividing two numbers.

# ----------

# Integer division and modulus
print(divmod(9, 4))  # Output: (2, 1)
print(divmod(10, 3))  # Output: (3, 1)

# Float division and modulus
print(divmod(9.0, 4.0))  # Output: (2.0, 1.0)
print(divmod(10.0, 3.0))  # Output: (3.0, 1.0)

# ----------
# ----------

""" (FOOTNOTE) """

divmod() # As a function, it returns the quotient and remainder of dividing two numbers.
# Assigning the result to variables
#  Can be used with integers and floats.
#   It returns a tuple containing the quotient and remainder.

my_divmod = divmod(9, 4)  # Creates a variable with value (2, 1)
print(my_divmod)  # Output: (2, 1)

# ---------
