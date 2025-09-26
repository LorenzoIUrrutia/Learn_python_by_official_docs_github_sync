""" 3.4.0_Python_VARIABLES.py """

# =============================================================================
# PYTHON VARIABLES - COMPLETE MASTERY GUIDE
# =============================================================================
# Version: 3.4.0 | Educational Excellence Target: 9.5/10
# Purpose: Master Python variables with professional programming standards
# Target: Beginner to Advanced Python programmers
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python variables, you will:
✓ Understand variable creation, assignment, and memory management
✓ Master naming conventions and best practices
✓ Apply type systems, annotations, and dynamic typing
✓ Use scope, lifetime, and namespace concepts effectively
✓ Handle multiple assignments and unpacking operations
✓ Implement advanced variable patterns and techniques

🚀 QUICK NAVIGATION:
├── 1. VARIABLE FUNDAMENTALS (FOUNDATION)
├── 2. NAMING CONVENTIONS & RULES (STANDARDS)
├── 3. VARIABLE ASSIGNMENT PATTERNS (OPERATIONS)
├── 4. TYPE SYSTEM & ANNOTATIONS (TYPES)
├── 5. SCOPE & NAMESPACE MANAGEMENT (STRUCTURE)
├── 6. MEMORY & PERFORMANCE OPTIMIZATION
├── 7. ADVANCED VARIABLE TECHNIQUES
├── 8. VARIABLE VALIDATION & SAFETY
├── 9. BEST PRACTICES & PATTERNS
└── 10. REAL-WORLD VARIABLE APPLICATIONS

