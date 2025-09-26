""" 3.6.0_Python_BOOLEANS.py """

# =============================================================================
# PYTHON BOOLEAN LOGIC - COMPREHENSIVE MASTERY GUIDE
# =============================================================================
# Version: 3.6.0 | Educational Excellence Target: 9.5/10
# Purpose: Master boolean operations and truth evaluation in Python
# Target: Intermediate Python learners and logic programmers
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python booleans, you will:
✓ Understand boolean data type and truth values
✓ Apply logical operators effectively (and, or, not)
✓ Master truthiness and falsiness concepts
✓ Write complex boolean expressions
✓ Use short-circuit evaluation strategically
✓ Apply boolean logic in real-world scenarios

🚀 QUICK NAVIGATION:
├── 1. BOOLEAN DATA TYPE FUNDAMENTALS
├── 2. LOGICAL OPERATORS & OPERATIONS
├── 3. TRUTHINESS & FALSINESS RULES
├── 4. BOOLEAN EXPRESSIONS & PRECEDENCE
├── 5. SHORT-CIRCUIT EVALUATION
├── 6. COMPARISON & IDENTITY OPERATORS
├── 7. BOOLEAN PATTERNS & IDIOMS
├── 8. REAL-WORLD APPLICATIONS
├── 9. PERFORMANCE & OPTIMIZATION
└── 10. COMMON MISTAKES & DEBUGGING

