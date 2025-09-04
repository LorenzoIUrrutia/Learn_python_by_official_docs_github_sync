""" 4.1.4_Python_TYPE_CONV_FUNC_BOOL """

# ----------

bool () # Converts a value to a boolean.

# ----------

# String to boolean conversion
print(bool("True"))  # Output: True
print(bool("False"))  # Output: True (non-empty string is True)
print(bool(""))  # Output: False (empty string is False)

# Integer to boolean conversion
print(bool(1))  # Output: True
print(bool(0))  # Output: False

# Float to boolean conversion
print(bool(3.14))  # Output: True
print(bool(0.0))  # Output: False

# List to boolean conversion
print(bool([1, 2, 3]))  # Output: True
print(bool([]))  # Output: False

# ----------
# ----------

""" (FOOTNOTE) """

bool () # As a constructor, it creates a boolean object.
# Assigning a BOOLEAN value to a variable

my_bool = bool(True)  # Creates a boolean object with value True
print(my_bool)  # Output: True

# ---------