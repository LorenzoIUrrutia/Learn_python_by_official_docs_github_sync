""" 4.1.11_Python_TYPE_CONV_FUNC_TUPLE """

# ----------

tuple () # Converts a value to a tuple.

# ----------

# String to tuple conversion
print(tuple("Hello"))  # Output: ('H', 'e', 'l', 'l', 'o')

# List to tuple conversion
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

# Set to tuple conversion
print(tuple({1, 2, 3}))  # Output: (1, 2, 3)

# Dictionary to tuple conversion
print(tuple({"a": 1, "b": 2}))  # Output: ('a', 'b')

# ----------
# ----------

""" (FOOTNOTE) """

tuple () # As a constructor, it creates a tuple object.
# Assigning a TUPLE value to a variable

my_tuple = tuple((1, 2, 3))
print(my_tuple)  # Output: (1, 2, 3)

# ---------