🔍 CORE CONCEPT:
Boolean logic is the foundation of all conditional programming
and decision-making in software applications.
"""

# =============================================================================
# 1. BOOLEAN DATA TYPE FUNDAMENTALS - COMPLETE FOUNDATION
# =============================================================================

"""
BOOLEAN DATA TYPE DEEP DIVE:
Understanding the foundation of logical operations
"""

# Boolean Literals and Basic Properties
boolean_fundamentals = {
    "literal_values": {
        "True": {
            "value": True,
            "type": bool,
            "integer_value": int(True),  # 1
            "description": "Represents logical truth"
        },
        "False": {
            "value": False,
            "type": bool,
            "integer_value": int(False),  # 0
            "description": "Represents logical falsehood"
        }
    },
    
    "type_characteristics": {
        "inheritance": "bool is a subclass of int",
        "immutable": True,
        "singleton": "True and False are singleton objects",
        "memory_efficiency": "Only two instances exist in memory"
    },
    
    "creation_methods": [
        "bool()        # False (default)",
        "bool(value)   # Convert value to boolean",
        "True, False   # Direct literals",
        "not not value # Double negation conversion"
    ]
}

def demonstrate_boolean_basics():
    """
    COMPREHENSIVE BOOLEAN BASIC OPERATIONS
    Foundation concepts with practical examples
    """
    
    # Type verification
    type_examples = [
        ("type(True)", type(True)),                    # <class 'bool'>
        ("isinstance(True, bool)", isinstance(True, bool)),  # True
        ("isinstance(True, int)", isinstance(True, int)),    # True (bool inherits from int)
        ("True is True", True is True),                # True (singleton)
        ("False is False", False is False),            # True (singleton)
    ]
    
    # Arithmetic with booleans
    arithmetic_examples = [
        ("True + False", True + False),        # 1 (1 + 0)
        ("True * 5", True * 5),               # 5 (1 * 5)
        ("False * 100", False * 100),         # 0 (0 * 100)
        ("True / 2", True / 2),               # 0.5 (1 / 2)
        ("sum([True, False, True])", sum([True, False, True]))  # 2
    ]
    
    # Boolean conversion examples
    conversion_examples = [
        ("bool(1)", bool(1)),                 # True
        ("bool(0)", bool(0)),                 # False
        ("bool('hello')", bool('hello')),     # True
        ("bool('')", bool('')),               # False
        ("bool([1, 2, 3])", bool([1, 2, 3])), # True
        ("bool([])", bool([])),               # False
        ("bool(None)", bool(None)),           # False
    ]
    
    return {
        'type_verification': type_examples,
        'arithmetic_operations': arithmetic_examples,
        'conversions': conversion_examples
    }

# =============================================================================
# 2. LOGICAL OPERATORS & OPERATIONS - COMPLETE MASTERY
# =============================================================================

"""
COMPREHENSIVE LOGICAL OPERATORS GUIDE:
Master and, or, not operators with advanced patterns
"""

logical_operators_reference = {
    "and_operator": {
        "syntax": "expression1 and expression2",
        "behavior": "Returns first falsy value, or last value if all truthy",
        "truth_table": [
            (True, True, True),
            (True, False, False),
            (False, True, False),
            (False, False, False)
        ],
        "examples": [
            ("True and True", True),
            ("True and False", False),
            ("5 and 3", 3),          # Both truthy, returns last
            ("0 and 5", 0),          # First falsy, returns first
            ("'' and 'hello'", ''),  # First falsy, returns first
        ]
    },
    
    "or_operator": {
        "syntax": "expression1 or expression2",
        "behavior": "Returns first truthy value, or last value if all falsy",
        "truth_table": [
            (True, True, True),
            (True, False, True),
            (False, True, True),
            (False, False, False)
        ],
        "examples": [
            ("True or False", True),
            ("False or True", True),
            ("5 or 3", 5),           # First truthy, returns first
            ("0 or 5", 5),           # First falsy, second truthy
            ("'' or 'hello'", 'hello'),  # First falsy, second truthy
            ("0 or ''", ''),         # All falsy, returns last
        ]
    },
    
    "not_operator": {
        "syntax": "not expression",
        "behavior": "Returns boolean opposite of expression truthiness",
        "examples": [
            ("not True", False),
            ("not False", True),
            ("not 5", False),        # 5 is truthy
            ("not 0", True),         # 0 is falsy
            ("not []", True),        # Empty list is falsy
            ("not [1, 2]", False),   # Non-empty list is truthy
        ]
    }
}

def demonstrate_logical_operators():
    """
    ADVANCED LOGICAL OPERATOR PATTERNS
    Real-world applications and complex expressions
    """
    
    # Chained logical operations
    def chained_operations():
        """Demonstrate chained logical operations."""
        examples = [
            # Multiple AND operations
            ("True and True and True", True and True and True),     # True
            ("True and False and True", True and False and True),   # False
            ("1 and 2 and 3", 1 and 2 and 3),                     # 3 (last truthy)
            ("1 and 0 and 3", 1 and 0 and 3),                     # 0 (first falsy)
            
            # Multiple OR operations
            ("False or False or True", False or False or True),     # True
            ("0 or '' or 5", 0 or '' or 5),                       # 5 (first truthy)
            ("0 or '' or []", 0 or '' or []),                     # [] (last falsy)
            
            # Mixed operations
            ("True and False or True", True and False or True),     # True
            ("False or True and False", False or True and False),   # False
            ("not True or False", not True or False),               # False
        ]
        return examples
    
    # Operator precedence demonstration
    def precedence_examples():
        """Demonstrate logical operator precedence."""
        # Precedence: not > and > or
        examples = [
            ("not False or True", not False or True),               # True (not has highest precedence)
            ("True or False and False", True or False and False),   # True (and before or)
            ("not True and False or True", not True and False or True),  # True
            ("(not True) and (False or True)", (not True) and (False or True)),  # False
        ]
        return examples
    
    # Practical patterns
    def practical_patterns():
        """Real-world logical operator patterns."""
        
        # Default value pattern
        def get_name(name=None):
            return name or "Anonymous"
        
        # Validation pattern
        def validate_user(user_data):
            return (user_data and 
                   isinstance(user_data, dict) and
                   'username' in user_data and
                   'email' in user_data and
                   len(user_data['username']) > 0)
        
        # Guard clause pattern
        def process_data(data):
            if not data or not isinstance(data, list):
                return []
            return [item.upper() for item in data if isinstance(item, str)]
        
        # Range checking
        def is_valid_age(age):
            return isinstance(age, int) and 0 <= age <= 150
        
        # Multi-condition checks
        def can_drive(age, has_license, has_car):
            return age >= 18 and has_license and has_car
        
        examples = {
            'default_value': get_name(),
            'validation': validate_user({'username': 'john', 'email': 'john@example.com'}),
            'range_check': is_valid_age(25),
            'multi_condition': can_drive(20, True, True)
        }
        return examples
    
    return {
        'chained': chained_operations(),
        'precedence': precedence_examples(),
        'patterns': practical_patterns()
    }

# =============================================================================
# 3. TRUTHINESS & FALSINESS RULES - COMPLETE GUIDE
# =============================================================================

"""
COMPREHENSIVE TRUTHINESS EVALUATION:
Master what Python considers True and False
"""

truthiness_reference = {
    "falsy_values": {
        "description": "Values that evaluate to False in boolean context",
        "complete_list": [
            ("False", False, "Boolean literal"),
            ("None", None, "None type"),
            ("0", 0, "Integer zero"),
            ("0.0", 0.0, "Float zero"),
            ("0j", 0j, "Complex zero"),
            ("''", '', "Empty string"),
            ("[]", [], "Empty list"),
            ("()", (), "Empty tuple"),
            ("{}", {}, "Empty dictionary"),
            ("set()", set(), "Empty set"),
            ("frozenset()", frozenset(), "Empty frozenset"),
        ]
    },
    
    "truthy_values": {
        "description": "Everything else evaluates to True",
        "examples": [
            ("True", True, "Boolean literal"),
            ("1", 1, "Non-zero integer"),
            ("3.14", 3.14, "Non-zero float"),
            ("'hello'", 'hello', "Non-empty string"),
            ("' '", ' ', "String with whitespace"),
            ("[0]", [0], "List with falsy element"),
            ("{'key': False}", {'key': False}, "Dict with falsy value"),
            ("object()", "Any object instance"),
            ("lambda: None", "Any function"),
        ]
    },
    
    "special_cases": {
        "numeric_zeros": {
            "int_zero": (0, "Falsy"),
            "float_zero": (0.0, "Falsy"),
            "negative_zero": (-0.0, "Falsy"),
            "complex_zero": (0+0j, "Falsy"),
            "decimal_zero": "Decimal('0') - Falsy"
        },
        
        "container_edge_cases": {
            "list_with_falsy": ([0, False, None], "Truthy - contains elements"),
            "string_with_zero": ("0", "Truthy - non-empty string"),
            "string_false": ("False", "Truthy - non-empty string"),
            "nested_empty": ([[], {}], "Truthy - contains empty containers")
        }
    }
}

def demonstrate_truthiness():
    """
    COMPREHENSIVE TRUTHINESS TESTING
    Test truth values of various Python objects
    """
    
    # Test all falsy values
    def test_falsy_values():
        """Test all values that are falsy in Python."""
        falsy_tests = [
            (False, bool(False)),
            (None, bool(None)),
            (0, bool(0)),
            (0.0, bool(0.0)),
            (0j, bool(0j)),
            ('', bool('')),
            ([], bool([])),
            ((), bool(())),
            ({}, bool({})),
            (set(), bool(set())),
            (frozenset(), bool(frozenset())),
        ]
        
        all_falsy = all(not result for _, result in falsy_tests)
        return {'tests': falsy_tests, 'all_falsy': all_falsy}
    
    # Test common truthy edge cases
    def test_truthy_edge_cases():
        """Test edge cases that might be confusing."""
        edge_cases = [
            ("String '0'", bool("0")),              # True
            ("String 'False'", bool("False")),      # True
            ("List [0]", bool([0])),                # True
            ("List [False]", bool([False])),        # True
            ("Dict {'': 0}", bool({'': 0})),        # True
            ("Whitespace ' '", bool(" ")),          # True
            ("Newline '\\n'", bool("\n")),          # True
        ]
        return edge_cases
    
    # Custom object truthiness
    class CustomObject:
        """Demonstrate custom object truthiness."""
        
        def __init__(self, value):
            self.value = value
        
        def __bool__(self):
            """Define custom truthiness based on value."""
            return bool(self.value)
        
        def __len__(self):
            """Alternative: define truthiness based on length."""
            return len(str(self.value))
    
    def test_custom_objects():
        """Test custom object truthiness."""
        obj1 = CustomObject("")      # Should be falsy
        obj2 = CustomObject("hello") # Should be truthy
        
        return [
            ("CustomObject('')", bool(obj1)),      # False
            ("CustomObject('hello')", bool(obj2)), # True
        ]
    
    return {
        'falsy_tests': test_falsy_values(),
        'edge_cases': test_truthy_edge_cases(),
        'custom_objects': test_custom_objects()
    }

# =============================================================================
# 4. BOOLEAN EXPRESSIONS & PRECEDENCE - ADVANCED PATTERNS
# =============================================================================

"""
COMPLEX BOOLEAN EXPRESSIONS:
Master operator precedence and complex logical structures
"""

def demonstrate_boolean_expressions():
    """
    ADVANCED BOOLEAN EXPRESSION PATTERNS
    Complex logical structures with precedence rules
    """
    
    # Operator precedence (highest to lowest)
    precedence_rules = [
        "1. Parentheses: ()",
        "2. Logical NOT: not",
        "3. Comparison: <, <=, >, >=, ==, !=, is, is not, in, not in",
        "4. Logical AND: and",
        "5. Logical OR: or"
    ]
    
    # Complex expression examples
    complex_expressions = [
        {
            "expression": "not False and True or False",
            "evaluation": not False and True or False,
            "step_by_step": [
                "not False → True",
                "True and True → True", 
                "True or False → True"
            ]
        },
        {
            "expression": "5 > 3 and 2 < 4 or 1 == 0",
            "evaluation": 5 > 3 and 2 < 4 or 1 == 0,
            "step_by_step": [
                "5 > 3 → True",
                "2 < 4 → True",
                "1 == 0 → False",
                "True and True → True",
                "True or False → True"
            ]
        },
        {
            "expression": "not (True and False) or (False or True)",
            "evaluation": not (True and False) or (False or True),
            "step_by_step": [
                "(True and False) → False",
                "(False or True) → True",
                "not False → True",
                "True or True → True"
            ]
        }
    ]
    
    # Comparison chaining
    comparison_chaining = [
        {
            "expression": "1 < 2 < 3",
            "evaluation": 1 < 2 < 3,
            "equivalent": "(1 < 2) and (2 < 3)",
            "result": True
        },
        {
            "expression": "5 > 3 > 1",
            "evaluation": 5 > 3 > 1,
            "equivalent": "(5 > 3) and (3 > 1)",
            "result": True
        },
        {
            "expression": "x == y == z",
            "equivalent": "(x == y) and (y == z)",
            "note": "Checks if all three are equal"
        }
    ]
    
    # De Morgan's Laws demonstration
    de_morgans_laws = [
        {
            "law": "not (A and B) ≡ (not A) or (not B)",
            "example_A": True,
            "example_B": False,
            "left_side": not (True and False),      # True
            "right_side": (not True) or (not False), # True
            "equal": not (True and False) == ((not True) or (not False))
        },
        {
            "law": "not (A or B) ≡ (not A) and (not B)",
            "example_A": True,
            "example_B": False,
            "left_side": not (True or False),       # False
            "right_side": (not True) and (not False), # False
            "equal": not (True or False) == ((not True) and (not False))
        }
    ]
    
    return {
        'precedence_rules': precedence_rules,
        'complex_expressions': complex_expressions,
        'comparison_chaining': comparison_chaining,
        'de_morgans_laws': de_morgans_laws
    }

# =============================================================================
# 5. SHORT-CIRCUIT EVALUATION - PERFORMANCE & LOGIC
# =============================================================================

"""
SHORT-CIRCUIT EVALUATION MASTERY:
Understand and leverage Python's evaluation optimization
"""

def demonstrate_short_circuit():
    """
    SHORT-CIRCUIT EVALUATION PATTERNS
    Performance optimization and side-effect control
    """
    
    # Function with side effects for demonstration
    def side_effect_function(name, return_value):
        """Function with side effects to demonstrate short-circuiting."""
        print(f"Function {name} called!")
        return return_value
    
    # AND short-circuit examples
    def and_short_circuit_examples():
        """Demonstrate AND operator short-circuiting."""
        print("AND Short-Circuit Examples:")
        
        # First operand is falsy - second not evaluated
        result1 = False and side_effect_function("B", True)
        print(f"False and func() = {result1}")  # func() not called
        
        # First operand is truthy - second is evaluated
        result2 = True and side_effect_function("C", False)
        print(f"True and func() = {result2}")   # func() is called
        
        return [result1, result2]
    
    # OR short-circuit examples
    def or_short_circuit_examples():
        """Demonstrate OR operator short-circuiting."""
        print("\nOR Short-Circuit Examples:")
        
        # First operand is truthy - second not evaluated
        result1 = True or side_effect_function("D", False)
        print(f"True or func() = {result1}")    # func() not called
        
        # First operand is falsy - second is evaluated
        result2 = False or side_effect_function("E", True)
        print(f"False or func() = {result2}")   # func() is called
        
        return [result1, result2]
    
    # Practical short-circuit applications
    practical_applications = {
        "safe_division": {
            "code": "result = divisor != 0 and dividend / divisor",
            "explanation": "Avoids division by zero without try/except",
            "example": lambda dividend, divisor: divisor != 0 and dividend / divisor
        },
        
        "safe_attribute_access": {
            "code": "value = obj and hasattr(obj, 'attr') and obj.attr",
            "explanation": "Safely access object attributes",
            "example": lambda obj, attr: obj and hasattr(obj, attr) and getattr(obj, attr)
        },
        
        "default_values": {
            "code": "name = provided_name or 'Default'",
            "explanation": "Use default if provided value is falsy",
            "example": lambda provided: provided or "Default"
        },
        
        "early_validation": {
            "code": "valid = data and len(data) > 0 and data[0] != ''",
            "explanation": "Validate data structure safely",
            "example": lambda data: data and len(data) > 0 and data[0] != ''
        }
    }
    
    return {
        'and_examples': and_short_circuit_examples,
        'or_examples': or_short_circuit_examples,
        'applications': practical_applications
    }

# =============================================================================
# 6. COMPARISON & IDENTITY OPERATORS - COMPLETE GUIDE
# =============================================================================

"""
COMPARISON AND IDENTITY OPERATORS:
Master equality, identity, and membership testing
"""

comparison_operators_reference = {
    "equality_operators": {
        "==": {
            "name": "Equal to",
            "description": "Compares values for equality",
            "examples": [
                ("5 == 5", True),
                ("'hello' == 'hello'", True),
                ("[1, 2] == [1, 2]", True),
                ("True == 1", True),  # Bool is subclass of int
            ]
        },
        "!=": {
            "name": "Not equal to", 
            "description": "Compares values for inequality",
            "examples": [
                ("5 != 3", True),
                ("'hello' != 'world'", True),
                ("[1, 2] != [1, 2, 3]", True),
            ]
        }
    },
    
    "ordering_operators": {
        "<": "Less than",
        "<=": "Less than or equal to",
        ">": "Greater than", 
        ">=": "Greater than or equal to"
    },
    
    "identity_operators": {
        "is": {
            "name": "Identity (same object)",
            "description": "Tests if two variables refer to the same object",
            "examples": [
                ("a = [1, 2]; b = a; a is b", True),
                ("[1, 2] is [1, 2]", False),  # Different objects
                ("True is True", True),        # Singleton
                ("None is None", True),        # Singleton
            ]
        },
        "is not": {
            "name": "Not identity",
            "description": "Tests if two variables refer to different objects",
            "examples": [
                ("[1, 2] is not [1, 2]", True),
                ("x = 5; y = 5; x is not y", False),  # Small ints are cached
            ]
        }
    },
    
    "membership_operators": {
        "in": {
            "name": "Membership test",
            "description": "Tests if item exists in container",
            "examples": [
                ("'a' in 'apple'", True),
                ("2 in [1, 2, 3]", True),
                ("'key' in {'key': 'value'}", True),
            ]
        },
        "not in": {
            "name": "Non-membership test",
            "description": "Tests if item doesn't exist in container",
            "examples": [
                ("'z' not in 'apple'", True),
                ("5 not in [1, 2, 3]", True),
            ]
        }
    }
}

def demonstrate_comparison_operators():
    """
    COMPREHENSIVE COMPARISON OPERATOR EXAMPLES
    Including edge cases and best practices
    """
    
    # Equality vs Identity
    def equality_vs_identity():
        """Demonstrate difference between == and is."""
        # Small integers are cached (-5 to 256)
        a = 100
        b = 100
        small_int_same = a is b  # True (cached)
        
        # Large integers are not cached
        c = 1000
        d = 1000
        large_int_different = c is d  # May be False
        
        # Lists with same content
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        equal_content = list1 == list2    # True
        same_object = list1 is list2      # False
        
        # Same object reference
        list3 = list1
        same_reference = list1 is list3   # True
        
        return {
            'small_integers': (a, b, small_int_same),
            'large_integers': (c, d, large_int_different),
            'list_equality': equal_content,
            'list_identity': same_object,
            'same_reference': same_reference
        }
    
    # Chained comparisons
    def chained_comparisons():
        """Demonstrate chained comparison operators."""
        x, y, z = 5, 10, 15
        
        examples = [
            ("x < y < z", x < y < z),                    # True
            ("x <= y <= z", x <= y <= z),                # True
            ("z > y > x", z > y > x),                    # True
            ("x == x == x", x == x == x),                # True
            ("x < y > z", x < y > z),                    # False
            ("1 < 2 < 3 < 4", 1 < 2 < 3 < 4),          # True
        ]
        
        return examples
    
    # Membership testing optimization
    def membership_testing():
        """Demonstrate membership testing with different containers."""
        import time
        
        # Performance comparison: list vs set
        large_list = list(range(10000))
        large_set = set(range(10000))
        target = 9999
        
        # List membership (O(n))
        start_time = time.time()
        result1 = target in large_list
        list_time = time.time() - start_time
        
        # Set membership (O(1))
        start_time = time.time()
        result2 = target in large_set
        set_time = time.time() - start_time
        
        return {
            'list_result': result1,
            'set_result': result2,
            'list_time': list_time,
            'set_time': set_time,
            'performance_ratio': list_time / set_time if set_time > 0 else 0
        }
    
    return {
        'equality_identity': equality_vs_identity(),
        'chained': chained_comparisons(),
        'membership': membership_testing()
    }

# =============================================================================
# QUICK REFERENCE SUMMARY - MEMORIZE THESE!
# =============================================================================

"""
PYTHON BOOLEAN LOGIC CHEAT SHEET - ESSENTIAL PATTERNS

