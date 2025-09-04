""" 4.2.7_Python_NUM_FUNC_MAX """

# ----------

max() # Returns the largest of the input values.

# ----------

# Finding the maximum of integers
print(max(1, 2, 3))  # Output: 3
print(max(-1, -2, -3))  # Output: -1

# Finding the maximum of floats
print(max(1.1, 2.2, 3.3))  # Output: 3.3
print(max(-1.1, -2.2, -3.3))  # Output: -1.1

# Finding the maximum in a list
print(max([1, 2, 3, 0]))  # Output: 3
print(max([-1, -2, -3, -4]))  # Output: -1

# ----------
# ----------

""" (FOOTNOTE) """

max() # As a function, it returns the largest of the input values.
# Assigning a maximum value to a variable
#  Can be used with integers, floats, and other comparable types.
#   It returns the maximum value among the inputs.

my_max = max(1, 2, 3)  # Creates a variable with value 3
print(my_max)  # Output: 3

# ---------
# ---------

# Note:
#  Strings, comparing them lexicographically.
print(max("apple", "banana", "cherry"))  # Output: "cherry"
#  Mixed types, but all elements must be comparable.
print(max(1, 2.5, 3))  # Output: 3
#  Empty iterables, raising a ValueError.
print(max([]))  # Raises ValueError: max() arg is an empty sequence

# ---------