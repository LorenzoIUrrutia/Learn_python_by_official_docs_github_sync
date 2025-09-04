""" 5.5.0_Python_CONTINUE_STATEMENT """

# ----------

# The continue statement is used to skip the current iteration of a loop and proceed to the next iteration.
#  When a continue statement is encountered, the remaining code in the loop for the current iteration is skipped.

i = 0
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
# Found an even number 2
# Found an odd number 3
# Found an even number 4
# Found an odd number 5
# Found an even number 6
# Found an odd number 7
# Found an even number 8
# Found an odd number 9

# ----------

""" Example using a continue statement: Filtering even numbers """
# Filter out even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 == 0:
        continue
    print("Odd number found:", n)
# Odd number found: 1
# Odd number found: 3
# Odd number found: 5

# ---------

""" Use of "continue" in loops """
# The continue statement can be used in both for and while loops.
#  It provides a way to skip the current iteration based on a condition.

# ----------
