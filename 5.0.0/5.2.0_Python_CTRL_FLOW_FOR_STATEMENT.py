""" 5.2.0_Python_CTRL_FLOW_FOR_STATEMENT """

# ---------

# For loops allow you to iterate over a sequence or other iterable objects.
#   Like a list, tuple, or string
#     The code block is executed for each item in the sequence.

# The syntax is:
#   For item in sequence:
#     code execute for each item in the sequence
#     code not execute if sequence is empty
#       Is not require indexing variable to set beforehand.

# ----------

""" Example using a for loop """

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # fruit is the loop variable
    print(fruit)

# apple
# banana
# cherry

# OR

fruits = ["apple", "banana", "cherry"]
for x in fruits:  # x is the loop variable
  print(x)
# apple
# banana
# cherry

# ----------

""" Break statement in a FOR loop """
# The break statement is used to exit the loop prematurely.
#   Before it has looped through all the items 

fruits = ["apple", "banana", "cherry"]
for x in fruits:  # x is the loop variable
  print(x)
  if x == "banana":
    break  # Stop the loop when "banana" is encountered
# # apple
# # banana

#   The loop stops when the break statement is encountered.
#     The remaining items in the sequence are not processed.
#       The loop will not continue to the next item
#         And not execute the code block for the items after the break statement.

# ----------

""" Continue statement in a FOR loop """
# The continue statement is used to skip the current iteration
#   And continue with the next item in the sequence.

fruits = ["apple", "banana", "cherry"]
for x in fruits:  # x is the loop variable
  if x == "banana":
    continue  # Skip the current iteration when "banana" is encountered
  print(x)
# # apple
# # cherry

#   The loop skips the code block for the current item
#     And continues with the next item in the sequence.

# ----------

"""The RANGE function in a FOR loop"""
# The range() function is often used with for loops
#   To generate a sequence of numbers.
#     Starting from 0 by default.
#       Increments by 1 (by default).
#         Ends at a specified number.
#           The end number is NOT included in the sequence.

for i in range(5):  # i will take values from 0 to 4
    print(i)
# 0
# 1
# 2
# 3
# 4


""" Change the range of numbers in a FOR loop """
# The range() function can take up to three arguments:
#   Range(start, stop[, step])
#       First argument is the starting value (inclusive).
#           Start: The starting value of the sequence (inclusive).
#       Second argument is the stopping value (exclusive).
#           Stop: The end value of the sequence (exclusive).
#       Third argument is the step value (optional).
#           Step: The increment between each number in the sequence (optional, default is 1).

for i in range(2, 10, 2):  # i will take values from 2 to 8 (even numbers)
    print(i)
# 2
# 4
# 6
# 8

# ----------

""" ELSE in a FOR loop """
# The else statement can be used with a for loop.
#   It is executed when the loop completes normally.
#     The else block is executed after the loop has iterated through all items.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # fruit is the loop variable
    print(fruit)
else:
    print("No more fruits!")
# apple
# banana
# cherry
# No more fruits!

#  If the loop is exited prematurely 
#    By a break statement, the else block is NOT executed.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # fruit is the loop variable
    print(fruit)
    if fruit == "banana":
        break  # Stop the loop when "banana" is encountered
else:
    print("No more fruits!")
# apple
# banana # (BREAK) The else block is not executed because the loop was exited early.


#   This allows you to handle cases where the loop completes normally
#     And cases where it is exited early.
#      Useful for cleanup actions or final messages.

# ----------

"""" PASS in a FOR loop """
# FOR loops can not be empty.
#   If you need a loop that does nothing, you can use the pass statement.
#     The pass statement is a null operation.
#       It is used when a statement is required syntactically
#         But you do not want to execute any code.
#           And avoid getting an error.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # fruit is the loop variable
    if fruit == "banana":
        pass  # Do nothing for "banana"
    print(fruit)
# apple
# banana
# cherry

# ----------

""" Nested loops in a FOR loop """
# You can nest for loops inside each other.
#   The INNER loop will be executed for each iteration of the OUTER loop.

outer_fruits = ["apple", "banana"]
inner_fruits = ["cherry", "date"]

for outer_fruit in outer_fruits:  # outer_fruit is the loop variable for the outer loop
    for inner_fruit in inner_fruits:  # inner_fruit is the loop variable for the inner loop
        print(outer_fruit, inner_fruit)

# apple cherry
# apple date
# banana cherry
# banana date

# ----------

""" Use of "":"" in FOR statement """
# The colon ":" is used to indicate the start of the block 
#   That will be executed as part of the for statement.
#     The indentation of the code block is crucial
#       It defines the scope of the for statement.

# ----------



