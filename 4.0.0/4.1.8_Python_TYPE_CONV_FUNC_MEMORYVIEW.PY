""" 4.1.8_Python_TYPE_CONV_FUNC_MEMORYVIEW """

# ----------

memoryview () # Converts a value to a memoryview.

# ----------

# Bytes to memoryview conversion
b = bytes("Hello", "utf-8")
mv = memoryview(b)
print(mv)  # Output: <memory at 0x...>

# Bytearray to memoryview conversion
ba = bytearray("Hello", "utf-8")
mv = memoryview(ba)
print(mv)  # Output: <memory at 0x...>

# ----------
# ----------

""" (FOOTNOTE) """

memoryview () # As a constructor, it creates a memoryview object.
# Assigning a MEMORYVIEW value to a variable

my_memoryview = memoryview(b)
print(my_memoryview)  # Output: <memory at 0x...>

# ---------