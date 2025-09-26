""" 3.3.0_Python_SYNTAX.py """

# =============================================================================
# PYTHON SYNTAX - COMPLETE MASTERY GUIDE
# =============================================================================
# Version: 3.3.0 | Educational Excellence Target: 9.5/10
# Purpose: Master Python syntax rules with professional coding standards
# Target: Beginner to Advanced Python programmers
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python syntax, you will:
✓ Understand indentation rules and code block structure
✓ Master comments, docstrings, and documentation practices
✓ Apply Python naming conventions and style guidelines
✓ Use statements, expressions, and control structures correctly
✓ Handle Python's line structure and statement continuation
✓ Write clean, readable, and maintainable Python code

🚀 QUICK NAVIGATION:
├── 1. INDENTATION & CODE BLOCKS (FUNDAMENTAL)
├── 2. COMMENTS & DOCUMENTATION (PROFESSIONAL)
├── 3. STATEMENTS & EXPRESSIONS (CORE)
├── 4. NAMING CONVENTIONS (STANDARDS)
├── 5. LINE STRUCTURE & CONTINUATION
├── 6. LITERALS & CONSTANTS
├── 7. ADVANCED SYNTAX FEATURES
├── 8. ERROR HANDLING SYNTAX
├── 9. STYLE GUIDELINES & BEST PRACTICES
└── 10. REAL-WORLD SYNTAX APPLICATIONS

