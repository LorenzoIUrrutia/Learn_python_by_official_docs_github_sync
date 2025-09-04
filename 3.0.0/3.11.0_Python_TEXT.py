""" 3.11.0_Python_TEXT """

# ----------

""" Python handles text using the String type, known as strings, "Str". """
# Stings are IMMUTABLE, meaning they cannot be changed after creation.

""" Simple strings """
#   These can be characters, words, names, or full sentences
#       Enclosed in single (') or double(") quotes interchangeably.

print("Hello World!")
# Hello World!

""" Quotes inside quotes """
# If you want to include a quote inside a string, as characters. 
#   Place a backslash (\) before each quote.

print("Hello \"World!\"")
# Hello "World!"

# OR

# Use different quotes to enclose the string.
#   As long they don't match the quotes surrounding the string

print("Hello 'World!'")
# Hello 'World!'

# ----------

""" Multiline strings """
# One way is using triple-quotes (""") or (''') inside the print() function.

print("""
Hello World!
This is a multiline string.
It can span multiple lines.
It is useful for long text or documentation.
""")
# (Automatic initial line break)
# Hello World!
# This is a multiline string.
# It can span multiple lines.
# It is useful for long text or documentation.
 
""" Avoid the automatic initial line break """
# Inside the Print() function
#   Add a backslash (\) at the end of the first line.
#       The backslash (\) is not printed, but it indicates that the line continues on the next line.
            
print("""\
Hello World!
This is a multiline string.
It can span multiple lines.
It is useful for long text or documentation.
""")
# (Automatic initial line break)
# Hello World!
# This is a multiline string.
# It can span multiple lines.
# It is useful for long text or documentation.            

# ----------

""" Line breaks """
# Line breaks inside a Print() function, generate a new line in the output.
# Use "\n" as a line break character inside the Print() function.
#   The "\n" character is not printed, but it generates a line break in the output.

print("Hello \nWorld!") 
# Hello
# World!

""" Exception """
# "\n" is included as part of the Str content.
# Not included in the print() function as a line break.
#       "... \Name\..."
# In the print() function 
#       Use r or R before the "Str" to indicate that it is a raw string.
#           >>> print(r"...\Name\...")
#               "...\Name\...            

print(r"Hollow world... trying to use \n... as a non-line break character")
# Hollow world... trying to use \n... as a non-line break character

# ----------

""" Strings length """
# Use the len() function to obtain the length of a string.
#   The len() function returns the number of characters in the string.
#       Includes all characters, including spaces and punctuation.

p1 = "Python"
len(p1)
# 6

# ----------

""" Concatenated strings """

""" Glue together two or more strings using the "+" operator. """

p1 = "Py"
p2 = "thon"
p3 = " is a programming language"

print(p1 + p2 + p3)
# Python is a programming language

""" Repeat a string multiple times using the "*" operator. """

p1 = "Py"
p2 = "thon"
p3 = " is a programming language"

print(p1*2 + p2*3 + p3)
# PyPYthonthonthon is a programming language

""" Automatic concatenation of string literals """
# Two o more strings literals next to each other are automatically concatenated.
#       The interpreter automatically concatenates them.

print("Py" "thon")
#Python
          
# OR

text = ('Put several strings within parentheses '
'to have them joined together.')
print(text)
# 'Put several strings within parentheses to have them joined together.'

# ----------

"""Indexed strings"""
# Strings are indexed, meaning each character has a unique number, obtaining individual characters.
#   Works similar to an array and allows you to locate a character using a numerical index
#       The first character (counting right to left) is at index 0, the second at index 1, and so on.
#           The last character (counting right to left) is at index -1, the second to last at -2, and so on.

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

""" Slide index"""
# An indexed string can be sliced, allowing you to obtain a substring.
#   The slice is defined by two indexes, the first and the last.
#       The first index is included in the slice, while the last index is excluded.
#           The slice is defined by the syntax [first:last].
#               Following the  logical string recomposition rule: s[:i] + s[i:]
#                   The length of a slice is the difference of the indices
#                       word[1:3] length equals 2

text = 'Python' 

text[:2]   # Slice from the beginning of the string to index 2 (excluding index 2)
# 'Py'

text[2:]   # Slice from index 2 to the end of the string
# 'thon'

text[0:2]  # Slice from index 0 to index 2 (excluding index 2)
# 'Py'

text[2:5]  # Slice from index 2 to index 5 (excluding index 5)
# 'tho'

text[:]    # Slice the entire string
# 'Python'

text[::2]  # Slice the string with a step of 2
# 'Pto'

text[::-1] # Slice the string in reverse order
# 'nohtyP'

text[-2:]  # Slice the last two characters of the string
# 'on'

text[-2:-1] # Slice the last two characters of the string
# 'o'

""" Slice out of range can be handled without error. """

#   The slice will be empty if the first index is greater than the last index.
text[42:]  # Slice from index 42 to the end of index
# ''             # Empty string

text[:42]  # Slice from index 0 to index 42 (excluding index 42)
# 'Python'       # The entire string, included the character after the last number of the index

# ----------

""" Check if a string contains a substring using "in" """
# Use the "in" operator to check if a substring is present in a string. 

text = "Python is a programming language"
print("Python" in text)  
# True

""" Check if a string contains a substring using "if" and "in". """
# Use an "if" statement to check if a substring is present in a string.

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Yes, 'free' is present.

""" Check if a string does not contain a substring using "if", "not", "in" """
# Use an "if not" statement to check if a substring is not present in a string.

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
# No, 'expensive' is NOT present.

# ----------