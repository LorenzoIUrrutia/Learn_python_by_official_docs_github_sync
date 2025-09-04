""" 3.4.0_Python_VARIABLES """

# ----------

""" Variables """
# Variables are used to store data values.
#  And refers to a memory address in which data is stored.

""" Creating Variables """
#  Python has no command for declaring a variable
#   To created, simply assign a value to it using the equals sign (=).
#    Do not need to be declared with any particular type
#     You can even change type after they have been set

x = 5
y = "John"
    
""" Variable Naming RULES """
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
#   Keywords are reserved words that cannot be used as variable names.
#     There are 35 keywords in Python 3.13:

import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
# 'while', 'with', 'yield']

# ----------

""" Multi Words Variable Names """
# Variable names can be made up of multiple words.
#   They must follow certain naming conventions.

# Camel Case
# The first letter of each word is capitalized, except for the first word.
myVariableName = "Hello"

# Pascal Case
# The first letter of each word is capitalized, including the first word.
MyVariableName = "Hello"

# Snake Case
# Words are separated by underscores, and all letters are lowercase.
my_variable_name = "Hello"

# ---------

"""" Assigning Multiple Variables """
# You can assign multiple variables in one line.

x, y, z = "Orange", "Banana", "Cherry"
# This is equivalent to:
x = "Orange"
y = "Banana"
z = "Cherry"

""" Unpacking a Collection """
# Unpack a collection (like a list or tuple), into multiple variables.

fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
# This is equivalent to:
x = "Apple"
y = "Banana"
z = "Cherry"

""" Assigning the Same Value to Multiple Variables """
# You can assign the same value to multiple variables in one line.

x = y = z = "Orange"
# This is equivalent to:
x = "Orange"
y = "Orange"
z = "Orange"

# ---------

""" Variable Type """
# Python is dynamically typed so you don't need to declare the type.
#   The type of a variable is determined by the value assigned to it.

x = 5          # x is of type int
y = "Hello"    # y is of type str
z = 3.14       # z is of type float

""" Checking Variable Type """
# You can check the type of a variable using the type() function.

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

""" Changing Variable Type """
# You can change the type by assigning a new value of a different type.

x = "Hello"  # Now x is of type str
y = 10       # Now y is of type int
z = True     # Now z is of type bool

print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'bool'>

""" Assigning a specific type to a variable """
# You can explicitly convert a variable to a specific type 
#   Using cast functions like 
#     int(), str(), float(), etc.

x = int(5)          # x is 5 and type int
y = str("Hello")    # y is "Hellos" type str
z = float(3.14)     # z is 3.14 type float


# ---------

""" Output Variables """
# You can output variables using the print() function.
#   Are called GLOBAL VARIABLES
#     Can be used by everyone, both inside of functions and outside. 

x = "Hello"

print(x)  
# Hello

""" Output Multiple Variables """
# You can output multiple variables in one print() function.
#  By using commas to separate them.

x = "Hello"
y = "World"

print(x, y) 
# Hello World

# Also using operators like ("+")" for concatenation (only for strings).
#   Not for numbers, as it will raise a TypeError.

x = "Hello"
y = "World"

print(x + " " + y)
# Hello World


""" Output Variables with String Formatting """

""" F-Strings method """
# You can use the f-strings to include variables .
#   Are a way to embed expressions inside string literals.
#     Using curly braces {} to include variables.

name = "John"
age = 30

print(f"My name is {name} and I am {age} years old.")
# My name is John and I am 30 years old.

""" Format Method """
# You can also use the format() method to format strings.
#   The format() method allows you to insert variables into a string.
#     Using curly braces {} as placeholders for the variables.

name = "John"
age = 30

print("My name is {} and I am {} years old.".format(name, age))
# My name is John and I am 30 years old.

""" % Operator method """ 
# You can also use the % operator for string formatting.
#   The % operator allows you to insert variables into a string.
#     Using %s for strings and %d for integers as placeholders.


name = "John"
age = 30

print("My name is %s and I am %d years old." % (name, age))
# My name is John and I am 30 years old.

# -----------

""" Inside a function variables """
# Variables defined inside a function are local to that function.
#   They cannot be accessed from outside the function.

def my_function():
    x = "Hello"
    print(x)

my_function()
# Hello

print(x)  # NameError: name 'x' is not defined

# -----------
