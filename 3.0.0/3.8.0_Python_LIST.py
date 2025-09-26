""" 3.8.0_Python_LIST.py """

# =============================================================================
# PYTHON LISTS - COMPREHENSIVE MASTERY GUIDE
# =============================================================================
# Version: 3.8.0 | Educational Excellence Target: 9.5/10
# Purpose: Master Python's most versatile and powerful data structure
# Target: Intermediate Python learners and data processors
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python lists, you will:
✓ Create and manipulate lists efficiently
✓ Apply all list methods and operations
✓ Write powerful list comprehensions
✓ Handle complex data structures and algorithms
✓ Optimize list performance for real-world applications
✓ Debug common list-related issues

🚀 QUICK NAVIGATION:
├── 1. LIST FUNDAMENTALS & CREATION
├── 2. LIST OPERATIONS & METHODS
├── 3. INDEXING & SLICING MASTERY
├── 4. LIST COMPREHENSIONS & GENERATORS
├── 5. NESTED LISTS & MULTIDIMENSIONAL DATA
├── 6. LIST ALGORITHMS & PATTERNS
├── 7. PERFORMANCE & MEMORY OPTIMIZATION
├── 8. COMMON MISTAKES & DEBUGGING
├── 9. REAL-WORLD APPLICATIONS
└── 10. ADVANCED TECHNIQUES & BEST PRACTICES

