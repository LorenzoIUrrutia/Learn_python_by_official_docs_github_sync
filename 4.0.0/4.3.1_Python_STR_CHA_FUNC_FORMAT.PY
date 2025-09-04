""" 4.3.1_Python_STR_CHA_FUNC_FORMAT """

# ----------

format() # Returns a formatted string.

# ----------

# Using format() to format strings
print("Hello, {}".format("World"))  # Output: Hello, World
print("The value of pi is approximately {:.2f}".format(3.14159))  # Output: The value of pi is approximately 3.14

# Using format() with multiple arguments
print("Coordinates: x = {}, y = {}".format(10, 20))  # Output: Coordinates: x = 10, y = 20
print("Name: {}, Age: {}".format("Alice", 30))  # Output: Name: Alice, Age: 30

# Using format() with named placeholders
print("Name: {name}, Age: {age}".format(name="Bob", age=25))  # Output: Name: Bob, Age: 25
print

# Using format() with dictionary unpacking
data = {"name": "Charlie", "age": 35}
print("Name: {name}, Age: {age}".format(**data))  # Output: Name: Charlie, Age: 35
("Coordinates: x = {x}, y = {y}".format(x=5, y=15))  # Output: Coordinates: x = 5, y = 15
print("Coordinates: x = {x}, y = {y}".format(x=5, y=15))  # Output: Coordinates: x = 5, y = 15

# Using format() with padding and alignment
print("{:>10}".format("Right"))  # Output:      Right (right-aligned)
print("{:<10}".format("Left"))  # Output: Left      (left-aligned)
print("{:^10}".format("Center"))  # Output:   Center   (center-aligned)
print("{:10}".format("Space"))  # Output: Space     (default right-aligned with spaces) 

# Using format() with number formatting
print("Integer: {:d}".format(42))  # Output: Integer: 42
print("Float: {:.2f}".format(3.14159))  # Output: Float: 3.14
print("Percentage: {:.1%}".format(0.1234))  # Output: Percentage: 12.3%
print("Hexadecimal: {:x}".format(255))  # Output: Hexadecimal: ff
print("Binary: {:b}".format(5))  # Output: Binary: 101
print("Scientific: {:.2e}".format(1234567.89))  # Output: Scientific: 1.23e+06
print("Currency: ${:.2f}".format(1234.56))  # Output: Currency: $1234.56
print("Custom format: {0:.2f} is approximately {1:.2f}".format(3.14159, 3.14))  # Output: Custom format: 3.14 is approximately 3.14

# Using format() with nested fields
nested = {"outer": {"inner": "value"}}
print("Nested value: {0[outer][inner]}".format(nested))  # Output: Nested value: value

# Using format() with lists and tuples
print("List: {0[0]}, {0[1]}, {0[2]}".format([1, 2, 3]))  # Output: List: 1, 2, 3
print("Tuple: {0[0]}, {0[1]}, {0[2]}".format((4, 5, 6)))  # Output: Tuple: 4, 5, 6

# Using format() with complex numbers
print("Complex: {0.real} + {0.imag}j".format(complex(1, 2)))  # Output: Complex: 1.0 + 2.0j
print("Complex: {0.real} + {0.imag}j".format(complex(1, 2)))  # Output: Complex: 1.0 + 2.0j

# Using format() with booleans
print("Boolean: {}".format(True))  # Output: Boolean: True
print("Boolean: {}".format(False))  # Output: Boolean: False

# Using format() with special characters
print("Special: {}".format("\nNewline"))  # Output: Special: (newline character)
print("Special: {}".format("\tTab"))  # Output: Special: (tab character)

# Using format() with escape sequences
print("Escape: {}".format("This is a backslash: \\"))  # Output: Escape: This is a backslash: \
print("Escape: {}".format("This is a quote: \""))  # Output: Escape: This is a quote: "

# Using format() with Unicode characters
print("Unicode: {}".format("\u03A9"))  # Output: Unicode: Ω (Greek capital letter Omega)
print("Unicode: {}".format("\U0001F600"))  # Output: Unicode: 😀 (grinning face emoji)
print("Unicode: {}".format("\U0001F600"))  # Output: Unicode: 😀 (grinning face emoji)

# Using format() with raw strings
print(r"Raw string: {}".format(r"C:\Users\Name"))  # Output: Raw string: C:\Users\Name (raw string, no escape sequences processed)
print("Raw string: {}".format(r"C:\Users\Name"))  # Output: Raw string: C:\Users\Name (raw string, no escape sequences processed)

# ----------

""" (FOOTNOTE) """

format() # As a function, it returns a formatted string.
# It can format strings, numbers, and other data types.
# It supports various formatting options, including alignment, padding, and number formatting.

print("Formatted: {}".format("Hello, World!"))  # Output: Formatted: Hello, World!

# ----------
