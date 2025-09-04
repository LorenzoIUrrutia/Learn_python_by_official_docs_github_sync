""" 4.1.1_Python_TYPE_CONV_FUNC_INT """ 

# ----------

int () # Converts a value to an integer.

# ----------

# String to integer conversion
print(int("42"))  # Output: 42
print(int("3.14"))  # Output: 3 (truncates the decimal part)

# Float to integer conversion
print(int(3.99))  # Output: 3 (truncates the decimal part)
print(int(-3.99))  # Output: -3 (truncates the decimal part)

# Boolean to integer conversion
print(int(True))  # Output: 1
print(int(False))  # Output: 0

# Hexadecimal string to integer conversion
print(int("0x1A", 16))  # Output: 26 (base 16)
print(int("0b1010", 2))  # Output: 10 (base 2)

# ----------
# ----------

""" (FOOTNOTE) """

int () # As a constructor, it creates an integer object.
# Assigning a INTEGER value to a variable

my_integer = int(42)  # Creates an integer object with value 42
print(my_integer)  # Output: 42

# ---------