📊 KEY CONCEPTS:
Lists are ordered, mutable collections that can store any Python object
Perfect for dynamic data, algorithms, and data processing tasks
"""

# =============================================================================
# 1. LIST FUNDAMENTALS & CREATION - COMPLETE GUIDE
# =============================================================================

"""
LIST CREATION METHODS:
Master every way to create and initialize Python lists
"""

# Basic List Creation Examples
def demonstrate_list_creation():
    """
    COMPREHENSIVE LIST CREATION TECHNIQUES
    All methods for creating lists with practical examples
    """
    
    # Empty lists
    empty_list1 = []                    # Most common method
    empty_list2 = list()               # Constructor method
    
    # Lists with initial values
    numbers = [1, 2, 3, 4, 5]          # Integer list
    mixed_types = [1, 'hello', 3.14, True]  # Mixed data types
    nested = [[1, 2], [3, 4], [5, 6]]  # Nested lists
    
    # Lists from other iterables
    from_string = list('hello')         # ['h', 'e', 'l', 'l', 'o']
    from_range = list(range(1, 6))      # [1, 2, 3, 4, 5]
    from_tuple = list((1, 2, 3))        # [1, 2, 3]
    
    # List multiplication (repetition)
    repeated = [0] * 5                  # [0, 0, 0, 0, 0]
    pattern = [1, 2] * 3               # [1, 2, 1, 2, 1, 2]
    
    # Pre-allocated lists for performance
    large_list = [None] * 1000         # Pre-allocated with 1000 None values
    
    # List comprehensions (preview - detailed later)
    squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
    
    return {
        'empty_methods': [empty_list1, empty_list2],
        'basic_lists': [numbers, mixed_types, nested],
        'from_iterables': [from_string, from_range, from_tuple],
        'repeated_patterns': [repeated, pattern],
        'comprehensions': squares
    }

# List Properties and Characteristics
list_characteristics = {
    "mutability": {
        "description": "Lists can be modified after creation",
        "operations": ["append", "extend", "insert", "remove", "pop", "clear"],
        "examples": [
            "my_list = [1, 2, 3]; my_list.append(4)  # [1, 2, 3, 4]",
            "my_list[0] = 10  # [10, 2, 3, 4] - direct assignment"
        ]
    },
    
    "ordering": {
        "description": "Lists maintain insertion order",
        "implications": [
            "Elements have definite positions (indices)",
            "Order is preserved through operations",
            "Slicing maintains relative order"
        ]
    },
    
    "duplicates": {
        "description": "Lists allow duplicate elements",
        "examples": [
            "[1, 1, 2, 2, 3] - duplicates allowed",
            "Different from sets which remove duplicates"
        ]
    },
    
    "dynamic_sizing": {
        "description": "Lists grow and shrink automatically",
        "performance": "O(1) amortized for append, O(n) for insert at beginning"
    }
}

# =============================================================================
# 2. LIST OPERATIONS & METHODS - COMPLETE REFERENCE
# =============================================================================

"""
COMPREHENSIVE LIST METHODS GUIDE:
Master all built-in list operations with practical examples
"""

def demonstrate_list_methods():
    """
    ALL LIST METHODS WITH DETAILED EXAMPLES
    Professional patterns for list manipulation
    """
    
    # Sample data for demonstrations
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    fruits = ['apple', 'banana', 'cherry']
    mixed = [1, 'hello', 3.14, True]
    
    # Adding elements
    adding_examples = {
        "append": {
            "method": "list.append(item)",
            "description": "Add single item to end",
            "example": "fruits.append('date')  # ['apple', 'banana', 'cherry', 'date']",
            "time_complexity": "O(1) amortized"
        },
        
        "extend": {
            "method": "list.extend(iterable)",
            "description": "Add all items from iterable to end",
            "example": "fruits.extend(['elderberry', 'fig'])  # adds multiple items",
            "time_complexity": "O(k) where k is length of iterable"
        },
        
        "insert": {
            "method": "list.insert(index, item)",
            "description": "Insert item at specific position",
            "example": "fruits.insert(1, 'apricot')  # Insert at index 1",
            "time_complexity": "O(n) due to shifting elements"
        }
    }
    
    # Removing elements
    removing_examples = {
        "remove": {
            "method": "list.remove(value)",
            "description": "Remove first occurrence of value",
            "example": "numbers.remove(1)  # Removes first 1",
            "raises": "ValueError if value not found"
        },
        
        "pop": {
            "method": "list.pop(index=-1)",
            "description": "Remove and return item at index (default: last)",
            "examples": [
                "last_item = fruits.pop()      # Remove and return last",
                "first_item = fruits.pop(0)    # Remove and return first"
            ],
            "time_complexity": "O(1) for last, O(n) for others"
        },
        
        "clear": {
            "method": "list.clear()",
            "description": "Remove all elements",
            "example": "fruits.clear()  # [] - empty list",
            "equivalent": "del fruits[:]"
        }
    }
    
    # Searching and counting
    searching_examples = {
        "index": {
            "method": "list.index(value, start=0, end=len)",
            "description": "Return index of first occurrence",
            "example": "numbers.index(5)  # Returns index of first 5",
            "raises": "ValueError if value not found"
        },
        
        "count": {
            "method": "list.count(value)",
            "description": "Return number of occurrences",
            "example": "numbers.count(1)  # Returns 2 (appears twice)",
            "time_complexity": "O(n)"
        }
    }
    
    # Sorting and reversing
    sorting_examples = {
        "sort": {
            "method": "list.sort(key=None, reverse=False)",
            "description": "Sort list in place",
            "examples": [
                "numbers.sort()                    # Ascending order",
                "numbers.sort(reverse=True)        # Descending order",
                "words.sort(key=len)              # Sort by length",
                "words.sort(key=str.lower)        # Case-insensitive"
            ],
            "returns": "None (modifies original list)"
        },
        
        "reverse": {
            "method": "list.reverse()",
            "description": "Reverse list in place",
            "example": "numbers.reverse()  # [6, 2, 9, 5, 1, 4, 1, 3]",
            "time_complexity": "O(n)"
        }
    }
    
    # Creating copies
    copying_examples = {
        "copy": {
            "method": "list.copy()",
            "description": "Create shallow copy",
            "example": "new_list = original.copy()",
            "equivalent": "new_list = original[:]"
        }
    }
    
    return {
        'adding': adding_examples,
        'removing': removing_examples,
        'searching': searching_examples,
        'sorting': sorting_examples,
        'copying': copying_examples
    }

# Practical List Operations Examples
def practical_list_operations():
    """
    REAL-WORLD LIST OPERATION PATTERNS
    Common use cases and professional techniques
    """
    
    # Data processing patterns
    data = [10, 25, 30, 15, 40, 20, 35]
    
    # Finding elements
    max_value = max(data)                    # Built-in functions work with lists
    min_value = min(data)
    total = sum(data)
    average = sum(data) / len(data)
    
    # Filtering data
    high_values = [x for x in data if x > 25]      # List comprehension
    above_average = [x for x in data if x > average]
    
    # Data transformation
    doubled = [x * 2 for x in data]
    normalized = [x / max_value for x in data]
    
    # Batch processing
    def process_in_batches(items, batch_size):
        """Process list in chunks of specified size."""
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            yield batch  # Generator for memory efficiency
    
    # Safe operations (avoiding common errors)
    def safe_remove(lst, value):
        """Remove value if it exists, otherwise do nothing."""
        if value in lst:
            lst.remove(value)
            return True
        return False
    
    def safe_pop(lst, index=None):
        """Pop from list with index validation."""
        if not lst:
            return None
        if index is None:
            return lst.pop()
        if 0 <= index < len(lst):
            return lst.pop(index)
        return None
    
    return {
        'statistics': {'max': max_value, 'min': min_value, 'avg': average},
        'filtered_data': {'high': high_values, 'above_avg': above_average},
        'transformed': {'doubled': doubled, 'normalized': normalized},
        'batch_processing': list(process_in_batches(data, 3))
    }

# =============================================================================
# 3. INDEXING & SLICING MASTERY - ADVANCED TECHNIQUES
# =============================================================================

"""
COMPREHENSIVE INDEXING AND SLICING GUIDE:
Master list element access and manipulation
"""

def demonstrate_indexing_slicing():
    """
    COMPLETE INDEXING AND SLICING REFERENCE
    All patterns for accessing list elements
    """
    
    sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Basic indexing
    indexing_examples = {
        "positive_indexing": {
            "description": "Access elements from beginning (0-based)",
            "examples": [
                ("first_element = sample_list[0]", sample_list[0]),      # 0
                ("second_element = sample_list[1]", sample_list[1]),     # 1
                ("last_element = sample_list[9]", sample_list[9])        # 9
            ]
        },
        
        "negative_indexing": {
            "description": "Access elements from end (-1 is last)",
            "examples": [
                ("last = sample_list[-1]", sample_list[-1]),        # 9
                ("second_last = sample_list[-2]", sample_list[-2]), # 8
                ("first_from_end = sample_list[-10]", sample_list[-10]) # 0
            ]
        }
    }
    
    # Slicing patterns
    slicing_examples = {
        "basic_slicing": {
            "syntax": "list[start:end:step]",
            "examples": [
                ("first_three = sample_list[:3]", sample_list[:3]),      # [0, 1, 2]
                ("last_three = sample_list[-3:]", sample_list[-3:]),     # [7, 8, 9]
                ("middle = sample_list[3:7]", sample_list[3:7]),         # [3, 4, 5, 6]
                ("every_other = sample_list[::2]", sample_list[::2]),    # [0, 2, 4, 6, 8]
                ("reverse = sample_list[::-1]", sample_list[::-1])       # [9, 8, 7, ..., 0]
            ]
        },
        
        "advanced_slicing": {
            "examples": [
                ("skip_first_last = sample_list[1:-1]", sample_list[1:-1]),        # [1, 2, ..., 8]
                ("every_third = sample_list[::3]", sample_list[::3]),              # [0, 3, 6, 9]
                ("reverse_every_two = sample_list[::-2]", sample_list[::-2]),      # [9, 7, 5, 3, 1]
                ("middle_reverse = sample_list[7:2:-1]", sample_list[7:2:-1])      # [7, 6, 5, 4, 3]
            ]
        }
    }
    
    # Slice assignment (modifying lists)
    modification_examples = {
        "replace_elements": {
            "description": "Replace multiple elements with slice assignment",
            "examples": [
                "my_list[1:4] = [10, 20, 30]  # Replace elements 1-3",
                "my_list[::2] = [100] * 5     # Replace every other element",
                "my_list[2:2] = [99, 98]      # Insert without replacing"
            ]
        },
        
        "delete_elements": {
            "description": "Delete elements using slice assignment",
            "examples": [
                "del my_list[1:4]      # Delete elements 1-3",
                "my_list[1:4] = []     # Same as above",
                "del my_list[::2]      # Delete every other element"
            ]
        }
    }
    
    return {
        'indexing': indexing_examples,
        'slicing': slicing_examples,
        'modification': modification_examples
    }

# Advanced Indexing Techniques
def advanced_indexing_patterns():
    """
    PROFESSIONAL INDEXING PATTERNS
    Real-world techniques for complex data access
    """
    
    # Multi-dimensional list indexing
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Safe indexing patterns
    def safe_get(lst, index, default=None):
        """Get list element safely with default value."""
        try:
            return lst[index]
        except IndexError:
            return default
    
    def safe_slice(lst, start=None, end=None, step=None):
        """Safe slicing that handles out-of-bounds indices."""
        length = len(lst)
        if start is not None and start > length:
            return []
        return lst[start:end:step]
    
    # Dynamic indexing
    def get_elements_by_condition(lst, condition_func):
        """Get elements and their indices based on condition."""
        return [(i, value) for i, value in enumerate(lst) if condition_func(value)]
    
    # Circular indexing (wrap around)
    def circular_get(lst, index):
        """Get element with circular indexing (wraps around)."""
        return lst[index % len(lst)] if lst else None
    
    examples = [
        ("Matrix element: matrix[1][2]", matrix[1][2]),           # 6
        ("Safe get: safe_get([1,2,3], 10, 'N/A')", safe_get([1,2,3], 10, 'N/A')),
        ("Circular: circular_get([1,2,3], 5)", circular_get([1,2,3], 5)),  # Same as index 2
    ]
    
    return {
        'matrix_example': matrix,
        'safe_functions': [safe_get, safe_slice, get_elements_by_condition],
        'examples': examples
    }

# =============================================================================
# 4. LIST COMPREHENSIONS & GENERATORS - POWERFUL PATTERNS
# =============================================================================

"""
COMPREHENSIVE LIST COMPREHENSIONS:
Master Python's most powerful list creation technique
"""

def demonstrate_list_comprehensions():
    """
    COMPLETE LIST COMPREHENSION GUIDE
    From basic to advanced patterns with performance insights
    """
    
    # Basic list comprehension syntax
    basic_examples = {
        "squares": {
            "comprehension": "[x**2 for x in range(5)]",
            "result": [x**2 for x in range(5)],
            "equivalent_loop": """
            squares = []
            for x in range(5):
                squares.append(x**2)
            """,
            "performance": "~2x faster than equivalent loop"
        },
        
        "filtering": {
            "comprehension": "[x for x in range(10) if x % 2 == 0]",
            "result": [x for x in range(10) if x % 2 == 0],
            "description": "Filter even numbers from 0-9"
        },
        
        "transformation": {
            "comprehension": "[word.upper() for word in ['hello', 'world']]",
            "result": [word.upper() for word in ['hello', 'world']],
            "description": "Transform strings to uppercase"
        }
    }
    
    # Advanced list comprehension patterns
    advanced_examples = {
        "nested_loops": {
            "comprehension": "[(x, y) for x in range(3) for y in range(2)]",
            "result": [(x, y) for x in range(3) for y in range(2)],
            "description": "Cartesian product of two ranges"
        },
        
        "conditional_expression": {
            "comprehension": "[x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]]",
            "result": [x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]],
            "description": "Replace negative numbers with 0"
        },
        
        "multiple_conditions": {
            "comprehension": "[x for x in range(20) if x % 2 == 0 if x % 3 == 0]",
            "result": [x for x in range(20) if x % 2 == 0 if x % 3 == 0],
            "description": "Numbers divisible by both 2 and 3"
        },
        
        "nested_comprehension": {
            "comprehension": "[[j for j in range(i)] for i in range(4)]",
            "result": [[j for j in range(i)] for i in range(4)],
            "description": "Create nested lists with increasing lengths"
        }
    }
    
    # Real-world list comprehension examples
    practical_examples = {
        "data_processing": {
            "description": "Process CSV-like data",
            "data": [
                "name,age,city",
                "John,25,NYC", 
                "Jane,30,LA",
                "Bob,35,Chicago"
            ],
            "comprehension": "[line.split(',') for line in data[1:]]",
            "result": [line.split(',') for line in [
                "John,25,NYC", "Jane,30,LA", "Bob,35,Chicago"
            ]]
        },
        
        "file_filtering": {
            "description": "Filter files by extension",
            "files": ["doc.txt", "image.jpg", "script.py", "data.csv", "photo.png"],
            "comprehension": "[f for f in files if f.endswith(('.jpg', '.png'))]",
            "result": [f for f in ["doc.txt", "image.jpg", "script.py", "data.csv", "photo.png"] 
                      if f.endswith(('.jpg', '.png'))]
        },
        
        "mathematical_operations": {
            "description": "Statistical calculations",
            "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "mean": "sum(data) / len(data)",
            "deviations": "[x - mean for x in data]",
            "squared_deviations": "[(x - mean)**2 for x in data]"
        }
    }
    
    return {
        'basic': basic_examples,
        'advanced': advanced_examples,
        'practical': practical_examples
    }

# Generator Expressions (Memory-Efficient Alternative)
def demonstrate_generator_expressions():
    """
    GENERATOR EXPRESSIONS VS LIST COMPREHENSIONS
    When to use generators for memory efficiency
    """
    
    # Memory comparison examples
    import sys
    
    # List comprehension (creates entire list in memory)
    list_comp = [x**2 for x in range(1000)]
    list_memory = sys.getsizeof(list_comp)
    
    # Generator expression (lazy evaluation)
    gen_expr = (x**2 for x in range(1000))
    gen_memory = sys.getsizeof(gen_expr)
    
    examples = {
        "memory_usage": {
            "list_comprehension_memory": f"{list_memory} bytes",
            "generator_memory": f"{gen_memory} bytes",
            "memory_savings": f"~{(list_memory - gen_memory) / list_memory * 100:.1f}% savings"
        },
        
        "use_cases": {
            "list_comprehension": "When you need the entire result immediately",
            "generator_expression": "When processing large datasets or streaming data",
            "example": "sum(x**2 for x in range(1000000))  # Memory efficient"
        },
        
        "conversion": {
            "to_list": "list(gen_expr)  # Convert generator to list",
            "to_tuple": "tuple(gen_expr)  # Convert to tuple",
            "iterate_once": "Generators can only be iterated once"
        }
    }
    
    return examples

# =============================================================================
# 5. NESTED LISTS & MULTIDIMENSIONAL DATA - ADVANCED STRUCTURES
# =============================================================================

"""
MULTIDIMENSIONAL DATA STRUCTURES:
Handle complex nested data with confidence
"""

def demonstrate_nested_lists():
    """
    COMPREHENSIVE NESTED LIST OPERATIONS
    Master multidimensional data structures
    """
    
    # Creating nested lists
    creation_methods = {
        "manual_creation": {
            "2D_matrix": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            "jagged_array": [
                [1],
                [2, 3],
                [4, 5, 6],
                [7, 8, 9, 10]
            ],
            "3D_structure": [
                [[1, 2], [3, 4]],
                [[5, 6], [7, 8]]
            ]
        },
        
        "programmatic_creation": {
            "zeros_matrix": "[[0 for _ in range(cols)] for _ in range(rows)]",
            "identity_matrix": "[[1 if i==j else 0 for j in range(n)] for i in range(n)]",
            "multiplication_table": "[[i*j for j in range(1, 11)] for i in range(1, 11)]"
        }
    }
    
    # Common operations on nested lists
    def matrix_operations():
        """Demonstrate common matrix operations."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        # Accessing elements
        element = matrix[1][2]  # Row 1, Column 2 = 6
        
        # Getting rows and columns
        row_1 = matrix[1]                    # [4, 5, 6]
        col_1 = [row[1] for row in matrix]   # [2, 5, 8]
        
        # Matrix transpose
        transpose = [[matrix[i][j] for i in range(len(matrix))] 
                    for j in range(len(matrix[0]))]
        
        # Flattening matrix
        flattened = [item for row in matrix for item in row]
        
        return {
            'original': matrix,
            'element': element,
            'row': row_1,
            'column': col_1,
            'transpose': transpose,
            'flattened': flattened
        }
    
    # Deep vs shallow copy considerations
    copy_examples = {
        "shallow_copy_problem": {
            "code": """
            original = [[1, 2], [3, 4]]
            shallow = original.copy()
            shallow[0][0] = 999  # Modifies original too!
            """,
            "issue": "Nested objects are still shared"
        },
        
        "deep_copy_solution": {
            "code": """
            import copy
            original = [[1, 2], [3, 4]]
            deep = copy.deepcopy(original)
            deep[0][0] = 999  # Original unchanged
            """,
            "solution": "Use copy.deepcopy for nested structures"
        }
    }
    
    return {
        'creation': creation_methods,
        'operations': matrix_operations(),
        'copying': copy_examples
    }

