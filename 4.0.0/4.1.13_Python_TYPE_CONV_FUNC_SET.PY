""" 4.1.13_Python_TYPE_CONV_FUNC_SET """

# ----------

set () # Converts a value to a set.

# ----------

# List to set conversion
print(set([1, 2, 3]))  # Output: {1, 2, 3}
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# Tuple to set conversion
print(set((1, 2, 3)))  # Output: {1, 2, 3}

# String to set conversion
print(set("Hello"))  # Output: {'H', 'e', 'l', 'o'}

# ----------
# ----------

""" (FOOTNOTE) """

set () # As a constructor, it creates a set object.
# Assigning a SET value to a variable

my_set = set([1, 2, 3])
print(my_set)  # Output: {1, 2, 3}

# ---------