🔍 CORE CONCEPT:
Variables are named references to memory locations that store data values.
Python uses dynamic typing and automatic memory management.
"""

# =============================================================================
# 1. VARIABLE FUNDAMENTALS - FOUNDATION CONCEPTS
# =============================================================================

"""
PYTHON VARIABLE SYSTEM:
Understanding the core mechanics of Python variables
"""

def demonstrate_variable_fundamentals():
    """
    COMPREHENSIVE VARIABLE FUNDAMENTALS
    Core concepts and mechanisms of Python variables
    """
    
    # Variable creation and assignment fundamentals
    variable_basics = {
        "definition": "Named reference to memory location storing data",
        "dynamic_typing": "Type determined at runtime, can change",
        "automatic_memory": "Garbage collection handles memory management",
        "reference_semantics": "Variables are references, not containers"
    }
    
    # Basic variable creation examples
    print("=== BASIC VARIABLE CREATION ===")
    
    # Simple assignments
    integer_variable = 42
    string_variable = "Hello, Python!"
    float_variable = 3.14159
    boolean_variable = True
    none_variable = None
    
    # Python's dynamic typing in action
    dynamic_example = 100         # Initially an integer
    print(f"Initial type: {type(dynamic_example)} = {dynamic_example}")
    
    dynamic_example = "Now a string"  # Changed to string
    print(f"Changed type: {type(dynamic_example)} = {dynamic_example}")
    
    dynamic_example = [1, 2, 3, 4]   # Now a list
    print(f"Changed type: {type(dynamic_example)} = {dynamic_example}")
    
    # Memory address and object identity
    print("\n=== MEMORY AND IDENTITY ===")
    
    # Demonstrating object identity
    x = 1000
    y = 1000
    print(f"x id: {id(x)}, y id: {id(y)}")
    print(f"x is y: {x is y}")  # May be False for large numbers
    
    # Small integers are cached (singleton pattern)
    a = 5
    b = 5
    print(f"a id: {id(a)}, b id: {id(b)}")
    print(f"a is b: {a is b}")  # True for small integers
    
    # String interning example
    str1 = "hello"
    str2 = "hello"
    print(f"str1 is str2: {str1 is str2}")  # True for simple strings
    
    # Mutable vs Immutable objects
    print("\n=== MUTABLE VS IMMUTABLE ===")
    
    # Immutable objects (int, str, tuple)
    immutable_demo = 10
    print(f"Before: immutable_demo = {immutable_demo}, id = {id(immutable_demo)}")
    immutable_demo += 5  # Creates new object
    print(f"After: immutable_demo = {immutable_demo}, id = {id(immutable_demo)}")
    
    # Mutable objects (list, dict, set)
    mutable_demo = [1, 2, 3]
    print(f"Before: mutable_demo = {mutable_demo}, id = {id(mutable_demo)}")
    mutable_demo.append(4)  # Modifies existing object
    print(f"After: mutable_demo = {mutable_demo}, id = {id(mutable_demo)}")
    
    # Reference vs Value semantics
    print("\n=== REFERENCE SEMANTICS ===")
    
    # Immutable reference example
    original_number = 100
    copied_number = original_number  # Both reference same object
    copied_number = 200  # Creates new object, original unchanged
    print(f"original_number: {original_number}, copied_number: {copied_number}")
    
    # Mutable reference example
    original_list = [1, 2, 3]
    referenced_list = original_list  # Both reference same object
    referenced_list.append(4)  # Modifies shared object
    print(f"original_list: {original_list}, referenced_list: {referenced_list}")
    
    # Creating independent copy
    independent_list = original_list.copy()  # Shallow copy
    independent_list.append(5)
    print(f"original_list: {original_list}, independent_list: {independent_list}")
    
    # Variable deletion and garbage collection
    print("\n=== VARIABLE DELETION ===")
    
    temp_variable = "This will be deleted"
    print(f"temp_variable exists: {'temp_variable' in locals()}")
    
    del temp_variable  # Remove variable from namespace
    # print(temp_variable)  # Would raise NameError
    print(f"temp_variable exists: {'temp_variable' in locals()}")
    
    # Garbage collection example
    import gc
    
    # Create circular reference
    class Node:
        def __init__(self, value):
            self.value = value
            self.refs = []
    
    node1 = Node("first")
    node2 = Node("second")
    node1.refs.append(node2)
    node2.refs.append(node1)  # Circular reference
    
    # Delete references
    del node1, node2
    
    # Force garbage collection
    collected = gc.collect()
    print(f"Objects collected: {collected}")
    
    return {
        'basics': variable_basics,
        'examples': {
            'integer': integer_variable,
            'string': string_variable,
            'float': float_variable,
            'boolean': boolean_variable,
            'none': none_variable
        },
        'memory_info': {
            'gc_stats': gc.get_stats(),
            'reference_count_demo': "Completed successfully"
        }
    }

# =============================================================================
# 2. NAMING CONVENTIONS & RULES - PROFESSIONAL STANDARDS
# =============================================================================

"""
VARIABLE NAMING MASTERY:
Professional naming conventions and standards
"""

def demonstrate_naming_conventions():
    """
    COMPREHENSIVE NAMING CONVENTIONS
    Professional variable naming standards and patterns
    """
    
    # Core naming rules
    naming_rules = {
        "must_start_with": "Letter (a-z, A-Z) or underscore (_)",
        "can_contain": "Letters, digits (0-9), underscores",
        "cannot_start_with": "Digit (0-9)",
        "case_sensitive": "age, Age, AGE are different variables",
        "cannot_be": "Python keywords or built-in names",
        "length_limit": "No limit, but keep reasonable for readability"
    }
    
    # Python keywords (reserved names)
    import keyword
    python_keywords = keyword.kwlist
    print(f"Python keywords ({len(python_keywords)}): {python_keywords}")
    
    # Built-in names to avoid shadowing
    import builtins
    builtin_names = [name for name in dir(builtins) if not name.startswith('_')]
    print(f"Built-in names to avoid: {builtin_names[:10]}... (showing first 10)")
    
    # Professional naming conventions
    print("\n=== PROFESSIONAL NAMING CONVENTIONS ===")
    
    # 1. Snake Case (Recommended for variables and functions)
    user_name = "john_doe"
    user_age = 30
    is_user_active = True
    max_retry_attempts = 3
    database_connection_string = "postgresql://localhost:5432/db"
    
    # 2. Camel Case (Common in some contexts, but not PEP 8 standard)
    userName = "john_doe"  # Not recommended in Python
    userAge = 30           # Not recommended in Python
    
    # 3. Pascal Case (Used for classes, not variables)
    # UserAccount = "Not for variables"  # This would be confusing
    
    # 4. Constants (UPPER_SNAKE_CASE)
    MAX_FILE_SIZE_MB = 100
    DEFAULT_TIMEOUT_SECONDS = 30
    API_BASE_URL = "https://api.example.com"
    SUPPORTED_FILE_EXTENSIONS = ('.txt', '.csv', '.json')
    
    # Descriptive naming examples
    print("\n=== DESCRIPTIVE NAMING PATTERNS ===")
    
    # Good variable names (clear and descriptive)
    customer_email_address = "user@example.com"
    total_order_amount = 299.99
    is_payment_successful = True
    user_registration_timestamp = 1672531200
    database_query_result_count = 150
    
    # Context-specific naming
    # In a web application context
    http_status_code = 200
    request_headers = {"Content-Type": "application/json"}
    response_body_size_bytes = 1024
    
    # In a data science context
    training_data_features = ['age', 'income', 'education']
    model_accuracy_score = 0.95
    cross_validation_fold_count = 5
    
    # In a game development context
    player_health_points = 100
    enemy_damage_per_second = 25
    game_level_completion_percentage = 75.5
    
    # Boolean variable naming patterns
    print("\n=== BOOLEAN NAMING PATTERNS ===")
    
    # Use 'is_' prefix for state checks
    is_user_authenticated = True
    is_file_exists = False
    is_data_valid = True
    is_connection_active = False
    
    # Use 'has_' prefix for possession checks
    has_admin_privileges = True
    has_required_permissions = False
    has_valid_email = True
    has_pending_notifications = False
    
    # Use 'can_' prefix for capability checks
    can_edit_document = True
    can_delete_record = False
    can_access_admin_panel = True
    can_modify_settings = False
    
    # Use 'should_' prefix for recommendation flags
    should_send_notification = True
    should_cache_result = False
    should_retry_operation = True
    should_log_error = False
    
    # Collection and container naming
    print("\n=== COLLECTION NAMING PATTERNS ===")
    
    # Use plural for collections
    user_accounts = ["user1", "user2", "user3"]
    product_categories = ["electronics", "clothing", "books"]
    error_messages = ["Invalid input", "Connection failed"]
    
    # Use descriptive container names
    active_user_sessions = {"user1": "session123", "user2": "session456"}
    product_price_lookup = {"laptop": 999.99, "mouse": 29.99}
    configuration_settings = {"debug": True, "port": 8080}
    
    # Use specific naming for different collection types
    user_id_list = [1, 2, 3, 4, 5]
    user_data_dict = {"id": 1, "name": "John"}
    unique_tags_set = {"python", "programming", "tutorial"}
    coordinates_tuple = (10.5, 20.3)
    
    # Temporary and counter variables
    print("\n=== TEMPORARY AND COUNTER VARIABLES ===")
    
    # Acceptable short names for limited scope
    for index in range(5):
        temp_value = index * 2
        print(f"Index: {index}, Temp: {temp_value}")
    
    # Loop variables with clear purpose
    for user_index, user_data in enumerate(user_accounts):
        print(f"Processing user {user_index}: {user_data}")
    
    # Counter variables
    successful_operations_count = 0
    failed_attempts_counter = 0
    processed_items_total = 0
    
    # Private and internal variables
    print("\n=== PRIVATE AND INTERNAL VARIABLES ===")
    
    # Single underscore prefix (convention for internal use)
    _internal_cache = {}
    _temporary_storage = []
    _debug_mode = True
    
    # Double underscore prefix (name mangling in classes)
    # __private_key = "secret"  # Would be mangled in class context
    
    # Variable naming anti-patterns (what NOT to do)
    print("\n=== NAMING ANTI-PATTERNS (AVOID THESE) ===")
    
    # Too short and unclear
    # x = "user@example.com"  # What does x represent?
    # n = 42                  # What count or number is this?
    # flag = True             # What kind of flag?
    
    # Too long and verbose
    # extremely_long_variable_name_that_describes_everything_in_detail = "value"
    
    # Misleading names
    # count = "not a number"  # Name suggests integer, but holds string
    # is_valid = "maybe"      # Boolean name but holds string
    
    # Using reserved words (would cause errors)
    # class = "MyClass"       # 'class' is a keyword
    # def = "function name"   # 'def' is a keyword
    
    # Hungarian notation (not Pythonic)
    # strUserName = "john"    # Type prefix not recommended
    # intCount = 42           # Type prefix not recommended
    
    return {
        'naming_rules': naming_rules,
        'python_keywords': python_keywords,
        'builtin_names_sample': builtin_names[:20],
        'examples': {
            'snake_case': {
                'user_name': user_name,
                'user_age': user_age,
                'is_user_active': is_user_active
            },
            'constants': {
                'MAX_FILE_SIZE_MB': MAX_FILE_SIZE_MB,
                'DEFAULT_TIMEOUT_SECONDS': DEFAULT_TIMEOUT_SECONDS,
                'API_BASE_URL': API_BASE_URL
            },
            'booleans': {
                'is_user_authenticated': is_user_authenticated,
                'has_admin_privileges': has_admin_privileges,
                'can_edit_document': can_edit_document,
                'should_send_notification': should_send_notification
            },
            'collections': {
                'user_accounts': user_accounts,
                'product_categories': product_categories,
                'user_data_dict': user_data_dict
            }
        }
    }

# =============================================================================
# 3. VARIABLE ASSIGNMENT PATTERNS - ADVANCED OPERATIONS
# =============================================================================

"""
ASSIGNMENT PATTERN MASTERY:
Advanced variable assignment techniques and patterns
"""

def demonstrate_assignment_patterns():
    """
    COMPREHENSIVE ASSIGNMENT PATTERNS
    Advanced techniques for variable assignment and manipulation
    """
    
    # Basic assignment patterns
    print("=== BASIC ASSIGNMENT PATTERNS ===")
    
    # Single assignment
    single_value = 42
    
    # Multiple assignment (parallel assignment)
    x, y, z = 1, 2, 3
    print(f"Multiple assignment: x={x}, y={y}, z={z}")
    
    # Chained assignment
    a = b = c = "same value"
    print(f"Chained assignment: a={a}, b={b}, c={c}")
    
    # Augmented assignment operators
    print("\n=== AUGMENTED ASSIGNMENT OPERATORS ===")
    
    # Arithmetic augmented assignment
    counter = 10
    counter += 5    # counter = counter + 5
    print(f"After +=: {counter}")
    
    counter -= 3    # counter = counter - 3
    print(f"After -=: {counter}")
    
    counter *= 2    # counter = counter * 2
    print(f"After *=: {counter}")
    
    counter //= 3   # counter = counter // 3 (floor division)
    print(f"After //=: {counter}")
    
    counter %= 5    # counter = counter % 5 (modulus)
    print(f"After %=: {counter}")
    
    counter **= 2   # counter = counter ** 2 (exponentiation)
    print(f"After **=: {counter}")
    
    # String augmented assignment
    message = "Hello"
    message += " World"    # String concatenation
    print(f"String +=: {message}")
    
    message *= 2           # String repetition
    print(f"String *=: {message}")
    
    # List augmented assignment
    numbers = [1, 2, 3]
    numbers += [4, 5]      # List extension
    print(f"List +=: {numbers}")
    
    numbers *= 2           # List repetition
    print(f"List *=: {numbers}")
    
    # Bitwise augmented assignment
    bit_value = 12         # Binary: 1100
    bit_value &= 8         # Bitwise AND: 1100 & 1000 = 1000 (8)
    print(f"Bitwise &=: {bit_value}")
    
    bit_value |= 4         # Bitwise OR: 1000 | 0100 = 1100 (12)
    print(f"Bitwise |=: {bit_value}")
    
    bit_value ^= 3         # Bitwise XOR: 1100 ^ 0011 = 1111 (15)
    print(f"Bitwise ^=: {bit_value}")
    
    bit_value <<= 1        # Left shift: 1111 << 1 = 11110 (30)
    print(f"Left shift <<=: {bit_value}")
    
    bit_value >>= 2        # Right shift: 11110 >> 2 = 0111 (7)
    print(f"Right shift >>=: {bit_value}")
    
    # Unpacking patterns
    print("\n=== UNPACKING PATTERNS ===")
    
    # Basic tuple unpacking
    coordinates = (10, 20)
    x_coord, y_coord = coordinates
    print(f"Tuple unpacking: x={x_coord}, y={y_coord}")
    
    # List unpacking
    colors = ["red", "green", "blue"]
    primary1, primary2, primary3 = colors
    print(f"List unpacking: {primary1}, {primary2}, {primary3}")
    
    # Extended unpacking with asterisk (Python 3+)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Unpack first, last, and collect middle
    first, *middle, last = numbers
    print(f"Extended unpacking: first={first}, middle={middle}, last={last}")
    
    # Unpack first two and collect rest
    first, second, *rest = numbers
    print(f"Collect rest: first={first}, second={second}, rest={rest}")
    
    # Unpack with specific positions
    first, *_, last_two_a, last_two_b = numbers
    print(f"Skip middle: first={first}, last_two={last_two_a}, {last_two_b}")
    
    # Dictionary unpacking in assignment (Python 3.5+)
    user_data = {"name": "John", "age": 30, "city": "New York"}
    
    # This creates individual variables (not common, shown for completeness)
    # name, age, city = user_data.values()  # Order dependent, risky
    
    # Better: use dict methods for specific keys
    user_name = user_data["name"]
    user_age = user_data["age"]
    user_city = user_data.get("city", "Unknown")
    
    # Nested unpacking
    print("\n=== NESTED UNPACKING ===")
    
    nested_data = [("John", 30), ("Jane", 25), ("Bob", 35)]
    
    # Unpack nested tuples in loop
    for name, age in nested_data:
        print(f"Nested unpacking in loop: {name} is {age} years old")
    
    # Complex nested unpacking
    complex_data = [(1, 2, [3, 4]), (5, 6, [7, 8])]
    for x, y, [z, w] in complex_data:
        print(f"Complex unpacking: x={x}, y={y}, z={z}, w={w}")
    
    # Walrus operator (Assignment expressions, Python 3.8+)
    print("\n=== WALRUS OPERATOR (ASSIGNMENT EXPRESSIONS) ===")
    
    # Traditional approach
    data = [1, 2, 3, 4, 5]
    length = len(data)
    if length > 3:
        print(f"Traditional: List is long with {length} items")
    
    # With walrus operator
    if (length := len(data)) > 3:
        print(f"Walrus operator: List is long with {length} items")
    
    # Walrus in while loops
    import random
    attempts = 0
    while (value := random.randint(1, 10)) != 7 and attempts < 5:
        print(f"Attempt {attempts + 1}: Got {value}, looking for 7")
        attempts += 1
    
    if value == 7:
        print(f"Found 7 after {attempts + 1} attempts!")
    else:
        print(f"Gave up after {attempts + 1} attempts, last value was {value}")
    
    # Walrus in list comprehensions
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares_over_threshold = [
        square for x in data
        if (square := x ** 2) > 25
    ]
    print(f"Squares over 25: {squares_over_threshold}")
    
    # Variable swapping patterns
    print("\n=== VARIABLE SWAPPING PATTERNS ===")
    
    # Python's tuple swapping (elegant)
    a, b = 10, 20
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")
    
    # Multiple variable rotation
    x, y, z = 1, 2, 3
    print(f"Before rotation: x={x}, y={y}, z={z}")
    x, y, z = z, x, y  # Rotate right
    print(f"After rotation: x={x}, y={y}, z={z}")
    
    # Conditional assignment patterns
    print("\n=== CONDITIONAL ASSIGNMENT PATTERNS ===")
    
    # Ternary operator for conditional assignment
    user_type = "admin"
    max_attempts = 10 if user_type == "admin" else 3
    print(f"Conditional assignment: max_attempts = {max_attempts}")
    
    # Default value assignment
    config = {"debug": True}
    debug_mode = config.get("debug", False)
    log_level = config.get("log_level", "INFO")
    print(f"Default assignments: debug={debug_mode}, log_level={log_level}")
    
    # None-coalescing pattern
    def get_user_name():
        return None  # Simulate no user
    
    username = get_user_name() or "Anonymous"
    print(f"None-coalescing: username = {username}")
    
    # Short-circuit assignment
    existing_value = "keep this"
    existing_value = existing_value or "default value"  # Keeps existing
    print(f"Short-circuit (keep): {existing_value}")
    
    empty_value = ""
    empty_value = empty_value or "default value"  # Uses default
    print(f"Short-circuit (default): {empty_value}")
    
    return {
        'basic_assignments': {
            'single': single_value,
            'multiple': (x, y, z),
            'chained': (a, b, c)
        },
        'augmented_examples': {
            'final_counter': counter,
            'final_message': message,
            'final_numbers': numbers,
            'final_bit_value': bit_value
        },
        'unpacking_examples': {
            'coordinates': (x_coord, y_coord),
            'colors': (primary1, primary2, primary3),
            'extended': {'first': first, 'middle_count': len(middle), 'last': last}
        },
        'advanced_patterns': {
            'squares_over_threshold': squares_over_threshold,
            'swap_result': (a, b),
            'rotation_result': (x, y, z),
            'conditional_max_attempts': max_attempts,
            'coalescing_username': username
        }
    }

    return {
        'basic_assignments': {
            'single': single_value,
            'multiple': (x, y, z),
            'chained': (a, b, c)
        },
        'augmented_examples': {
            'final_counter': counter,
            'final_message': message,
            'final_numbers': numbers,
            'final_bit_value': bit_value
        },
        'unpacking_examples': {
            'coordinates': (x_coord, y_coord),
            'colors': (primary1, primary2, primary3),
            'extended': {'first': first, 'middle_count': len(middle), 'last': last}
        },
        'advanced_patterns': {
            'squares_over_threshold': squares_over_threshold,
            'swap_result': (a, b),
            'rotation_result': (x, y, z),
            'conditional_max_attempts': max_attempts,
            'coalescing_username': username
        }
    }

# =============================================================================
# 6. MEMORY & PERFORMANCE OPTIMIZATION
# =============================================================================

"""
MEMORY AND PERFORMANCE OPTIMIZATION:
Understanding memory usage and performance optimization techniques
"""

def demonstrate_memory_performance():
    """
    COMPREHENSIVE MEMORY AND PERFORMANCE DEMONSTRATION
    Variable memory optimization and performance techniques
    """
    
    print("=== MEMORY MANAGEMENT FUNDAMENTALS ===")
    
    import sys
    import gc
    from memory_profiler import profile  # pip install memory-profiler if needed
    
    # Memory usage of different variable types
    def compare_memory_usage():
        """Compare memory usage of different data types."""
        
        # Basic types memory usage
        int_var = 42
        float_var = 3.14
        str_var = "Hello World"
        bool_var = True
        none_var = None
        
        print("Memory usage of basic types:")
        print(f"int(42): {sys.getsizeof(int_var)} bytes")
        print(f"float(3.14): {sys.getsizeof(float_var)} bytes")
        print(f"str('Hello World'): {sys.getsizeof(str_var)} bytes")
        print(f"bool(True): {sys.getsizeof(bool_var)} bytes")
        print(f"None: {sys.getsizeof(none_var)} bytes")
        
        # Collection memory usage
        small_list = [1, 2, 3]
        large_list = list(range(1000))
        small_dict = {"a": 1, "b": 2}
        large_dict = {i: i**2 for i in range(1000)}
        
        print("\nMemory usage of collections:")
        print(f"Small list [1,2,3]: {sys.getsizeof(small_list)} bytes")
        print(f"Large list (1000 items): {sys.getsizeof(large_list)} bytes")
        print(f"Small dict: {sys.getsizeof(small_dict)} bytes")
        print(f"Large dict (1000 items): {sys.getsizeof(large_dict)} bytes")
        
        return {
            'basic_sizes': {
                'int': sys.getsizeof(int_var),
                'float': sys.getsizeof(float_var),
                'str': sys.getsizeof(str_var),
                'bool': sys.getsizeof(bool_var),
                'none': sys.getsizeof(none_var)
            },
            'collection_sizes': {
                'small_list': sys.getsizeof(small_list),
                'large_list': sys.getsizeof(large_list),
                'small_dict': sys.getsizeof(small_dict),
                'large_dict': sys.getsizeof(large_dict)
            }
        }
    
    memory_comparison = compare_memory_usage()
    
    # Variable interning and caching
    print("\n=== VARIABLE INTERNING AND CACHING ===")
    
    def demonstrate_interning():
        """Demonstrate Python's variable interning."""
        
        # Small integers are cached (-5 to 256)
        a1 = 100
        a2 = 100
        print(f"Small integers (100): a1 is a2 = {a1 is a2}")
        print(f"IDs: a1={id(a1)}, a2={id(a2)}")
        
        # Large integers are not cached
        b1 = 1000
        b2 = 1000
        print(f"Large integers (1000): b1 is b2 = {b1 is b2}")
        print(f"IDs: b1={id(b1)}, b2={id(b2)}")
        
        # String interning for identifiers
        s1 = "hello"
        s2 = "hello"
        print(f"Simple strings: s1 is s2 = {s1 is s2}")
        
        # Complex strings may not be interned
        complex1 = "hello world!"
        complex2 = "hello world!"
        print(f"Complex strings: complex1 is complex2 = {complex1 is complex2}")
        
        # Manual interning
        import sys
        manual1 = sys.intern("custom_string")
        manual2 = sys.intern("custom_string")
        print(f"Manually interned: manual1 is manual2 = {manual1 is manual2}")
        
        return {
            'small_int_cached': a1 is a2,
            'large_int_cached': b1 is b2,
            'simple_string_cached': s1 is s2,
            'complex_string_cached': complex1 is complex2,
            'manual_interning': manual1 is manual2
        }
    
    interning_results = demonstrate_interning()
    
    # Memory-efficient programming patterns
    print("\n=== MEMORY-EFFICIENT PATTERNS ===")
    
    def demonstrate_efficient_patterns():
        """Demonstrate memory-efficient programming patterns."""
        
        # 1. Use generators instead of lists for large datasets
        def memory_hungry_approach():
            """Memory-intensive approach using lists."""
            return [x**2 for x in range(100000)]
        
        def memory_efficient_approach():
            """Memory-efficient approach using generators."""
            return (x**2 for x in range(100000))
        
        # Compare memory usage
        list_data = memory_hungry_approach()
        gen_data = memory_efficient_approach()
        
        print(f"List comprehension memory: {sys.getsizeof(list_data)} bytes")
        print(f"Generator expression memory: {sys.getsizeof(gen_data)} bytes")
        
        # 2. Use slots to reduce instance memory usage
        class RegularClass:
            """Regular class without slots."""
            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z
        
        class SlottedClass:
            """Memory-efficient class with slots."""
            __slots__ = ['x', 'y', 'z']
            
            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z
        
        regular_obj = RegularClass(1, 2, 3)
        slotted_obj = SlottedClass(1, 2, 3)
        
        print(f"Regular class instance: {sys.getsizeof(regular_obj)} bytes")
        print(f"Slotted class instance: {sys.getsizeof(slotted_obj)} bytes")
        
        # 3. Use appropriate data structures
        # Sets for membership testing
        large_list = list(range(10000))
        large_set = set(range(10000))
        
        # Membership testing is O(n) for lists, O(1) for sets
        import time
        
        # Time list lookup
        start = time.time()
        9999 in large_list
        list_time = time.time() - start
        
        # Time set lookup
        start = time.time()
        9999 in large_set
        set_time = time.time() - start
        
        print(f"List lookup time: {list_time:.6f} seconds")
        print(f"Set lookup time: {set_time:.6f} seconds")
        print(f"Set is {list_time/set_time:.2f}x faster")
        
        # 4. Use collections.namedtuple for structured data
        from collections import namedtuple
        
        # Regular tuple
        regular_tuple = (1, 2, 3)
        
        # Named tuple (more memory efficient than class)
        Point = namedtuple('Point', ['x', 'y', 'z'])
        named_tuple = Point(1, 2, 3)
        
        print(f"Regular tuple memory: {sys.getsizeof(regular_tuple)} bytes")
        print(f"Named tuple memory: {sys.getsizeof(named_tuple)} bytes")
        print(f"Regular class memory: {sys.getsizeof(regular_obj)} bytes")
        
        return {
            'list_vs_generator': {
                'list_size': sys.getsizeof(list_data),
                'generator_size': sys.getsizeof(gen_data)
            },
            'regular_vs_slotted': {
                'regular_size': sys.getsizeof(regular_obj),
                'slotted_size': sys.getsizeof(slotted_obj)
            },
            'lookup_performance': {
                'list_time': list_time,
                'set_time': set_time,
                'speedup': list_time / set_time
            },
            'data_structure_sizes': {
                'regular_tuple': sys.getsizeof(regular_tuple),
                'named_tuple': sys.getsizeof(named_tuple),
                'regular_class': sys.getsizeof(regular_obj)
            }
        }
    
    efficiency_results = demonstrate_efficient_patterns()
    
    # Garbage collection and weak references
    print("\n=== GARBAGE COLLECTION AND WEAK REFERENCES ===")
    
    def demonstrate_garbage_collection():
        """Demonstrate garbage collection concepts."""
        
        import weakref
        import gc
        
        class TrackableObject:
            """Object that tracks its lifecycle."""
            count = 0
            
            def __init__(self, name):
                self.name = name
                TrackableObject.count += 1
                print(f"Created: {self.name} (total: {TrackableObject.count})")
            
            def __del__(self):
                TrackableObject.count -= 1
                print(f"Deleted: {self.name} (remaining: {TrackableObject.count})")
        
        # Strong references keep objects alive
        obj1 = TrackableObject("Object1")
        obj2 = TrackableObject("Object2")
        
        # Weak references don't prevent garbage collection
        weak_ref1 = weakref.ref(obj1)
        weak_ref2 = weakref.ref(obj2)
        
        print(f"Objects exist: {weak_ref1() is not None}, {weak_ref2() is not None}")
        
        # Delete strong references
        del obj1
        print(f"After deleting obj1: {weak_ref1() is not None}")
        
        # Circular references
        class Node:
            def __init__(self, value):
                self.value = value
                self.children = []
                self.parent = None
            
            def add_child(self, child):
                child.parent = self
                self.children.append(child)
        
        # Create circular reference
        parent = Node("parent")
        child = Node("child")
        parent.add_child(child)  # Now child.parent points to parent
        
        # Use weak reference to break cycle
        class SmartNode:
            def __init__(self, value):
                self.value = value
                self.children = []
                self._parent_ref = None
            
            @property
            def parent(self):
                return self._parent_ref() if self._parent_ref else None
            
            @parent.setter
            def parent(self, parent):
                self._parent_ref = weakref.ref(parent) if parent else None
            
            def add_child(self, child):
                child.parent = self
                self.children.append(child)
        
        # Create smart nodes without circular reference issues
        smart_parent = SmartNode("smart_parent")
        smart_child = SmartNode("smart_child")
        smart_parent.add_child(smart_child)
        
        # Force garbage collection
        gc.collect()
        
        return {
            'object_count': TrackableObject.count,
            'weak_refs_alive': [weak_ref1() is not None, weak_ref2() is not None],
            'gc_stats': gc.get_stats()[0] if gc.get_stats() else {}
        }
    
    gc_results = demonstrate_garbage_collection()
    
    # Variable assignment performance
    print("\n=== VARIABLE ASSIGNMENT PERFORMANCE ===")
    
    def benchmark_assignment_patterns():
        """Benchmark different assignment patterns."""
        import time
        
        # Single vs multiple assignment
        def single_assignments():
            start = time.perf_counter()
            for _ in range(100000):
                a = 1
                b = 2
                c = 3
            return time.perf_counter() - start
        
        def multiple_assignments():
            start = time.perf_counter()
            for _ in range(100000):
                a, b, c = 1, 2, 3
            return time.perf_counter() - start
        
        single_time = single_assignments()
        multiple_time = multiple_assignments()
        
        print(f"Single assignments: {single_time:.6f} seconds")
        print(f"Multiple assignments: {multiple_time:.6f} seconds")
        print(f"Ratio: {multiple_time/single_time:.2f}")
        
        # List vs tuple unpacking performance
        def list_unpacking():
            data = [1, 2, 3] * 33333  # 100,000 elements
            start = time.perf_counter()
            for i in range(0, len(data), 3):
                a, b, c = data[i:i+3]
            return time.perf_counter() - start
        
        def tuple_unpacking():
            data = [(1, 2, 3)] * 33333  # 33,333 tuples
            start = time.perf_counter()
            for item in data:
                a, b, c = item
            return time.perf_counter() - start
        
        list_unpack_time = list_unpacking()
        tuple_unpack_time = tuple_unpacking()
        
        print(f"List unpacking: {list_unpack_time:.6f} seconds")
        print(f"Tuple unpacking: {tuple_unpack_time:.6f} seconds")
        
        return {
            'assignment_times': {
                'single': single_time,
                'multiple': multiple_time,
                'ratio': multiple_time / single_time
            },
            'unpacking_times': {
                'list': list_unpack_time,
                'tuple': tuple_unpack_time
            }
        }
    
    performance_results = benchmark_assignment_patterns()
    
    return {
        'memory_comparison': memory_comparison,
        'interning_results': interning_results,
        'efficiency_results': efficiency_results,
        'gc_results': gc_results,
        'performance_results': performance_results
    }

