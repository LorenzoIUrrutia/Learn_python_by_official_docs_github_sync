""" 5.1.0_Python_CTRL_FLOW_IF_STATEMENT """

# ---------

# If statements allow you to execute a block of code based on a condition.
#   If statement is True, the block of code is executed.
#   If statement is False, the block of code is skipped.

#     Elif (else if) to check multiple conditions.
#       Can be zero or more elif statements.
#     Else to execute a block of code if none of the conditions are True.
#       Is optional
#         To handle cases not covered by the if or elif statements.

# The syntax is:
# if condition:
#   code execute if condition is True
#   code not execute if condition is False
# elif another_condition:
#   code to execute if another_condition is True
# else:
#   code to execute if neither condition is True
#

# ----------

""" Example using a if statement """

x = int(input("Please enter an integer: "))
# Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# More

# ----------

""" Use of "":"" in IF statement """
# The colon ":" is used to indicate the start of the block 
#   That will be executed as part of the if statement.
#     The indentation of the code block is crucial
#       It defines the scope of the if statement.

# ----------

""" ELSE clauses in IF statements """
# An else clause can be used with an if statement.
#   The code block under the else clause will execute when the if condition becomes FALSE.
#     This is useful for scenarios where you want to execute a block of code when the if condition is not met.
x = 42
if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
# More

# ----------

""" PASS statement in IF statements """
# The pass statement is a null operation; nothing happens when it is executed.
# It is useful as a placeholder in situations where syntactically some code is required but you have nothing to write.
x = 42
if x < 0:
    pass  # Placeholder for future code, nothing happens here
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# ----------

""" Elif clauses in IF statements """
# Elif clauses allow you to check multiple conditions in an if statement.
#   If the initial if condition is FALSE, the program will check the elif conditions in order.
#     If an elif condition is TRUE, its block of code will execute.
#       If all if and elif conditions are FALSE, the else block will execute (if present).

x = 42
if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")   
# More  

# ----------

""" Nested IF statements """
# You can nest if statements within each other to create more complex conditions.
#   This allows you to check additional conditions based on the outcome of previous conditions.
#   Indentation is crucial for defining the scope of nested if statements.

x = 42
if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
    if x < 50:
        print("Less than 50")
    else:
        print("50 or more")

# ----------