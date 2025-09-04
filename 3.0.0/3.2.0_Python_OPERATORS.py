""" 3.2.0_Python_OPERATORS """

# ----------

""" Arithmetic Operators """
# Used to perform mathematical operations on numeric values.

#  +	 Addition	 x + y
#  -	 Subtraction	 x - y
#  *	 Multiplication	 x * y
#  /	 Division	 x / y
#  // Floor division	 x // y
#  %	 Modulo (remainder)	 x % y
#  ** Exponentiation	 x ** y

# ----------

""" Assignment Operators """
# Used to assign values to variables, 
#   Often in combination with arithmetic operations.

#  =	  Assign	x = 10
#  +=  Add and assign	x += 5
#  -=  Subtract and assign	x -= 5
#  *=  Multiply and assign	x *= 5
#  /=  Divide and assign	x /= 5
#  //= Floor divide and assign	x //= 5
#  %=  Modulo and assign	x %= 5
#  **= Power and assign	x **= 2
#  &=  Bitwise AND and assign	x &= y
#  `=` Bitwise OR and assign
#  ^=  Bitwise XOR and assign	x ^= y
#  >>= Right shift and assign	x >>= 1
#  <<= Left shift and assign	x <<= 1

# ----------

""" Comparison Operators """
# Used to compare two values and return a boolean result.

#  ==	Equal	x == y
#  !=	Not equal	x != y
#  >	Greater than	x > y
#  <	Less than	x < y
#  >=	Greater or equal	x >= y
#  <=	Less or equal	x <= y

# ----------

""" Logical Operators """
# Used to combine conditional statements.

#  and 	Returns True if both statements are true	x < 5 and  x < 10	
#  or	Returns True if one of the statements is true	x < 5 or x < 4	
#  not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# ----------

""" Identity Operators """
# Used to check if two values refer to the same object in memory.

#  is 	Returns True if both variables are the same object	x is y	
#  is not	Returns True if both variables are not the same object	x is not y

# ----------

""" Membership Operators """
# Used to check if a value is present in a sequence.

#  in 	Returns True if a sequence with the specified value is present in the object	x in y	
#  not in	Returns True if a sequence with the specified value is not present in the object

# ----------

""" Bitwise Operators """
# Used to perform bit-level operations on integers.

#  & 	AND	Sets each bit to 1 if both bits are 1	x & y	
#  |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
#  ~	NOT	Inverts all the bits	~x	
#  <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
#  >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# ----------

""" Special Operators """
# Used for specific operations like slicing and indexing.

#  :=	Walrus operator (assignment expression)	if (n := len(data)) > 10:
#  ...	Ellipsis object	Used in slicing or placeholders
#  []	Indexing	x[0]
#  [:]	Slicing	x[1:5]
#  ()	Call function	f(x, y)
#  .	Attribute access	x.attribute
#  ,	Comma separator	x, y, z

# ----------