🔍 CORE CONCEPT:
Python syntax emphasizes readability and simplicity,
using indentation to define code structure and scope.
"""

# =============================================================================
# 1. INDENTATION & CODE BLOCKS - FUNDAMENTAL RULES
# =============================================================================

"""
PYTHON INDENTATION MASTERY:
The foundation of Python's readability and structure
"""

# Indentation fundamentals
indentation_rules = {
# =============================================================================
# 5. LINE STRUCTURE & CONTINUATION
# =============================================================================

"""
PYTHON LINE STRUCTURE:
Master line continuation, statement separation, and code organization
"""

def demonstrate_line_structure():
    """
    COMPREHENSIVE LINE STRUCTURE EXAMPLES
    Proper line continuation and statement organization
    """
    
    # Line structure fundamentals
    line_structure_rules = {
        "basic_rules": {
            "line_termination": "Newline character ends a statement",
            "statement_separation": "Each statement on its own line",
            "multiple_statements": "Use semicolon (;) sparingly",
            "continuation": "Use backslash (\\) or implicit continuation"
        },
        
        "implicit_continuation": {
            "parentheses": "Inside (), [], {} - automatic continuation",
            "operators": "Lines ending with operators continue",
            "string_literals": "Triple quotes allow multi-line strings"
        },
        
        "explicit_continuation": {
            "backslash": "Use \\ to continue line explicitly",
            "usage": "Avoid when implicit continuation possible",
            "placement": "Must be last character on line"
        }
    }
    
    # Examples of proper line continuation
    
    # 1. Implicit continuation with parentheses (PREFERRED)
    long_calculation = (
        (first_value + second_value) * 
        (third_value - fourth_value) +
        (fifth_value / sixth_value) -
        (seventh_value ** eighth_value)
    ) if all([
        first_value, second_value, third_value, fourth_value,
        fifth_value, sixth_value, seventh_value, eighth_value
    ]) else 0
    
    # 2. Function calls with many parameters
    def complex_function_with_many_parameters(
            parameter_one,
            parameter_two,
            parameter_three,
            parameter_four='default_value',
            parameter_five=None,
            parameter_six=True,
            *args,
            **kwargs
    ):
        """Function demonstrating proper parameter line breaks."""
        return {
            'param1': parameter_one,
            'param2': parameter_two,
            'param3': parameter_three,
            'param4': parameter_four,
            'param5': parameter_five,
            'param6': parameter_six,
            'args': args,
            'kwargs': kwargs
        }
    
    # 3. Long function call with multiple arguments
    result = complex_function_with_many_parameters(
        "first argument",
        "second argument", 
        "third argument",
        parameter_four="custom value",
        parameter_five=[1, 2, 3, 4, 5],
        parameter_six=False,
        "additional positional arg",
        extra_keyword="extra value"
    )
    
    # 4. List comprehensions with line breaks
    filtered_and_transformed_data = [
        transform_item(item)
        for item in original_data_source
        if item is not None 
        and item.meets_criteria()
        and item.has_required_attributes()
    ]
    
    # 5. Dictionary with proper line breaks
    comprehensive_configuration = {
        'database_settings': {
            'host': 'localhost',
            'port': 5432,
            'database': 'production_db',
            'username': 'app_user',
            'password': 'secure_password'
        },
        'api_settings': {
            'base_url': 'https://api.example.com',
            'timeout': 30,
            'retry_attempts': 3,
            'rate_limit': 100
        },
        'logging_settings': {
            'level': 'INFO',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'handlers': ['console', 'file'],
            'file_path': '/var/log/application.log'
        }
    }
    
    # 6. Chain method calls with proper line breaks
    processed_text = (
        input_text
        .strip()
        .lower()
        .replace(' ', '_')
        .replace('-', '_')
        .replace('.', '')
        .replace(',', '')
    )
    
    # 7. Boolean expressions with line breaks
    is_valid_user = (
        user.is_authenticated() and
        user.has_required_permissions() and
        not user.is_suspended() and
        user.account_is_active() and
        user.email_is_verified()
    )
    
    # 8. Explicit continuation with backslash (use sparingly)
    total_sum = first_number + second_number + \
                third_number + fourth_number + \
                fifth_number
    
    # 9. Multi-line string literals
    sql_query = """
        SELECT 
            u.id,
            u.username,
            u.email,
            p.first_name,
            p.last_name,
            p.phone_number
        FROM users u
        JOIN profiles p ON u.id = p.user_id
        WHERE u.is_active = true
          AND u.created_at >= %s
          AND u.last_login >= %s
        ORDER BY u.last_login DESC
        LIMIT 100
    """
    
    # 10. Complex data structure with proper formatting
    api_response_structure = {
        'status': 'success',
        'data': {
            'users': [
                {
                    'id': user_id,
                    'profile': {
                        'name': f"{first_name} {last_name}",
                        'email': email_address,
                        'preferences': {
                            'notifications': True,
                            'theme': 'dark',
                            'language': 'en-US'
                        }
                    },
                    'permissions': [
                        permission 
                        for permission in available_permissions
                        if user_has_permission(user_id, permission)
                    ]
                }
                for user_id in active_user_ids
                if user_id is not None
            ],
            'pagination': {
                'current_page': current_page_number,
                'total_pages': total_page_count,
                'items_per_page': items_per_page_limit,
                'total_items': total_item_count
            }
        },
        'metadata': {
            'request_id': request_identifier,
            'timestamp': request_timestamp,
            'processing_time_ms': processing_duration
        }
    }
    
    return {
        'line_structure_rules': line_structure_rules,
        'function_result': result,
        'configuration': comprehensive_configuration,
        'processed_text': processed_text,
        'validation_result': is_valid_user,
        'sql_query': sql_query.strip(),
        'api_structure': api_response_structure
    }

# =============================================================================
# 6. LITERALS & CONSTANTS
# =============================================================================

"""
PYTHON LITERALS AND CONSTANTS:
Master all literal types and constant declaration patterns
"""

def demonstrate_literals_constants():
    """
    COMPREHENSIVE LITERALS AND CONSTANTS GUIDE
    All Python literal types and constant patterns
    """
    
    # Numeric literals
    numeric_literals = {
        "integers": {
            "decimal": 42,
            "binary": 0b101010,      # 42 in binary
            "octal": 0o52,           # 42 in octal  
            "hexadecimal": 0x2A,     # 42 in hexadecimal
            "large_number": 1_000_000,  # Underscores for readability
            "negative": -42
        },
        
        "floating_point": {
            "standard": 3.14159,
            "scientific": 1.23e-4,   # 0.000123
            "large_scientific": 6.022e23,  # Avogadro's number
            "negative_exponent": 5e-3,     # 0.005
            "positive_exponent": 2e3,      # 2000.0
            "with_underscores": 1_000.123_456
        },
        
        "complex_numbers": {
            "standard": 3 + 4j,
            "imaginary_only": 5j,
            "real_only": 7 + 0j,
            "scientific": 1.5e-2 + 2.3e3j
        }
    }
    
    # String literals
    string_literals = {
        "single_quotes": 'Hello, World!',
        "double_quotes": "Hello, Python!",
        "triple_single": '''
            Multi-line string
            with single quotes
            preserves whitespace
        ''',
        "triple_double": """
            Multi-line string
            with double quotes
            also preserves whitespace
        """,
        
        "escape_sequences": {
            "newline": "Line 1\nLine 2",
            "tab": "Column 1\tColumn 2",
            "backslash": "Path\\to\\file",
            "quote": "She said \"Hello\"",
            "unicode": "Unicode: \u03B1\u03B2\u03B3",  # αβγ
            "hex_escape": "Hex: \x41\x42\x43",         # ABC
        },
        
        "raw_strings": {
            "regex_pattern": r"\d+\.\d+",
            "file_path": r"C:\Users\username\Documents",
            "with_quotes": r"Raw string with 'quotes' and \"double quotes\""
        },
        
        "formatted_strings": {
            "f_string": f"Current time: {datetime.now()}",
            "expression": f"Calculation: {2 + 2 = }",
            "formatting": f"Pi to 3 places: {3.14159:.3f}",
            "multiline_f": f"""
                Name: {'John Doe'}
                Age: {30}
                Score: {85.5:.1f}%
            """
        }
    }
    
    # Collection literals
    collection_literals = {
        "lists": {
            "empty": [],
            "numbers": [1, 2, 3, 4, 5],
            "mixed": [1, "two", 3.0, True, None],
            "nested": [[1, 2], [3, 4], [5, 6]],
            "multiline": [
                "item_one",
                "item_two", 
                "item_three",
                "item_four"
            ]
        },
        
        "tuples": {
            "empty": (),
            "single_item": (42,),  # Note the comma!
            "coordinates": (10, 20),
            "rgb_color": (255, 128, 0),
            "nested": ((1, 2), (3, 4), (5, 6))
        },
        
        "sets": {
            "empty": set(),  # Not {} - that's a dict!
            "numbers": {1, 2, 3, 4, 5},
            "strings": {"apple", "banana", "cherry"},
            "mixed": {1, "two", 3.0, True}  # Note: True == 1, so only 1 remains
        },
        
        "dictionaries": {
            "empty": {},
            "simple": {"name": "John", "age": 30},
            "mixed_keys": {1: "one", "two": 2, 3.0: "three"},
            "nested": {
                "user": {
                    "name": "John Doe",
                    "contact": {
                        "email": "john@example.com",
                        "phone": "+1-555-0123"
                    }
                },
                "settings": {
                    "theme": "dark",
                    "notifications": True
                }
            }
        }
    }
    
    # Boolean and None literals
    special_literals = {
        "boolean": {
            "true_value": True,
            "false_value": False,
            "note": "True and False are keywords, not strings"
        },
        "none_type": {
            "null_value": None,
            "usage": "Represents absence of value",
            "comparison": "Use 'is None' not '== None'"
        }
    }
    
    # Constants (by convention - Python doesn't enforce)
    class Constants:
        """Class demonstrating constant declaration patterns."""
        
        # Mathematical constants
        PI = 3.141592653589793
        E = 2.718281828459045
        GOLDEN_RATIO = 1.618033988749895
        
        # Application constants
        MAX_RETRY_ATTEMPTS = 3
        DEFAULT_TIMEOUT_SECONDS = 30
        CACHE_EXPIRY_HOURS = 24
        
        # String constants
        APP_NAME = "Python Syntax Guide"
        VERSION = "3.3.0"
        DEFAULT_ENCODING = "utf-8"
        
        # Collection constants (use tuples for immutability)
        SUPPORTED_FILE_TYPES = ('.txt', '.csv', '.json', '.xml')
        HTTP_SUCCESS_CODES = (200, 201, 202, 204)
        WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
        
        # Configuration constants
        DATABASE_CONFIG = {
            'HOST': 'localhost',
            'PORT': 5432,
            'NAME': 'production_db',
            'POOL_SIZE': 10
        }
        
        # Regex pattern constants
        EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        PHONE_PATTERN = r'^\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$'
        
        @classmethod
        def get_all_constants(cls):
            """Return all constants as a dictionary."""
            return {
                attr: getattr(cls, attr)
                for attr in dir(cls)
                if not attr.startswith('_') and not callable(getattr(cls, attr))
            }
    
    # Demonstrate constant usage
    def calculate_circle_properties(radius):
        """Calculate circle properties using constants."""
        area = Constants.PI * radius ** 2
        circumference = 2 * Constants.PI * radius
        
        return {
            'radius': radius,
            'area': area,
            'circumference': circumference,
            'diameter': 2 * radius
        }
    
    return {
        'numeric_literals': numeric_literals,
        'string_literals': string_literals,
        'collection_literals': collection_literals,
        'special_literals': special_literals,
        'constants_class': Constants,
        'circle_example': calculate_circle_properties(5.0),
        'all_constants': Constants.get_all_constants()
    }

# =============================================================================
# 7. ADVANCED SYNTAX FEATURES
# =============================================================================

"""
ADVANCED PYTHON SYNTAX:
Modern Python syntax features and advanced constructs
"""

def demonstrate_advanced_syntax():
    """
    COMPREHENSIVE ADVANCED SYNTAX EXAMPLES
    Modern Python features and advanced constructs
    """
    
    # Assignment expressions (Walrus operator := Python 3.8+)
    def walrus_operator_examples():
        """Demonstrate assignment expressions in various contexts."""
        
        # Example 1: In while loops
        data_stream = iter([1, 2, 3, 4, 5, None, 6, 7])
        results = []
        while (value := next(data_stream, None)) is not None:
            results.append(value * 2)
        
        # Example 2: In list comprehensions
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        squared_evens = [
            square for num in numbers
            if (square := num ** 2) % 2 == 0
        ]
        
        # Example 3: In if statements
        user_input = "hello world"
        if (length := len(user_input)) > 5:
            message = f"Input is long ({length} characters)"
        else:
            message = f"Input is short ({length} characters)"
        
        # Example 4: In function calls
        import re
        text = "Contact us at support@example.com or admin@test.org"
        if (matches := re.findall(r'\S+@\S+', text)):
            email_count = len(matches)
        else:
            email_count = 0
        
        return {
            'stream_results': results,
            'squared_evens': squared_evens,
            'input_message': message,
            'email_matches': matches if 'matches' in locals() else [],
            'email_count': email_count
        }
    
    # Pattern matching (Match-Case, Python 3.10+)
    def pattern_matching_examples():
        """Demonstrate structural pattern matching."""
        
        def process_data(data):
            """Process different data types using pattern matching."""
            match data:
                # Match literal values
                case 0:
                    return "Zero value"
                
                case 1 | 2 | 3:  # Multiple patterns
                    return f"Small number: {data}"
                
                # Match with conditions (guard)
                case x if x > 100:
                    return f"Large number: {x}"
                
                # Match sequences with unpacking
                case [x]:
                    return f"Single item list: {x}"
                
                case [x, y]:
                    return f"Two item list: {x}, {y}"
                
                case [x, *rest]:
                    return f"List starting with {x}, rest: {rest}"
                
                # Match dictionaries
                case {"name": str(name), "age": int(age)} if age >= 18:
                    return f"Adult: {name}, age {age}"
                
                case {"name": str(name), "age": int(age)}:
                    return f"Minor: {name}, age {age}"
                
                # Match objects/classes
                case {"type": "user", "data": user_data}:
                    return f"User data: {user_data}"
                
                # Wildcard pattern
                case _:
                    return f"Unknown data type: {type(data).__name__}"
        
        # Test cases for pattern matching
        test_cases = [
            0,
            2,
            150,
            [42],
            [1, 2],
            [1, 2, 3, 4, 5],
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 16},
            {"type": "user", "data": {"id": 123}},
            "unexpected string"
        ]
        
        return {case: process_data(case) for case in test_cases}
    
    # Type hints and annotations (Python 3.5+, enhanced in later versions)
    from typing import List, Dict, Optional, Union, Callable, TypeVar, Generic
    
    # Generic types and type variables
    T = TypeVar('T')
    
    class DataContainer(Generic[T]):
        """Generic container class with type hints."""
        
        def __init__(self, items: List[T]) -> None:
            self._items: List[T] = items
        
        def add(self, item: T) -> None:
            """Add an item to the container."""
            self._items.append(item)
        
        def get_all(self) -> List[T]:
            """Get all items from the container."""
            return self._items.copy()
        
        def filter_items(self, predicate: Callable[[T], bool]) -> List[T]:
            """Filter items using a predicate function."""
            return [item for item in self._items if predicate(item)]
        
        def transform(self, transformer: Callable[[T], T]) -> 'DataContainer[T]':
            """Transform all items and return new container."""
            transformed_items = [transformer(item) for item in self._items]
            return DataContainer(transformed_items)
    
    # Advanced type annotations
    def advanced_type_annotations(
        name: str,
        age: int,
        scores: List[float],
        metadata: Optional[Dict[str, Union[str, int]]] = None,
        processor: Callable[[List[float]], float] = sum
    ) -> Dict[str, Union[str, int, float, List[float]]]:
        """Function demonstrating advanced type annotations."""
        
        if metadata is None:
            metadata = {}
        
        average_score = processor(scores) / len(scores) if scores else 0.0
        
        return {
            'name': name,
            'age': age,
            'scores': scores,
            'average': average_score,
            'metadata': metadata
        }
    
    # Decorators and advanced function features
    import functools
    import time
    
    def timing_decorator(func: Callable) -> Callable:
        """Decorator to measure function execution time."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                print(f"{func.__name__} took {execution_time:.4f} seconds")
        return wrapper
    
    def cache_decorator(maxsize: int = 128):
        """Parameterized decorator for caching function results."""
        def decorator(func: Callable) -> Callable:
            cache = {}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Create cache key from arguments
                key = str(args) + str(sorted(kwargs.items()))
                
                if key in cache:
                    return cache[key]
                
                result = func(*args, **kwargs)
                
                # Simple LRU: remove oldest if cache is full
                if len(cache) >= maxsize:
                    oldest_key = next(iter(cache))
                    del cache[oldest_key]
                
                cache[key] = result
                return result
            
            wrapper.cache_info = lambda: {'size': len(cache), 'maxsize': maxsize}
            wrapper.cache_clear = lambda: cache.clear()
            return wrapper
        return decorator
    
    @timing_decorator
    @cache_decorator(maxsize=64)
    def fibonacci(n: int) -> int:
        """Calculate Fibonacci number with timing and caching."""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    # Context managers and advanced with statements
    class DatabaseConnection:
        """Example context manager for database connections."""
        
        def __init__(self, connection_string: str):
            self.connection_string = connection_string
            self.connection = None
            self.transaction = None
        
        def __enter__(self):
            print(f"Connecting to {self.connection_string}")
            self.connection = f"Connection to {self.connection_string}"
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is not None:
                print(f"Error occurred: {exc_value}")
                if self.transaction:
                    print("Rolling back transaction")
            else:
                if self.transaction:
                    print("Committing transaction")
            
            print("Closing connection")
            self.connection = None
            return False  # Don't suppress exceptions
        
        def begin_transaction(self):
            """Begin a database transaction."""
            self.transaction = "Active transaction"
            print("Transaction started")
        
        def execute_query(self, query: str):
            """Execute a database query."""
            if not self.connection:
                raise RuntimeError("No active connection")
            return f"Executed: {query}"
    
    # Multiple context managers
    def demonstrate_context_managers():
        """Demonstrate advanced context manager usage."""
        
        # Multiple context managers in one with statement
        with (
            DatabaseConnection("postgresql://localhost:5432/db") as db1,
            DatabaseConnection("mysql://localhost:3306/db") as db2
        ):
            db1.begin_transaction()
            result1 = db1.execute_query("SELECT * FROM users")
            
            db2.begin_transaction() 
            result2 = db2.execute_query("SELECT * FROM products")
            
            return {'db1_result': result1, 'db2_result': result2}
    
    # Async syntax (basic demonstration)
    async def async_syntax_example():
        """Demonstrate basic async/await syntax."""
        import asyncio
        
        async def fetch_data(url: str) -> str:
            """Simulate async data fetching."""
            print(f"Fetching {url}")
            await asyncio.sleep(0.1)  # Simulate network delay
            return f"Data from {url}"
        
        async def process_multiple_urls():
            """Process multiple URLs concurrently."""
            urls = [
                "https://api1.example.com",
                "https://api2.example.com", 
                "https://api3.example.com"
            ]
            
            # Concurrent execution
            tasks = [fetch_data(url) for url in urls]
            results = await asyncio.gather(*tasks)
            
            return dict(zip(urls, results))
        
        return await process_multiple_urls()
    
    return {
        'walrus_examples': walrus_operator_examples(),
        'pattern_matching': pattern_matching_examples(),
        'type_container': DataContainer,
        'typed_function': advanced_type_annotations,
        'fibonacci_func': fibonacci,
        'context_manager': DatabaseConnection,
        'context_demo': demonstrate_context_managers(),
        'async_example': async_syntax_example
    }