# =============================================================================
# 7. ADVANCED VARIABLE TECHNIQUES
# =============================================================================

"""
ADVANCED VARIABLE TECHNIQUES:
Professional patterns and advanced variable manipulation
"""

def demonstrate_advanced_techniques():
    """
    COMPREHENSIVE ADVANCED VARIABLE TECHNIQUES
    Professional patterns for variable manipulation and management
    """
    
    print("=== ADVANCED VARIABLE TECHNIQUES ===")
    
    # Context managers for variable lifecycle
    class VariableManager:
        """Context manager for temporary variable management."""
        
        def __init__(self, namespace, **variables):
            self.namespace = namespace
            self.variables = variables
            self.original_values = {}
        
        def __enter__(self):
            # Save original values and set new ones
            for name, value in self.variables.items():
                if name in self.namespace:
                    self.original_values[name] = self.namespace[name]
                self.namespace[name] = value
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            # Restore original values
            for name in self.variables:
                if name in self.original_values:
                    self.namespace[name] = self.original_values[name]
                else:
                    del self.namespace[name]
    
    # Demonstrate context manager usage
    test_namespace = {'existing_var': 'original'}
    
    print("Before context manager:", test_namespace)
    
    with VariableManager(test_namespace, existing_var='temporary', new_var='created'):
        print("Inside context manager:", test_namespace)
    
    print("After context manager:", test_namespace)
    
    # Property-based variable access
    print("\n=== PROPERTY-BASED VARIABLE ACCESS ===")
    
    class SmartVariable:
        """Class demonstrating advanced property usage."""
        
        def __init__(self, initial_value=0):
            self._value = initial_value
            self._access_count = 0
            self._modification_count = 0
        
        @property
        def value(self):
            """Get value with access tracking."""
            self._access_count += 1
            return self._value
        
        @value.setter
        def value(self, new_value):
            """Set value with validation and tracking."""
            if not isinstance(new_value, (int, float)):
                raise TypeError("Value must be numeric")
            
            if new_value < 0:
                raise ValueError("Value must be non-negative")
            
            self._value = new_value
            self._modification_count += 1
        
        @property
        def statistics(self):
            """Get access statistics."""
            return {
                'current_value': self._value,
                'access_count': self._access_count,
                'modification_count': self._modification_count
            }
        
        def reset_stats(self):
            """Reset access statistics."""
            self._access_count = 0
            self._modification_count = 0
    
    # Demonstrate smart variable
    smart_var = SmartVariable(10)
    
    # Access value multiple times
    for _ in range(3):
        _ = smart_var.value
    
    # Modify value
    smart_var.value = 20
    smart_var.value = 30
    
    print(f"Smart variable stats: {smart_var.statistics}")
    
    # Variable factories and builders
    print("\n=== VARIABLE FACTORIES AND BUILDERS ===")
    
    class ConfigBuilder:
        """Builder pattern for configuration variables."""
        
        def __init__(self):
            self._config = {}
        
        def set_database(self, host='localhost', port=5432, name='mydb'):
            """Set database configuration."""
            self._config['database'] = {
                'host': host,
                'port': port,
                'name': name
            }
            return self
        
        def set_cache(self, enabled=True, ttl=3600, size_mb=100):
            """Set cache configuration."""
            self._config['cache'] = {
                'enabled': enabled,
                'ttl': ttl,
                'size_mb': size_mb
            }
            return self
        
        def set_logging(self, level='INFO', file_path=None):
            """Set logging configuration."""
            self._config['logging'] = {
                'level': level,
                'file_path': file_path
            }
            return self
        
        def build(self):
            """Build final configuration."""
            return self._config.copy()
        
        def validate(self):
            """Validate configuration before building."""
            if 'database' not in self._config:
                raise ValueError("Database configuration required")
            
            db_config = self._config['database']
            if not (1 <= db_config['port'] <= 65535):
                raise ValueError("Database port must be between 1-65535")
            
            return self
    
    # Use configuration builder
    config = (ConfigBuilder()
              .set_database(host='prod-db', port=5432, name='production')
              .set_cache(enabled=True, ttl=7200)
              .set_logging(level='WARNING', file_path='/var/log/app.log')
              .validate()
              .build())
    
    print(f"Built configuration: {config}")
    
    # Metaclass for automatic variable tracking
    print("\n=== METACLASS VARIABLE TRACKING ===")
    
    class VariableTrackingMeta(type):
        """Metaclass that tracks variable assignments in classes."""
        
        def __new__(mcs, name, bases, namespace):
            # Track all non-special attributes
            tracked_vars = {
                key: value for key, value in namespace.items()
                if not key.startswith('_') and not callable(value)
            }
            
            namespace['_tracked_variables'] = tracked_vars
            namespace['_variable_history'] = {}
            
            return super().__new__(mcs, name, bases, namespace)
    
    class TrackedClass(metaclass=VariableTrackingMeta):
        """Class with automatic variable tracking."""
        
        class_var1 = "original value 1"
        class_var2 = "original value 2"
        number_var = 42
        
        @classmethod
        def get_tracked_variables(cls):
            """Get all tracked variables."""
            return cls._tracked_variables.copy()
        
        @classmethod
        def get_variable_history(cls):
            """Get variable modification history."""
            return cls._variable_history.copy()
    
    print(f"Tracked variables: {TrackedClass.get_tracked_variables()}")
    
    # Descriptor protocol for advanced variable control
    print("\n=== DESCRIPTOR PROTOCOL ===")
    
    class ValidatedAttribute:
        """Descriptor for validated attributes."""
        
        def __init__(self, validator=None, name=None):
            self.validator = validator
            self.name = name
        
        def __set_name__(self, owner, name):
            self.name = name
            self.private_name = f'_{name}'
        
        def __get__(self, instance, owner):
            if instance is None:
                return self
            return getattr(instance, self.private_name, None)
        
        def __set__(self, instance, value):
            if self.validator:
                if not self.validator(value):
                    raise ValueError(f"Invalid value for {self.name}: {value}")
            setattr(instance, self.private_name, value)
    
    # Validator functions
    def positive_number(value):
        return isinstance(value, (int, float)) and value > 0
    
    def non_empty_string(value):
        return isinstance(value, str) and len(value.strip()) > 0
    
    class ValidatedUser:
        """Class using descriptor validation."""
        
        age = ValidatedAttribute(positive_number)
        name = ValidatedAttribute(non_empty_string)
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    # Demonstrate descriptor validation
    try:
        user = ValidatedUser("John Doe", 30)
        print(f"Valid user created: {user.name}, {user.age}")
        
        # This will raise an error
        user.age = -5
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Variable serialization and persistence
    print("\n=== VARIABLE SERIALIZATION ===")
    
    import json
    import pickle
    from datetime import datetime
    
    class SerializableVariables:
        """Class for serializing variables."""
        
        def __init__(self):
            self.variables = {}
            self.metadata = {
                'created': datetime.now().isoformat(),
                'version': '1.0'
            }
        
        def set_variable(self, name, value, description=None):
            """Set a variable with metadata."""
            self.variables[name] = {
                'value': value,
                'type': type(value).__name__,
                'description': description,
                'modified': datetime.now().isoformat()
            }
        
        def get_variable(self, name):
            """Get variable value."""
            if name in self.variables:
                return self.variables[name]['value']
            raise KeyError(f"Variable {name} not found")
        
        def to_json(self):
            """Export to JSON (only JSON-serializable values)."""
            exportable = {}
            for name, info in self.variables.items():
                try:
                    json.dumps(info['value'])  # Test serialization
                    exportable[name] = info
                except TypeError:
                    exportable[name] = {
                        **info,
                        'value': f"<non-serializable {info['type']}>"
                    }
            
            return json.dumps({
                'variables': exportable,
                'metadata': self.metadata
            }, indent=2)
        
        def to_pickle(self):
            """Export to pickle (all Python objects)."""
            return pickle.dumps({
                'variables': self.variables,
                'metadata': self.metadata
            })
    
    # Demonstrate serialization
    serializable = SerializableVariables()
    serializable.set_variable('username', 'john_doe', 'User identifier')
    serializable.set_variable('scores', [95, 87, 91], 'Test scores list')
    serializable.set_variable('config', {'debug': True}, 'Application config')
    serializable.set_variable('function_ref', lambda x: x*2, 'Function reference')
    
    json_export = serializable.to_json()
    print("JSON export (truncated):", json_export[:200] + "...")
    
    return {
        'context_manager': VariableManager,
        'smart_variable': smart_var.statistics,
        'config_builder': config,
        'tracked_class': TrackedClass.get_tracked_variables(),
        'serializable': serializable
    }

