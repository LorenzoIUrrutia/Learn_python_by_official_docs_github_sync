""" 3.3.0_Python_SYNTAX """

# ----------

""" Python INDENTATION """
#  Indentation is used to define the scope of a block of code.
#    It is crucial for defining the structure of the code.
#      Its not an option, its a requirement.
#        Usually 4 spaces are used, but it can be as long as it needs.
#          It has to be at least one.
#           Nerver mix tabs and spaces in the same file.

if 5 > 2:
  print("Five is greater than two!")
  
# Have to use the same number of spaces in the same block of code
#  If you use a different number of spaces in the same block of code.
#    Otherwise, it will raise an IndentationError

if 5 > 2:
    print("Five is greater than two!")
else:
    print("Five is not greater than two!")
    
#  File "<python-input-0>", line 3
#    print("Five is greater than two!")
# IndentationError: unexpected indent

# ----------

""" Comments """
# Comments are text not printed in the output, completely ignored by the interpreter during execution
#   Use "#" to indicate a comment.

""" Multi-line Comments """
# Python does not have a native syntax for multi-line comments
#   Use multiple lines of code with # as comments
# OR
#  Use triple quotes (''' or """) to create a multi-line string to simulate block comments
#       Technically, these are string literals, not true comments. 
#           The triple quotes are not printed in the output, but they are included in the code.

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
    
# ----------

""" Naming in Python """
# Use consistent and descriptive names 
#   Depending on what you're defining.

""" Python Identifier Naming Formats """
# CamelCase: The first letter of the variable is a lowercase letter.
#  Each additional word starts with an uppercase letter.

MyVariable = 10

# PascalCase: The first letter of each word is capitalized, often used for class names

MyVariableClass = 30

# snake_case: Words are lowercase and separated by underscores

my_variable = 20

""" Naming Conventions (depending the situation) """

# Variable Names
#  snake_case 
#   Lowercase letters with underscores 
#    Keep them short but meaningful

my_variable_example = 15

# Function Names
#  snake_case
#   Lowercase letters with underscores
#    Describe short but meaningful

def my_function_example():
    pass
  
# Class Names
#  CapitalizedWords
#   PascalCase / CamelCase
#    Avoid underscores or lowercase-only names

class ShoppingCart:
    def __init__(self):
        self.items = []
        
# Constant Names
#  ALL_CAPS with underscores
#  Should not change during program execution

MAX_USERS = 100
PI_VALUE = 3.14159

# ---------

""" Spacing in Python and break lines """

# Use consistent spacing around operators and after commas
#  Improve readability and maintainability
#   Avoid excessive whitespace
#    Keep it clean and simple

""" Between Operators and Function Calls """

result = 10 + 5
area = my_function_example()

# EXCEPTIONS
#  Do not use space 
#   * Parentheses around function arguments 
#      After the opening parenthesis 
#      Before the closing parenthesis in function calls
#   * Square brackets around list elements
#      After the opening bracket
#      Before the closing bracket in list definitions
#   * Curly braces around dictionary keys and values
#      After the opening brace
#      Before the closing brace in dictionary definitions
#   * Quotes around string literals
#      After the opening quote
#      Before the closing quote in string literals
#  * Commas in function arguments, list elements, and dictionary key-value pairs
#      After the opening comma
#      Before the closing comma in function calls, list definitions, and dictionary definitions

A = 5; C = 10; F = 15
print(A, "B", C, "D", F) 
print([A, C, F]) 
print({"A": A, "C": C, "F": F})

""" Function """ 
#  Use one blank line break between functions

def my_first_function():
    pass

def my_second_function():
    pass
  
""" Inside Functions """
# Use single blank line break to separate logical blocks
#  Inside the same function
do_something = lambda: print("Doing something")
do_something_else = lambda: print("Doing something else")

def my_function():
    do_something() # First logical block

    do_something_else() # Second logical block
    
""" Class """
#  Use two blank lines break between classes

class MyClass:
    def __init__(self):
        pass


class AnotherClass:
    def __init__(self):
        pass  

""" Importing Modules """
# Separate imports sections with a single blank line
#  Standard library imports

#  Third-party imports

#  Local application/library specific imports


# ----------      

""" Importing Modules """
# Use one import statement per line
#  Keep imports at the top of the file
#   Maintain alphabetical order
#    Divide imports into three sections:
#     * Standard library imports
#     * Related third-party imports
#     * Local application/library specific imports
# AVOID use wildcard imports (e.g., from module import *)
#  " * " imports everything from the module

# Standard library imports
"""
import os
import sys

"""

# Third-party imports
"""
import requests
from math import sqrt

"""

# Local application/library specific imports
"""
from mymodule import my_function

"""

# ----------

""" Conditions and Booleans """
# To check if a variable is None,
#  Use 'is None' instead of '== None'.
#   NONE = SINGLETON (a unique instance)
#    More explicit and avoids potential issues 
#     With equality checks.

value = None
if value is None:
    print("Value is not defined")
    
# -----------

""" Length of Lines """
# Limit lines to a maximum of 79 characters 
#  Improves readability, especially in terminals or side-by-side views.
#   Use parentheses and line breaks to split long expressions cleanly.

long_expression = (
    "This is a very long expression "
    "that needs to be split "
    "across multiple lines for better readability."
)

# -----------

""" Cleanliness and Style """
# Aim for a clean and consistent code style
#  Use meaningful variable and function names
#   Keep code DRY (Don't Repeat Yourself)
#    Use comments and docstrings to explain non-obvious code
# AVOID unused variables or print statements

# Use TODO, FIXME, or NOTE to flag areas for attention
# TODO: Implement error handling
# FIXME: Resolve performance issue in data processing
# NOTE: Review code for potential security vulnerabilities


# AVOID use \n in strings for line breaks
#  Can cause issues in some environments
#   Use print() to display messages on separate lines
#    Use print() before input()
#     Ensure consistent behavior across different terminals
print("Enter your favorite color:")
color_6 = input("> ")
print("Color entered:", color_6)

# -----------