# =============================================================================
# 8. ERROR HANDLING SYNTAX
# =============================================================================

"""
PYTHON ERROR HANDLING:
Comprehensive exception handling and error management
"""

def demonstrate_error_handling():
    """
    COMPREHENSIVE ERROR HANDLING EXAMPLES
    Professional exception handling patterns
    """
    
    # Basic exception handling patterns
    def basic_exception_handling():
        """Demonstrate basic try-except-finally patterns."""
        
        results = []
        
        # Example 1: Basic try-except
        try:
            result = 10 / 2
            results.append(f"Division successful: {result}")
        except ZeroDivisionError:
            results.append("Cannot divide by zero")
        
        # Example 2: Multiple exception types
        test_data = ["10", "abc", "20", "0"]
        for item in test_data:
            try:
                number = int(item)
                result = 100 / number
                results.append(f"100 / {number} = {result}")
            except ValueError:
                results.append(f"'{item}' is not a valid number")
            except ZeroDivisionError:
                results.append(f"Cannot divide by zero (item: {item})")
        
        # Example 3: Catching multiple exceptions in one block
        try:
            user_input = "not_a_number"
            number = int(user_input)
            result = 100 / number
        except (ValueError, ZeroDivisionError) as e:
            results.append(f"Error processing input: {type(e).__name__}: {e}")
        
        # Example 4: Generic exception handling with specific exceptions first
        try:
            # Simulating various potential errors
            import random
            error_type = random.choice(['value', 'type', 'key', 'index'])
            
            if error_type == 'value':
                int("not_a_number")
            elif error_type == 'type':
                "string" + 42
            elif error_type == 'key':
                {"a": 1}["b"]
            else:
                [1, 2, 3][10]
                
        except ValueError as e:
            results.append(f"Value error: {e}")
        except TypeError as e:
            results.append(f"Type error: {e}")
        except KeyError as e:
            results.append(f"Key error: {e}")
        except IndexError as e:
            results.append(f"Index error: {e}")
        except Exception as e:
            results.append(f"Unexpected error: {type(e).__name__}: {e}")
        
        return results
    
    # Advanced exception handling with finally and else
    def advanced_exception_handling():
        """Demonstrate try-except-else-finally patterns."""
        
        execution_log = []
        
        def process_file(filename, operation="read"):
            """Process file with comprehensive error handling."""
            file_handle = None
            
            try:
                execution_log.append(f"Opening file: {filename}")
                
                # Simulate file operations
                if filename.endswith('.txt'):
                    file_handle = f"Handle for {filename}"
                    
                    if operation == "read":
                        content = f"Content of {filename}"
                    elif operation == "write":
                        content = f"Written to {filename}"
                    else:
                        raise ValueError(f"Unsupported operation: {operation}")
                else:
                    raise FileNotFoundError(f"File not found: {filename}")
                
            except FileNotFoundError as e:
                execution_log.append(f"File error: {e}")
                return None
            except ValueError as e:
                execution_log.append(f"Operation error: {e}")
                return None
            except Exception as e:
                execution_log.append(f"Unexpected error: {e}")
                return None
            else:
                # Executes only if no exception occurred
                execution_log.append(f"File processing successful: {filename}")
                return content
            finally:
                # Always executes
                if file_handle:
                    execution_log.append(f"Closing file handle: {filename}")
                execution_log.append(f"Finished processing: {filename}")
        
        # Test the function with different scenarios
        test_files = [
            ("document.txt", "read"),
            ("data.txt", "write"), 
            ("config.txt", "invalid"),
            ("missing.doc", "read")
        ]
        
        results = {}
        for filename, operation in test_files:
            results[f"{filename}_{operation}"] = process_file(filename, operation)
        
        return {
            'results': results,
            'execution_log': execution_log
        }
    
    # Custom exceptions
    class DataValidationError(Exception):
        """Custom exception for data validation errors."""
        
        def __init__(self, field_name, field_value, message="Invalid data"):
            self.field_name = field_name
            self.field_value = field_value
            self.message = message
            super().__init__(self.message)
        
        def __str__(self):
            return f"{self.message}: {self.field_name}='{self.field_value}'"
    
    class BusinessLogicError(Exception):
        """Custom exception for business logic violations."""
        
        def __init__(self, rule_name, details=None):
            self.rule_name = rule_name
            self.details = details or {}
            message = f"Business rule violation: {rule_name}"
            super().__init__(message)
    
    class ConfigurationError(Exception):
        """Custom exception for configuration issues."""
        pass
    
    def demonstrate_custom_exceptions():
        """Demonstrate custom exception usage."""
        
        def validate_user_data(user_data):
            """Validate user data with custom exceptions."""
            
            # Check required fields
            required_fields = ['name', 'email', 'age']
            for field in required_fields:
                if field not in user_data:
                    raise DataValidationError(field, None, "Required field missing")
            
            # Validate name
            if not isinstance(user_data['name'], str) or len(user_data['name']) < 2:
                raise DataValidationError('name', user_data['name'], 
                                        "Name must be string with at least 2 characters")
            
            # Validate email
            if '@' not in user_data['email']:
                raise DataValidationError('email', user_data['email'], 
                                        "Email must contain @ symbol")
            
            # Validate age
            try:
                age = int(user_data['age'])
                if age < 0 or age > 150:
                    raise DataValidationError('age', age, 
                                            "Age must be between 0 and 150")
            except ValueError:
                raise DataValidationError('age', user_data['age'], 
                                        "Age must be a valid integer")
            
            # Business logic validation
            if age < 13:
                raise BusinessLogicError('minimum_age', 
                                       {'current_age': age, 'minimum_required': 13})
            
            return True
        
        def create_user_account(user_data):
            """Create user account with comprehensive error handling."""
            try:
                # Validate input data
                validate_user_data(user_data)
                
                # Check if user already exists (simulated)
                if user_data.get('email') == 'existing@example.com':
                    raise BusinessLogicError('duplicate_email', 
                                           {'email': user_data['email']})
                
                # Simulate account creation
                account_id = hash(user_data['email']) % 100000
                
                return {
                    'success': True,
                    'account_id': account_id,
                    'message': f"Account created for {user_data['name']}"
                }
                
            except DataValidationError as e:
                return {
                    'success': False,
                    'error_type': 'validation',
                    'error_message': str(e),
                    'field_name': e.field_name,
                    'field_value': e.field_value
                }
            except BusinessLogicError as e:
                return {
                    'success': False,
                    'error_type': 'business_logic',
                    'error_message': str(e),
                    'rule_name': e.rule_name,
                    'details': e.details
                }
            except Exception as e:
                return {
                    'success': False,
                    'error_type': 'unexpected',
                    'error_message': str(e)
                }
        
        # Test cases
        test_users = [
            {'name': 'John Doe', 'email': 'john@example.com', 'age': '30'},
            {'name': 'A', 'email': 'short@example.com', 'age': '25'},
            {'name': 'Jane Doe', 'email': 'invalid-email', 'age': '28'},
            {'name': 'Bob Smith', 'email': 'bob@example.com', 'age': 'not-a-number'},
            {'name': 'Alice Johnson', 'email': 'alice@example.com', 'age': '12'},
            {'email': 'missing-name@example.com', 'age': '25'},
            {'name': 'Existing User', 'email': 'existing@example.com', 'age': '35'}
        ]
        
        results = {}
        for i, user_data in enumerate(test_users, 1):
            results[f'test_case_{i}'] = create_user_account(user_data)
        
        return results
    
    # Exception chaining and context
    def demonstrate_exception_chaining():
        """Demonstrate exception chaining with raise from."""
        
        def low_level_function():
            """Simulate a low-level function that might fail."""
            import random
            if random.choice([True, False]):
                raise ValueError("Low-level processing error")
            return "Low-level success"
        
        def mid_level_function():
            """Mid-level function that calls low-level function."""
            try:
                return low_level_function()
            except ValueError as e:
                # Chain the exception with additional context
                raise RuntimeError("Mid-level processing failed") from e
        
        def high_level_function():
            """High-level function with error handling."""
            try:
                return mid_level_function()
            except RuntimeError as e:
                # Access the original exception
                original_error = e.__cause__
                return {
                    'success': False,
                    'error_message': str(e),
                    'original_error': str(original_error) if original_error else None,
                    'error_chain': [str(exc) for exc in [e, original_error] if exc]
                }
        
        # Suppress exception chaining
        def suppress_chaining_example():
            """Demonstrate suppressing exception chaining."""
            try:
                x = 1 / 0
            except ZeroDivisionError:
                # Suppress the original exception context
                raise ValueError("Custom error message") from None
        
        return {
            'chaining_result': high_level_function(),
            'suppress_example': suppress_chaining_example
        }
    
    return {
        'basic_handling': basic_exception_handling(),
        'advanced_handling': advanced_exception_handling(),
        'custom_exceptions': {
            'DataValidationError': DataValidationError,
            'BusinessLogicError': BusinessLogicError,
            'ConfigurationError': ConfigurationError
        },
        'custom_exception_demo': demonstrate_custom_exceptions(),
        'exception_chaining': demonstrate_exception_chaining()
    }# =============================================================================
