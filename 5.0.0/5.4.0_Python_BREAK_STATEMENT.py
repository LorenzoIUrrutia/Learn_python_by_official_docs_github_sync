""" 5.4.0_Python_BREAK_STATEMENT """

# ---------

# The break statement is used to exit a loop prematurely.
#  When a break statement is encountered, the loop is terminated immediately.

i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
# 1
# 2

# ---------

""" Example using a break statement: Finding a number in a list """
# Find the first even number in a list.

numbers = [1, 3, 5, 7, 8, 9]
for n in numbers:
    if n % 2 == 0:
        print("First even number found:", n)
        break

# ---------

""" Use of "break" in loops """
# The break statement can be used in both for and while loops.
#  It provides a way to exit the loop based on a condition.

# ----------
