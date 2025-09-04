""" 4.2.6_Python_NUM_FUNC_MIN """
min() # Returns the smallest of the input values.

# ----------

# Finding the minimum of integers
print(min(1, 2, 3))  # Output: 1
print(min(-1, -2, -3))  # Output: -3

# Finding the minimum of floats
print(min(1.1, 2.2, 3.3))  # Output: 1.1
print(min(-1.1, -2.2, -3.3))  # Output: -3.3

# Finding the minimum in a list
print(min([1, 2, 3, 0]))  # Output: 0
print(min([-1, -2, -3, -4]))  # Output: -4

# ----------
# ----------

""" (FOOTNOTE) """

min() # As a function, it returns the smallest of the input values.
# Assigning a minimum value to a variable
#  Can be used with integers, floats, and other comparable types.
#   It returns the minimum value among the inputs.

my_min = min(1, 2, 3)  # Creates a variable with value 1
print(my_min)  # Output: 1

# ---------
# ---------

# Note:
#  Strings, comparing them lexicographically.
print(min("apple", "banana", "cherry"))  # Output: "apple"
#  Mixed types, but all elements must be comparable.
print(min(1, 2.5, 3))  # Output: 1  
#  Empty iterables, raising a ValueError.
print(min([]))  # Raises ValueError: min() arg is an empty sequence

# ---------