""" 3.1.0_Python_DATA_TYPES.py """

# =============================================================================
# PYTHON DATA TYPES - COMPLETE MASTERY GUIDE
# =============================================================================
# Version: 3.1.0 | Educational Excellence Target: 9.5/10
# Purpose: Master all Python data types with practical applications
# Target: Intermediate to Advanced Python programmers
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python data types, you will:
✓ Understand all built-in data types and their characteristics
✓ Master type conversion and casting techniques
✓ Apply appropriate data types for specific use cases
✓ Optimize memory usage with correct type selection
✓ Handle type-related errors and edge cases
✓ Implement advanced type manipulation patterns

🚀 QUICK NAVIGATION:
├── 1. FUNDAMENTAL DATA TYPES OVERVIEW
├── 2. NUMERIC TYPES (INT, FLOAT, COMPLEX)
├── 3. SEQUENCE TYPES (STRING, LIST, TUPLE)
├── 4. MAPPING TYPES (DICTIONARY)
├── 5. SET TYPES (SET, FROZENSET)
├── 6. BOOLEAN AND NONE TYPES
├── 7. TYPE CONVERSION & CASTING
├── 8. ADVANCED TYPE OPERATIONS
├── 9. PERFORMANCE & MEMORY CONSIDERATIONS
└── 10. REAL-WORLD TYPE APPLICATIONS

