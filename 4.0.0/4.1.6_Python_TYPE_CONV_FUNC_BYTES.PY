""" 4.1.6_Python_TYPE_CONV_FUNC_BYTES """

# ----------

bytes () # Converts a value to bytes.

# ----------

# String to bytes conversion
print(bytes("Hello", "utf-8"))  # Output: b'Hello'
print(bytes("Hello", "ascii"))  # Output: b'Hello'

# Integer to bytes conversion
print(bytes(42))  # Output: b'*'
print(bytes(-42))  # Output: b'*'

# Float to bytes conversion
print(bytes(3.14))  # Output: b'3.14'
print(bytes(-3.14))  # Output: b'-3.14'

# Boolean to bytes conversion
print(bytes(True))  # Output: b'\x01'
print(bytes(False))  # Output: b'\x00'

# ----------
# ----------

""" (FOOTNOTE) """

bytes () # As a constructor, it creates a bytes object.
# Assigning a BYTES value to a variable

my_bytes = bytes("Hello", "utf-8")  # Creates a bytes object with value b'Hello'
print(my_bytes)  # Output: b'Hello'

# ---------