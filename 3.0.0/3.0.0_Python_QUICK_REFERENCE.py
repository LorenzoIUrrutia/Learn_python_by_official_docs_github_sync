""" 3.0.0_Python_QUICK_REFERENCE.py """

# =============================================================================
# PYTHON FUNDAMENTALS QUICK REFERENCE GUIDE - COMPREHENSIVE EDITION
# =============================================================================
# Version: 3.0.0 | Educational Excellence Target: 9.5/10
# Purpose: Complete cheat sheet for Python fundamentals mastery
# Target: Students, developers, and Python learners at all levels
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering this reference, you will:
✓ Understand all Python fundamental concepts
✓ Apply correct syntax and best practices
✓ Navigate Python data types with confidence
✓ Use operators and control structures effectively
✓ Write clean, professional Python code
✓ Debug and troubleshoot common issues

🚀 QUICK NAVIGATION:
├── 1. DATA TYPES & TYPE SYSTEM
├── 2. VARIABLES & NAMING CONVENTIONS  
├── 3. OPERATORS & PRECEDENCE RULES
├── 4. SYNTAX & CODE FORMATTING
├── 5. BOOLEAN LOGIC & TRUTH VALUES
├── 6. KEYWORDS & CONTROL STRUCTURES
├── 7. NUMBERS & MATHEMATICAL OPERATIONS
├── 8. STRINGS & TEXT PROCESSING
├── 9. LISTS & DYNAMIC COLLECTIONS
├── 10. ARRAYS & MEMORY OPTIMIZATION
├── 11. INDEXING & SLICING MASTERY
├── 12. COMMON PATTERNS & IDIOMS
└── 13. TROUBLESHOOTING & DEBUG GUIDE

