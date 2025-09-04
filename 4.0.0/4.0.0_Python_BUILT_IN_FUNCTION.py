""" 4.0.0_Python_BUILT_IN_FUNCTION """

# ----------

""" 4.1.0_Type Conversion Functions (TYPE_CONV_FUNC) """

int() # Converts a value to an integer.
float() # Converts a value to a floating-point number.
str() # Converts a value to a string.
bool() # Converts a value to a boolean.
complex() # Creates a complex number.
bytes() # Creates an immutable bytes object.
bytearray() # Creates a mutable byte array.
memoryview() # Creates a memory view on a bytes-like object.
frozenset() # Creates an immutable set.
list() # Creates a list.
tuple() # Creates a tuple.
dict() # Creates a dictionary.
set() # Creates a set (no duplicates).

# ----------

""" 4.2.0_Numeric Functions (NUM_FUNC) """

abs() # Absolute value of a number.
round() # Rounds a number to a specified number of decimals.
pow() # Raises a number to a power (optionally modulo).
divmod() # Returns quotient and remainder.
sum() # Adds the elements of an iterable.
min() # Returns the smallest item.
max() # Returns the largest item.

# ----------

""" 4.3.0_String and Character Functions (STR_CHA_FUNC) """

format() # Returns a formatted string.
ascii() # Returns an ASCII-only representation.
repr() # Returns a printable representation of an object.
chr() # Converts Unicode code point to character.
ord() # Converts character to Unicode code point.

# ----------

""" 4.4.0_Introspection Functions (INT_FUNC) """

type() # Returns the type of an object.
id() # Returns the memory address of an object.
dir() # Returns a list of valid attributes.
vars() # Returns the __dict__ of an object.
getattr() # Returns the value of a named attribute.
setattr() # Sets the value of a named attribute.
hasattr() # Checks if object has a given attribute.
delattr() # Deletes a named attribute.
callable() # Checks if an object is callable.
hash() # Returns the hash value of an object.

# ----------

""" 4.5.0_Environment Inspection and Documentation Functions (ENV_DOC_FUNC) """

globals() # Returns the global symbol table.
locals() # Returns the local symbol table.
isinstance() # Checks if an object is an instance of a class.
issubclass() # Checks if a class is a subclass of another.
help() # Launches the built-in help system.

# ----------

""" 4.6.0_Iterators and Collection Utilities Functions (ITER_COL_UTIL_FUNC) """

len() # Returns the length of an object.
sorted() # Returns a sorted list.
reversed() # Returns a reversed iterator.
enumerate() # Returns index-item pairs.
zip() # Aggregates items from iterables.
map() # Applies a function to items in an iterable.
filter() # Filters items using a function.
all() # Returns True if all items are True.
any() # Returns True if any item is True.
range() # Returns a sequence of numbers.
iter() # Returns an iterator.
next() # Retrieves the next item from an iterator.

# ----------

""" 4.7.0_Dynamic Evaluation and Execution Functions (DYN_EVAL_EXEC_FUNC) """

eval() # Evaluates an expression string.
exec() # Executes a statement string.
compile() # Compiles source into a code object.

# ----------

""" 4.8.0_Input / Output Functions (IN_OUT_FUNC) """

input() # Reads input from the user.
print() # Writes to standard output.
open() # Opens a file.

# ----------

""" 4.9.0_Object-Oriented Programming Functions (OBJ_ORI_FUNC) """

object() # Returns a new base object.
classmethod() # Declares a method as a class method.
staticmethod() # Declares a method as static.
property() # Returns a property attribute.
super() # Returns a proxy to the superclass.

# ----------

""" 4.10.0_Special Low-Level Functions (SPE_LOW_LVL_FUNC) """

bin() # Converts an integer to a binary string.
oct() # Converts an integer to an octal string.
hex() # Converts an integer to a hexadecimal string.
breakpoint() # Drops into debugger.
__import__() # Dynamically imports a module.
aiter() # Returns an async iterator.
anext() # Gets the next item from an async iterator.

# ----------