BOOLEAN LITERALS:
True, False           # Only two boolean values (case-sensitive)

LOGICAL OPERATORS:
and                   # Returns first falsy or last value
or                    # Returns first truthy or last value  
not                   # Returns boolean opposite

FALSY VALUES (evaluate to False):
False, None, 0, 0.0, 0j, '', [], (), {}, set(), frozenset()

TRUTHY VALUES (evaluate to True):
Everything else, including: True, 1, 'hello', [0], {'key': False}

COMPARISON OPERATORS:
==, !=               # Value equality/inequality
<, <=, >, >=         # Ordering comparisons
is, is not           # Identity (same object)
in, not in           # Membership testing

SHORT-CIRCUIT EVALUATION:
False and x          # x not evaluated
True or x            # x not evaluated
True and x           # x is evaluated
False or x           # x is evaluated

OPERATOR PRECEDENCE (high to low):
()                   # Parentheses
not                  # Logical NOT
<, <=, >, >=, ==, != # Comparisons
is, is not, in, not in # Identity and membership
and                  # Logical AND
or                   # Logical OR

COMMON PATTERNS:
value or default     # Default value assignment
x and y              # Guard pattern (check x before using y)
not not value        # Convert to boolean
bool(value)          # Explicit boolean conversion
"""  
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False

# NOT operator
print(not True)         # False
print(not False)        # True

# ----------

""" Truth Values """
# In Python, all values have a truth value when evaluated in a boolean context.
# The following values are considered False (falsy):

falsy_values = [
    False,      # Boolean False
    0,          # Zero integer
    0.0,        # Zero float
    0j,         # Zero complex number
    "",         # Empty string
    '',         # Empty string (single quotes)
    [],         # Empty list
    (),         # Empty tuple
    {},         # Empty dictionary
    set(),      # Empty set
    None        # None value
]

for value in falsy_values:
    print(f"{value} is {bool(value)}")

# All other values are considered True (truthy):
truthy_values = [
    True,           # Boolean True
    1,              # Non-zero integers
    -1,             # Negative integers
    3.14,           # Non-zero floats
    "Hello",        # Non-empty strings
    [1, 2, 3],     # Non-empty lists
    (1, 2),        # Non-empty tuples
    {"a": 1},      # Non-empty dictionaries
    {1, 2, 3}      # Non-empty sets
]

for value in truthy_values:
    print(f"{value} is {bool(value)}")

# ----------

""" Boolean Conversion """
# Use bool() function to convert values to boolean:

print(bool(1))          # True
print(bool(0))          # False
print(bool("Hello"))    # True
print(bool(""))         # False
print(bool([1, 2, 3]))  # True
print(bool([]))         # False

# ----------

""" Comparison Operators Return Booleans """
# All comparison operations return boolean values:

print(5 > 3)            # True
print(5 < 3)            # False
print(5 == 5)           # True
print(5 != 3)           # True
print("apple" == "apple")  # True
print("apple" != "banana") # True

# ----------

""" Boolean in Conditional Statements """
# Booleans are primarily used in if statements and while loops:

is_sunny = True
is_warm = False

if is_sunny:
    print("It's a sunny day!")

if is_sunny and is_warm:
    print("Perfect weather!")
else:
    print("Weather could be better")

# Using truthiness of values
name = "Alice"
if name:  # Non-empty string is truthy
    print(f"Hello, {name}!")

numbers = []
if not numbers:  # Empty list is falsy, so 'not []' is True
    print("No numbers in the list")

# ----------

""" Boolean Arithmetic """
# Since booleans are a subclass of int, they can be used in arithmetic:

print(True + True)      # 2 (True is treated as 1)
print(False + True)     # 1
print(True * 5)         # 5
print(False * 100)      # 0

# This can be useful for counting:
conditions = [True, False, True, True, False]
true_count = sum(conditions)  # Counts how many True values
print(f"Number of True conditions: {true_count}")  # 3

# ----------

""" Short-Circuit Evaluation """
# Python uses short-circuit evaluation for 'and' and 'or':

def expensive_operation():
    print("This function was called!")
    return True

# With 'and': if first operand is False, second is not evaluated
print(False and expensive_operation())  # False (function not called)
print(True and expensive_operation())   # Function is called, returns True

# With 'or': if first operand is True, second is not evaluated  
print(True or expensive_operation())    # True (function not called)
print(False or expensive_operation())   # Function is called, returns True

# ----------

""" Boolean Identity """
# There's only one True object and one False object in Python:

a = True
b = True
print(a is b)           # True (same object)

c = False  
d = False
print(c is d)           # True (same object)

# However, be careful with bool() conversion:
x = bool(1)
y = bool(2)
print(x is y)           # True (both are the same True object)

# ----------

""" Common Boolean Patterns """

# Check if a list has elements
my_list = [1, 2, 3]
if my_list:
    print("List has elements")

# Check if a string is not empty
user_input = input("Enter your name: ")
if user_input.strip():  # .strip() removes whitespace
    print(f"Hello, {user_input}!")
else:
    print("No name entered")

# Multiple conditions
age = 25
has_license = True
has_car = False

can_drive = age >= 18 and has_license
should_buy_car = can_drive and not has_car

print(f"Can drive: {can_drive}")         # True
print(f"Should buy car: {should_buy_car}") # True

# ----------

""" Boolean Methods """
# Some useful methods that return booleans:

text = "Hello World"
print(text.startswith("Hello"))    # True
print(text.endswith("World"))      # True  
print(text.isalpha())              # False (contains space)
print("123".isdigit())             # True
print("Hello".islower())           # False
print("WORLD".isupper())           # True

number = 42
numbers_list = [1, 2, 3, 42, 5]
print(number in numbers_list)      # True

# ----------

""" Practice Examples """

# Example 1: User authentication
username = "admin"
password = "secret123"

user_input_name = "admin"
user_input_pass = "secret123"

is_authenticated = (username == user_input_name) and (password == user_input_pass)
print(f"User authenticated: {is_authenticated}")

# Example 2: Grade evaluation
score = 85
passed = score >= 60
honor_roll = score >= 90
needs_improvement = score < 50

print(f"Passed: {passed}")                      # True
print(f"Honor roll: {honor_roll}")              # False  
print(f"Needs improvement: {needs_improvement}") # False

# Example 3: Data validation
email = "user@example.com"
is_valid_email = "@" in email and "." in email and len(email) > 5
print(f"Valid email: {is_valid_email}")         # True

# ----------