📚 CROSS-REFERENCES:
Each section links to detailed files for deeper learning
Use this as your go-to reference during development
"""

# =============================================================================
# 1. DATA TYPES & TYPE SYSTEM - COMPLETE REFERENCE
# =============================================================================

"""
PYTHON'S BUILT-IN DATA TYPES HIERARCHY:
Master the foundation of all Python programming
"""

# Core Data Types with Examples
python_data_types = {
    "numeric_types": {
        "int": {
            "description": "Integer numbers (whole numbers)",
            "examples": [42, -17, 0, 1000000],
            "operations": ["arithmetic", "bitwise", "comparison"],
            "memory": "Variable size based on value",
            "range": "Unlimited precision"
        },
        "float": {
            "description": "Floating-point decimal numbers", 
            "examples": [3.14, -0.5, 1.0, 2.5e10],
            "operations": ["arithmetic", "comparison", "formatting"],
            "precision": "IEEE 754 double precision",
            "special_values": ["inf", "-inf", "nan"]
        },
        "complex": {
            "description": "Complex numbers with real and imaginary parts",
            "examples": ["3+4j", "1j", "complex(2, 3)"],
            "operations": ["arithmetic", "conjugate", "abs"],
            "use_cases": ["scientific computing", "signal processing"]
        }
    },
    
    "sequence_types": {
        "str": {
            "description": "Text strings (immutable sequence of characters)",
            "examples": ["'hello'", '"world"', "'''multiline'''"],
            "operations": ["concatenation", "slicing", "formatting", "methods"],
            "immutable": True,
            "encoding": "UTF-8 by default"
        },
        "list": {
            "description": "Ordered, mutable collection of items",
            "examples": ["[1, 2, 3]", "['a', 'b', 'c']", "[1, 'mix', 3.14]"],
            "operations": ["append", "extend", "insert", "remove", "sort"],
            "mutable": True,
            "indexing": "0-based, supports negative indices"
        },
        "tuple": {
            "description": "Ordered, immutable collection of items",
            "examples": ["(1, 2, 3)", "('a', 'b')", "(single,)"],
            "operations": ["indexing", "slicing", "unpacking"],
            "immutable": True,
            "use_cases": ["coordinates", "database records", "function returns"]
        }
    },
    
    "mapping_types": {
        "dict": {
            "description": "Key-value pairs (hash table/map)",
            "examples": ["{'a': 1, 'b': 2}", "{1: 'one', 2: 'two'}"],
            "operations": ["get", "set", "delete", "keys", "values", "items"],
            "mutable": True,
            "key_requirements": "Immutable types only"
        }
    },
    
    "set_types": {
        "set": {
            "description": "Unordered collection of unique items",
            "examples": ["{1, 2, 3}", "set(['a', 'b', 'c'])"],
            "operations": ["union", "intersection", "difference", "add", "remove"],
            "mutable": True,
            "duplicates": "Automatically removed"
        },
        "frozenset": {
            "description": "Immutable version of set",
            "examples": ["frozenset([1, 2, 3])", "frozenset('abc')"],
            "operations": ["union", "intersection", "difference"],
            "immutable": True,
            "use_cases": ["dictionary keys", "set elements"]
        }
    },
    
    "boolean_type": {
        "bool": {
            "description": "Boolean truth values",
            "values": [True, False],
            "operations": ["and", "or", "not"],
            "conversion": "Any object can be tested for truth",
            "falsy_values": [False, None, 0, "", [], {}, set()]
        }
    },
    
    "none_type": {
        "NoneType": {
            "description": "Represents absence of value",
            "value": None,
            "use_cases": ["default parameter", "uninitialized variable", "no return"],
            "comparison": "Use 'is None' not '== None'"
        }
    }
}

# Type Checking and Conversion Examples
def demonstrate_type_operations():
    """
    COMPREHENSIVE TYPE CHECKING AND CONVERSION EXAMPLES
    Essential patterns for type management in Python
    """
    
    # Type checking methods
    examples = [
        # Basic type checking
        ("type(42)", type(42), "Get exact type"),
        ("isinstance(42, int)", isinstance(42, int), "Check if instance of type"),
        ("isinstance(42, (int, float))", isinstance(42, (int, float)), "Check multiple types"),
        
        # Type conversion (casting)
        ("int('42')", int('42'), "String to integer"),
        ("float('3.14')", float('3.14'), "String to float"),
        ("str(42)", str(42), "Number to string"),
        ("bool(1)", bool(1), "Number to boolean"),
        ("list('abc')", list('abc'), "String to list"),
        ("tuple([1, 2, 3])", tuple([1, 2, 3]), "List to tuple"),
        ("set([1, 2, 2, 3])", set([1, 2, 2, 3]), "List to set (removes duplicates)"),
        ("dict([('a', 1), ('b', 2)])", dict([('a', 1), ('b', 2)]), "Pairs to dictionary"),
        
        # Advanced type operations
        ("hasattr([], 'append')", hasattr([], 'append'), "Check if object has attribute"),
        ("callable(print)", callable(print), "Check if object is callable"),
        ("len('hello')", len('hello'), "Get length of sequence")
    ]
    
    return examples

# =============================================================================
# 2. VARIABLES & NAMING CONVENTIONS - PROFESSIONAL STANDARDS
# =============================================================================

"""
COMPREHENSIVE VARIABLE MANAGEMENT GUIDE:
Professional naming, scoping, and best practices
"""

# Variable Assignment Patterns
variable_patterns = {
    "basic_assignment": {
        "single": "x = 42",
        "multiple": "a, b, c = 1, 2, 3",
        "unpacking": "first, *middle, last = [1, 2, 3, 4, 5]",
        "swap": "a, b = b, a"
    },
    
    "naming_conventions": {
        "snake_case": {
            "variables": "user_name, total_count, is_valid",
            "functions": "calculate_total(), get_user_info()",
            "modules": "data_processor.py, user_manager.py",
            "description": "Lowercase with underscores"
        },
        "UPPER_CASE": {
            "constants": "MAX_SIZE = 100, API_URL = 'https://...'",
            "description": "All uppercase for constants"
        },
        "CamelCase": {
            "classes": "UserAccount, DataProcessor, HTTPClient",
            "description": "Capital first letter, no underscores"
        },
        "private_convention": {
            "_single_underscore": "Internal use indicator",
            "__double_underscore": "Name mangling for classes",
            "__dunder__": "Special methods (magic methods)"
        }
    },
    
    "scope_rules": {
        "local": "Variables inside functions",
        "global": "Variables at module level",
        "builtin": "Python built-in names",
        "enclosing": "Variables in enclosing function (closures)",
        "legb_rule": "Local → Enclosing → Global → Built-in"
    }
}

# Professional Variable Examples
def demonstrate_variable_best_practices():
    """
    PROFESSIONAL VARIABLE USAGE PATTERNS
    Industry-standard approaches to variable management
    """
    
    # Good variable names (descriptive and clear)
    user_count = 150
    is_authenticated = True
    shopping_cart_items = []
    max_retry_attempts = 3
    
    # Constants (module-level)
    MAX_FILE_SIZE = 1024 * 1024  # 1MB
    DEFAULT_TIMEOUT = 30
    API_BASE_URL = "https://api.example.com"
    
    # Multiple assignment patterns
    x = y = z = 0  # Same value to multiple variables
    a, b = 10, 20  # Tuple unpacking
    first, *rest = [1, 2, 3, 4, 5]  # Extended unpacking
    
    # Type hints (Python 3.5+)
    name: str = "John"
    age: int = 25
    scores: list[int] = [95, 87, 92]
    
    # Context-aware naming
    for index, item in enumerate(shopping_cart_items):
        print(f"Item {index}: {item}")
    
    # Avoid these (poor naming)
    # x = "John"  # Not descriptive
    # data = []   # Too generic
    # temp = 42   # Unclear purpose
    
    return {
        "descriptive_names": True,
        "consistent_style": True,
        "type_hints": True,
        "clear_intent": True
    }

# =============================================================================
# 3. OPERATORS & PRECEDENCE - COMPLETE REFERENCE
# =============================================================================

"""
COMPREHENSIVE OPERATOR GUIDE:
All Python operators with precedence rules and examples
"""

operator_reference = {
    "arithmetic_operators": {
        "basic": {
            "+": {"name": "Addition", "example": "5 + 3 = 8", "types": "Numbers, strings, lists"},
            "-": {"name": "Subtraction", "example": "5 - 3 = 2", "types": "Numbers, sets"},
            "*": {"name": "Multiplication", "example": "5 * 3 = 15", "types": "Numbers, strings, lists"},
            "/": {"name": "Division", "example": "5 / 2 = 2.5", "types": "Numbers (always float result)"},
            "//": {"name": "Floor Division", "example": "5 // 2 = 2", "types": "Numbers (integer result)"},
            "%": {"name": "Modulo", "example": "5 % 3 = 2", "types": "Numbers (remainder)"},
            "**": {"name": "Exponentiation", "example": "5 ** 2 = 25", "types": "Numbers"}
        },
        "compound_assignment": {
            "+=": "x += 5  # Same as x = x + 5",
            "-=": "x -= 3  # Same as x = x - 3", 
            "*=": "x *= 2  # Same as x = x * 2",
            "/=": "x /= 4  # Same as x = x / 4",
            "//=": "x //= 3  # Same as x = x // 3",
            "%=": "x %= 7  # Same as x = x % 7",
            "**=": "x **= 2  # Same as x = x ** 2"
        }
    },
    
    "comparison_operators": {
        "equality": {
            "==": {"name": "Equal", "example": "5 == 5 → True", "note": "Value comparison"},
            "!=": {"name": "Not equal", "example": "5 != 3 → True", "note": "Value comparison"}
        },
        "ordering": {
            "<": {"name": "Less than", "example": "3 < 5 → True"},
            "<=": {"name": "Less or equal", "example": "5 <= 5 → True"},
            ">": {"name": "Greater than", "example": "5 > 3 → True"},
            ">=": {"name": "Greater or equal", "example": "5 >= 5 → True"}
        },
        "identity": {
            "is": {"name": "Identity", "example": "x is None", "note": "Object identity"},
            "is not": {"name": "Not identity", "example": "x is not None", "note": "Object identity"}
        },
        "membership": {
            "in": {"name": "Membership", "example": "'a' in 'apple' → True"},
            "not in": {"name": "Not membership", "example": "'z' not in 'apple' → True"}
        }
    },
    
    "logical_operators": {
        "and": {"name": "Logical AND", "example": "True and False → False", "short_circuit": True},
        "or": {"name": "Logical OR", "example": "True or False → True", "short_circuit": True},
        "not": {"name": "Logical NOT", "example": "not True → False", "unary": True}
    },
    
    "bitwise_operators": {
        "&": {"name": "Bitwise AND", "example": "5 & 3 → 1", "binary": "101 & 011 = 001"},
        "|": {"name": "Bitwise OR", "example": "5 | 3 → 7", "binary": "101 | 011 = 111"},
        "^": {"name": "Bitwise XOR", "example": "5 ^ 3 → 6", "binary": "101 ^ 011 = 110"},
        "~": {"name": "Bitwise NOT", "example": "~5 → -6", "note": "Two's complement"},
        "<<": {"name": "Left shift", "example": "5 << 1 → 10", "note": "Multiply by 2^n"},
        ">>": {"name": "Right shift", "example": "5 >> 1 → 2", "note": "Divide by 2^n"}
    }
}

# Operator Precedence (Highest to Lowest)
operator_precedence = [
    "() [] {} - Parentheses, brackets, braces",
    "** - Exponentiation (right-to-left)",
    "+x -x ~x - Unary plus, minus, bitwise NOT", 
    "* / // % - Multiplication, division, floor division, modulo",
    "+ - - Addition, subtraction",
    "<< >> - Bitwise shifts",
    "& - Bitwise AND",
    "^ - Bitwise XOR", 
    "| - Bitwise OR",
    "< <= > >= != == - Comparisons, identity, membership",
    "not - Logical NOT",
    "and - Logical AND",
    "or - Logical OR",
    "= += -= *= /= //= %= **= - Assignment operators"
]

def demonstrate_operator_precedence():
    """
    OPERATOR PRECEDENCE DEMONSTRATION
    Understanding order of operations in complex expressions
    """
    
    examples = [
        # Basic precedence
        ("2 + 3 * 4", 2 + 3 * 4, "Multiplication before addition: 2 + 12 = 14"),
        ("(2 + 3) * 4", (2 + 3) * 4, "Parentheses first: 5 * 4 = 20"),
        ("2 ** 3 ** 2", 2 ** 3 ** 2, "Exponentiation right-to-left: 2 ** 9 = 512"),
        
        # Comparison chains
        ("1 < 2 < 3", 1 < 2 < 3, "Chained comparisons: True and True = True"),
        ("1 < 2 > 0", 1 < 2 > 0, "Mixed comparisons: True and True = True"),
        
        # Logical operators
        ("True or False and False", True or False and False, "AND before OR: True or False = True"),
        ("not False or True", not False or True, "NOT before OR: True or True = True"),
        
        # Mixed operations
        ("5 > 3 and 2 + 2 == 4", 5 > 3 and 2 + 2 == 4, "Arithmetic, comparison, then logical"),
        ("x in [1, 2, 3] and x > 0", "Requires x value", "Membership and comparison")
    ]
    
    return examples

# =============================================================================
# 4. SYNTAX & CODE FORMATTING - PROFESSIONAL STANDARDS
# =============================================================================

"""
PYTHON SYNTAX RULES & STYLE GUIDE:
Write clean, readable, maintainable code
"""

python_syntax_rules = {
    "indentation": {
        "rule": "4 spaces per indentation level (PEP 8 standard)",
        "examples": {
            "correct": """