# 2. COMMENTS & DOCUMENTATION - PROFESSIONAL PRACTICES
# =============================================================================

"""
COMPREHENSIVE DOCUMENTATION GUIDE:
Professional commenting and documentation standards
"""

# Comment types and best practices
comment_standards = {
    "single_line_comments": {
        "syntax": "# This is a single line comment",
        "purpose": "Explain complex logic, provide context",
        "placement": "Above the code it describes",
        "style": "Complete sentences with proper capitalization"
    },
    
    "inline_comments": {
        "syntax": "x = 5  # Initialize counter variable",
        "usage": "Sparingly, for non-obvious code",
        "spacing": "Two spaces before the #",
        "warning": "Don't state the obvious"
    },
    
    "block_comments": {
        "syntax": "# Multiple lines\n# of comments\n# for complex sections",
        "purpose": "Explain algorithms, business logic",
        "formatting": "Each line starts with #"
    },
    
    "docstrings": {
        "syntax": '"""Triple quoted strings for documentation"""',
        "purpose": "Document modules, classes, and functions",
        "accessibility": "Available via help() and __doc__",
        "standards": "Follow PEP 257 conventions"
    }
}

def demonstrate_documentation():
    """
    COMPREHENSIVE DOCUMENTATION EXAMPLES
    Professional documentation patterns and standards
    """
    
    # Example 1: Function with comprehensive docstring
    def calculate_compound_interest(principal, rate, time, compound_frequency=1):
        """
        Calculate compound interest using the standard formula.
        
        This function computes the compound interest on a principal amount
        over a specified period, with customizable compounding frequency.
        
        Args:
            principal (float): The initial amount of money (P)
            rate (float): Annual interest rate as a decimal (r)
            time (float): Time period in years (t)
            compound_frequency (int, optional): Number of times interest
                is compounded per year (n). Defaults to 1.
        
        Returns:
            dict: A dictionary containing:
                - 'final_amount': Total amount after interest
                - 'interest_earned': Interest earned
                - 'effective_rate': Effective annual rate
        
        Raises:
            ValueError: If principal or rate is negative, or if time <= 0
            TypeError: If inputs are not numeric
        
        Example:
            >>> result = calculate_compound_interest(1000, 0.05, 2, 4)
            >>> print(f"Final amount: ${result['final_amount']:.2f}")
            Final amount: $1104.94
            
        Note:
            Formula used: A = P(1 + r/n)^(nt)
            Where A = final amount, P = principal, r = rate, 
            n = compound frequency, t = time
        """
        # Input validation with descriptive comments
        if not all(isinstance(x, (int, float)) for x in [principal, rate, time]):
            raise TypeError("All inputs must be numeric")
        
        if principal < 0 or rate < 0:
            raise ValueError("Principal and rate must be non-negative")
        
        if time <= 0:
            raise ValueError("Time must be positive")
        
        # Calculate compound interest using the standard formula
        # A = P(1 + r/n)^(nt)
        final_amount = principal * ((1 + rate / compound_frequency) ** (compound_frequency * time))
        
        # Calculate derived values
        interest_earned = final_amount - principal
        effective_rate = (final_amount / principal) ** (1 / time) - 1
        
        return {
            'final_amount': round(final_amount, 2),
            'interest_earned': round(interest_earned, 2),
            'effective_rate': round(effective_rate, 4)
        }
    
    # Example 2: Class with comprehensive documentation
    class DataProcessor:
        """
        A comprehensive data processing utility class.
        
        This class provides methods for cleaning, transforming, and analyzing
        data from various sources. It supports multiple data formats and
        provides extensive error handling and logging capabilities.
        
        Attributes:
            processed_count (int): Number of records processed
            error_count (int): Number of errors encountered
            processing_time (float): Total processing time in seconds
            
        Example:
            processor = DataProcessor(max_errors=10)
            result = processor.process_data(raw_data, format='json')
        """
        
        def __init__(self, max_errors=5, verbose=False):
            """
            Initialize the DataProcessor.
            
            Args:
                max_errors (int): Maximum errors before stopping processing
                verbose (bool): Enable verbose output
            """
            self.max_errors = max_errors
            self.verbose = verbose
            self.processed_count = 0
            self.error_count = 0
            self.processing_time = 0.0
            
            # Initialize internal state
            self._start_time = None
            self._current_batch = []
        
        def process_data(self, data, format='auto'):
            """
            Process input data with format detection and error handling.
            
            Args:
                data (various): Input data to process
                format (str): Data format ('json', 'csv', 'xml', 'auto')
            
            Returns:
                dict: Processing results with statistics
                
            Note:
                This method is the main entry point for data processing.
                It automatically detects format if 'auto' is specified.
            """
            import time
            self._start_time = time.time()
            
            try:
                # Format detection logic
                if format == 'auto':
                    format = self._detect_format(data)
                
                # Process based on detected/specified format
                if format == 'json':
                    result = self._process_json(data)
                elif format == 'csv':
                    result = self._process_csv(data)
                else:
                    raise ValueError(f"Unsupported format: {format}")
                
                return result
                
            except Exception as e:
                self.error_count += 1
                if self.verbose:
                    print(f"Processing error: {e}")
                raise
            
            finally:
                # Always update processing time
                if self._start_time:
                    self.processing_time += time.time() - self._start_time
        
        def _detect_format(self, data):
            """
            Detect data format automatically.
            
            This is a private method used internally for format detection.
            It analyzes the data structure and content to determine the format.
            """
            # Implementation would go here
            return 'json'  # Simplified for example
        
        def _process_json(self, data):
            """Process JSON format data."""
            # JSON processing logic would go here
            self.processed_count += 1
            return {'status': 'success', 'format': 'json'}
        
        def _process_csv(self, data):
            """Process CSV format data."""
            # CSV processing logic would go here
            self.processed_count += 1
            return {'status': 'success', 'format': 'csv'}
    
    # Example 3: Module-level documentation
    """
    Module: Advanced Documentation Examples
    
    This module demonstrates professional documentation practices for Python code.
    It includes examples of proper docstring formatting, comment placement,
    and documentation standards that make code maintainable and understandable.
    
    The module covers:
    - Function documentation with comprehensive docstrings
    - Class documentation with attribute descriptions
    - Method documentation with parameter details
    - Private method documentation
    - Module-level documentation
    
    For more information on Python documentation standards, see:
    - PEP 257: Docstring Conventions
    - PEP 8: Style Guide for Python Code
    - Google Style Python Docstrings
    - NumPy Style Python Docstrings
    """
    
    return {
        'compound_interest': calculate_compound_interest,
        'data_processor': DataProcessor,
        'standards': comment_standards
    }