# =============================================================================
# 6. LIST ALGORITHMS & PATTERNS - PROFESSIONAL TECHNIQUES
# =============================================================================

"""
ALGORITHMIC PATTERNS WITH LISTS:
Common algorithms and professional coding patterns
"""

def demonstrate_list_algorithms():
    """
    ESSENTIAL LIST ALGORITHMS FOR INTERVIEWS AND REAL-WORLD USE
    """
    
    # Searching algorithms
    def linear_search(lst, target):
        """Find index of target value using linear search."""
        for i, value in enumerate(lst):
            if value == target:
                return i
        return -1  # Not found
    
    def binary_search(sorted_lst, target):
        """Find target in sorted list using binary search."""
        left, right = 0, len(sorted_lst) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if sorted_lst[mid] == target:
                return mid
            elif sorted_lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Not found
    
    # Sorting algorithms (educational - use built-in sort() for production)
    def bubble_sort(lst):
        """Bubble sort implementation (O(n²))."""
        n = len(lst)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst
    
    def quicksort(lst):
        """Quicksort implementation (O(n log n) average)."""
        if len(lst) <= 1:
            return lst
        
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        
        return quicksort(left) + middle + quicksort(right)
    
    # Common patterns
    def find_duplicates(lst):
        """Find all duplicate values in list."""
        seen = set()
        duplicates = set()
        
        for item in lst:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        
        return list(duplicates)
    
    def remove_duplicates(lst):
        """Remove duplicates while preserving order."""
        seen = set()
        result = []
        
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        
        return result
    
    def find_max_subarray_sum(lst):
        """Find maximum sum of contiguous subarray (Kadane's algorithm)."""
        max_sum = current_sum = lst[0]
        
        for num in lst[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    # Two pointers technique
    def two_sum(lst, target):
        """Find two numbers that sum to target."""
        num_map = {}
        
        for i, num in enumerate(lst):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []  # No solution found
    
    def merge_sorted_lists(list1, list2):
        """Merge two sorted lists into one sorted list."""
        result = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        
        # Add remaining elements
        result.extend(list1[i:])
        result.extend(list2[j:])
        
        return result
    
    return {
        'searching': {'linear': linear_search, 'binary': binary_search},
        'sorting': {'bubble': bubble_sort, 'quick': quicksort},
        'patterns': {
            'duplicates': find_duplicates,
            'remove_dups': remove_duplicates,
            'max_subarray': find_max_subarray_sum,
            'two_sum': two_sum,
            'merge': merge_sorted_lists
        }
    }

# =============================================================================
# 7. PERFORMANCE & MEMORY OPTIMIZATION - PROFESSIONAL INSIGHTS
# =============================================================================

"""
LIST PERFORMANCE OPTIMIZATION:
Write efficient, scalable list operations
"""

performance_guide = {
    "time_complexity": {
        "access": {
            "operation": "list[index]",
            "complexity": "O(1)",
            "note": "Constant time for any valid index"
        },
        "search": {
            "operation": "item in list",
            "complexity": "O(n)",
            "note": "Linear search through elements"
        },
        "append": {
            "operation": "list.append(item)",
            "complexity": "O(1) amortized",
            "note": "Occasional O(n) when resizing"
        },
        "insert": {
            "operation": "list.insert(0, item)",
            "complexity": "O(n)",
            "note": "Must shift all existing elements"
        },
        "delete": {
            "operation": "list.pop(0)",
            "complexity": "O(n)",
            "note": "Must shift remaining elements"
        }
    },
    
    "memory_optimization": {
        "pre_allocation": {
            "technique": "Pre-allocate lists when size is known",
            "example": "[None] * expected_size",
            "benefit": "Avoids repeated memory allocation"
        },
        "generators": {
            "technique": "Use generators for large datasets",
            "example": "(x for x in large_data if condition)",
            "benefit": "Lazy evaluation saves memory"
        },
        "list_reuse": {
            "technique": "Reuse existing lists instead of creating new ones",
            "example": "result.clear(); result.extend(new_data)",
            "benefit": "Reduces garbage collection"
        }
    },
    
    "common_performance_mistakes": {
        "repeated_concatenation": {
            "bad": "result = []; result = result + [item]  # O(n²)",
            "good": "result = []; result.append(item)     # O(n)",
            "reason": "List concatenation creates new list each time"
        },
        "membership_testing": {
            "bad": "item in large_list  # O(n) each time",
            "good": "item_set = set(large_list); item in item_set  # O(1)",
            "reason": "Set membership is much faster"
        },
        "unnecessary_sorting": {
            "bad": "max(sorted(lst))",
            "good": "max(lst)",
            "reason": "Built-in functions are optimized"
        }
    }
}

def demonstrate_performance_techniques():
    """
    PRACTICAL PERFORMANCE OPTIMIZATION EXAMPLES
    """
    import time
    
    # Efficient list building
    def build_list_efficiently(n):
        """Demonstrate efficient list building techniques."""
        
        # Method 1: Append (good)
        start_time = time.time()
        result1 = []
        for i in range(n):
            result1.append(i)
        append_time = time.time() - start_time
        
        # Method 2: List comprehension (better)
        start_time = time.time()
        result2 = [i for i in range(n)]
        comprehension_time = time.time() - start_time
        
        # Method 3: Pre-allocation (best for known size)
        start_time = time.time()
        result3 = [None] * n
        for i in range(n):
            result3[i] = i
        prealloc_time = time.time() - start_time
        
        return {
            'append_time': append_time,
            'comprehension_time': comprehension_time,
            'preallocation_time': prealloc_time
        }
    
    # Memory-efficient processing
    def process_large_dataset(data):
        """Process large dataset memory-efficiently."""
        
        # Memory-efficient: Generator expression
        def memory_efficient():
            return sum(x * 2 for x in data if x % 2 == 0)
        
        # Memory-intensive: List comprehension
        def memory_intensive():
            filtered = [x * 2 for x in data if x % 2 == 0]
            return sum(filtered)
        
        return memory_efficient, memory_intensive
    
    return {
        'building_techniques': build_list_efficiently,
        'processing_techniques': process_large_dataset
    }

# =============================================================================
# QUICK REFERENCE SUMMARY - MEMORIZE THESE!
# =============================================================================

"""
PYTHON LISTS CHEAT SHEET - ESSENTIAL OPERATIONS

CREATION:
[]                     # Empty list
[1, 2, 3]             # Literal creation
list(iterable)        # From iterable
[x for x in range(5)] # List comprehension

ADDING ELEMENTS:
list.append(item)      # Add to end - O(1)
list.extend(iterable)  # Add multiple - O(k)
list.insert(i, item)   # Insert at index - O(n)

REMOVING ELEMENTS:
list.remove(value)     # Remove first occurrence - O(n)
list.pop(index)        # Remove and return - O(1) for last
list.clear()           # Remove all - O(n)

SEARCHING:
item in list           # Membership test - O(n)
list.index(value)      # Find index - O(n)
list.count(value)      # Count occurrences - O(n)

SORTING:
list.sort()            # Sort in place - O(n log n)
sorted(list)           # Return new sorted list
list.reverse()         # Reverse in place - O(n)

SLICING:
list[start:end:step]   # Slice notation
list[::-1]             # Reverse copy
list[::2]              # Every other element

COMPREHENSIONS:
[expr for item in iterable]                    # Basic
[expr for item in iterable if condition]      # With filter
[expr if cond else alt for item in iterable]  # With conditional

PERFORMANCE TIPS:
• Use append() instead of concatenation
• Use list comprehensions for speed
• Pre-allocate when size is known
• Convert to set for membership testing
• Use generators for memory efficiency
"""
p2 = [4, 5, 6]
p3 = [7, 8, 9]
p4 = [10]

print([p1, p2])
# [[1, 2, 3], [4, 5, 6]]

# OR

p10 = ([p1],
... [p2])

print(p10)
# [[1, 2, 3], [4, 5, 6]]

# ----------

"""Indexed List"""
# Lists are indexed, meaning each element has a unique number position.
#   Works similar to an array and allows you to locate an element using a numerical index
#       The first element (counting left to right) is at index 0, the second at index 1, and so on.
#           The last element can also be accessed with negative indexing: -1 for last, -2 for second to last, etc.

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   
-6  -5  -4  -3  -2  -1
"""

""" Slice index"""
# An indexed list can be sliced, allowing you to obtain a sub-list.
#   The slice is defined by two indices, the start and the end.
#       The start index is included in the slice, while the end index is excluded.
#           The slice is defined by the syntax [start:end].
#               Following the logical list recomposition rule: lst[:i] + lst[i:]
#                   The length of a slice is the difference of the indices
#                       my_list[1:3] length equals 2

p1 = [1, 2, 3]
p2 = [4, 5, 6]
p3 = [7, 8, 9]
p4 = [10]

p1[:2]   # Slice from the beginning of the list to index 2 (excluding index 2)
# [1, 2]

p1[2:]   # Slice from index 2 to the end of the list
# [3]

p1[0:2]  # Slice from index 0 to index 2 (excluding index 2)
# [1, 2]

p1[2:5]  # Slice from index 2 to index 5 (excluding index 5)
# [3]

p1[:]    # Slice the entire string
# [1, 2, 3]

p1[::2]  # Slice the string with a step of 2
# [1, 3]

p1[::-1] # Slice the string in reverse order
# [3, 2, 1]

p1[-2:]  # Slice the last two characters of the string
# [2, 3]

p1[-2:-1] # Slice the last two characters of the string
# [2]

""" Slice out of range can be handled without error. """
#   The slice will be empty if the first index is greater than the last index.

p1[42:]  # Slice from index 42 to the end of index
# ""             # Empty string

p1[:42]  # Slice from index 0 to index 42 (excluding index 42)
# [1, 2, 3]       # The entire string, included the character after the last number of the index

# ----------

"""Modify INDEX items"""
#   Lists are mutable, meaning you can change the value of an item in a list.
#       You can change the value of an item in a list 
#           Assigning a new value to the index of the item.

""" Change the value of an item in a INDEX """
#  You can change the value of an item in a list by assigning a new value to the index of the item.

p10 = [10, 22, 30]

p10[1] = 20
print(p10)
# [10, 20, 30]

""" Add an item to a INDEX """
# You can add an item to a list by using the append() method.

p10 = [10, 20, 30]

p10.append(40)
print(p10)
# [10, 20, 30, 40]

""" Remove an item from a INDEX """
# You can remove an item from a list by using the remove() method.

p10 = [10, 20, 30]

p10.remove(20)
print(p10)
# [10, 30]

""" Sort a INDEX """
# You can sort a list by using the sort() method.

p10 = [30, 10, 20]

p10.sort()
print(p10)
# [10, 20, 30]

""" Reverse a INDEX """
# You can reverse a list by using the reverse() method.

p10 = [10, 20, 30]

p10.reverse()
print(p10)
# [30, 20, 10]

""" Clear a INDEX """
# You can clear a list by using the clear() method.

p10 = [10, 20, 30]

p10.clear()
print(p10)
# []

#OR

# You can clear a list by using the del statement.

p10 = [10, 20, 30]

p10 = []
print(p10)
# []

# ----------

""" INDEX Methods """
# List methods are functions that can be used to manipulate lists.
#   They are called on a list object and can be used to perform various operations on the list.

#  append()   Adds an element at the end of the list
#  clear()	  Removes all the elements from the list
#  copy()	  Returns a copy of the list
#  count()	  Returns the number of elements with the specified value
#  extend()	  Add the elements of a list (or any iterable), to the end of the current list
#  index()	  Returns the index of the first element with the specified value
#  insert()	  Adds an element at the specified position
#  pop()	  Removes the element at the specified position
#  remove()	  Removes the item with the specified value
#  reverse()  Reverses the order of the list
#  sort()     Sorts the list

# ---------
