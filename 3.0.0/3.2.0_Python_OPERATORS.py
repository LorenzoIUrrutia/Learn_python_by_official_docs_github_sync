""" 3.2.0_Python_OPERATORS.py """

# =============================================================================
# PYTHON OPERATORS - COMPLETE MASTERY GUIDE
# =============================================================================
# Version: 3.2.0 | Educational Excellence Target: 9.5/10
# Purpose: Master all Python operators with advanced techniques
# Target: Intermediate to Advanced Python programmers
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python operators, you will:
✓ Understand all operator types and their precedence
✓ Master arithmetic, comparison, and logical operations
✓ Apply bitwise and assignment operators effectively
✓ Use advanced operator techniques and patterns
✓ Optimize code with proper operator selection
✓ Handle operator overloading and special methods

🚀 QUICK NAVIGATION:
├── 1. OPERATOR CLASSIFICATION & PRECEDENCE
├── 2. ARITHMETIC OPERATORS (COMPLETE)
├── 3. COMPARISON OPERATORS (ADVANCED)
├── 4. LOGICAL OPERATORS (MASTERY)
├── 5. BITWISE OPERATORS (EXPERT)
├── 6. ASSIGNMENT OPERATORS (PATTERNS)
├── 7. IDENTITY & MEMBERSHIP OPERATORS
├── 8. OPERATOR OVERLOADING & MAGIC METHODS
├── 9. ADVANCED OPERATOR TECHNIQUES
└── 10. REAL-WORLD OPERATOR APPLICATIONS

