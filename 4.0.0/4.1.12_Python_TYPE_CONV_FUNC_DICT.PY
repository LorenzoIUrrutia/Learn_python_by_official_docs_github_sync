""" 4.1.12_Python_TYPE_CONV_FUNC_DICT """

# ----------

dict () # Converts a value to a dictionary.

# ----------

# List to dictionary conversion
print(dict([("a", 1), ("b", 2), ("c", 3)]))  # Output: {'a': 1, 'b': 2, 'c': 3}

# Tuple to dictionary conversion
print(dict((("a", 1), ("b", 2), ("c", 3))))  # Output: {'a': 1, 'b': 2, 'c': 3}

# Set to dictionary conversion
print(dict({("a", 1), ("b", 2), ("c", 3)}))  # Output: {'a': 1, 'b': 2, 'c': 3}

# String to dictionary conversion
print(dict("abc"))  # Output: {'a': 97, 'b': 98, 'c': 99}

# ----------
# ----------

""" (FOOTNOTE) """

dict () # As a constructor, it creates a dictionary object.
# Assigning a DICTIONARY value to a variable

my_dict = dict(a=1, b=2, c=3)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# ---------