# Final sections continue...
if __name__ == "__main__":
    print("🎯 PYTHON VARIABLES MASTERY GUIDE LOADED")
    print("📚 Ready for comprehensive variable mastery!")
    
    # Quick demonstration
    fundamentals_results = demonstrate_variable_fundamentals()
    print(f"✓ Variable fundamentals loaded: {len(fundamentals_results['examples'])} basic types")
    
    naming_results = demonstrate_naming_conventions()  
    print(f"✓ Naming conventions loaded: {len(naming_results['examples'])} pattern categories")
    
    assignment_results = demonstrate_assignment_patterns()
    print(f"✓ Assignment patterns loaded: {len(assignment_results)} pattern types")
    
    print("\n🚀 Continue execution to explore type system, scope management, and advanced variable techniques!")
y = str("Hello")    # y is "Hellos" type str
z = float(3.14)     # z is 3.14 type float


# ---------

""" Output Variables """
# You can output variables using the print() function.
#   Are called GLOBAL VARIABLES
#     Can be used by everyone, both inside of functions and outside. 

x = "Hello"

print(x)  
# Hello

""" Output Multiple Variables """
# You can output multiple variables in one print() function.
#  By using commas to separate them.

x = "Hello"
y = "World"

print(x, y) 
# Hello World

# Also using operators like ("+")" for concatenation (only for strings).
#   Not for numbers, as it will raise a TypeError.