# =============================================================================
# 3. STATEMENTS & EXPRESSIONS - CORE LANGUAGE CONSTRUCTS
# =============================================================================

"""
STATEMENTS VS EXPRESSIONS:
Master the fundamental building blocks of Python code
"""

def demonstrate_statements_expressions():
    """
    COMPREHENSIVE STATEMENTS AND EXPRESSIONS GUIDE
    Understanding the difference and proper usage
    """
    
    # Statement types
    statement_types = {
        "assignment_statements": {
            "simple": "x = 5",
            "multiple": "a, b, c = 1, 2, 3",
            "augmented": "x += 10",
            "walrus": "if (n := len(data)) > 0:"
        },
        
        "expression_statements": {
            "function_call": "print('Hello')",
            "method_call": "list.append(item)",
            "arithmetic": "5 + 3 * 2"
        },
        
        "compound_statements": {
            "if_statement": "if condition:",
            "for_loop": "for item in iterable:",
            "while_loop": "while condition:",
            "try_except": "try: ... except:",
            "with_statement": "with open(file):",
            "function_def": "def function_name():",
            "class_def": "class ClassName:"
        },
        
        "simple_statements": {
            "expression": "2 + 2",
            "assert": "assert x > 0",
            "pass": "pass",
            "del": "del variable",
            "return": "return value",
            "yield": "yield value",
            "raise": "raise Exception",
            "break": "break",
            "continue": "continue",
            "import": "import module",
            "global": "global variable",
            "nonlocal": "nonlocal variable"
        }
    }
    
    # Expression examples
    expression_examples = {
        "arithmetic_expressions": {
            "basic": 2 + 3 * 4,                     # 14
            "parentheses": (2 + 3) * 4,             # 20
            "power": 2 ** 3 ** 2,                   # 512
            "mixed": 10.5 / 2 + 3 * 2               # 11.25
        },
        
        "boolean_expressions": {
            "comparison": 5 > 3 and 2 < 4,          # True
            "membership": 'a' in 'apple',           # True
            "identity": None is None,               # True
            "complex": not (False or True) and 5 > 3 # False
        },
        
        "string_expressions": {
            "concatenation": "Hello" + " " + "World",
            "formatting": f"Value is {42}",
            "multiplication": "Ha" * 3,
            "slicing": "Hello"[1:4]                 # "ell"
        },
        
        "collection_expressions": {
            "list_literal": [1, 2, 3, 4],
            "dict_literal": {"key": "value", "num": 42},
            "set_literal": {1, 2, 3, 4},
            "tuple_literal": (1, 2, 3)
        },
        
        "comprehension_expressions": {
            "list_comp": [x**2 for x in range(5)],
            "dict_comp": {x: x**2 for x in range(5)},
            "set_comp": {x**2 for x in range(5)},
            "gen_exp": (x**2 for x in range(5))
        },
        
        "conditional_expressions": {
            "ternary": "positive" if 5 > 0 else "negative",
            "complex": max([1, 2, 3]) if [1, 2, 3] else 0,
            "nested": "A" if True else ("B" if False else "C")
        }
    }
    
    # Statement vs Expression demonstration
    def statement_expression_demo():
        """Demonstrate the difference between statements and expressions."""
        
        # Expressions can be used anywhere a value is expected
        expression_results = [
            2 + 3,                          # Arithmetic expression
            "hello".upper(),                # Method call expression
            [1, 2, 3][0],                  # Indexing expression
            len([1, 2, 3, 4]),             # Function call expression
            5 if True else 0,              # Conditional expression
            sum(x for x in range(5))       # Generator expression
        ]
        
        # Statements perform actions but don't return values
        x = 10                             # Assignment statement
        if x > 5:                          # If statement
            print(f"x is {x}")             # Expression statement (print call)
        
        for i in range(3):                 # For statement
            x += 1                         # Augmented assignment statement
        
        def example_function():            # Function definition statement
            return x * 2                   # Return statement with expression
        
        try:                               # Try statement
            result = example_function()    # Assignment with function call
        except Exception as e:             # Except clause
            print(f"Error: {e}")           # Expression statement
        
        return {
            'expression_results': expression_results,
            'final_x': x,
            'function_result': result if 'result' in locals() else None
        }
    
    return {
        'statement_types': statement_types,
        'expressions': expression_examples,
        'demo_results': statement_expression_demo()
    }

