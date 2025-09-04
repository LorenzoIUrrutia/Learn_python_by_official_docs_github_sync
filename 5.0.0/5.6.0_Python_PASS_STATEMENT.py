""" 5.6.0_Python_PASS_STATEMENT """

# The pass statement is a null operation; nothing happens when it is executed.
#  It is useful as a placeholder in situations where syntactically some code is required but you have nothing to write.

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