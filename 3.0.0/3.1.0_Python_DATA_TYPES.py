""" 3.1.0_Python_DATA_TYPES """

# ----------

""" Casting in Python """
# The process of designated a specific data type to a variable.
# OR / ALSO
# The process of converting a variable from one data type to another.

# Use built-in functions to cast variables to specific data types.

#-----------

""" Type of DATA in Python and how to Check it. """

# ----------

""" "100" = Integer = Int """
# Number without decimals; can be "+" , "-" or "0".

# Checking D.T "Int" on Python... type()
print(type(10))          
# Int

# ----------

""" "5.5" = Floating-point-number = Float """
# Number with decimals; can be "+" , "-" or "0".

# Checking D.T "Float" on Python... type()
print(type(3.14))        
# Float

# ----------

""" N + J = Complex number = Complex """
# Number with a REAL or Float part and an Imaginary part.

# Checking D.T "Complex number" on Python... type() 
print(type(1 + 3j))      
# Complex

# ----------

""" "True(T) / False(F)" = Boolean = Bool """
# A data type that can have one of two values: True (T) or False (F).
# Always in uppercase.

# Checking D.T "Bool" on Python... type()
print(type(True))  
# Bool

# ----------

""" "abcdef" = String = Str """
# A sequence of consecutive characters. 

# Between single ('') or double quote (""). 
# If is more than one sentence then we use a triple quote (""""."""").
# Separated by a comma (,).

# Checking D.T "String" on Python... type()
print(type('Asabeneh'))  
# Str

# ----------

""" "[1, 2, 3,]" = List = List """
# A data structure, that represents an ordered collection of elements.
# Changeable and indexed.
# Between "[]" brackets.
# separated by a comma (,).

# If is a "Str" it should be enclosed in ("") or ('').
# If is more than one sentence then we use a triple quote (""""."""").


# Checking D.T "List" on Python... type()
print(type([1, 2, 3]))   
# List

# ----------

""" "((9.8, 3.14, 2.7))" = Tuple = Tuple """
# A data structure, that represents an ordered collection of elements.
# Unchangeable and indexed.
# Between () parenthesis.
# Separated by a comma (,).

# Checking D.T "Tuple" on Python... type() 
print(type((9.8, 3.14, 2.7)))    
# Tuple

# ----------

""" "({'name':'Asabeneh'})" = Dictionary = Dict """
# A data type, that represents an ordered collection in a key value pair format. 
# Changeable and indexed.
# Each key is unique and maps to a corresponding value.
# Between {} brackets, the key and value, both between ("") or ('')
# Separated by a colon (:).
# The key-value pairs are separated by a comma (,). 

# Checking D.T "Dictionary" on Python... type()
print(type({'name':'Asabeneh'})) 
# Dict

# ----------

""" "({9.8, 3.14, 2.7})" = Set = Set """
# A data type, that represents an unordered collection of unique elements.
# Unchangeable and non-indexed.
# Between {} brackets.
# Separated by a comma (,).

# Checking D.T "Set" on Python... type() 
print(type({9.8, 3.14, 2.7}))    
# Set

# ----------

""" "frozenset([1, 2, 3])" = FrozenSet = frozenset """
# A built-in data type, that represents an immutable version of a set.
#   Between frozenset() function.
#     Separated by a comma (,).

# Checking D.T "FrozenSet" on Python... type()
print(type(frozenset([1, 2, 3])))
# frozenset

# ----------

""" "range(5)" = Range = range """
# A built-in data type, that represents an immutable sequence of Int numbers.
#   It is often used for looping a specific number of times in for loops.
#     Extremely useful in memory efficiency.
#       It is created using the range() function.   
#         Between range() function.
#           Separated by a comma (,).

range(5)        # range(stop)   
# → 0, 1, 2, 3, 4

range(2, 6)        # range(start, stop)
# → 2, 3, 4, 5

range(1, 10, 2)    # range(start, stop, step)
# → 1, 3, 5, 7, 9

# Checking D.T "Range" on Python... type()
print(type(range(1, 10)))
# range

# ----------

""" "bytes([65, 66, 67])" = Bytes = bytes """
# A built-in data type, that represents an immutable sequence of bytes.
#   It is often used to represent binary data, such as images or files.
#     Between bytes() function.
#       Separated by a comma (,).

bytes(5)        # bytes(length)
# → b'\x00\x00\x00\x00\x00'

bytes([65, 66, 67])  # bytes(iterable)
# → b'ABC'

# Checking D.T "Bytes" on Python... type()
print(type(bytes(5)))
# bytes

# ----------

""" bytearray = ByteArray = bytearray """
# A built-in data type, that represents a mutable sequence of bytes.
#   It is often used to represent binary data, such as images or files.
#     Between bytearray() function.
#       Separated by a comma (,).

bytearray(5)        # bytearray(length)
# → bytearray(b'\x00\x00\x00\x00\x00')

bytearray([65, 66, 67])  # bytearray(iterable)
# → bytearray(b'ABC')

# Checking D.T "ByteArray" on Python... type()
print(type(bytearray(5)))
# bytearray

# ----------

""" "memoryview(b'Hello')" = MemoryView = memoryview """
# A built-in data type, that represents a memory view of a byte array.
#   It allows you to access the memory of a byte array without copying it.
#     Between memoryview() function.

memoryview(b'Hello')  # memoryview(obj)
# → <memory at 0x7f8c8c0b4d00>

# Checking D.T "MemoryView" on Python... type()
print(type(memoryview(b'Hello')))
# memoryview

# ----------

""" "None" = NoneType = None """
# A built-in data type, that represents the absence of a value or a null value.
#   It is often used to indicate that a variable has no value or that a function does not return a value.
#     Between None.

# Checking D.T "NoneType" on Python... type()
print(type(None))
# NoneType

# ----------
