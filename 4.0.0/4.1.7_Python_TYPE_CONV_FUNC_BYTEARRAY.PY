""" 4.1.7_Python_TYPE_CONV_FUNC_BYTEARRAY """

# ----------

bytearray () # Converts a value to a bytearray.

# ----------

# String to bytearray conversion
print(bytearray("Hello", "utf-8"))  # Output: bytearray(b'Hello')
print(bytearray("Hello", "ascii"))  # Output: bytearray(b'Hello')

# Integer to bytearray conversion
print(bytearray(42))  # Output: bytearray(b'*')
print(bytearray(-42))  # Output: bytearray(b'*')

# Float to bytearray conversion
print(bytearray(3.14))  # Output: bytearray(b'3.14')
print(bytearray(-3.14))  # Output: bytearray(b'-3.14')

# Boolean to bytearray conversion
print(bytearray(True))  # Output: bytearray(b'\x01')
print(bytearray(False))  # Output: bytearray(b'\x00')

# ----------
# ----------

""" (FOOTNOTE) """

bytearray () # As a constructor, it creates a bytearray object.
# Assigning a BYTEARRAY value to a variable

my_bytearray = bytearray("Hello", "utf-8")  # Creates a bytearray object with value bytearray(b'Hello')
print(my_bytearray)  # Output: bytearray(b'Hello')

# ---------