x = "Hello"
y = "World"

print(x + " " + y)
# Hello World


""" Output Variables with String Formatting """

""" F-Strings method """
# You can use the f-strings to include variables .
#   Are a way to embed expressions inside string literals.
#     Using curly braces {} to include variables.

name = "John"
age = 30

print(f"My name is {name} and I am {age} years old.")
# My name is John and I am 30 years old.

""" Format Method """
# You can also use the format() method to format strings.
#   The format() method allows you to insert variables into a string.
#     Using curly braces {} as placeholders for the variables.

name = "John"
age = 30

print("My name is {} and I am {} years old.".format(name, age))
# My name is John and I am 30 years old.

""" % Operator method """ 
# You can also use the % operator for string formatting.
#   The % operator allows you to insert variables into a string.
#     Using %s for strings and %d for integers as placeholders.


name = "John"
age = 30

print("My name is %s and I am %d years old." % (name, age))
# My name is John and I am 30 years old.

# -----------

""" Inside a function variables """
# Variables defined inside a function are local to that function.
#   They cannot be accessed from outside the function.

def my_function():
    x = "Hello"
    print(x)

my_function()
# Hello

print(x)  # NameError: name 'x' is not defined

# -----------

""" COMMON VARIABLE MISTAKES TO AVOID """

