""" 5.3.0_Python_CTRL_FLOW_WHILE_STATEMENT """

# ---------

# While loops execute a block of code as long as a condition is TRUE.
#  Always ensure relevant variables are ready.
#    True == Any non-zero number.  
#    False == Zero and empty values.


i = 1
while i < 6:
  print(i)
  i += 1 # Increment i by 1 in each iteration or the loop will run indefinitely.
# 1
# 2
# 3
# 4
# 5

# ---------

""" Example using a while loop: Fibonacci sequence """
# Fibonacci sequence 
# A series of numbers where each number is the sum of the two preceding ones. 
# Usually starting with 0 and 1.

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
# 0
# 1
#  1
# 2
#  3
# 5
#  8

# ---------

""" Use of "":"" in WHILE statement """
# The colon ":" is used to indicate the start of the block
#   That will be executed as part of the while statement.
#     The indentation of the code block is crucial
#       It defines the scope of the while statement.

# ----------

""" ELSE clauses in WHILE loops """
# An else clause can be used with a while loop.
#   The code block under the else clause will execute when the while condition becomes FALSE.
#     This is useful for scenarios where you want to execute a block of code after the loop finishes.

i = 1
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

# ---------

""" PASS statement in a WHILE loop """
# The pass statement can be used in a while loop when a statement is required syntactically but you do not want any command or code to execute.
#  It is a null operation; nothing happens when it executes.

i = 1
while i < 6:
    i += 1
    pass
# The loop will run until i is no longer less than 6, but nothing will be printed or executed.
#  This is useful when you want to define a loop structure but do not want to perform any action in the loop body. 
#   It can be used as a placeholder for future code.

# ---------