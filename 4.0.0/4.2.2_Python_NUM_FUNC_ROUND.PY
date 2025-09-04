""" 4.2.2_Python_NUM_FUNC_ROUND """

round() # Rounds a number to a specified number of decimals.

# ----------

# Rounding integers
print(round(3.14))  # Output: 3
print(round(2.718))  # Output: 3

# Rounding floats
print(round(3.14159, 2))  # Output: 3.14
print(round(2.71828, 3))  # Output: 2.718

# Rounding with ties (round half to even)
print(round(0.5))  # Output: 0
print(round(1.5))  # Output: 2

# ----------
# ----------

""" (FOOTNOTE) """

round() # As a function, it rounds a number to a specified number of decimals.
# Assigning a rounded value to a variable
#  Use "round half to even" strategy, also known as "bankers' rounding".
#   Is the number exactly halfway between two integers, it rounds to the nearest even integer.
#    Round(0.5) results in 0, and round(1.5) results in 2.

my_round = round(3.14159, 2)  # Creates a variable with value 3.14
print(my_round)  # Output: 3.14

# ---------