🔍 CORE CONCEPT:
Operators are special symbols that perform operations on operands
and are the building blocks of all computational expressions.
"""

# =============================================================================
# 1. OPERATOR CLASSIFICATION & PRECEDENCE - COMPLETE FOUNDATION
# =============================================================================

"""
COMPLETE OPERATOR HIERARCHY:
Master operator precedence and classification
"""

# Complete operator precedence (highest to lowest)
operator_precedence = [
    ("()", "Parentheses", "Highest priority - explicit grouping"),
    ("**", "Exponentiation", "Right-associative power operation"),
    ("+x, -x, ~x", "Unary operators", "Positive, negative, bitwise NOT"),
    ("*, /, //, %", "Multiplicative", "Multiplication, division, floor division, modulo"),
    ("+, -", "Additive", "Addition and subtraction"),
    ("<<, >>", "Bitwise shifts", "Left shift and right shift"),
    ("&", "Bitwise AND", "Binary AND operation"),
    ("^", "Bitwise XOR", "Binary exclusive OR"),
    ("|", "Bitwise OR", "Binary inclusive OR"),
    ("==, !=, <, <=, >, >=, is, is not, in, not in", "Comparisons", "All comparison operators"),
    ("not", "Boolean NOT", "Logical negation"),
    ("and", "Boolean AND", "Logical AND"),
    ("or", "Boolean OR", "Logical OR"),
    ("if-else", "Conditional expression", "Ternary operator"),
    ("lambda", "Lambda expression", "Anonymous functions"),
    ("=, +=, -=, etc.", "Assignment", "Lowest priority - assignment operators")
]

# Operator categories
operator_categories = {
    "arithmetic": {
        "description": "Mathematical operations on numbers",
        "operators": ["+", "-", "*", "/", "//", "%", "**"],
        "operands": "Numeric types (int, float, complex)",
        "examples": ["5 + 3", "10 / 3", "2 ** 8"]
    },
    
    "comparison": {
        "description": "Compare values and return boolean results",
        "operators": ["==", "!=", "<", "<=", ">", ">="],
        "operands": "Any comparable types",
        "examples": ["5 > 3", "'a' < 'b'", "[1,2] == [1,2]"]
    },
    
    "logical": {
        "description": "Boolean operations with short-circuit evaluation",
        "operators": ["and", "or", "not"],
        "operands": "Any type (evaluated for truthiness)",
        "examples": ["True and False", "5 or 0", "not []"]
    },
    
    "bitwise": {
        "description": "Binary operations on integer bit patterns",
        "operators": ["&", "|", "^", "~", "<<", ">>"],
        "operands": "Integer types only",
        "examples": ["5 & 3", "8 >> 2", "~42"]
    },
    
    "assignment": {
        "description": "Assign values with optional operation",
        "operators": ["=", "+=", "-=", "*=", "/=", "//=", "%=", "**="],
        "operands": "Variable and compatible value",
        "examples": ["x = 5", "x += 3", "x **= 2"]
    },
    
    "identity": {
        "description": "Test object identity (same memory location)",
        "operators": ["is", "is not"],
        "operands": "Any objects",
        "examples": ["x is y", "value is not None"]
    },
    
    "membership": {
        "description": "Test membership in sequences/collections",
        "operators": ["in", "not in"],
        "operands": "Item and iterable container",
        "examples": ["'a' in 'apple'", "5 not in [1,2,3]"]
    }
}

def demonstrate_operator_precedence():
    """
    COMPREHENSIVE PRECEDENCE DEMONSTRATION
    Show how operator precedence affects expression evaluation
    """
    
    # Complex expressions with precedence examples
    precedence_examples = [
        {
            "expression": "2 + 3 * 4",
            "result": 2 + 3 * 4,                    # 14 (not 20)
            "evaluation": "2 + (3 * 4)",
            "explanation": "Multiplication before addition"
        },
        {
            "expression": "2 ** 3 ** 2",
            "result": 2 ** 3 ** 2,                  # 512 (not 64)
            "evaluation": "2 ** (3 ** 2)",
            "explanation": "Exponentiation is right-associative"
        },
        {
            "expression": "10 - 5 - 2",
            "result": 10 - 5 - 2,                   # 3 (not 7)
            "evaluation": "(10 - 5) - 2",
            "explanation": "Subtraction is left-associative"
        },
        {
            "expression": "not False or True and False",
            "result": not False or True and False,  # True
            "evaluation": "(not False) or (True and False)",
            "explanation": "not > and > or"
        },
        {
            "expression": "5 < 10 and 10 < 20",
            "result": 5 < 10 and 10 < 20,          # True
            "evaluation": "(5 < 10) and (10 < 20)",
            "explanation": "Comparisons before logical operators"
        }
    ]
    
    # Demonstrate associativity
    associativity_examples = [
        {
            "operation": "Exponentiation (right-associative)",
            "expression": "2 ** 3 ** 2",
            "left_to_right": (2 ** 3) ** 2,        # 64
            "right_to_left": 2 ** (3 ** 2),        # 512
            "python_result": 2 ** 3 ** 2,          # 512 (right-associative)
        },
        {
            "operation": "Subtraction (left-associative)",
            "expression": "10 - 5 - 2",
            "left_to_right": (10 - 5) - 2,         # 3
            "right_to_left": 10 - (5 - 2),         # 7
            "python_result": 10 - 5 - 2,           # 3 (left-associative)
        }
    ]
    
    return {
        'precedence_examples': precedence_examples,
        'associativity': associativity_examples
    }

# =============================================================================
# 2. ARITHMETIC OPERATORS - COMPLETE MASTERY
# =============================================================================

"""
COMPREHENSIVE ARITHMETIC OPERATORS:
Master all mathematical operations with advanced techniques
"""

def demonstrate_arithmetic_operators():
    """
    COMPLETE ARITHMETIC OPERATIONS GUIDE
    All arithmetic operators with edge cases and optimizations
    """
    
    # Basic arithmetic operations
    basic_arithmetic = {
        "addition": {
            "integers": 15 + 25,                    # 40
            "floats": 3.14 + 2.86,                  # 6.0
            "mixed": 10 + 3.5,                     # 13.5
            "complex": (1+2j) + (3+4j),            # (4+6j)
            "string_concat": "Hello" + " World",    # "Hello World"
            "list_concat": [1, 2] + [3, 4],        # [1, 2, 3, 4]
        },
        
        "subtraction": {
            "integers": 25 - 15,                    # 10
            "floats": 5.5 - 2.3,                   # 3.2
            "negative_result": 5 - 10,              # -5
            "complex": (5+3j) - (2+1j),            # (3+2j)
            "set_difference": {1,2,3} - {2,3},      # {1}
        },
        
        "multiplication": {
            "integers": 6 * 7,                      # 42
            "floats": 3.14 * 2,                    # 6.28
            "complex": (2+1j) * (1+2j),            # (0+5j)
            "string_repeat": "Ha" * 3,              # "HaHaHa"
            "list_repeat": [1, 2] * 3,             # [1, 2, 1, 2, 1, 2]
        },
        
        "division": {
            "true_division": 10 / 3,                # 3.3333333333333335
            "float_result": 8 / 2,                  # 4.0 (always float)
            "complex_division": (1+2j) / (1+1j),    # (1.5+0.5j)
        },
        
        "floor_division": {
            "integers": 10 // 3,                    # 3
            "floats": 10.0 // 3.0,                 # 3.0
            "negative": -10 // 3,                   # -4 (floors toward negative infinity)
            "mixed": 10 // 3.0,                    # 3.0
        },
        
        "modulo": {
            "basic": 10 % 3,                       # 1
            "float": 10.5 % 3.2,                   # 0.8999999999999995
            "negative_dividend": -10 % 3,           # 2 (same sign as divisor)
            "negative_divisor": 10 % -3,            # -2
        },
        
        "exponentiation": {
            "integer_power": 2 ** 8,                # 256
            "float_power": 2.0 ** 0.5,             # 1.4142135623730951 (sqrt(2))
            "negative_power": 2 ** -3,              # 0.125
            "complex_power": (1+1j) ** 2,           # (0+2j)
            "large_power": 2 ** 100,               # Very large integer
        }
    }
    
    # Advanced arithmetic techniques
    advanced_techniques = {
        "precision_handling": {
            "float_precision": {
                "issue": 0.1 + 0.2,                # 0.30000000000000004
                "solution": "Use decimal.Decimal for exact arithmetic",
                "decimal_example": "Decimal('0.1') + Decimal('0.2')"
            },
            "integer_division": {
                "python2_style": "Use // for integer division",
                "python3_behavior": "/ always returns float",
                "exact_division": "Use divmod() for quotient and remainder"
            }
        },
        
        "performance_optimization": {
            "power_alternatives": {
                "square": "x * x is faster than x ** 2",
                "cube": "x * x * x is faster than x ** 3",
                "sqrt": "Use math.sqrt() instead of ** 0.5 for clarity"
            },
            "integer_operations": {
                "bit_shifting": "x << 1 is faster than x * 2 for powers of 2",
                "modulo_powers_2": "x & (n-1) is faster than x % n when n is power of 2"
            }
        },
        
        "special_cases": {
            "division_by_zero": {
                "integer": "ZeroDivisionError",
                "float": "inf or -inf",
                "complex": "complex(inf, nan)"
            },
            "overflow_behavior": {
                "integer": "Arbitrary precision (no overflow)",
                "float": "inf for overflow, -inf for underflow",
                "complex": "Follows float rules for real and imaginary parts"
            }
        }
    }
    
    # Mathematical function equivalents
    math_equivalents = {
        "absolute_value": {
            "builtin": "abs(-5)",                   # 5
            "math_module": "math.fabs(-5.5)",       # 5.5
            "complex": "abs(3+4j)",                 # 5.0
        },
        
        "power_functions": {
            "builtin": "pow(2, 8)",                 # 256
            "with_modulo": "pow(2, 8, 10)",         # 6 (256 % 10)
            "math_module": "math.pow(2, 8)",        # 256.0 (always float)
        },
        
        "rounding": {
            "builtin_round": "round(3.14159, 2)",   # 3.14
            "math_floor": "math.floor(3.7)",        # 3
            "math_ceil": "math.ceil(3.1)",          # 4
            "math_trunc": "math.trunc(3.7)",        # 3
        }
    }
    
    return {
        'basic': basic_arithmetic,
        'advanced': advanced_techniques,
        'math_functions': math_equivalents
    }

# =============================================================================
# 3. COMPARISON OPERATORS - ADVANCED TECHNIQUES
# =============================================================================

"""
COMPARISON OPERATORS MASTERY:
Advanced comparison techniques and edge cases
"""

def demonstrate_comparison_operators():
    """
    COMPREHENSIVE COMPARISON DEMONSTRATIONS
    All comparison operators with advanced patterns
    """
    
    # Basic comparison operations
    basic_comparisons = {
        "equality": {
            "numbers": 5 == 5,                      # True
            "strings": "hello" == "hello",          # True
            "lists": [1, 2, 3] == [1, 2, 3],       # True
            "mixed_types": 5 == "5",                # False
            "boolean_int": True == 1,               # True (bool is int subclass)
        },
        
        "inequality": {
            "numbers": 5 != 3,                      # True
            "strings": "apple" != "orange",         # True
            "case_sensitive": "Hello" != "hello",   # True
            "empty_containers": [] != {},           # True
        },
        
        "ordering": {
            "integers": 10 > 5,                     # True
            "floats": 3.14 < 3.15,                 # True
            "strings": "apple" < "banana",          # True (lexicographic)
            "mixed_numeric": 5 <= 5.0,             # True
        }
    }
    
    # Advanced comparison techniques
    advanced_comparisons = {
        "chained_comparisons": {
            "range_check": 1 < 5 < 10,              # True
            "equality_chain": 5 == 5 == 5,          # True
            "mixed_chain": 1 < 2 <= 2 < 3,          # True
            "complex_chain": 0 <= abs(-5) < 10,     # True
        },
        
        "string_comparison": {
            "lexicographic": "apple" < "banana",     # True
            "case_sensitivity": "A" < "a",          # True (ASCII values)
            "length_vs_lexical": "z" > "hello",     # True (character comparison)
            "unicode": "café" > "cafe",             # True
        },
        
        "container_comparison": {
            "list_element_wise": [1, 2, 3] < [1, 2, 4],      # True
            "tuple_comparison": (1, 2) < (1, 3),             # True  
            "length_matters": [1, 2] < [1, 2, 3],            # True
            "empty_comparison": [] < [1],                     # True
        },
        
        "special_value_comparisons": {
            "none_comparison": None == None,         # True
            "nan_comparison": float('nan') == float('nan'),  # False!
            "infinity": float('inf') > 1000000,     # True
            "negative_infinity": float('-inf') < -1000000,  # True
        }
    }
    
    # Comparison edge cases and gotchas
    edge_cases = {
        "type_compatibility": {
            "numeric_types": 1 == 1.0,              # True
            "bool_int": True == 1,                  # True
            "incompatible": "Cannot compare '5' < [1, 2, 3] in some cases",
        },
        
        "floating_point": {
            "precision_issue": 0.1 + 0.2 == 0.3,   # False!
            "epsilon_comparison": "abs(a - b) < epsilon",
            "isclose_function": "math.isclose(0.1 + 0.2, 0.3)",
        },
        
        "object_comparison": {
            "same_content": [1, 2, 3] == [1, 2, 3], # True (content)
            "same_identity": "[1, 2, 3] is [1, 2, 3]", # False (different objects)
            "mutable_vs_immutable": "(1, 2, 3) is (1, 2, 3)",  # May be True (implementation detail)
        }
    }
    
    return {
        'basic': basic_comparisons,
        'advanced': advanced_comparisons,
        'edge_cases': edge_cases
    }

# =============================================================================
# 4. LOGICAL OPERATORS - COMPLETE MASTERY
# =============================================================================

"""
LOGICAL OPERATORS COMPLETE GUIDE:
Master boolean logic with short-circuit evaluation
"""

def demonstrate_logical_operators():
    """
    COMPREHENSIVE LOGICAL OPERATIONS
    All logical operators with advanced patterns and optimizations
    """
    
    # Basic logical operations
    basic_logical = {
        "and_operator": {
            "basic_truth": True and True,           # True
            "false_result": True and False,         # False
            "return_behavior": 5 and 3,             # 3 (returns last truthy)
            "short_circuit": 0 and print("Never printed"), # 0 (print not executed)
        },
        
        "or_operator": {
            "basic_truth": False or True,           # True
            "false_result": False or False,         # False
            "return_behavior": 5 or 3,              # 5 (returns first truthy)
            "short_circuit": 5 or print("Never printed"), # 5 (print not executed)
        },
        
        "not_operator": {
            "boolean_negation": not True,           # False
            "truthy_negation": not 5,               # False
            "falsy_negation": not 0,                # True
            "double_negation": not not 5,           # True
        }
    }
    
    # Advanced logical patterns
    advanced_logical = {
        "short_circuit_patterns": {
            "safe_division": {
                "pattern": "divisor != 0 and dividend / divisor",
                "benefit": "Avoids ZeroDivisionError without try/except"
            },
            "safe_attribute": {
                "pattern": "obj and hasattr(obj, 'attr') and obj.attr",
                "benefit": "Safely accesses attributes"
            },
            "default_values": {
                "pattern": "value or default",
                "benefit": "Provides fallback for falsy values"
            }
        },
        
        "complex_expressions": {
            "validation_chain": "(data and isinstance(data, dict) and 'key' in data)",
            "permission_check": "(user.is_active and user.has_permission('read'))",
            "range_validation": "(0 <= value <= 100 and isinstance(value, (int, float)))"
        },
        
        "performance_optimization": {
            "order_matters": "Put likely-false conditions first in AND chains",
            "expensive_last": "Put expensive operations last in logical chains",
            "cache_results": "Store complex boolean expressions in variables"
        }
    }
    
    # Truth value testing
    truthiness_guide = {
        "falsy_values": [False, None, 0, 0.0, 0j, '', [], (), {}, set()],
        "truthy_examples": [True, 1, 'hello', [1], {'key': 'value'}],
        
        "custom_truthiness": {
            "bool_method": "Define __bool__() method in custom classes",
            "len_method": "If no __bool__, Python uses __len__()",
            "default_true": "Objects are truthy by default"
        },
        
        "practical_applications": {
            "validation": "if user and user.is_active:",
            "default_assignment": "name = provided_name or 'Anonymous'",
            "guard_clauses": "if not data: return"
        }
    }
    
# =============================================================================
# 5. BITWISE OPERATORS - EXPERT LEVEL TECHNIQUES
# =============================================================================

"""
BITWISE OPERATORS MASTERY:
Advanced binary operations and bit manipulation
"""

def demonstrate_bitwise_operators():
    """
    COMPREHENSIVE BITWISE OPERATIONS
    Expert-level bit manipulation techniques
    """
    
    # Basic bitwise operations
    basic_bitwise = {
        "bitwise_and": {
            "operation": 12 & 10,                   # 8 (1100 & 1010 = 1000)
            "binary_view": f"{12:04b} & {10:04b} = {12 & 10:04b}",
            "use_case": "Mask operations, flag checking"
        },
        
        "bitwise_or": {
            "operation": 12 | 10,                   # 14 (1100 | 1010 = 1110)
            "binary_view": f"{12:04b} | {10:04b} = {12 | 10:04b}",
            "use_case": "Set flags, combine permissions"
        },
        
        "bitwise_xor": {
            "operation": 12 ^ 10,                   # 6 (1100 ^ 1010 = 0110)
            "binary_view": f"{12:04b} ^ {10:04b} = {12 ^ 10:04b}",
            "use_case": "Toggle flags, simple encryption"
        },
        
        "bitwise_not": {
            "operation": ~12,                       # -13 (two's complement)
            "binary_view": f"~{12:08b} = {~12 & 0xFF:08b}",
            "use_case": "Invert all bits"
        },
        
        "left_shift": {
            "operation": 5 << 2,                    # 20 (101 << 2 = 10100)
            "binary_view": f"{5:08b} << 2 = {5 << 2:08b}",
            "use_case": "Multiply by powers of 2"
        },
        
        "right_shift": {
            "operation": 20 >> 2,                   # 5 (10100 >> 2 = 101)
            "binary_view": f"{20:08b} >> 2 = {20 >> 2:08b}",
            "use_case": "Divide by powers of 2"
        }
    }
    
    # Advanced bitwise techniques
    advanced_bitwise = {
        "bit_manipulation_tricks": {
            "check_even_odd": {
                "technique": "n & 1",
                "example": f"5 & 1 = {5 & 1} (odd), 4 & 1 = {4 & 1} (even)"
            },
            "power_of_two": {
                "technique": "n & (n - 1) == 0",
                "example": f"8 & 7 = {8 & 7}, 16 & 15 = {16 & 15}"
            },
            "swap_variables": {
                "technique": "a ^= b; b ^= a; a ^= b",
                "note": "XOR swap without temporary variable"
            },
            "count_set_bits": {
                "technique": "bin(n).count('1')",
                "example": f"bin(13).count('1') = {bin(13).count('1')}"
            }
        },
        
        "flag_operations": {
            "set_flag": "flags |= FLAG_VALUE",
            "clear_flag": "flags &= ~FLAG_VALUE",
            "toggle_flag": "flags ^= FLAG_VALUE",
            "check_flag": "bool(flags & FLAG_VALUE)"
        },
        
        "performance_optimizations": {
            "multiply_by_power_2": "x << n instead of x * (2**n)",
            "divide_by_power_2": "x >> n instead of x // (2**n)",
            "modulo_power_2": "x & (2**n - 1) instead of x % (2**n)"
        }
    }
    
    return {
        'basic': basic_bitwise,
        'advanced': advanced_bitwise
    }

# =============================================================================
# 6. ASSIGNMENT OPERATORS - PATTERNS & TECHNIQUES
# =============================================================================

"""
ASSIGNMENT OPERATORS MASTERY:
Advanced assignment patterns and techniques
"""

def demonstrate_assignment_operators():
    """
    COMPREHENSIVE ASSIGNMENT OPERATIONS
    All assignment operators with advanced patterns
    """
    
    # Basic assignment operations
    basic_assignment = {
        "simple_assignment": {
            "syntax": "variable = value",
            "example": "x = 42",
            "note": "Creates new binding"
        },
        
        "augmented_arithmetic": {
            "add_assign": "x += 5  # x = x + 5",
            "sub_assign": "x -= 3  # x = x - 3",
            "mul_assign": "x *= 2  # x = x * 2",
            "div_assign": "x /= 4  # x = x / 4",
            "floor_div_assign": "x //= 3  # x = x // 3",
            "mod_assign": "x %= 7  # x = x % 7",
            "pow_assign": "x **= 2  # x = x ** 2"
        },
        
        "augmented_bitwise": {
            "and_assign": "x &= mask  # x = x & mask",
            "or_assign": "x |= flag  # x = x | flag",
            "xor_assign": "x ^= toggle  # x = x ^ toggle",
            "lshift_assign": "x <<= 2  # x = x << 2",
            "rshift_assign": "x >>= 1  # x = x >> 1"
        }
    }
    
    # Advanced assignment patterns
    advanced_assignment = {
        "multiple_assignment": {
            "parallel": "a, b, c = 1, 2, 3",
            "unpacking": "first, *middle, last = [1, 2, 3, 4, 5]",
            "swap": "a, b = b, a"
        },
        
        "chained_assignment": {
            "basic": "a = b = c = 0",
            "warning": "Careful with mutable objects: a = b = []"
        },
        
        "walrus_operator": {
            "syntax": "variable := expression",
            "in_if": "if (n := len(data)) > 10:",
            "in_while": "while (line := file.readline()):",
            "in_comprehension": "[y for x in data if (y := func(x)) is not None]"
        },
        
        "performance_considerations": {
            "in_place_ops": "list.extend() vs list = list + other_list",
            "method_chaining": "obj.method1().method2().method3()",
            "cache_results": "result = expensive_function(); use result multiple times"
        }
    }
    
    return {
        'basic': basic_assignment,
        'advanced': advanced_assignment
    }

# =============================================================================
# 7. IDENTITY & MEMBERSHIP OPERATORS
# =============================================================================

"""
IDENTITY AND MEMBERSHIP OPERATORS:
Master object identity and collection membership testing
"""

def demonstrate_identity_membership():
    """
    IDENTITY AND MEMBERSHIP OPERATIONS
    Object identity and container membership patterns
    """
    
    # Identity operators (is, is not)
    identity_operations = {
        "object_identity": {
            "same_object": {
                "example": "a = [1, 2, 3]; b = a; a is b",
                "result": True,
                "explanation": "Same memory location"
            },
            "different_objects": {
                "example": "[1, 2, 3] is [1, 2, 3]",
                "result": False,
                "explanation": "Different memory locations"
            },
            "singleton_objects": {
                "none": "None is None",              # Always True
                "true_false": "True is True",        # Always True
                "small_ints": "1 is 1",             # True (cached)
                "large_ints": "1000 is 1000"        # May be False
            }
        },
        
        "identity_best_practices": {
            "none_checking": "Use 'value is None' not 'value == None'",
            "boolean_checking": "Use 'value is True' for exact True check",
            "performance": "'is' is faster than '==' for identity checks"
        }
    }
    
    # Membership operators (in, not in)
    membership_operations = {
        "sequence_membership": {
            "string": "'a' in 'apple'",             # True
            "list": "5 in [1, 2, 3, 4, 5]",        # True
            "tuple": "'x' not in ('a', 'b', 'c')", # True
            "range": "5 in range(10)"               # True
        },
        
        "mapping_membership": {
            "dict_keys": "'key' in {'key': 'value'}", # True
            "dict_values": "'value' in {'key': 'value'}.values()", # True
            "dict_items": "('key', 'value') in {'key': 'value'}.items()" # True
        },
        
        "set_membership": {
            "basic": "5 in {1, 2, 3, 4, 5}",       # True
            "performance": "Sets have O(1) average membership testing"
        },
        
        "custom_membership": {
            "contains_method": "Implement __contains__ for custom membership",
            "example": "class Container: def __contains__(self, item): ..."
        }
    }
    
    return {
        'identity': identity_operations,
        'membership': membership_operations
    }

# =============================================================================
# 8. OPERATOR OVERLOADING & MAGIC METHODS
# =============================================================================

"""
OPERATOR OVERLOADING MASTERY:
Create custom operator behavior for your classes
"""

def demonstrate_operator_overloading():
    """
    COMPREHENSIVE OPERATOR OVERLOADING
    Custom classes with overloaded operators
    """
    
    # Complete magic method reference
    magic_methods_reference = {
        "arithmetic_operators": {
            "__add__": "x + y",
            "__sub__": "x - y",
            "__mul__": "x * y",
            "__truediv__": "x / y",
            "__floordiv__": "x // y",
            "__mod__": "x % y",
            "__pow__": "x ** y",
            "__radd__": "y + x (when x.__add__ not implemented)",
            "__iadd__": "x += y (in-place addition)"
        },
        
        "comparison_operators": {
            "__eq__": "x == y",
            "__ne__": "x != y",
            "__lt__": "x < y",
            "__le__": "x <= y",
            "__gt__": "x > y",
            "__ge__": "x >= y"
        },
        
        "bitwise_operators": {
            "__and__": "x & y",
            "__or__": "x | y",
            "__xor__": "x ^ y",
            "__invert__": "~x",
            "__lshift__": "x << y",
            "__rshift__": "x >> y"
        },
        
        "unary_operators": {
            "__pos__": "+x",
            "__neg__": "-x",
            "__abs__": "abs(x)",
            "__round__": "round(x)"
        }
    }
    
    # Example: Vector class with operator overloading
    class Vector:
        """Comprehensive example of operator overloading."""
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        # Arithmetic operators
        def __add__(self, other):
            if isinstance(other, Vector):
                return Vector(self.x + other.x, self.y + other.y)
            return NotImplemented
        
        def __sub__(self, other):
            if isinstance(other, Vector):
                return Vector(self.x - other.x, self.y - other.y)
            return NotImplemented
        
        def __mul__(self, scalar):
            if isinstance(scalar, (int, float)):
                return Vector(self.x * scalar, self.y * scalar)
            return NotImplemented
        
        def __rmul__(self, scalar):
            return self.__mul__(scalar)
        
        # Comparison operators
        def __eq__(self, other):
            if isinstance(other, Vector):
                return self.x == other.x and self.y == other.y
            return False
        
        def __lt__(self, other):
            if isinstance(other, Vector):
                return self.magnitude() < other.magnitude()
            return NotImplemented
        
        # Special methods
        def __abs__(self):
            return self.magnitude()
        
        def __str__(self):
            return f"Vector({self.x}, {self.y})"
        
        def __repr__(self):
            return f"Vector({self.x!r}, {self.y!r})"
        
        def magnitude(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5
    
    # Advanced overloading patterns
    overloading_patterns = {
        "type_checking": {
            "isinstance": "Use isinstance() to check operand types",
            "notimplemented": "Return NotImplemented for unsupported types",
            "reverse_methods": "Implement __radd__, __rmul__ for commutative ops"
        },
        
        "performance_tips": {
            "inplace_ops": "Implement __iadd__, __imul__ for efficiency",
            "caching": "Cache expensive calculations in properties",
            "type_hints": "Use type hints for better IDE support"
        },
        
        "common_mistakes": {
            "mutating_self": "Don't mutate self in arithmetic operators",
            "inconsistent_types": "Ensure consistent return types",
            "missing_reverse": "Don't forget reverse operation methods"
        }
    }
    
    return {
        'magic_methods': magic_methods_reference,
        'vector_example': Vector,
        'patterns': overloading_patterns
    }

# =============================================================================
# 9. ADVANCED OPERATOR TECHNIQUES
# =============================================================================

"""
EXPERT OPERATOR TECHNIQUES:
Professional patterns and advanced operator usage
"""

def demonstrate_advanced_techniques():
    """
    ADVANCED OPERATOR TECHNIQUES
    Professional patterns and optimization strategies
    """
    
    # Operator precedence mastery
    precedence_mastery = {
        "complex_expressions": {
            "scientific": "a * b + c / d - e ** f",
            "bitwise_logical": "flags & mask or default_flags",
            "comparison_chains": "min_val <= value <= max_val and value != excluded"
        },
        
        "parentheses_strategy": {
            "clarity": "Use parentheses for clarity even when not required",
            "performance": "Parentheses don't affect performance",
            "readability": "(a + b) * (c - d) vs a + b * c - d"
        }
    }
    
    # Operator pattern library
    operator_patterns = {
        "validation_patterns": {
            "range_check": "min_val <= value <= max_val",
            "type_and_value": "isinstance(x, int) and x > 0",
            "existence_check": "obj and hasattr(obj, 'method')"
        },
        
        "default_value_patterns": {
            "or_default": "value or default",
            "conditional": "value if condition else default",
            "walrus_default": "result if (result := func()) is not None else default"
        },
        
        "transformation_patterns": {
            "conditional_transform": "func(x) if condition else x",
            "safe_division": "a / b if b != 0 else 0",
            "normalize": "value / max_value if max_value else 0"
        }
    }
    
    # Performance optimization techniques
    performance_techniques = {
        "short_circuit_optimization": {
            "and_chains": "Put likely-false conditions first",
            "or_chains": "Put likely-true conditions first",
            "expensive_last": "Place expensive operations at the end"
        },
        
        "operator_selection": {
            "membership": "Use 'in' with sets for O(1) lookup",
            "comparison": "Use 'is' for identity, '==' for equality",
            "arithmetic": "Use bit operations for powers of 2"
        },
        
        "micro_optimizations": {
            "square": "x * x is faster than x ** 2",
            "increment": "Use += 1 instead of = + 1 for large objects",
            "boolean_conversion": "bool(x) vs not not x"
        }
    }
    
    return {
        'precedence': precedence_mastery,
        'patterns': operator_patterns,
        'performance': performance_techniques
    }

# =============================================================================
# 10. REAL-WORLD OPERATOR APPLICATIONS
# =============================================================================

"""
PRACTICAL OPERATOR APPLICATIONS:
See operators in action across different domains
"""

def demonstrate_real_world_applications():
    """
    REAL-WORLD OPERATOR APPLICATIONS
    Practical examples across different programming domains
    """
    
    # Data validation system
    class DataValidator:
        """Comprehensive data validation using operators."""
        
        def __init__(self):
            self.error_count = 0
            self.validation_rules = {}
        
        def validate_age(self, age):
            """Validate age using comparison operators."""
            return (isinstance(age, int) and 
                   0 <= age <= 150 and 
                   age is not None)
        
        def validate_email(self, email):
            """Validate email using membership and logical operators."""
            return (email and 
                   isinstance(email, str) and 
                   '@' in email and 
                   '.' in email.split('@')[1] and
                   not email.startswith('@') and
                   not email.endswith('@'))
        
        def validate_password(self, password):
            """Complex validation using multiple operators."""
            if not password or not isinstance(password, str):
                return False
            
            return (len(password) >= 8 and
                   any(c.isupper() for c in password) and
                   any(c.islower() for c in password) and
                   any(c.isdigit() for c in password) and
                   any(c in "!@#$%^&*" for c in password))
    
    # Configuration management
    class ConfigManager:
        """Configuration with operator-based logic."""
        
        def __init__(self, config=None):
            self.config = config or {}
            self.defaults = {
                'debug': False,
                'max_connections': 100,
                'timeout': 30.0
            }
        
        def get_value(self, key, default=None):
            """Get config value with fallback logic."""
            return (self.config.get(key) or 
                   self.defaults.get(key) or 
                   default)
        
        def is_feature_enabled(self, feature):
            """Check feature flags with complex logic."""
            return (feature in self.config.get('features', {}) and
                   self.config['features'][feature].get('enabled', False) and
                   not self.config['features'][feature].get('deprecated', False))
    
    # Mathematical computations
    class MathOperations:
        """Mathematical operations using various operators."""
        
        @staticmethod
        def is_prime(n):
            """Prime check using various operators."""
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            
            return not any(n % i == 0 for i in range(3, int(n**0.5) + 1, 2))
        
        @staticmethod
        def gcd(a, b):
            """Greatest common divisor using modulo operator."""
            while b:
                a, b = b, a % b
            return a
        
        @staticmethod
        def power_of_two(n):
            """Check if number is power of 2 using bitwise operators."""
            return n > 0 and (n & (n - 1)) == 0
    
    # Game logic system
    class GameLogic:
        """Game state management using operators."""
        
        def __init__(self):
            self.player_health = 100
            self.player_mana = 50
            self.game_flags = 0  # Bitwise flags
            
            # Flag constants
            self.FLAG_PAUSED = 1 << 0      # 1
            self.FLAG_MUTED = 1 << 1       # 2
            self.FLAG_GODMODE = 1 << 2     # 4
            self.FLAG_DEBUG = 1 << 3       # 8
        
        def can_cast_spell(self, mana_cost):
            """Check if player can cast spell."""
            return (self.player_mana >= mana_cost and
                   self.player_health > 0 and
                   not (self.game_flags & self.FLAG_PAUSED))
        
        def set_flag(self, flag):
            """Set a game flag using bitwise OR."""
            self.game_flags |= flag
        
        def clear_flag(self, flag):
            """Clear a game flag using bitwise AND and NOT."""
            self.game_flags &= ~flag
        
        def toggle_flag(self, flag):
            """Toggle a game flag using bitwise XOR."""
            self.game_flags ^= flag
        
        def has_flag(self, flag):
            """Check if flag is set using bitwise AND."""
            return bool(self.game_flags & flag)
    
    return {
        'validator': DataValidator,
        'config_manager': ConfigManager,
        'math_operations': MathOperations,
        'game_logic': GameLogic
    }

# =============================================================================
# COMPREHENSIVE EXERCISES & CHALLENGES
# =============================================================================

def create_operator_exercises():
    """
    HANDS-ON OPERATOR EXERCISES
    Practice problems to master all operators
    """
    
    # Exercise 1: Expression evaluator
    def exercise_expression_evaluator():
        """
        Create a safe expression evaluator.
        
        Requirements:
        1. Parse and evaluate mathematical expressions
        2. Support all arithmetic operators
        3. Handle operator precedence correctly
        4. Provide security (no eval)
        5. Support variables and functions
        """
        class ExpressionEvaluator:
            def __init__(self):
                self.variables = {}
                self.functions = {}
            
            def evaluate(self, expression):
                """Safely evaluate mathematical expression."""
                # TODO: Implement safe expression evaluation
                pass
        
        return ExpressionEvaluator
    
    # Exercise 2: Bitwise calculator
    def exercise_bitwise_calculator():
        """
        Create advanced bitwise operations calculator.
        
        Requirements:
        1. Support all bitwise operations
        2. Display binary representations
        3. Handle different number bases
        4. Provide bit manipulation utilities
        5. Support flag operations
        """
        class BitwiseCalculator:
            def __init__(self, word_size=32):
                self.word_size = word_size
                self.mask = (1 << word_size) - 1
            
            def calculate(self, operation, *operands):
                """Perform bitwise calculation with visualization."""
                # TODO: Implement bitwise calculator
                pass
        
        return BitwiseCalculator
    
    # Exercise 3: Custom comparison class
    def exercise_comparison_class():
        """
        Create a class with custom comparison logic.
        
        Requirements:
        1. Implement all comparison operators
        2. Support multiple comparison criteria
        3. Handle edge cases gracefully
        4. Provide sorting compatibility
        5. Support comparison with different types
        """
        class ComparableItem:
            def __init__(self, value, priority=0, category="default"):
                self.value = value
                self.priority = priority
                self.category = category
            
            def __eq__(self, other):
                """Implement equality comparison."""
                # TODO: Implement comparison logic
                pass
        
        return ComparableItem
    
    return {
        'expression_evaluator': exercise_expression_evaluator(),
        'bitwise_calculator': exercise_bitwise_calculator(),
        'comparison_class': exercise_comparison_class()
    }

# =============================================================================
# MAIN EXECUTION & EXAMPLES
# =============================================================================

if __name__ == "__main__":
    """
    COMPREHENSIVE OPERATORS DEMONSTRATION
    Run examples and see all operators in action
    """
    
    print("🎯 PYTHON OPERATORS - COMPLETE MASTERY GUIDE")
    print("=" * 60)
    
    # Operator precedence demonstration
    print("\n📊 1. OPERATOR PRECEDENCE & ASSOCIATIVITY:")
    precedence_demo = demonstrate_operator_precedence()
    print(f"Precedence examples: {len(precedence_demo['precedence_examples'])}")
    print("Associativity rules demonstrated ✓")
    
    # Arithmetic operators
    print("\n🔢 2. ARITHMETIC OPERATORS:")
    arithmetic_demo = demonstrate_arithmetic_operators()
    print("Basic arithmetic operations ✓")
    print("Advanced techniques ✓")
    print("Performance optimizations ✓")
    
    # Comparison operators
    print("\n⚖️ 3. COMPARISON OPERATORS:")
    comparison_demo = demonstrate_comparison_operators()
    print("Equality and ordering ✓")
    print("Chained comparisons ✓")
    print("Edge cases handled ✓")
    
    # Logical operators
    print("\n🧠 4. LOGICAL OPERATORS:")
    logical_demo = demonstrate_logical_operators()
    print("Boolean logic ✓")
    print("Short-circuit evaluation ✓")
    print("Truthiness patterns ✓")
    
    # Bitwise operators
    print("\n🔧 5. BITWISE OPERATORS:")
    bitwise_demo = demonstrate_bitwise_operators()
    print("Binary operations ✓")
    print("Bit manipulation tricks ✓")
    print("Flag operations ✓")
    
    # Assignment operators
    print("\n📝 6. ASSIGNMENT OPERATORS:")
    assignment_demo = demonstrate_assignment_operators()
    print("Augmented assignment ✓")
    print("Multiple assignment ✓")
    print("Walrus operator ✓")
    
    # Identity and membership
    print("\n🔍 7. IDENTITY & MEMBERSHIP:")
    identity_demo = demonstrate_identity_membership()
    print("Object identity ✓")
    print("Container membership ✓")
    
    # Operator overloading
    print("\n🎭 8. OPERATOR OVERLOADING:")
    overloading_demo = demonstrate_operator_overloading()
    print("Magic methods ✓")
    print("Custom classes ✓")
    print("Best practices ✓")
    
    # Advanced techniques
    print("\n🎪 9. ADVANCED TECHNIQUES:")
    advanced_demo = demonstrate_advanced_techniques()
    print("Complex expressions ✓")
    print("Operator patterns ✓")
    print("Performance optimization ✓")
    
    # Real-world applications
    print("\n🌍 10. REAL-WORLD APPLICATIONS:")
    apps_demo = demonstrate_real_world_applications()
    print("Data validation ✓")
    print("Configuration management ✓")
    print("Mathematical operations ✓")
    print("Game logic ✓")
    
    # Exercises
    print("\n💪 11. HANDS-ON EXERCISES:")
    exercises = create_operator_exercises()
    print("Expression evaluator challenge ✓")
    print("Bitwise calculator project ✓")
    print("Custom comparison class ✓")
    
    print("\n" + "=" * 60)
    print("🎉 OPERATORS MASTERY COMPLETE!")
    print("You now have comprehensive knowledge of Python operators.")
    print("Practice with the exercises to become an operator expert!")

# =============================================================================
# END OF COMPREHENSIVE OPERATORS GUIDE
# =============================================================================
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

""" PRACTICAL OPERATOR EXAMPLES """

# Arithmetic Operations in Real Scenarios
""" Shopping Cart Calculation """
item_price = 29.99
quantity = 3
tax_rate = 0.08

subtotal = item_price * quantity        # 89.97
tax = subtotal * tax_rate               # 7.20
total = subtotal + tax                  # 97.17

print(f"Subtotal: ${subtotal:.2f}")     # $89.97
print(f"Tax: ${tax:.2f}")               # $7.20
print(f"Total: ${total:.2f}")           # $97.17

""" Time Calculations """
total_seconds = 3725
hours = total_seconds // 3600           # 1 hour
remaining_seconds = total_seconds % 3600 # 125 seconds  
minutes = remaining_seconds // 60       # 2 minutes
seconds = remaining_seconds % 60        # 5 seconds

print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")

# Assignment Operators in Practice
""" Score Accumulation """
player_score = 0
player_score += 100    # Gained 100 points
player_score += 50     # Gained 50 more points  
player_score -= 25     # Lost 25 points
player_score *= 2      # Double score bonus
print(f"Final score: {player_score}")  # 250

""" Comparison Operators for Data Validation """
age = 25
min_age = 18
max_age = 65

is_adult = age >= min_age               # True
is_senior = age >= 65                   # False
is_working_age = min_age <= age <= max_age  # True

print(f"Is adult: {is_adult}")
print(f"Is senior: {is_senior}")  
print(f"Is working age: {is_working_age}")

""" Logical Operators for Complex Conditions """
has_license = True
has_insurance = True
car_working = False

can_drive_legally = has_license and has_insurance    # True
can_actually_drive = can_drive_legally and car_working  # False
needs_repair = not car_working                       # True

print(f"Can drive legally: {can_drive_legally}")
print(f"Can actually drive: {can_actually_drive}")
print(f"Needs repair: {needs_repair}")

""" Identity vs Equality """
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 == list2: {list1 == list2}")  # True (same content)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is list3: {list1 is list3}")  # True (same object)

""" Membership Operators """
vowels = ['a', 'e', 'i', 'o', 'u']
user_input = 'hello'

vowel_count = 0
for char in user_input:
    if char in vowels:
        vowel_count += 1

print(f"'{user_input}' has {vowel_count} vowels")  # 2 vowels

""" Bitwise Operations (Advanced) """
# Useful for permissions, flags, and optimization
READ_PERMISSION = 1    # Binary: 001
WRITE_PERMISSION = 2   # Binary: 010  
EXECUTE_PERMISSION = 4 # Binary: 100

# Combine permissions using OR
user_permissions = READ_PERMISSION | WRITE_PERMISSION  # 3 (011)

# Check specific permission using AND
can_read = bool(user_permissions & READ_PERMISSION)    # True
can_write = bool(user_permissions & WRITE_PERMISSION)  # True
can_execute = bool(user_permissions & EXECUTE_PERMISSION)  # False

print(f"Can read: {can_read}")
print(f"Can write: {can_write}")
print(f"Can execute: {can_execute}")

# Remove permission using XOR
user_permissions ^= WRITE_PERMISSION  # Remove write permission
can_write_after = bool(user_permissions & WRITE_PERMISSION)  # False
print(f"Can write after removal: {can_write_after}")

""" Operator Precedence Example """
# Without parentheses
result1 = 2 + 3 * 4        # 14 (multiplication first)
result2 = (2 + 3) * 4      # 20 (parentheses first)

print(f"2 + 3 * 4 = {result1}")      # 14
print(f"(2 + 3) * 4 = {result2}")    # 20

# Complex expression
calculation = 10 + 2 * 3 ** 2 - 4 / 2
# Order: 3**2=9, 2*9=18, 4/2=2.0, 10+18=28, 28-2.0=26.0
print(f"Complex calculation: {calculation}")  # 26.0

""" Walrus Operator (Python 3.8+) """
# Useful for avoiding duplicate calculations
numbers = [1, 4, 9, 16, 25]

# Traditional approach
squared_values = []
for n in numbers:
    sqrt_n = n ** 0.5
    if sqrt_n > 2:
        squared_values.append(sqrt_n)

# With walrus operator  
squared_values_walrus = []
for n in numbers:
    if (sqrt_n := n ** 0.5) > 2:
        squared_values_walrus.append(sqrt_n)

print(f"Values > 2: {squared_values_walrus}")

# ----------