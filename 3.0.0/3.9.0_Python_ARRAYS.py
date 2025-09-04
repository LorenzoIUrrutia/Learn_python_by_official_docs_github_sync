""" 3.9.0_Python_ARRAYS """

# ---------

# Python does not have a built-in array data type.
# You can use "Python's list" as an array.
# However, if you need a more efficient array implementation.
#   You can use the "array" module.
import array
# A special variable, which can hold many values under a single name.
# You can access the values by referring to an index number.

# ---------

"""Indexed Arrays """
# List and Arrays are indexed, meaning each character has a unique number, obtaining individual characters.
#   The first character (counting right to left) is at index 0, the second at index 1, and so on.
#     The last character (counting right to left) is at index -1, the second to last at -2, and so on.

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

""" Slice index"""
# An indexed list can be sliced, allowing you to obtain a substring.
#   The slice is defined by two indexes, the first and the last.
#       The first index is included in the slice, while the last index is excluded.
#           The slice is defined by the syntax [first:last].
#               Following the  logical string recomposition rule: s[:i] + s[i:]
#                   The length of a slice is the difference of the indices
#                       word[1:3] length equals 2

p1 = [1, 2, 3]
p2 = [4, 5, 6]
p3 = [7, 8, 9]
p4 = [10]

p1[:2]   # Slice from the beginning of the string to index 2 (excluding index 2)
# [1, 2]

p1[2:]   # Slice from index 2 to the end of the string
# [3]

p1[0:2]  # Slice from index 0 to index 2 (excluding index 2)
# [1, 2]

p1[2:5]  # Slice from index 2 to index 5 (excluding index 5)
# [3]

p1[:]    # Slice the entire string
# [1, 2, 3]

p1[::2]  # Slice the string with a step of 2
# [1, 3]

p1[::-1] # Slice the string in reverse order
# [3, 2, 1]

p1[-2:]  # Slice the last two characters of the string
# [2, 3]

p1[-2:-1] # Slice the last two characters of the string
# [2]

""" Slice out of range can be handled without error. """
#   The slice will be empty if the first index is greater than the last index.

p1[42:]  # Slice from index 42 to the end of index
# ""             # Empty string

p1[:42]  # Slice from index 0 to index 42 (excluding index 42)
# [1, 2, 3]       # The entire string, included the character after the last number of the index

# ----------

"""Modify INDEX items"""
#   Lists are mutable, meaning you can change the value of an item in a list.
#       You can change the value of an item in a list 
#           Assigning a new value to the index of the item.

""" Change the value of an item in a INDEX """
#  You can change the value of an item in a list by assigning a new value to the index of the item.

p10 = [10, 22, 30]

p10[1] = 20
print(p10)
# [10, 20, 30]

""" Add an item to a INDEX """
# You can add an item to a list by using the append() method.

p10 = [10, 20, 30]

p10.append(40)
print(p10)
# [10, 20, 30, 40]

""" Remove an item from a INDEX """
# You can remove an item from a list by using the remove() method.

p10 = [10, 20, 30]

p10.remove(20)
print(p10)
# [10, 30]

""" Sort a INDEX """
# You can sort a list by using the sort() method.

p10 = [30, 10, 20]

p10.sort()
print(p10)
# [10, 20, 30]

""" Reverse a INDEX """
# You can reverse a list by using the reverse() method.

p10 = [10, 20, 30]

p10.reverse()
print(p10)
# [30, 20, 10]

""" Clear a INDEX """
# You can clear a list by using the clear() method.

p10 = [10, 20, 30]

p10.clear()
print(p10)
# []

#OR

# You can clear a list by using the del statement.

p10 = [10, 20, 30]

p10 = []
print(p10)
# []

# ----------

""" INDEX Methods """
# List methods are functions that can be used to manipulate lists.
#   They are called on a list object and can be used to perform various operations on the list.

#  append()   Adds an element at the end of the list
#  clear()	  Removes all the elements from the list
#  copy()	  Returns a copy of the list
#  count()	  Returns the number of elements with the specified value
#  extend()	  Add the elements of a list (or any iterable), to the end of the current list
#  index()	  Returns the index of the first element with the specified value
#  insert()	  Adds an element at the specified position
#  pop()	  Removes the element at the specified position
#  remove()	  Removes the item with the specified value
#  reverse()  Reverses the order of the list
#  sort()     Sorts the list

# ---------