# Mistake 1: Using reserved keywords as variable names
# DON'T DO THIS:
# class = "Python"      # Error: 'class' is a keyword
# def = 5               # Error: 'def' is a keyword
# if = True             # Error: 'if' is a keyword

# DO THIS INSTEAD:
class_name = "Python"
definition = 5
condition = True

# Mistake 2: Starting variable names with numbers
# DON'T DO THIS:
# 1st_variable = "Hello"    # SyntaxError: invalid decimal literal
# 2name = "John"            # SyntaxError: invalid decimal literal

# DO THIS INSTEAD:
first_variable = "Hello"
name2 = "John"
variable_1 = "Hello"

# Mistake 3: Case sensitivity confusion
Name = "John"        # This is different from 'name'
name = "Jane"        # This is different from 'Name'
print(Name)          # John
print(name)          # Jane

# Mistake 4: Accidentally overwriting built-in functions
# DON'T DO THIS:
# list = [1, 2, 3]      # Shadows the built-in list() function
# print = "Hello"       # Shadows the built-in print() function

# DO THIS INSTEAD:
my_list = [1, 2, 3]
message = "Hello"

# Mistake 5: Using global when you meant local
counter = 0  # Global variable

def increment():
    global counter    # Explicitly use global
    counter += 1      # Modify global counter

def local_increment():
    counter = 0       # Creates new local variable
    counter += 1      # Only affects local counter
    return counter

print("Original counter:", counter)  # 0
increment()
print("After increment():", counter)  # 1
result = local_increment()
print("local_increment() returned:", result)  # 1
print("Counter unchanged:", counter)  # 1

# -----------