if condition:
    print("Indented with 4 spaces")
    if nested_condition:
        print("8 spaces for nested block")
            """,
            "avoid": """
if condition:
  print("2 spaces - not recommended") 
	print("Tabs - inconsistent")
            """
        },
        "tools": ["autopep8", "black", "editor auto-indent"]
    },
    
    "line_length": {
        "rule": "Maximum 79 characters per line (PEP 8)",
        "exceptions": "88-120 characters acceptable in modern development",
        "techniques": [
            "Parentheses for implicit line continuation",
            "Backslash for explicit continuation",
            "Break after operators",
            "Use multiple lines for complex expressions"
        ]
    },
    
    "naming_conventions": {
        "variables_functions": "snake_case (lowercase with underscores)",
        "classes": "CamelCase (capitalize each word)",
        "constants": "UPPER_CASE (all uppercase)", 
        "private": "_single_leading_underscore",
        "special": "__double_leading_and_trailing__"
    },
    
    "whitespace_rules": {
        "around_operators": "x = 1 + 2  # Spaces around operators",
        "after_commas": "a, b, c = 1, 2, 3  # Space after commas",
        "function_calls": "func(a, b)  # No space before parentheses", 
        "indexing": "list[0]  # No space before brackets",
        "keyword_arguments": "func(arg=value)  # No space around = in kwargs"
    }
}

def demonstrate_clean_syntax():
    """
    CLEAN CODE EXAMPLES
    Professional Python formatting and style
    """
    
    # Good formatting examples
    class DataProcessor:
        """Professional class with clean formatting."""
        
        MAX_ITEMS = 1000  # Constant in UPPER_CASE
        
        def __init__(self, data_source: str) -> None:
            """Initialize with type hints and docstring."""
            self.data_source = data_source
            self._processed_count = 0  # Private attribute
        
        def process_data(self, 
                        items: list[dict], 
                        batch_size: int = 100) -> list[dict]:
            """
            Process data in batches with proper parameter formatting.
            
            Args:
                items: List of data items to process
                batch_size: Number of items per batch
                
            Returns:
                List of processed items
            """
            processed_items = []
            
            for i in range(0, len(items), batch_size):
                batch = items[i:i + batch_size]
                
                # Complex expression with proper line breaking
                processed_batch = [
                    self._transform_item(item) 
                    for item in batch 
                    if self._is_valid_item(item)
                ]
                
                processed_items.extend(processed_batch)
                self._processed_count += len(processed_batch)
            
            return processed_items
        
        def _is_valid_item(self, item: dict) -> bool:
            """Private method with clear naming."""
            return (
                item is not None 
                and len(item) > 0 
                and 'required_field' in item
            )
        
        def _transform_item(self, item: dict) -> dict:
            """Transform single item with error handling."""
            try:
                return {
                    'id': item.get('id'),
                    'value': item.get('value', 0),
                    'processed': True
                }
            except (KeyError, TypeError) as e:
                logger.error(f"Error processing item {item}: {e}")
                return {'error': str(e), 'processed': False}

# =============================================================================
# 5. BOOLEAN LOGIC & TRUTH VALUES - COMPLETE GUIDE
# =============================================================================

"""
COMPREHENSIVE BOOLEAN OPERATIONS:
Master truth evaluation and logical operations
"""

boolean_reference = {
    "truth_values": {
        "truthy": {
            "description": "Values that evaluate to True in boolean context",
            "examples": [
                True, 1, -1, 0.1, "hello", [1], {'a': 1}, {1, 2}, 
                "any non-empty string", "any non-empty collection"
            ]
        },
        "falsy": {
            "description": "Values that evaluate to False in boolean context", 
            "examples": [
                False, 0, 0.0, 0j, "", [], {}, set(), None,
                "empty string", "empty collections", "zero numbers"
            ]
        }
    },
    
    "logical_operations": {
        "and_operator": {
            "behavior": "Returns first falsy value or last value if all truthy",
            "examples": [
                ("True and True", True),
                ("True and False", False),
                ("5 and 3", 3),  # Both truthy, returns last
                ("0 and 5", 0),  # First falsy, returns first
                ("'' and 'hello'", ''),  # First falsy
            ]
        },
        "or_operator": {
            "behavior": "Returns first truthy value or last value if all falsy",
            "examples": [
                ("True or False", True),
                ("False or True", True),
                ("5 or 3", 5),  # First truthy
                ("0 or 5", 5),  # First falsy, second truthy
                ("'' or 'hello'", 'hello'),  # First falsy, second truthy
                ("0 or ''", ''),  # All falsy, returns last
            ]
        },
        "not_operator": {
            "behavior": "Returns opposite boolean value",
            "examples": [
                ("not True", False),
                ("not False", True), 
                ("not 5", False),  # 5 is truthy
                ("not 0", True),   # 0 is falsy
                ("not []", True),  # Empty list is falsy
            ]
        }
    },
    
    "comparison_chains": {
        "description": "Python allows chaining comparisons",
        "examples": [
            "1 < 2 < 3  # Same as: (1 < 2) and (2 < 3)",
            "x == y == z  # All three equal",
            "a <= b <= c  # Ascending order check",
            "10 > x >= 0  # Range check"
        ]
    }
}

def demonstrate_boolean_patterns():
    """
    PRACTICAL BOOLEAN USAGE PATTERNS
    Real-world applications of boolean logic
    """
    
    # Default value patterns
    def get_user_name(name=None):
        return name or "Anonymous"  # Use default if name is falsy
    
    def safe_divide(a, b):
        return (b != 0) and (a / b)  # Avoid division by zero
    
    # Validation patterns
    def validate_user_data(data):
        return (
            data and  # Not None or empty
            isinstance(data, dict) and
            'name' in data and
            'email' in data and
            len(data['name']) > 0 and
            '@' in data['email']
        )
    
    # Short-circuit evaluation
    def expensive_operation():
        print("This expensive operation runs")
        return True
    
    # Won't run expensive_operation if first condition is False
    result = False and expensive_operation()
    
    # Conditional assignment
    status = "active" if user_count > 0 else "inactive"
    
    # Multiple conditions
    can_access = (
        user.is_authenticated and 
        user.has_permission('read') and
        not user.is_suspended
    )
    
    return {
        "default_values": get_user_name(),
        "safe_operations": safe_divide(10, 2), 
        "validation": validate_user_data({'name': 'John', 'email': 'john@example.com'}),
        "conditional": status,
        "access_control": "Depends on user object"
    }

# =============================================================================
# 6. KEYWORDS & CONTROL STRUCTURES - COMPLETE REFERENCE  
# =============================================================================

"""
PYTHON KEYWORDS AND CONTROL FLOW:
Master all reserved words and control structures
"""

python_keywords = {
    "conditional_keywords": {
        "if": "Execute block if condition is True",
        "elif": "Alternative condition (else if)", 
        "else": "Execute if no previous conditions were True"
    },
    
    "loop_keywords": {
        "for": "Iterate over sequence or iterable",
        "while": "Loop while condition is True", 
        "break": "Exit loop immediately",
        "continue": "Skip rest of current iteration",
        "else": "Execute after loop completes normally (no break)"
    },
    
    "function_keywords": {
        "def": "Define function",
        "return": "Return value from function",
        "yield": "Create generator function",
        "lambda": "Create anonymous function",
        "global": "Access global variable",
        "nonlocal": "Access enclosing scope variable"
    },
    
    "class_keywords": {
        "class": "Define class",
        "pass": "Empty placeholder block"
    },
    
    "exception_keywords": {
        "try": "Begin exception handling block",
        "except": "Handle specific exception",
        "finally": "Always execute block",
        "raise": "Raise exception",
        "assert": "Debug assertion"
    },
    
    "import_keywords": {
        "import": "Import module",
        "from": "Import specific items from module", 
        "as": "Create alias for import"
    },
    
    "logical_keywords": {
        "and": "Logical AND operator",
        "or": "Logical OR operator", 
        "not": "Logical NOT operator",
        "is": "Identity comparison",
        "in": "Membership test"
    },
    
    "literal_keywords": {
        "True": "Boolean true value",
        "False": "Boolean false value",
        "None": "Null/empty value"
    }
}

def demonstrate_control_structures():
    """
    COMPREHENSIVE CONTROL STRUCTURE EXAMPLES
    All Python control flow patterns with best practices
    """
    
    # Conditional statements
    def grade_classifier(score):
        """Demonstrate if/elif/else chains."""
        if score >= 90:
            return "A - Excellent"
        elif score >= 80:
            return "B - Good" 
        elif score >= 70:
            return "C - Satisfactory"
        elif score >= 60:
            return "D - Passing"
        else:
            return "F - Failing"
    
    # Loop patterns
    def demonstrate_loops():
        """Various loop patterns and best practices."""
        
        # For loop with range
        squares = []
        for i in range(1, 6):
            squares.append(i ** 2)
        
        # For loop with enumerate
        items = ['apple', 'banana', 'cherry']
        for index, item in enumerate(items):
            print(f"{index}: {item}")
        
        # While loop with condition
        count = 0
        while count < 5:
            print(f"Count: {count}")
            count += 1
        
        # Loop with else clause
        for i in range(3):
            if i == 10:  # This won't happen
                break
        else:
            print("Loop completed normally")
        
        # List comprehension (Pythonic loop)
        even_squares = [x**2 for x in range(10) if x % 2 == 0]
        
        return squares, even_squares
    
    # Exception handling
    def safe_file_operation(filename):
        """Demonstrate exception handling patterns."""
        try:
            with open(filename, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"File {filename} not found")
            return None
        except PermissionError:
            print(f"Permission denied for {filename}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
        finally:
            print("File operation completed")
    
    # Function definitions
    def advanced_function_example(required, default="default", *args, **kwargs):
        """
        Demonstrate advanced function features.
        
        Args:
            required: Required positional argument
            default: Optional argument with default value
            *args: Variable positional arguments
            **kwargs: Variable keyword arguments
        """
        result = {
            'required': required,
            'default': default,
            'args': args,
            'kwargs': kwargs
        }
        return result
    
    # Generator function
    def fibonacci_generator(n):
        """Generate Fibonacci sequence using yield."""
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    return {
        "grading": grade_classifier(85),
        "loops": demonstrate_loops(),
        "file_handling": "Requires filename",
        "function_call": advanced_function_example("test", extra="value"),
        "fibonacci": list(fibonacci_generator(10))
    }

# =============================================================================
# 7. NUMBERS & MATHEMATICAL OPERATIONS - ADVANCED GUIDE
# =============================================================================

"""
COMPREHENSIVE NUMERIC COMPUTING IN PYTHON:
Master all number types and mathematical operations
"""

numeric_reference = {
    "number_types_detailed": {
        "integers": {
            "range": "Unlimited precision (limited by memory)",
            "literals": ["42", "0b1010 (binary)", "0o52 (octal)", "0x2A (hex)"],
            "operations": ["arithmetic", "bitwise", "comparison"],
            "methods": ["bit_length()", "to_bytes()", "from_bytes()"]
        },
        "floats": {
            "precision": "IEEE 754 double precision (64-bit)",
            "range": "±1.7976931348623157e+308",
            "special": ["float('inf')", "float('-inf')", "float('nan')"],
            "methods": ["is_integer()", "as_integer_ratio()", "hex()"]
        },
        "complex": {
            "format": "real + imaginary*j",
            "creation": ["3+4j", "complex(3, 4)"],
            "attributes": [".real", ".imag", ".conjugate()"],
            "operations": ["arithmetic", "abs()", "phase calculation"]
        }
    },
    
    "mathematical_functions": {
        "built_in": {
            "abs()": "Absolute value or magnitude",
            "round()": "Round to n decimal places",
            "pow()": "Power with optional modulo",
            "divmod()": "Quotient and remainder",
            "min()": "Minimum value",
            "max()": "Maximum value",
            "sum()": "Sum of iterable"
        },
        "math_module": {
            "constants": ["math.pi", "math.e", "math.tau", "math.inf", "math.nan"],
            "power_log": ["sqrt()", "pow()", "log()", "log10()", "log2()"],
            "trigonometry": ["sin()", "cos()", "tan()", "asin()", "acos()", "atan()"],
            "hyperbolic": ["sinh()", "cosh()", "tanh()"],
            "special": ["factorial()", "gcd()", "lcm()", "isqrt()"]
        }
    }
}

def demonstrate_numeric_operations():
    """
    ADVANCED NUMERIC OPERATIONS AND PATTERNS
    Professional mathematical computing in Python
    """
    import math
    import decimal
    import fractions
    
    # Integer operations
    def integer_examples():
        """Comprehensive integer operation examples."""
        examples = [
            # Number base conversions
            ("Binary: bin(42)", bin(42)),
            ("Octal: oct(42)", oct(42)), 
            ("Hex: hex(42)", hex(42)),
            ("From binary: int('1010', 2)", int('1010', 2)),
            
            # Bitwise operations
            ("Bit count: (42).bit_count()", (42).bit_count() if hasattr(42, 'bit_count') else "N/A"),
            ("Bit length: (42).bit_length()", (42).bit_length()),
            
            # Large number handling
            ("Large number: 10**100", 10**100),
            ("Factorial 20: math.factorial(20)", math.factorial(20))
        ]
        return examples
    
    # Float precision and special values
    def float_examples():
        """Float precision and special value handling."""
        examples = [
            # Precision examples
            ("0.1 + 0.2", 0.1 + 0.2),  # Famous floating point issue
            ("round(0.1 + 0.2, 10)", round(0.1 + 0.2, 10)),
            
            # Special values
            ("Infinity: float('inf')", float('inf')),
            ("Negative infinity: float('-inf')", float('-inf')),
            ("Not a number: float('nan')", float('nan')),
            ("Is finite: math.isfinite(3.14)", math.isfinite(3.14)),
            ("Is NaN: math.isnan(float('nan'))", math.isnan(float('nan'))),
            
            # Float methods
            ("(3.14).is_integer()", (3.14).is_integer()),
            ("(3.0).is_integer()", (3.0).is_integer()),
            ("(3.14).as_integer_ratio()", (3.14).as_integer_ratio())
        ]
        return examples
    
    # Complex number operations
    def complex_examples():
        """Complex number operations and applications."""
        z1 = 3 + 4j
        z2 = 1 - 2j
        
        examples = [
            ("Complex creation: 3+4j", z1),
            ("Real part: z1.real", z1.real),
            ("Imaginary part: z1.imag", z1.imag),
            ("Magnitude: abs(z1)", abs(z1)),
            ("Conjugate: z1.conjugate()", z1.conjugate()),
            ("Addition: z1 + z2", z1 + z2),
            ("Multiplication: z1 * z2", z1 * z2),
            ("Phase: cmath.phase(z1)", "import cmath; cmath.phase(z1)")
        ]
        return examples
    
    # High precision arithmetic
    def precision_examples():
        """High precision and exact arithmetic."""
        # Decimal for exact decimal arithmetic
        decimal.getcontext().prec = 50
        d1 = decimal.Decimal('0.1')
        d2 = decimal.Decimal('0.2')
        
        # Fractions for exact rational arithmetic
        f1 = fractions.Fraction(1, 3)
        f2 = fractions.Fraction(2, 5)
        
        examples = [
            ("Exact decimal: Decimal('0.1') + Decimal('0.2')", d1 + d2),
            ("Fraction: Fraction(1, 3) + Fraction(2, 5)", f1 + f2),
            ("Fraction from float: Fraction(0.25)", fractions.Fraction(0.25)),
            ("Limit denominator: Fraction(3.14159).limit_denominator(1000)", 
             fractions.Fraction(3.14159).limit_denominator(1000))
        ]
        return examples
    
    return {
        "integers": integer_examples(),
        "floats": float_examples(),
        "complex": complex_examples(),
        "precision": precision_examples()
    }

# =============================================================================
# QUICK REFERENCE SUMMARY - MEMORIZE THESE!
# =============================================================================

"""
PYTHON FUNDAMENTALS CHEAT SHEET - ESSENTIAL PATTERNS

