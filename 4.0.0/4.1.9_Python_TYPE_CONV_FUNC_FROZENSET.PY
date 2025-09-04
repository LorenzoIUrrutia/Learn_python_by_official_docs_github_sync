""" 4.1.9_Python_TYPE_CONV_FUNC_FROZENSET """

# ----------

frozenset () # Converts a value to a frozenset.

# ----------

# List to frozenset conversion
print(frozenset([1, 2, 3]))  # Output: frozenset({1, 2, 3})
print(frozenset([1, 2, 2, 3]))  # Output: frozenset({1, 2, 3})

# Set to frozenset conversion
print(frozenset({1, 2, 3}))  # Output: frozenset({1, 2, 3})

# Dictionary to frozenset conversion
print(frozenset({"a": 1, "b": 2}))  # Output: frozenset({'a', 'b'})

# ----------
# ----------

""" (FOOTNOTE) """

frozenset () # As a constructor, it creates a frozenset object.
# Assigning a FROZENSET value to a variable
#  Is immutable, meaning its elements cannot be changed after creation.
#   (Useful for set-like structure that should not be modified)

my_frozenset = frozenset([1, 2, 3])
print(my_frozenset)  # Output: frozenset({1, 2, 3})

# ---------
# Note: frozenset is immutable, meaning its elements cannot be changed after creation.
# It is useful when you need a set-like structure that should not be modified.