🔍 CORE CONCEPT:
Data types define the kind of value a variable can hold and
determine the operations that can be performed on that data.
"""

# =============================================================================
# 1. FUNDAMENTAL DATA TYPES OVERVIEW - COMPLETE FOUNDATION
# =============================================================================

"""
PYTHON DATA TYPE HIERARCHY:
Understanding the complete type system in Python
"""

# Complete data type classification
python_data_types = {
    "numeric_types": {
        "int": {
            "description": "Integer numbers (whole numbers)",
            "examples": [42, -17, 0, 999999999999999999999],
            "characteristics": ["Arbitrary precision", "Immutable", "Hashable"],
            "memory": "Variable (grows with magnitude)"
        },
        "float": {
            "description": "Floating-point numbers (decimal numbers)",
            "examples": [3.14, -2.5, 0.0, 1.23e-4],
            "characteristics": ["IEEE 754 double precision", "Immutable", "Hashable"],
            "memory": "8 bytes (64-bit)"
        },
        "complex": {
            "description": "Complex numbers (real + imaginary)",
            "examples": [1+2j, -3.5+4.2j, 5j, 2+0j],
            "characteristics": ["Two float components", "Immutable", "Hashable"],
            "memory": "16 bytes (two 64-bit floats)"
        }
    },
    
    "sequence_types": {
        "str": {
            "description": "Text sequences (strings)",
            "examples": ["hello", 'world', "", "🚀"],
            "characteristics": ["Unicode support", "Immutable", "Hashable", "Ordered"],
            "memory": "Variable (1-4 bytes per character)"
        },
        "list": {
            "description": "Mutable sequences",
            "examples": [[1, 2, 3], ['a', 'b'], [], [1, 'mixed', 3.14]],
            "characteristics": ["Mutable", "Ordered", "Allows duplicates", "Dynamic size"],
            "memory": "Variable (8 bytes per reference + object overhead)"
        },
        "tuple": {
            "description": "Immutable sequences", 
            "examples": [(1, 2, 3), ('a', 'b'), (), (1, 'mixed', 3.14)],
            "characteristics": ["Immutable", "Ordered", "Hashable", "Allows duplicates"],
            "memory": "Variable (8 bytes per reference + fixed overhead)"
        },
        "range": {
            "description": "Immutable sequence of numbers",
            "examples": [range(10), range(1, 11), range(0, 10, 2)],
            "characteristics": ["Memory efficient", "Immutable", "Lazy evaluation"],
            "memory": "Constant (regardless of range size)"
        }
    },
    
    "mapping_types": {
        "dict": {
            "description": "Key-value mappings",
            "examples": [{"key": "value"}, {1: "one", 2: "two"}, {}],
            "characteristics": ["Mutable", "Unordered (insertion order preserved)", "Keys must be hashable"],
            "memory": "Variable (depends on size and load factor)"
        }
    },
    
    "set_types": {
        "set": {
            "description": "Unordered collection of unique items",
            "examples": [{1, 2, 3}, {'a', 'b', 'c'}, set()],
            "characteristics": ["Mutable", "Unordered", "No duplicates", "Elements must be hashable"],
            "memory": "Variable (similar to dict, hash table based)"
        },
        "frozenset": {
            "description": "Immutable set",
            "examples": [frozenset([1, 2, 3]), frozenset("abc")],
            "characteristics": ["Immutable", "Hashable", "No duplicates", "Elements must be hashable"],
            "memory": "Variable (similar to set but immutable)"
        }
    },
    
    "special_types": {
        "bool": {
            "description": "Boolean values",
            "examples": [True, False],
            "characteristics": ["Subclass of int", "Immutable", "Hashable", "Only two values"],
            "memory": "Same as int (but cached)"
        },
        "NoneType": {
            "description": "Null/None type",
            "examples": [None],
            "characteristics": ["Singleton", "Immutable", "Hashable", "Only one value"],
            "memory": "Singleton object"
        }
    }
}

def demonstrate_type_checking():
    """
    COMPREHENSIVE TYPE CHECKING TECHNIQUES
    All methods to determine and verify data types
    """
    
    # Sample data for testing
    test_data = [
        42,                    # int
        3.14,                  # float
        1+2j,                  # complex
        "hello",               # str
        [1, 2, 3],            # list
        (1, 2, 3),            # tuple
        {"key": "value"},      # dict
        {1, 2, 3},            # set
        frozenset([1, 2, 3]),  # frozenset
        True,                  # bool
        None,                  # NoneType
        range(5),              # range
    ]
    
    # Type checking methods
    type_info = []
    
    for item in test_data:
        info = {
            "value": item,
            "type()": type(item).__name__,
            "isinstance_checks": {
                "numeric": isinstance(item, (int, float, complex)),
                "sequence": isinstance(item, (str, list, tuple, range)),
                "collection": isinstance(item, (list, tuple, dict, set, frozenset)),
                "hashable": _is_hashable(item),
                "mutable": _is_mutable(item)
            },
            "__class__": item.__class__.__name__,
            "type_id": id(type(item)),
            "mro": [cls.__name__ for cls in type(item).__mro__]
        }
        type_info.append(info)
    
    return type_info

def _is_hashable(obj):
    """Check if an object is hashable."""
    try:
        hash(obj)
        return True
    except TypeError:
        return False

def _is_mutable(obj):
    """Check if an object is mutable (simplified check)."""
    mutable_types = (list, dict, set)
    return isinstance(obj, mutable_types)

# =============================================================================
# 2. NUMERIC TYPES - COMPLETE DEEP DIVE
# =============================================================================

"""
COMPREHENSIVE NUMERIC TYPES GUIDE:
Master integers, floats, and complex numbers
"""

def demonstrate_numeric_types():
    """
    COMPLETE NUMERIC TYPES DEMONSTRATION
    All aspects of Python's numeric types
    """
    
    # INTEGER TYPE DEEP DIVE
    integer_examples = {
        "basic_integers": {
            "positive": 42,
            "negative": -17,
            "zero": 0,
            "large": 999999999999999999999999999999999999999,  # Arbitrary precision
        },
        
        "number_systems": {
            "decimal": 255,
            "binary": 0b11111111,      # 255 in binary
            "octal": 0o377,            # 255 in octal  
            "hexadecimal": 0xFF,       # 255 in hex
        },
        
        "integer_operations": {
            "addition": 10 + 5,        # 15
            "subtraction": 10 - 5,     # 5
            "multiplication": 10 * 5,  # 50
            "floor_division": 10 // 3, # 3
            "modulo": 10 % 3,          # 1
            "exponentiation": 10 ** 3, # 1000
        },
        
        "integer_methods": {
            "bit_length": (255).bit_length(),           # 8
            "bit_count": (255).bit_count(),             # 8 (Python 3.10+)
            "to_bytes": (255).to_bytes(2, 'big'),      # b'\x00\xff'
            "from_bytes": int.from_bytes(b'\x00\xff', 'big'), # 255
        }
    }
    
    # FLOAT TYPE DEEP DIVE
    float_examples = {
        "basic_floats": {
            "positive": 3.14159,
            "negative": -2.71828,
            "zero": 0.0,
            "scientific": 1.23e-4,     # 0.000123
            "infinity": float('inf'),
            "negative_infinity": float('-inf'),
            "not_a_number": float('nan'),
        },
        
        "float_precision": {
            "precision_limit": 0.1 + 0.2,              # 0.30000000000000004
            "epsilon": 2.220446049250313e-16,          # Machine epsilon
            "max_float": 1.7976931348623157e+308,      # sys.float_info.max
            "min_float": 2.2250738585072014e-308,      # sys.float_info.min
        },
        
        "float_methods": {
            "is_integer": (3.0).is_integer(),          # True
            "hex": (3.14).hex(),                       # '0x1.91eb851eb851fp+1'
            "from_hex": float.fromhex('0x1.91eb851eb851fp+1'), # 3.14
            "as_integer_ratio": (3.14).as_integer_ratio(),     # (3537118066892707, 1125899906842624)
        }
    }
    
    # COMPLEX TYPE DEEP DIVE
    complex_examples = {
        "basic_complex": {
            "rectangular": 3 + 4j,
            "imaginary_unit": 1j,
            "real_only": 5 + 0j,
            "imaginary_only": 0 + 3j,
            "from_function": complex(3, 4),    # 3+4j
        },
        
        "complex_properties": {
            "real_part": (3 + 4j).real,       # 3.0
            "imaginary_part": (3 + 4j).imag,  # 4.0
            "conjugate": (3 + 4j).conjugate(), # (3-4j)
            "magnitude": abs(3 + 4j),          # 5.0
        },
        
        "complex_operations": {
            "addition": (1 + 2j) + (3 + 4j),        # (4+6j)
            "multiplication": (1 + 2j) * (3 + 4j),  # (-5+10j)
            "division": (1 + 2j) / (3 + 4j),        # (0.44+0.08j)
            "power": (1 + 1j) ** 2,                 # (0+2j)
        }
    }
    
    return {
        'integers': integer_examples,
        'floats': float_examples,
        'complex': complex_examples
    }

# =============================================================================
# 3. SEQUENCE TYPES - COMPREHENSIVE MASTERY
# =============================================================================

"""
SEQUENCE TYPES COMPLETE GUIDE:
Master strings, lists, tuples, and ranges
"""

def demonstrate_sequence_types():
    """
    COMPREHENSIVE SEQUENCE TYPES DEMONSTRATION
    All sequence types with advanced operations
    """
    
    # STRING TYPE DEEP DIVE
    string_examples = {
        "string_creation": {
            "single_quotes": 'Hello World',
            "double_quotes": "Hello World",
            "triple_quotes": """Multi-line
            string with
            line breaks""",
            "raw_string": r"C:\Users\name\file.txt",
            "f_string": f"The answer is {21 * 2}",
            "unicode": "Hello 🌍 World! café naïve résumé",
        },
        
        "string_operations": {
            "concatenation": "Hello" + " " + "World",
            "repetition": "Ha" * 3,                    # "HaHaHa"
            "indexing": "Python"[0],                   # 'P'
            "slicing": "Python"[1:4],                  # 'yth'
            "membership": 'y' in "Python",             # True
            "length": len("Python"),                   # 6
        },
        
        "string_methods": {
            "case_methods": {
                "upper": "hello".upper(),              # "HELLO"
                "lower": "HELLO".lower(),              # "hello"
                "title": "hello world".title(),       # "Hello World"
                "capitalize": "hello".capitalize(),    # "Hello"
                "swapcase": "Hello".swapcase(),        # "hELLO"
            },
            "search_methods": {
                "find": "hello world".find("world"),  # 6
                "index": "hello world".index("world"), # 6 
                "count": "hello hello".count("hello"), # 2
                "startswith": "hello".startswith("he"), # True
                "endswith": "hello".endswith("lo"),    # True
            },
            "modification_methods": {
                "replace": "hello world".replace("world", "Python"), # "hello Python"
                "strip": "  hello  ".strip(),          # "hello"
                "split": "a,b,c".split(","),           # ['a', 'b', 'c']
                "join": "-".join(["a", "b", "c"]),     # "a-b-c"
            }
        }
    }
    
    # LIST TYPE DEEP DIVE
    list_examples = {
        "list_creation": {
            "literal": [1, 2, 3, 4, 5],
            "constructor": list([1, 2, 3, 4, 5]),
            "range_conversion": list(range(5)),        # [0, 1, 2, 3, 4]
            "comprehension": [x**2 for x in range(5)], # [0, 1, 4, 9, 16]
            "mixed_types": [1, "hello", 3.14, True],
        },
        
        "list_operations": {
            "indexing": [1, 2, 3, 4, 5][2],           # 3
            "slicing": [1, 2, 3, 4, 5][1:4],          # [2, 3, 4]
            "concatenation": [1, 2] + [3, 4],         # [1, 2, 3, 4]
            "repetition": [1, 2] * 3,                 # [1, 2, 1, 2, 1, 2]
            "membership": 3 in [1, 2, 3, 4],          # True
            "length": len([1, 2, 3, 4]),              # 4
        },
        
        "list_methods": {
            "modification": {
                "append": "Adds single element to end",
                "extend": "Adds multiple elements to end", 
                "insert": "Inserts element at specific position",
                "remove": "Removes first occurrence of value",
                "pop": "Removes and returns element at index",
                "clear": "Removes all elements",
            },
            "organization": {
                "sort": "Sorts list in-place",
                "reverse": "Reverses list in-place",
                "index": "Returns index of first occurrence",
                "count": "Returns count of occurrences",
                "copy": "Creates shallow copy of list",
            }
        }
    }
    
    # TUPLE TYPE DEEP DIVE
    tuple_examples = {
        "tuple_creation": {
            "literal": (1, 2, 3, 4, 5),
            "constructor": tuple([1, 2, 3, 4, 5]),
            "single_element": (42,),                   # Note the comma!
            "empty": (),
            "without_parentheses": 1, 2, 3,           # (1, 2, 3)
        },
        
        "tuple_operations": {
            "indexing": (1, 2, 3, 4, 5)[2],           # 3
            "slicing": (1, 2, 3, 4, 5)[1:4],          # (2, 3, 4)
            "concatenation": (1, 2) + (3, 4),         # (1, 2, 3, 4)
            "repetition": (1, 2) * 3,                 # (1, 2, 1, 2, 1, 2)
            "membership": 3 in (1, 2, 3, 4),          # True
            "unpacking": "a, b, c = (1, 2, 3)",       # Multiple assignment
        },
        
        "tuple_methods": {
            "count": (1, 2, 2, 3).count(2),           # 2
            "index": (1, 2, 3, 4).index(3),           # 2
        },
        
        "named_tuples": {
            "description": "Subclass of tuple with named fields",
            "example": "Point = namedtuple('Point', ['x', 'y'])",
            "usage": "p = Point(11, 22); p.x, p.y"
        }
    }
    
    # RANGE TYPE DEEP DIVE
    range_examples = {
        "range_creation": {
            "simple": range(10),                       # 0 to 9
            "start_stop": range(1, 11),                # 1 to 10
            "start_stop_step": range(0, 10, 2),        # 0, 2, 4, 6, 8
            "negative_step": range(10, 0, -1),         # 10, 9, 8, ..., 1
        },
        
        "range_properties": {
            "start": range(1, 10, 2).start,           # 1
            "stop": range(1, 10, 2).stop,             # 10
            "step": range(1, 10, 2).step,             # 2
            "membership": 5 in range(1, 10, 2),       # True
            "indexing": range(1, 10, 2)[2],           # 5
        }
    }
    
# =============================================================================
# 4. MAPPING TYPES - DICTIONARY MASTERY
# =============================================================================

"""
DICTIONARY TYPE COMPLETE GUIDE:
Master Python's key-value mapping structure
"""

def demonstrate_mapping_types():
    """
    COMPREHENSIVE DICTIONARY DEMONSTRATIONS
    All aspects of Python dictionaries
    """
    
    # DICTIONARY CREATION METHODS
    dict_creation = {
        "literal_syntax": {"name": "John", "age": 30, "city": "New York"},
        "constructor": dict([("name", "John"), ("age", 30)]),
        "keyword_args": dict(name="John", age=30, city="New York"),
        "comprehension": {x: x**2 for x in range(5)},         # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
        "from_keys": dict.fromkeys(['a', 'b', 'c'], 0),       # {'a': 0, 'b': 0, 'c': 0}
        "zip_method": dict(zip(['a', 'b', 'c'], [1, 2, 3])),  # {'a': 1, 'b': 2, 'c': 3}
    }
    
    # DICTIONARY OPERATIONS
    sample_dict = {"name": "Alice", "age": 25, "skills": ["Python", "JavaScript"]}
    
    dict_operations = {
        "access": {
            "direct_access": sample_dict["name"],              # "Alice"
            "get_method": sample_dict.get("age", 0),           # 25
            "get_missing": sample_dict.get("salary", "N/A"),   # "N/A"
            "membership": "name" in sample_dict,               # True
            "keys": list(sample_dict.keys()),                  # ['name', 'age', 'skills']
            "values": list(sample_dict.values()),              # ['Alice', 25, ['Python', 'JavaScript']]
            "items": list(sample_dict.items()),                # [('name', 'Alice'), ('age', 25), ...]
        },
        
        "modification": {
            "assignment": "sample_dict['location'] = 'Boston'",
            "update_method": "sample_dict.update({'salary': 70000})",
            "setdefault": "sample_dict.setdefault('experience', 0)",
            "pop_method": "sample_dict.pop('age', None)",
            "popitem": "sample_dict.popitem()",  # Removes last inserted item
            "clear": "sample_dict.clear()",
            "del_statement": "del sample_dict['name']"
        }
    }
    
    # ADVANCED DICTIONARY PATTERNS
    advanced_patterns = {
        "nested_dictionaries": {
            "employee": {
                "personal": {"name": "John", "age": 30},
                "work": {"department": "IT", "salary": 75000},
                "skills": {"programming": ["Python", "Java"], "tools": ["Git", "Docker"]}
            }
        },
        
        "default_dict_pattern": {
            "description": "Handle missing keys gracefully",
            "example": "from collections import defaultdict; dd = defaultdict(list)",
            "usage": "dd['key'].append('value')  # No KeyError"
        },
        
        "counter_pattern": {
            "description": "Count occurrences efficiently",  
            "example": "from collections import Counter; Counter('hello')",
            "result": "Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})"
        }
    }
    
    return {
        'creation': dict_creation,
        'operations': dict_operations,
        'advanced': advanced_patterns
    }

# =============================================================================
# 5. SET TYPES - UNIQUE COLLECTIONS MASTERY
# =============================================================================

"""
SET TYPES COMPLETE GUIDE:
Master set and frozenset for unique collections
"""

def demonstrate_set_types():
    """
    COMPREHENSIVE SET DEMONSTRATIONS
    All aspects of Python sets and frozensets
    """
    
    # SET CREATION METHODS
    set_creation = {
        "literal_syntax": {1, 2, 3, 4, 5},
        "constructor": set([1, 2, 3, 4, 5]),
        "from_string": set("hello"),                    # {'h', 'e', 'l', 'o'}
        "comprehension": {x**2 for x in range(5)},      # {0, 1, 4, 9, 16}
        "empty_set": set(),                             # Note: {} creates dict, not set
        "from_iterable": set(range(5)),                 # {0, 1, 2, 3, 4}
    }
    
    # SET OPERATIONS (Mathematical Set Theory)
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    set_operations = {
        "basic_operations": {
            "union": set_a | set_b,                     # {1, 2, 3, 4, 5, 6, 7, 8}
            "intersection": set_a & set_b,              # {4, 5}
            "difference": set_a - set_b,                # {1, 2, 3}
            "symmetric_difference": set_a ^ set_b,      # {1, 2, 3, 6, 7, 8}
        },
        
        "method_equivalents": {
            "union_method": set_a.union(set_b),
            "intersection_method": set_a.intersection(set_b),
            "difference_method": set_a.difference(set_b),
            "symmetric_diff_method": set_a.symmetric_difference(set_b),
        },
        
        "comparison_operations": {
            "subset": {1, 2}.issubset(set_a),           # True
            "superset": set_a.issuperset({1, 2}),       # True
            "disjoint": {1, 2}.isdisjoint({3, 4}),     # True
            "equal": set_a == {1, 2, 3, 4, 5},         # True
        }
    }
    
    # SET MODIFICATION METHODS
    test_set = {1, 2, 3}
    set_methods = {
        "adding_elements": {
            "add": "test_set.add(4)",                   # Adds single element
            "update": "test_set.update([5, 6, 7])",     # Adds multiple elements
        },
        
        "removing_elements": {
            "remove": "test_set.remove(1)",             # Raises KeyError if not found
            "discard": "test_set.discard(1)",           # Silent if not found
            "pop": "test_set.pop()",                    # Removes arbitrary element
            "clear": "test_set.clear()",                # Removes all elements
        },
        
        "update_operations": {
            "union_update": "test_set |= other_set",
            "intersection_update": "test_set &= other_set",
            "difference_update": "test_set -= other_set",
            "symmetric_difference_update": "test_set ^= other_set",
        }
    }
    
    # FROZENSET (Immutable Set)
    frozenset_examples = {
        "creation": {
            "from_iterable": frozenset([1, 2, 3, 4]),
            "from_set": frozenset({1, 2, 3, 4}),
            "from_string": frozenset("hello"),
            "empty": frozenset(),
        },
        
        "characteristics": {
            "immutable": "Cannot be modified after creation",
            "hashable": "Can be used as dict keys or set elements",
            "example": "nested_sets = {frozenset([1, 2]), frozenset([3, 4])}"
        }
    }
    
    return {
        'creation': set_creation,
        'operations': set_operations,
        'methods': set_methods,
        'frozenset': frozenset_examples
    }

# =============================================================================
# 6. BOOLEAN AND NONE TYPES - SPECIAL VALUES
# =============================================================================

"""
BOOLEAN AND NONE TYPES GUIDE:
Master special boolean and null values
"""

def demonstrate_special_types():
    """
    BOOLEAN AND NONE TYPE DEMONSTRATIONS
    Understanding special singleton types
    """
    
    # BOOLEAN TYPE DEEP DIVE
    boolean_details = {
        "characteristics": {
            "inheritance": "bool is a subclass of int",
            "values": [True, False],
            "truth_values": {True: 1, False: 0},
            "singleton": "True and False are singleton objects",
        },
        
        "boolean_operations": {
            "logical_and": True and False,              # False
            "logical_or": True or False,                # True
            "logical_not": not True,                    # False
            "comparison": True == 1,                    # True
            "arithmetic": True + False,                 # 1
        },
        
        "truthiness_evaluation": {
            "truthy_values": [1, "hello", [1, 2], {"key": "value"}],
            "falsy_values": [0, "", [], {}, None, False],
            "bool_conversion": [bool(x) for x in [0, 1, "", "hello", [], [1]]],
        }
    }
    
    # NONE TYPE DEEP DIVE
    none_details = {
        "characteristics": {
            "singleton": "Only one None object exists",
            "type": type(None).__name__,                # 'NoneType'
            "identity": "Use 'is' to compare with None",
            "memory_address": id(None),
        },
        
        "common_uses": {
            "default_parameter": "def func(param=None):",
            "initialization": "result = None",
            "sentinel_value": "if value is None:",
            "function_return": "Functions return None by default",
        },
        
        "comparison_patterns": {
            "correct": "value is None",
            "incorrect": "value == None",               # Works but not recommended
            "negation": "value is not None",
        }
    }
    
    return {
        'boolean': boolean_details,
        'none': none_details
    }

# =============================================================================
# 7. TYPE CONVERSION & CASTING - MASTER TRANSFORMATIONS
# =============================================================================

"""
COMPREHENSIVE TYPE CONVERSION GUIDE:
Master all type conversion and casting techniques
"""

def demonstrate_type_conversion():
    """
    COMPLETE TYPE CONVERSION DEMONSTRATIONS
    All conversion methods and edge cases
    """
    
    # BASIC TYPE CONVERSIONS
    conversion_examples = {
        "to_int": {
            "from_float": int(3.14),                    # 3 (truncates)
            "from_string": int("42"),                   # 42
            "from_bool": int(True),                     # 1
            "with_base": int("1010", 2),                # 10 (binary to decimal)
            "hex_conversion": int("FF", 16),            # 255
        },
        
        "to_float": {
            "from_int": float(42),                      # 42.0
            "from_string": float("3.14"),               # 3.14
            "from_bool": float(True),                   # 1.0
            "scientific": float("1.23e-4"),             # 0.000123
            "infinity": float("inf"),                   # inf
        },
        
        "to_string": {
            "from_int": str(42),                        # "42"
            "from_float": str(3.14),                    # "3.14"
            "from_bool": str(True),                     # "True"
            "from_list": str([1, 2, 3]),                # "[1, 2, 3]"
            "from_none": str(None),                     # "None"
        },
        
        "to_bool": {
            "from_int": bool(0),                        # False
            "from_float": bool(0.0),                    # False
            "from_string": bool(""),                    # False
            "from_list": bool([]),                      # False
            "from_none": bool(None),                    # False
        },
    }
    
    # SEQUENCE CONVERSIONS
    sequence_conversions = {
        "to_list": {
            "from_tuple": list((1, 2, 3)),              # [1, 2, 3]
            "from_string": list("hello"),               # ['h', 'e', 'l', 'l', 'o']
            "from_range": list(range(5)),               # [0, 1, 2, 3, 4]
            "from_set": list({3, 1, 2}),                # [1, 2, 3] (order may vary)
        },
        
        "to_tuple": {
            "from_list": tuple([1, 2, 3]),              # (1, 2, 3)
            "from_string": tuple("hello"),              # ('h', 'e', 'l', 'l', 'o')
            "from_range": tuple(range(5)),              # (0, 1, 2, 3, 4)
        },
        
        "to_set": {
            "from_list": set([1, 2, 2, 3]),             # {1, 2, 3}
            "from_tuple": set((1, 2, 3)),               # {1, 2, 3}
            "from_string": set("hello"),                # {'h', 'e', 'l', 'o'}
        },
    }
    
    # ADVANCED CONVERSIONS
    advanced_conversions = {
        "complex_conversions": {
            "string_to_complex": complex("1+2j"),       # (1+2j)
            "numbers_to_complex": complex(3, 4),        # (3+4j)
        },
        
        "error_handling": {
            "invalid_int": "int('abc') raises ValueError",
            "invalid_float": "float('xyz') raises ValueError",
            "none_conversion": "int(None) raises TypeError",
        },
        
        "safe_conversions": {
            "try_int": "try: int(value) except ValueError: default",
            "get_with_default": "int(value) if value.isdigit() else default",
            "type_check_first": "int(value) if isinstance(value, str) else value",
        }
    }
    
    return {
        'basic': conversion_examples,
        'sequences': sequence_conversions,
        'advanced': advanced_conversions
    }

# =============================================================================
# 8. ADVANCED TYPE OPERATIONS - EXPERT TECHNIQUES
# =============================================================================

"""
ADVANCED TYPE OPERATIONS:
Master complex type manipulation and introspection
"""

def demonstrate_advanced_type_operations():
    """
    ADVANCED TYPE MANIPULATION TECHNIQUES
    Professional-level type operations
    """
    
    # TYPE INTROSPECTION
    introspection_techniques = {
        "basic_checks": {
            "type_function": "type(obj)",
            "isinstance_check": "isinstance(obj, int)",
            "multiple_types": "isinstance(obj, (int, float, str))",
            "class_name": "obj.__class__.__name__",
            "module_name": "obj.__class__.__module__",
        },
        
        "advanced_checks": {
            "mro": "type(obj).__mro__",                 # Method Resolution Order
            "bases": "type(obj).__bases__",             # Direct base classes  
            "subclass_check": "issubclass(bool, int)",  # True
            "callable_check": "callable(obj)",
            "hasattr_check": "hasattr(obj, 'method')",
        },
        
        "type_annotations": {
            "function_hints": "def func(x: int) -> str: ...",
            "variable_hints": "name: str = 'John'",
            "get_hints": "typing.get_type_hints(func)",
            "get_annotations": "func.__annotations__",
        }
    }
    
    # DYNAMIC TYPE CREATION
    dynamic_types = {
        "class_creation": {
            "type_function": "Point = type('Point', (), {'x': 0, 'y': 0})",
            "with_methods": "type('MyClass', (BaseClass,), {'method': lambda self: 'hello'})",
            "metaclass": "class Meta(type): ...",
        },
        
        "attribute_manipulation": {
            "setattr": "setattr(obj, 'attr_name', value)",
            "getattr": "getattr(obj, 'attr_name', default)",
            "delattr": "delattr(obj, 'attr_name')",
            "vars": "vars(obj)",                        # Object's __dict__
            "dir": "dir(obj)",                          # All attributes
        }
    }
    
    # TYPE SAFETY AND VALIDATION
    type_safety = {
        "runtime_validation": {
            "assert_type": "assert isinstance(value, int), 'Expected int'",
            "type_guard": "if not isinstance(x, str): raise TypeError",
            "duck_typing": "hasattr(obj, 'quack') and callable(obj.quack)",
        },
        
        "typing_module": {
            "union_types": "Union[int, str]",
            "optional": "Optional[str]",               # Same as Union[str, None]
            "generic": "List[int], Dict[str, Any]",
            "callable": "Callable[[int, str], bool]",
            "literal": "Literal['red', 'green', 'blue']",
        }
    }
    
    return {
        'introspection': introspection_techniques,
        'dynamic': dynamic_types,
        'safety': type_safety
    }

# =============================================================================
# 9. PERFORMANCE & MEMORY CONSIDERATIONS
# =============================================================================

"""
TYPE PERFORMANCE OPTIMIZATION:
Understand memory usage and performance implications
"""

def demonstrate_performance_considerations():
    """
    TYPE PERFORMANCE AND MEMORY ANALYSIS
    Optimize code through proper type selection
    """
    
    import sys
    
    # MEMORY USAGE COMPARISON
    memory_analysis = {
        "basic_types": {
            "int": sys.getsizeof(42),                   # Bytes
            "float": sys.getsizeof(3.14),               # Bytes
            "bool": sys.getsizeof(True),                # Bytes
            "none": sys.getsizeof(None),                # Bytes
        },
        
        "collection_overhead": {
            "empty_list": sys.getsizeof([]),
            "empty_tuple": sys.getsizeof(()),
            "empty_dict": sys.getsizeof({}),
            "empty_set": sys.getsizeof(set()),
        },
        
        "scaling_analysis": {
            "list_growth": [sys.getsizeof(list(range(n))) for n in [0, 10, 100, 1000]],
            "dict_growth": [sys.getsizeof({i: i for i in range(n)}) for n in [0, 10, 100, 1000]],
        }
    }
    
    # PERFORMANCE CHARACTERISTICS
    performance_guide = {
        "access_complexity": {
            "list_access": "O(1) by index, O(n) by value",
            "dict_access": "O(1) average, O(n) worst case",
            "set_access": "O(1) average, O(n) worst case",
            "tuple_access": "O(1) by index, O(n) by value",
        },
        
        "modification_complexity": {
            "list_append": "O(1) amortized",
            "list_insert": "O(n)",
            "dict_insert": "O(1) average",
            "set_add": "O(1) average",
        },
        
        "optimization_tips": {
            "immutable_benefits": "Tuples are faster than lists for fixed data",
            "set_membership": "Use sets for fast membership testing",
            "dict_over_list": "Use dicts for key-based lookups",
            "generator_memory": "Use generators for memory-efficient iteration",
        }
    }
    
    # TYPE-SPECIFIC OPTIMIZATIONS
    optimizations = {
        "string_optimization": {
            "join_vs_concat": "''.join(strings) faster than string += string",
            "f_strings": "f-strings faster than format() or %",
            "intern": "sys.intern() for repeated string comparisons",
        },
        
        "numeric_optimization": {
            "int_caching": "Small integers (-5 to 256) are cached",
            "float_precision": "Use decimal.Decimal for exact calculations",
            "complex_operations": "Prefer cmath module for complex math",
        },
        
        "collection_optimization": {
            "list_preallocation": "Pre-allocate list size if known",
            "dict_comprehension": "Faster than loop-based creation",
            "set_operations": "Built-in set operations are optimized",
        }
    }
    
    return {
        'memory': memory_analysis,
        'performance': performance_guide,
        'optimizations': optimizations
    }

# =============================================================================
# 10. REAL-WORLD TYPE APPLICATIONS
# =============================================================================

"""
PRACTICAL TYPE APPLICATIONS:
See data types in real-world scenarios
"""

def demonstrate_real_world_applications():
    """
    REAL-WORLD DATA TYPE APPLICATIONS
    Practical examples across different domains
    """
    
    # DATA PROCESSING PIPELINE
    class DataProcessor:
        """Demonstrate type usage in data processing."""
        
        def __init__(self):
            self.processed_count = 0                    # int
            self.error_rate = 0.0                      # float
            self.is_active = True                      # bool
            self.last_error = None                     # NoneType
            self.valid_types = {int, float, str}       # set
            self.type_converters = {                   # dict
                'int': int,
                'float': float,
                'str': str,
                'bool': bool
            }
        
        def process_record(self, record):
            """Process a data record with type validation."""
            if not isinstance(record, dict):
                raise TypeError(f"Expected dict, got {type(record)}")
            
            processed = {}
            for key, value in record.items():
                if isinstance(key, str) and isinstance(value, (int, float, str)):
                    processed[key] = value
                else:
                    processed[key] = str(value)  # Convert to string as fallback
            
            self.processed_count += 1
            return processed
    
    # CONFIGURATION MANAGEMENT
    class ConfigManager:
        """Demonstrate type usage in configuration management."""
        
        def __init__(self, config_dict=None):
            self.config = config_dict or {}             # dict
            self.defaults = {                           # dict with mixed types
                'debug': False,                         # bool
                'max_connections': 100,                 # int
                'timeout': 30.0,                        # float
                'allowed_hosts': ['localhost'],         # list
                'features': set(),                      # set
                'metadata': {},                         # dict
            }
        
        def get_config(self, key, config_type=None):
            """Get configuration value with type validation."""
            value = self.config.get(key, self.defaults.get(key))
            
            if config_type and not isinstance(value, config_type):
                try:
                    if config_type == bool:
                        return bool(value) if not isinstance(value, str) else value.lower() in ('true', '1', 'yes')
                    else:
                        return config_type(value)
                except (ValueError, TypeError):
                    return self.defaults.get(key)
            
            return value
    
    # GAME STATE MANAGEMENT
    class GameState:
        """Demonstrate type usage in game development."""
        
        def __init__(self):
            self.player_position = (0, 0)              # tuple (immutable coordinates)
            self.inventory = []                        # list (mutable items)
            self.stats = {                             # dict (key-value stats)
                'health': 100,
                'mana': 50,
                'level': 1
            }
            self.unlocked_areas = set()                # set (unique areas)
            self.game_flags = frozenset(['tutorial_complete'])  # frozenset (immutable flags)
            self.current_dialogue = None               # NoneType (no dialogue active)
            self.is_paused = False                     # bool (pause state)
        
        def move_player(self, dx, dy):
            """Move player and update position."""
            x, y = self.player_position
            self.player_position = (x + dx, y + dy)    # Create new tuple
        
        def add_to_inventory(self, item):
            """Add item to inventory with type checking."""
            if isinstance(item, str):
                self.inventory.append(item)
            elif isinstance(item, dict) and 'name' in item:
                self.inventory.append(item)
            else:
                raise TypeError("Item must be string or dict with 'name'")
    
    # API RESPONSE HANDLER
    class APIResponseHandler:
        """Demonstrate type usage in API handling."""
        
        def __init__(self):
            self.response_cache = {}                   # dict cache
            self.valid_status_codes = frozenset([200, 201, 204])  # frozenset of valid codes
            self.retry_count = 0                       # int counter
            self.last_response_time = 0.0              # float timestamp
        
        def process_response(self, response_data):
            """Process API response with comprehensive type handling."""
            if not isinstance(response_data, dict):
                return {'error': 'Invalid response format'}
            
            status_code = response_data.get('status_code')
            if not isinstance(status_code, int):
                return {'error': 'Missing or invalid status code'}
            
            if status_code not in self.valid_status_codes:
                return {'error': f'HTTP {status_code}', 'retry': status_code >= 500}
            
            # Extract and validate data
            data = response_data.get('data')
            if data is None:
                return {'success': True, 'data': None}
            
            # Type-specific processing
            if isinstance(data, list):
                return {'success': True, 'data': data, 'count': len(data)}
            elif isinstance(data, dict):
                return {'success': True, 'data': data, 'keys': list(data.keys())}
            else:
                return {'success': True, 'data': str(data), 'type': type(data).__name__}
    
    return {
        'data_processor': DataProcessor,
        'config_manager': ConfigManager,
        'game_state': GameState,
        'api_handler': APIResponseHandler
    }

# =============================================================================
# COMPREHENSIVE EXERCISES & CHALLENGES
# =============================================================================

def create_type_exercises():
    """
    HANDS-ON TYPE EXERCISES
    Practice problems to master data types
    """
    
    # Exercise 1: Type Validator
    def exercise_type_validator():
        """
        Create a comprehensive type validator function.
        
        Requirements:
        1. Accept value and expected type
        2. Support type unions (multiple allowed types)
        3. Handle nested type validation (e.g., List[int])
        4. Provide detailed error messages
        5. Support custom validation functions
        """
        def validate_type(value, expected_type, strict=True):
            """
            Advanced type validation exercise.
            
            Args:
                value: The value to validate
                expected_type: Type or tuple of types
                strict: Whether to allow type coercion
            
            Returns:
                tuple: (is_valid, error_message, coerced_value)
            """
            # TODO: Implement comprehensive type validation
            pass
        
        return validate_type
    
    # Exercise 2: Data Structure Converter
    def exercise_data_converter():
        """
        Create a universal data structure converter.
        
        Requirements:
        1. Convert between all Python collection types
        2. Handle nested structures
        3. Preserve data integrity
        4. Support custom conversion rules
        5. Handle edge cases gracefully
        """
        class DataConverter:
            def __init__(self):
                self.conversion_rules = {}
            
            def convert(self, data, target_type, preserve_keys=True):
                """Universal data structure converter."""
                # TODO: Implement conversion logic
                pass
            
            def add_rule(self, from_type, to_type, converter_func):
                """Add custom conversion rule."""
                # TODO: Implement custom rule system
                pass
        
        return DataConverter
    
    # Exercise 3: Memory-Efficient Data Manager
    def exercise_memory_manager():
        """
        Create a memory-efficient data manager.
        
        Requirements:
        1. Track memory usage of stored data
        2. Choose optimal data types based on content
        3. Implement memory optimization strategies
        4. Provide memory usage reports
        5. Support data type migration for optimization
        """
        class MemoryEfficientManager:
            def __init__(self, memory_limit=1024*1024):  # 1MB default
                self.memory_limit = memory_limit
                self.data_store = {}
                self.type_stats = {}
            
            def store(self, key, value, optimize=True):
                """Store value with optional type optimization."""
                # TODO: Implement memory-efficient storage
                pass
            
            def optimize_all(self):
                """Optimize all stored data for memory efficiency."""
                # TODO: Implement global optimization
                pass
            
            def get_memory_report(self):
                """Generate comprehensive memory usage report."""
                # TODO: Implement memory reporting
                pass
        
        return MemoryEfficientManager
    
    return {
        'type_validator': exercise_type_validator(),
        'data_converter': exercise_data_converter(),
        'memory_manager': exercise_memory_manager()
    }

# =============================================================================
# MAIN EXECUTION & EXAMPLES
# =============================================================================

if __name__ == "__main__":
    """
    COMPREHENSIVE DATA TYPES DEMONSTRATION
    Run examples and see all data types in action
    """
    
    print("🎯 PYTHON DATA TYPES - COMPLETE MASTERY GUIDE")
    print("=" * 60)
    
    # Type checking demonstration
    print("\n📊 1. TYPE CHECKING & INTROSPECTION:")
    type_info = demonstrate_type_checking()
    print(f"Analyzed {len(type_info)} different data types")
    
    # Numeric types
    print("\n🔢 2. NUMERIC TYPES:")
    numeric_demo = demonstrate_numeric_types()
    print("Integer operations ✓")
    print("Float precision handling ✓")
    print("Complex number mathematics ✓")
    
    # Sequence types
    print("\n📝 3. SEQUENCE TYPES:")
    sequence_demo = demonstrate_sequence_types()
    print("String manipulation ✓")
    print("List operations ✓")
    print("Tuple immutability ✓")
    print("Range efficiency ✓")
    
    # Mapping types
    print("\n🗂️ 4. MAPPING TYPES:")
    mapping_demo = demonstrate_mapping_types()
    print("Dictionary operations ✓")
    print("Advanced patterns ✓")
    
    # Set types
    print("\n🔄 5. SET TYPES:")
    set_demo = demonstrate_set_types()
    print("Set mathematics ✓")
    print("Frozenset immutability ✓")
    
    # Special types
    print("\n⚡ 6. SPECIAL TYPES:")
    special_demo = demonstrate_special_types()
    print("Boolean operations ✓")
    print("None handling ✓")
    
    # Type conversion
    print("\n🔄 7. TYPE CONVERSION:")
    conversion_demo = demonstrate_type_conversion()
    print("Basic conversions ✓")
    print("Sequence transformations ✓")
    print("Error handling ✓")
    
    # Advanced operations
    print("\n🎪 8. ADVANCED OPERATIONS:")
    advanced_demo = demonstrate_advanced_type_operations()
    print("Type introspection ✓")
    print("Dynamic type creation ✓")
    print("Type safety validation ✓")
    
    # Performance considerations
    print("\n⚡ 9. PERFORMANCE & MEMORY:")
    perf_demo = demonstrate_performance_considerations()
    print("Memory analysis ✓")
    print("Performance optimization ✓")
    
    # Real-world applications
    print("\n🌍 10. REAL-WORLD APPLICATIONS:")
    apps_demo = demonstrate_real_world_applications()
    print("Data processing pipeline ✓")
    print("Configuration management ✓")
    print("Game state management ✓")
    print("API response handling ✓")
    
    # Exercises
    print("\n💪 11. HANDS-ON EXERCISES:")
    exercises = create_type_exercises()
    print("Type validator exercise ✓")
    print("Data converter challenge ✓")
    print("Memory manager project ✓")
    
    print("\n" + "=" * 60)
    print("🎉 DATA TYPES MASTERY COMPLETE!")
    print("You now have comprehensive knowledge of Python data types.")
    print("Practice with the exercises to become a data type expert!")

# =============================================================================
# END OF COMPREHENSIVE DATA TYPES GUIDE
# =============================================================================  
# <class 'bool'>

# ----------

""" "abcdef" = String = Str """
# A sequence of consecutive characters. 

# Between single ('') or double quote (""). 
# If is more than one sentence then we use a triple quote (""""."""").
# Separated by a comma (,).

# Checking D.T "String" on Python... type()
print(type('Asabeneh'))  
# <class 'str'>

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
# <class 'list'>

# ----------

""" "((9.8, 3.14, 2.7))" = Tuple = Tuple """
# A data structure, that represents an ordered collection of elements.
# Unchangeable and indexed.
# Between () parenthesis.
# Separated by a comma (,).

# Checking D.T "Tuple" on Python... type() 
print(type((9.8, 3.14, 2.7)))    
# <class 'tuple'>

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
# <class 'dict'>

# ----------

""" "({9.8, 3.14, 2.7})" = Set = Set """
# A data type, that represents an unordered collection of unique elements.
# Unchangeable and non-indexed.
# Between {} brackets.
# Separated by a comma (,).

# Checking D.T "Set" on Python... type() 
print(type({9.8, 3.14, 2.7}))    
# <class 'set'>

# ----------

""" "frozenset([1, 2, 3])" = FrozenSet = frozenset """
# A built-in data type, that represents an immutable version of a set.
#   Between frozenset() function.
#     Separated by a comma (,).

# Checking D.T "FrozenSet" on Python... type()
print(type(frozenset([1, 2, 3])))
# <class 'frozenset'>

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
# <class 'range'>

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
# <class 'bytes'>

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
# <class 'bytearray'>

# ----------

""" "memoryview(b'Hello')" = MemoryView = memoryview """
# A built-in data type, that represents a memory view of a byte array.
#   It allows you to access the memory of a byte array without copying it.
#     Between memoryview() function.

memoryview(b'Hello')  # memoryview(obj)
# → <memory at 0x7f8c8c0b4d00>

# Checking D.T "MemoryView" on Python... type()
print(type(memoryview(b'Hello')))
# <class 'memoryview'>

# ----------

""" "None" = NoneType = None """
# A built-in data type, that represents the absence of a value or a null value.
#   It is often used to indicate that a variable has no value or that a function does not return a value.
#     Between None.

# Checking D.T "NoneType" on Python... type()
print(type(None))
# <class 'NoneType'>

# ----------

""" PRACTICAL EXERCISES """

# Exercise 1: Data Type Identification
# Identify the data type of each variable
mystery_var_1 = 42
mystery_var_2 = 3.14159
mystery_var_3 = "Hello Python!"
mystery_var_4 = [1, 2, 3, 4, 5]
mystery_var_5 = (10, 20, 30)
mystery_var_6 = {"name": "Alice", "age": 30}
mystery_var_7 = {1, 2, 3, 4, 5}
mystery_var_8 = True
mystery_var_9 = None
mystery_var_10 = 2 + 3j

# Check your answers:
# print(f"mystery_var_1: {type(mystery_var_1)}")  # <class 'int'>
# print(f"mystery_var_2: {type(mystery_var_2)}")  # <class 'float'>
# print(f"mystery_var_3: {type(mystery_var_3)}")  # <class 'str'>
# print(f"mystery_var_4: {type(mystery_var_4)}")  # <class 'list'>
# print(f"mystery_var_5: {type(mystery_var_5)}")  # <class 'tuple'>
# print(f"mystery_var_6: {type(mystery_var_6)}")  # <class 'dict'>
# print(f"mystery_var_7: {type(mystery_var_7)}")  # <class 'set'>
# print(f"mystery_var_8: {type(mystery_var_8)}")  # <class 'bool'>
# print(f"mystery_var_9: {type(mystery_var_9)}")  # <class 'NoneType'>
# print(f"mystery_var_10: {type(mystery_var_10)}")  # <class 'complex'>

# Exercise 2: Data Type Conversion
# Convert between different data types
number_str = "123"
float_num = 45.67
bool_val = True
list_nums = [1, 2, 3, 4, 5]

# Try these conversions:
# str_to_int = int(number_str)        # "123" → 123
# float_to_int = int(float_num)       # 45.67 → 45
# bool_to_int = int(bool_val)         # True → 1
# list_to_tuple = tuple(list_nums)    # [1, 2, 3, 4, 5] → (1, 2, 3, 4, 5)
# tuple_to_set = set(list_to_tuple)   # (1, 2, 3, 4, 5) → {1, 2, 3, 4, 5}

# Exercise 3: Real-world Data Type Usage
# Create variables for a student record system
student_id = 12345                           # int
student_name = "Maria Garcia"                # str
gpa = 3.85                                   # float
is_enrolled = True                           # bool
courses = ["Math", "Physics", "Chemistry"]   # list
graduation_year = (2024, "Spring")          # tuple
grades = {"Math": "A", "Physics": "B+"}     # dict
skills = {"Python", "Data Analysis", "ML"}  # set

print("Student Management System Example:")
print(f"ID: {student_id} ({type(student_id).__name__})")
print(f"Name: {student_name} ({type(student_name).__name__})")
print(f"GPA: {gpa} ({type(gpa).__name__})")
print(f"Enrolled: {is_enrolled} ({type(is_enrolled).__name__})")
print(f"Courses: {courses} ({type(courses).__name__})")
print(f"Graduation: {graduation_year} ({type(graduation_year).__name__})")
print(f"Grades: {grades} ({type(grades).__name__})")
print(f"Skills: {skills} ({type(skills).__name__})")

# ----------