# =============================================================================
# 4. NAMING CONVENTIONS - PROFESSIONAL STANDARDS
# =============================================================================

"""
PYTHON NAMING CONVENTIONS:
Professional standards for identifiers and code organization
"""

naming_conventions = {
    "pep8_standards": {
        "modules": {
            "style": "lowercase with underscores",
            "examples": ["my_module.py", "data_processor.py", "utils.py"],
            "avoid": ["MyModule.py", "dataProcessor.py"]
        },
        
        "classes": {
            "style": "CapWords (PascalCase)",
            "examples": ["MyClass", "DataProcessor", "HTTPSConnection"],
            "avoid": ["myClass", "my_class", "data_processor"]
        },
        
        "functions_variables": {
            "style": "lowercase with underscores (snake_case)",
            "examples": ["my_function", "user_name", "total_count"],
            "avoid": ["myFunction", "userName", "totalCount"]
        },
        
        "constants": {
            "style": "UPPERCASE with underscores",
            "examples": ["MAX_SIZE", "API_KEY", "DEFAULT_TIMEOUT"],
            "scope": "Module level or class level"
        },
        
        "private_members": {
            "style": "leading underscore",
            "examples": ["_internal_method", "_private_var"],
            "note": "Convention, not enforced"
        },
        
        "special_methods": {
            "style": "double underscores (dunder methods)",
            "examples": ["__init__", "__str__", "__len__"],
            "avoid": "Don't create your own dunder names"
        }
    },
    
    "naming_best_practices": {
        "descriptive_names": {
            "good": ["user_count", "calculate_total", "is_valid"],
            "bad": ["n", "calc", "flag"]
        },
        
        "verb_noun_pattern": {
            "functions": ["get_user", "calculate_tax", "validate_input"],
            "methods": ["save_data", "load_config", "process_request"]
        },
        
        "boolean_naming": {
            "is_predicates": ["is_valid", "is_empty", "is_authenticated"],
            "has_predicates": ["has_permission", "has_data", "has_errors"],
            "can_predicates": ["can_edit", "can_delete", "can_access"]
        },
        
        "collection_naming": {
            "plural": ["users", "items", "results"],
            "descriptive": ["user_list", "item_dict", "result_set"],
            "avoid": ["user", "item", "result"] # for collections
        }
    }
}