DATA TYPES:
int, float, complex, str, list, tuple, dict, set, bool, None

TYPE CHECKING:
type(obj)           # Get exact type
isinstance(obj, type) # Check if instance of type
bool(obj)           # Convert to boolean

VARIABLES:
snake_case for variables/functions
CamelCase for classes  
UPPER_CASE for constants
_private for internal use

OPERATORS:
== != < > <= >=     # Comparison
and or not          # Logical  
+ - * / // % **     # Arithmetic
is, is not          # Identity
in, not in          # Membership

CONTROL FLOW:
if condition:       # Conditional
    pass
for item in seq:    # Iteration
    continue/break
while condition:    # While loop
    pass
try/except/finally  # Exception handling

FUNCTIONS:
def func(arg, default=None, *args, **kwargs):
    return result

COLLECTIONS:
list = [1, 2, 3]           # Mutable, ordered
tuple = (1, 2, 3)          # Immutable, ordered  
dict = {'a': 1, 'b': 2}    # Key-value pairs
set = {1, 2, 3}            # Unique items
"""

# ----------

""" 1. DATA TYPES & TYPE CHECKING """
# 📖 Detailed guide: 3.1.0_Python_DATA_TYPES.py

# Basic Data Types
data_type_examples = {
    "int": 42,                    # <class 'int'>
    "float": 3.14,               # <class 'float'>
    "str": "Hello",              # <class 'str'>
    "bool": True,                # <class 'bool'>
    "list": [1, 2, 3],          # <class 'list'>
    "tuple": (1, 2, 3),         # <class 'tuple'>
    "dict": {"key": "value"},    # <class 'dict'>
    "set": {1, 2, 3},           # <class 'set'>
    "NoneType": None            # <class 'NoneType'>
}

# Type Checking
x = 42
print(type(x))          # <class 'int'>
print(isinstance(x, int))  # True

# Type Conversion
int("123")      # String to integer
float(42)       # Integer to float  
str(123)        # Number to string
bool(1)         # Any value to boolean
# ----------

""" 2. VARIABLES & NAMING """
# 📖 Detailed guide: 3.4.0_Python_VARIABLES.py

# Variable Creation (No declaration needed)
name = "Alice"
age = 25
is_active = True

# Multiple Assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Naming Rules
valid_names = [
    "variable_name",    # Snake case (preferred)
    "variableName",     # Camel case  
    "_private_var",     # Private indication
    "CONSTANT_VALUE",   # Constants (uppercase)
    "var123",          # Numbers allowed (not first)
]

# Invalid Names (will cause SyntaxError)
# 123var, my-var, class, for, if

# Scope Levels
global_var = "Accessible everywhere"

def function_scope():
    local_var = "Only in this function"
    global global_var
    global_var = "Modified global"

# ----------

""" 3. OPERATORS & PRECEDENCE """
# 📖 Detailed guide: 3.2.0_Python_OPERATORS.py

# Arithmetic Operators (highest precedence)
x = 10; y = 3
print(x + y)    # Addition: 13
print(x - y)    # Subtraction: 7
print(x * y)    # Multiplication: 30
print(x / y)    # Division: 3.333...
print(x // y)   # Floor division: 3
print(x % y)    # Modulus: 1
print(x ** y)   # Exponentiation: 1000

# Comparison Operators
print(x == y)   # Equal: False
print(x != y)   # Not equal: True
print(x > y)    # Greater than: True
print(x < y)    # Less than: False
print(x >= y)   # Greater or equal: True
print(x <= y)   # Less or equal: False

# Logical Operators
a = True; b = False
print(a and b)  # False (both must be true)
print(a or b)   # True (at least one true)
print(not a)    # False (opposite)

# Assignment Operators
x += 5      # x = x + 5
x -= 3      # x = x - 3  
x *= 2      # x = x * 2
x /= 4      # x = x / 4

# Identity & Membership
print(x is y)           # Same object?
print("a" in "abc")     # Contains?

# Operator Precedence (high to low)
# 1. ** (exponentiation)
# 2. *, /, //, % (multiplication, division)
# 3. +, - (addition, subtraction)
# 4. ==, !=, <, >, <=, >= (comparison)
# 5. not (logical NOT)
# 6. and (logical AND)
# 7. or (logical OR)

# ----------

""" 4. SYNTAX & FORMATTING """
# 📖 Detailed guide: 3.3.0_Python_SYNTAX.py

# Indentation (4 spaces is standard)
if True:
    print("Properly indented")      # 4 spaces
    if True:
        print("Nested indentation") # 8 spaces

# Comments
# Single line comment
"""
Multi-line comment
or docstring
"""

# Line Continuation
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Or use parentheses (preferred)
total = (1 + 2 + 3 +
         4 + 5 + 6)

# Naming Conventions
class MyClass:          # PascalCase for classes
    def my_method(self): # snake_case for functions
        pass

MY_CONSTANT = 42        # UPPERCASE for constants
my_variable = "value"   # snake_case for variables

# ----------

""" 5. BOOLEAN LOGIC & TRUTH VALUES """
# 📖 Detailed guide: 3.6.0_Python_BOOLEANS.py

# Boolean Values
True    # Boolean true
False   # Boolean false

# Truthy Values (evaluate to True)
truthy_values = [
    True, 1, -1, 3.14, "hello", [1, 2, 3], 
    {"key": "value"}, {1, 2, 3}, (1, 2)
]

# Falsy Values (evaluate to False)
falsy_values = [
    False, 0, 0.0, "", [], {}, set(), None
]

# Boolean Operations
result = bool(5)        # True
result = not False      # True  
result = True and False # False
result = True or False  # True

# Short-circuit Evaluation
# result = False and expensive_function()  # expensive_function() not called
# result = True or expensive_function()    # expensive_function() not called

# Comparison Chains
x = 5
result = 1 < x < 10     # True (equivalent to 1 < x and x < 10)

# ----------

""" 6. KEYWORDS & CONTROL FLOW """
# 📖 Detailed guide: 3.5.0_Python_KEY_WORDS.py

# Python Keywords (35 reserved words)
python_keywords = [
    'False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert',
    'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
    'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
]

# Control Flow Examples
# Conditional
# if condition:
#     pass
# elif other_condition:
#     pass
# else:
#     pass

# Loops
# for item in collection:
#     if skip_condition:
#         continue    # Skip this iteration
#     if exit_condition:
#         break      # Exit loop
# else:
#     pass           # Executes if loop completes normally

# while condition:
#     pass

# Exception Handling
# try:
#     risky_operation()
# except SpecificError:
#     handle_specific_error()
# except Exception as e:
#     handle_general_error(e)
# finally:
#     cleanup_code()

# ----------

""" 7. NUMBERS & ARITHMETIC """
# 📖 Detailed guide: 3.7.0_Python_NUMBERS.py

# Number Types
integer = 42
floating_point = 3.14159
complex_number = 3 + 4j

# Common Operations
result = abs(-5)        # Absolute value: 5
result = round(3.7)     # Rounding: 4
result = pow(2, 3)      # Power: 8
result = divmod(17, 5)  # Division and modulus: (3, 2)

# Built-in Math Functions
numbers = [1, 5, 3, 9, 2]
result = sum(numbers)   # Sum: 20
result = min(numbers)   # Minimum: 1
result = max(numbers)   # Maximum: 9

# Mathematical Constants (import math)
# import math
# pi = math.pi           # 3.14159...
# e = math.e             # 2.71828...

# ----------

""" 8. STRINGS & TEXT """
# 📖 Detailed guide: 3.11.0_Python_TEXT.py

# String Creation
single_quotes = 'Hello World'
double_quotes = "Hello World"
triple_quotes = """Multi-line
string content"""

# String Operations
text = "Hello"
result = text + " World"        # Concatenation: "Hello World"
result = text * 3               # Repetition: "HelloHelloHello"
result = len(text)              # Length: 5
result = "e" in text            # Membership: True

# String Methods (commonly used)
text = "  Hello World  "
result = text.strip()           # Remove whitespace: "Hello World"
result = text.lower()           # Lowercase: "  hello world  "
result = text.upper()           # Uppercase: "  HELLO WORLD  "
result = text.replace("World", "Python")  # Replace: "  Hello Python  "
result = text.split()           # Split into list: ["Hello", "World"]

# String Formatting
name = "Alice"
age = 30
# f-strings (Python 3.6+)
message = f"Hi {name}, you are {age} years old"
# format() method
message = "Hi {}, you are {} years old".format(name, age)
# % formatting (older style)
message = "Hi %s, you are %d years old" % (name, age)

# Escape Sequences
escaped_text = "Line 1\nLine 2\tTabbed"
raw_string = r"C:\new\folder"   # Raw string (no escaping)

# ----------

""" 9. LISTS & COLLECTIONS """
# 📖 Detailed guide: 3.8.0_Python_LIST.py

# List Creation
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List Operations
numbers.append(6)               # Add to end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)            # Insert at position: [0, 1, 2, 3, 4, 5, 6]
removed = numbers.pop()         # Remove last: 6
numbers.remove(0)               # Remove by value: [1, 2, 3, 4, 5]
numbers.extend([6, 7, 8])       # Add multiple: [1, 2, 3, 4, 5, 6, 7, 8]

# List Properties
length = len(numbers)           # Count items
is_present = 3 in numbers      # Check membership
position = numbers.index(3)    # Find position
count = numbers.count(1)       # Count occurrences

# List Slicing (see section 11)
subset = numbers[1:4]          # Elements 1, 2, 3
reversed_list = numbers[::-1]  # Reverse order

# List Comprehension
squares = [x**2 for x in range(5)]     # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# ----------

""" 10. ARRAYS & MEMORY EFFICIENCY """
# 📖 Detailed guide: 3.9.0_Python_ARRAYS.py

# Array Module (for memory efficiency)
# import array

# Array Creation (all elements same type)
# int_array = array.array('i', [1, 2, 3, 4, 5])     # Integer array
# float_array = array.array('f', [1.1, 2.2, 3.3])   # Float array

# Type Codes
array_types = {
    'b': 'signed char',    'B': 'unsigned char',
    'h': 'signed short',   'H': 'unsigned short',  
    'i': 'signed int',     'I': 'unsigned int',
    'l': 'signed long',    'L': 'unsigned long',
    'f': 'float',          'd': 'double'
}

# Array vs List
# Arrays: Same type, memory efficient, fewer methods
# Lists: Mixed types, flexible, more methods, easier to use

# When to Use Arrays
# ✅ Large amounts of numeric data
# ✅ Memory optimization needed  
# ✅ Interfacing with C code
# ❌ Mixed data types needed
# ❌ Flexibility more important than memory

# ----------

""" 11. INDEXING & SLICING """
# 📖 Detailed guide: 3.10.0_Python_INDEX.py

# Sample Data
text = "Hello World"
numbers = [0, 1, 2, 3, 4, 5]

# Positive Indexing (left to right)
first = text[0]         # 'H' (first character)
second = numbers[1]     # 1 (second element)

# Negative Indexing (right to left)
last = text[-1]         # 'd' (last character)
second_last = numbers[-2]  # 4 (second to last)

# Slicing [start:stop:step]
substring = text[0:5]      # "Hello" (characters 0-4)
subset = numbers[1:4]      # [1, 2, 3] (elements 1-3)
every_other = numbers[::2] # [0, 2, 4] (every 2nd element)
reversed_slice = text[::-1] # "dlroW olleH" (reversed)

# Common Slicing Patterns
first_three = numbers[:3]      # [0, 1, 2] (first 3)
last_three = numbers[-3:]     # [3, 4, 5] (last 3)
middle = numbers[1:-1]        # [1, 2, 3, 4] (exclude first & last)
copy = numbers[:]             # [0, 1, 2, 3, 4, 5] (full copy)

# Slice Assignment (lists only)
# numbers[1:3] = [10, 20]       # Replace elements: [0, 10, 20, 3, 4, 5]
# numbers[::2] = [100, 200, 300] # Replace every 2nd: [100, 10, 200, 3, 300, 5]

# ----------

""" 12. COMMON PATTERNS & BEST PRACTICES """

# 🎯 IDIOMS & PATTERNS

# Check if variable exists and has value
# if variable_name:  # Pythonic way
#     do_something()

# Swap variables
a, b = b, a

# Multiple conditions
# if value in (1, 2, 3, 4, 5):  # More efficient than multiple 'or'
#     process_value()

# Default values with 'or'
# name = user_input or "Anonymous"

# Enumerate for index and value
# for index, value in enumerate(items):
#     print(f"{index}: {value}")

# Dictionary get with default
# value = my_dict.get('key', 'default_value')

# List comprehensions vs loops
# Good: squares = [x**2 for x in range(10)]
# Avoid: squares = []; [squares.append(x**2) for x in range(10)]

# String joining
# Good: result = ', '.join(items)
# Avoid: result = ''; [result += item + ', ' for item in items]

# 🚫 COMMON MISTAKES TO AVOID

# Mutable default arguments
# def bad_function(items=[]):  # DON'T DO THIS
#     items.append("new")
#     return items

# def good_function(items=None):  # DO THIS INSTEAD
#     if items is None:
#         items = []
#     items.append("new")
#     return items

# Modifying list while iterating
# numbers = [1, 2, 3, 4, 5]
# Bad
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # Can skip elements

# Good
# numbers = [num for num in numbers if num % 2 != 0]

# Late binding closure
# Bad
# functions = [lambda: i for i in range(3)]  # All return 2

# Good  
# functions = [lambda x=i: x for i in range(3)]  # Returns 0, 1, 2

# 🔧 PERFORMANCE TIPS

# Use 'in' for membership testing
# if item in large_list:  # O(n) for lists
#     pass

# if item in large_set:   # O(1) for sets - much faster!
#     pass

# String concatenation
# Slow for many strings
# result = ""
# for item in items:
#     result += str(item)  # Creates new string each time

# Fast for many strings
# result = "".join(str(item) for item in items)

# List vs Generator for memory
# Memory intensive
# squares = [x**2 for x in range(1000000)]

# Memory efficient
# squares = (x**2 for x in range(1000000))

# ----------

""" QUICK DEBUGGING CHECKLIST """

debug_checklist = [
    "✅ Check indentation (4 spaces, consistent)",
    "✅ Check parentheses/brackets balance",
    "✅ Check variable names (no typos)",
    "✅ Check data types (int vs str vs float)",
    "✅ Check list bounds (IndexError)",
    "✅ Check dictionary keys (KeyError)",
    "✅ Check None values before operations",
    "✅ Check division by zero",
    "✅ Check import statements",
    "✅ Check function return statements"
]

# ----------

""" HELPFUL BUILT-IN FUNCTIONS """

debugging_functions = {
    "type(obj)": "Check object type",
    "len(obj)": "Get length/count",
    "dir(obj)": "List object attributes/methods", 
    "help(obj)": "Get documentation",
    "id(obj)": "Get object memory address",
    "vars(obj)": "Get object's __dict__",
    "isinstance(obj, type)": "Check if object is instance of type",
    "hasattr(obj, 'attr')": "Check if object has attribute",
    "getattr(obj, 'attr', default)": "Get attribute with default",
    "callable(obj)": "Check if object is callable"
}

# ----------

print("🐍 Python Quick Reference Guide Loaded!")
print("📖 Use Ctrl+F to find any topic quickly")
print("🔍 Check the detailed guides for deeper learning:")
for i in range(1, 12):
    print(f"   • 3.{i}.0_Python_[TOPIC].py")
print("📋 See 3.0.1_Python_CONTENTS_INDEX.py for study paths")

# ----------

""" KEYBOARD SHORTCUTS REMINDER """
# While coding, remember these PyCharm/VS Code shortcuts:
# Ctrl+D        → Duplicate line
# Ctrl+/        → Comment/uncomment
# Ctrl+Shift+F  → Format code
# F2            → Rename variable everywhere
# Ctrl+Click    → Go to definition

# ----------