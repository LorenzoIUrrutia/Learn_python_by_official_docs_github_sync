""" 4.1.5_Python_TYPE_CONV_FUNC_COMPLEX """

# ----------

complex () # Converts a value to a complex number.

# ----------

# Integer to complex conversion
print(complex(42))  # Output: (42+0j)
print(complex(-42))  # Output: (-42+0j)

# Float to complex conversion
print(complex(3.14))  # Output: (3.14+0j)
print(complex(-3.14))  # Output: (-3.14+0j)

# String to complex conversion
print(complex("42+5j"))  # Output: (42+5j)
print(complex("3.14-2.5j"))  # Output: (3.14-2.5j)

# Boolean to complex conversion
print(complex(True))  # Output: (1+0j)
print(complex(False))  # Output: 0j

# ----------
# ----------

""" (FOOTNOTE) """

complex () # As a constructor, it creates a complex number object.
# Assigning a COMPLEX value to a variable

my_complex = complex(3, 4)  # Creates a complex number object with value (3+4j)
print(my_complex)  # Output: (3+4j)

# ---------