def demonstrate_naming_examples():
    """
    COMPREHENSIVE NAMING EXAMPLES
    Professional naming patterns in practice
    """
    
    # Good naming examples
    class UserAuthenticationManager:
        """
        Example class demonstrating excellent naming conventions.
        
        This class follows PEP 8 naming standards throughout,
        with descriptive names that clearly indicate purpose.
        """
        
        # Class constants (UPPER_CASE)
        MAX_LOGIN_ATTEMPTS = 3
        SESSION_TIMEOUT_MINUTES = 30
        DEFAULT_PERMISSION_LEVEL = 'read'
        
        def __init__(self, database_connection, logger=None):
            """Initialize with descriptive parameter names."""
            # Public attributes (snake_case)
            self.database_connection = database_connection
            self.logger = logger
            self.failed_login_count = 0
            self.is_authenticated = False
            self.current_user_id = None
            
            # Private attributes (leading underscore)
            self._session_data = {}
            self._last_activity_timestamp = None
            
            # Very private (name mangling with double underscore)
            self.__encryption_key = self._generate_encryption_key()
        
        def authenticate_user(self, username, password):
            """
            Authenticate user with descriptive method and parameter names.
            
            Args:
                username (str): User's login identifier
                password (str): User's password
                
            Returns:
                bool: True if authentication successful, False otherwise
            """
            # Local variables with clear, descriptive names
            is_username_valid = self._validate_username(username)
            is_password_valid = self._validate_password(password)
            user_account = self._get_user_account(username)
            
            # Boolean variables with is/has/can prefixes
            has_exceeded_attempts = self.failed_login_count >= self.MAX_LOGIN_ATTEMPTS
            is_account_locked = user_account and user_account.get('is_locked', False)
            can_attempt_login = not (has_exceeded_attempts or is_account_locked)
            
            if not can_attempt_login:
                self._log_authentication_failure("Account locked or too many attempts")
                return False
            
            # Process authentication
            if is_username_valid and is_password_valid:
                self._handle_successful_authentication(user_account)
                return True
            else:
                self._handle_failed_authentication(username)
                return False
        
        def _validate_username(self, username):
            """Private method with descriptive name (leading underscore)."""
            if not username or not isinstance(username, str):
                return False
            
            # Clear variable names for validation criteria
            min_length = 3
            max_length = 50
            allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-')
            
            length_is_valid = min_length <= len(username) <= max_length
            characters_are_valid = all(char in allowed_characters for char in username)
            
            return length_is_valid and characters_are_valid
        
        def _validate_password(self, password):
            """Private method demonstrating compound boolean names."""
            if not password:
                return False
            
            # Descriptive boolean variables
            has_minimum_length = len(password) >= 8
            has_uppercase_letter = any(char.isupper() for char in password)
            has_lowercase_letter = any(char.islower() for char in password)
            has_digit = any(char.isdigit() for char in password)
            has_special_character = any(char in "!@#$%^&*()_+-=" for char in password)
            
            # Clear aggregate validation
            meets_complexity_requirements = (
                has_uppercase_letter and
                has_lowercase_letter and
                has_digit and
                has_special_character
            )
            
            return has_minimum_length and meets_complexity_requirements
        
        def _get_user_account(self, username):
            """Retrieve user account with descriptive method name."""
            # Database query would go here
            return {"username": username, "is_locked": False, "user_id": 123}
        
        def _handle_successful_authentication(self, user_account):
            """Handle successful login with clear method name."""
            self.is_authenticated = True
            self.current_user_id = user_account['user_id']
            self.failed_login_count = 0
            self._create_user_session(user_account)
        
        def _handle_failed_authentication(self, username):
            """Handle failed login attempt."""
            self.failed_login_count += 1
            self._log_authentication_failure(f"Failed login for {username}")
        
        def _create_user_session(self, user_account):
            """Create user session with descriptive internal logic."""
            import time
            
            session_id = self._generate_session_id()
            session_start_time = time.time()
            session_expiry_time = session_start_time + (self.SESSION_TIMEOUT_MINUTES * 60)
            
            self._session_data = {
                'session_id': session_id,
                'user_id': user_account['user_id'],
                'start_time': session_start_time,
                'expiry_time': session_expiry_time,
                'permissions': [self.DEFAULT_PERMISSION_LEVEL]
            }
        
        def _generate_session_id(self):
            """Generate unique session identifier."""
            import uuid
            return str(uuid.uuid4())
        
        def _generate_encryption_key(self):
            """Generate encryption key (private method)."""
            import secrets
            return secrets.token_hex(32)
        
        def _log_authentication_failure(self, message):
            """Log authentication failure with proper naming."""
            if self.logger:
                self.logger.warning(f"Authentication failure: {message}")
    
    # Function naming examples
    def calculate_compound_interest_with_fees(principal_amount, annual_interest_rate, 
                                             time_period_years, compounding_frequency=1,
                                             management_fee_percentage=0.01):
        """
        Function demonstrating excellent parameter naming.
        
        All parameters have descriptive names that clearly indicate
        their purpose and expected units/format.
        """
        # Local variables with descriptive names
        base_compound_amount = principal_amount * (
            (1 + annual_interest_rate / compounding_frequency) ** 
            (compounding_frequency * time_period_years)
        )
        
        total_management_fees = base_compound_amount * management_fee_percentage
        final_amount_after_fees = base_compound_amount - total_management_fees
        total_interest_earned = final_amount_after_fees - principal_amount
        effective_annual_return_rate = (
            (final_amount_after_fees / principal_amount) ** (1 / time_period_years) - 1
        )
        
        return {
            'final_amount': final_amount_after_fees,
            'interest_earned': total_interest_earned,
            'fees_paid': total_management_fees,
            'effective_rate': effective_annual_return_rate
        }
    
    return {
        'authentication_manager': UserAuthenticationManager,
        'interest_calculator': calculate_compound_interest_with_fees,
        'naming_standards': naming_conventions
    }
