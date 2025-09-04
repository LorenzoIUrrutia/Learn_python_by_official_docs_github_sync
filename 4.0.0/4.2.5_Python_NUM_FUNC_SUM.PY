""" 4.2.5_Python_NUM_FUNC_SUM """

sum() # Sums the items of an iterable.

# ----------

# Summing a list of integers
print(sum([1, 2, 3, 4, 5]))  # Output: 15

# Summing a list of floats
print(sum([1.1, 2.2, 3.3]))  # Output: 6.6

# Summing with a start value
print(sum([1, 2, 3], 10))  # Output: 16

# ----------
# ----------

""" (FOOTNOTE) """

sum() # As a function, it sums the items of an iterable.
# Assigning a sum value to a variable
#  Can be used with lists, tuples, and other iterables.
#   It returns the total sum of the elements.

my_sum = sum([1, 2, 3, 4, 5])  # Creates a variable with value 15
print(my_sum)  # Output: 15

# ---------

# Note: 
#  The sum function can also handle empty iterables, returning 0.
print(sum([]))  # Output: 0 
#  The sum function can also handle mixed types, but all elements must be compatible with addition.
print(sum([1, 2.5, 3]))  # Output: 6.5  

# ---------