#   To created, simply assign a value to it using the equals sign (=).
#    Do not need to be declared with any particular type
#     You can even change type after they have been set

x = 5
y = "John"
    
# ----------

""" Naming in Python """
# Use consistent and descriptive names 
#   Depending on what you're defining.

""" Python Identifier Naming Formats """
# camelCase: The first letter of the variable is lowercase.
#  Each additional word starts with an uppercase letter.

MyVariable = 10

# PascalCase (also called CapitalCase): The first letter of each word is capitalized, often used for class names

MyVariableClass = 30

# snake_case: Words are lowercase and separated by underscores

my_variable = 20

""" Naming Conventions (depending the situation) """

# Variable Names
#  snake_case 
#   Lowercase letters with underscores 
#    Keep them short but meaningful

my_variable_example = 15

# Function Names
#  snake_case
#   Lowercase letters with underscores
#    Describe short but meaningful

def my_function_example():
    pass
  
# Class Names
#  CapitalizedWords
#   PascalCase / CamelCase
#    Avoid underscores or lowercase-only names

class ShoppingCart:
    def __init__(self):
        self.items = []
        
# Constant Names
#  ALL_CAPS with underscores
#  Should not change during program execution

MAX_USERS = 100
PI_VALUE = 3.14159

# ---------

""" Spacing in Python and break lines """

# Use consistent spacing around operators and after commas
#  Improve readability and maintainability
#   Avoid excessive whitespace
#    Keep it clean and simple

""" Between Operators and Function Calls """

result = 10 + 5
area = my_function_example()

# EXCEPTIONS
#  Do not use space 
#   * Parentheses around function arguments 
#      After the opening parenthesis 
#      Before the closing parenthesis in function calls
#   * Square brackets around list elements
#      After the opening bracket
#      Before the closing bracket in list definitions
#   * Curly braces around dictionary keys and values
#      After the opening brace
#      Before the closing brace in dictionary definitions
#   * Quotes around string literals
#      After the opening quote
#      Before the closing quote in string literals
#  * Commas in function arguments, list elements, and dictionary key-value pairs
#      After the opening comma
#      Before the closing comma in function calls, list definitions, and dictionary definitions

A = 5; C = 10; F = 15
print(A, "B", C, "D", F) 
print([A, C, F]) 
print({"A": A, "C": C, "F": F})

""" Function """ 
#  Use one blank line break between functions

def my_first_function():
    pass

def my_second_function():
    pass
  
""" Inside Functions """
# Use single blank line break to separate logical blocks
#  Inside the same function
do_something = lambda: print("Doing something")
do_something_else = lambda: print("Doing something else")

def my_function():
    do_something() # First logical block

    do_something_else() # Second logical block
    
""" Class """
#  Use two blank lines break between classes

class MyClass:
    def __init__(self):
        pass


class AnotherClass:
    def __init__(self):
        pass  

""" Importing Modules """
# Separate imports sections with a single blank line
#  Standard library imports

#  Third-party imports

#  Local application/library specific imports


# ----------      

""" Importing Modules """
# Use one import statement per line
#  Keep imports at the top of the file
#   Maintain alphabetical order
#    Divide imports into three sections:
#     * Standard library imports
#     * Related third-party imports
#     * Local application/library specific imports
# AVOID use wildcard imports (e.g., from module import *)
#  " * " imports everything from the module

# Standard library imports
"""
import os
import sys

"""

# Third-party imports
"""
import requests
from math import sqrt

"""

# Local application/library specific imports
"""
from mymodule import my_function

"""

# ----------

""" Conditions and Booleans """
# To check if a variable is None,
#  Use 'is None' instead of '== None'.
#   NONE = SINGLETON (a unique instance)
#    More explicit and avoids potential issues 
#     With equality checks.

value = None
if value is None:
    print("Value is not defined")
    
# -----------

""" Length of Lines """
# Limit lines to a maximum of 79 characters 
#  Improves readability, especially in terminals or side-by-side views.
#   Use parentheses and line breaks to split long expressions cleanly.

long_expression = (
    "This is a very long expression "
    "that needs to be split "
    "across multiple lines for better readability."
)

# -----------

""" Cleanliness and Style """
# Aim for a clean and consistent code style
#  Use meaningful variable and function names
#   Keep code DRY (Don't Repeat Yourself)
#    Use comments and docstrings to explain non-obvious code
# AVOID unused variables or print statements

# Use TODO, FIXME, or NOTE to flag areas for attention
# TODO: Implement error handling
# FIXME: Resolve performance issue in data processing
# NOTE: Review code for potential security vulnerabilities


# AVOID use \n in strings for line breaks
#  Can cause issues in some environments
#   Use print() to display messages on separate lines
#    Use print() before input()
#     Ensure consistent behavior across different terminals
print("Enter your favorite color:")
color_6 = input("> ")
print("Color entered:", color_6)

# -----------