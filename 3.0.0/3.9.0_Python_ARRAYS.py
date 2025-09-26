""" 3.9.0_Python_ARRAYS.py """

# =============================================================================
# PYTHON ARRAYS - COMPLETE MASTERY GUIDE
# =============================================================================
# Version: 3.9.0 | Educational Excellence Target: 9.5/10
# Purpose: Master Python arrays with comprehensive understanding
# Target: Beginner to Advanced Python programmers
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python arrays, you will:
✓ Understand Python array module vs lists and NumPy arrays
✓ Master array creation, manipulation, and memory efficiency
✓ Apply array operations for numeric data processing
✓ Understand type codes and memory optimization
✓ Implement array algorithms and data structures
✓ Use arrays in performance-critical applications

🚀 QUICK NAVIGATION:
├── 1. ARRAY FUNDAMENTALS & OVERVIEW (FOUNDATION)
├── 2. ARRAY CREATION & INITIALIZATION (CREATION)
├── 3. ARRAY OPERATIONS & METHODS (MANIPULATION)
├── 4. ARRAY INDEXING & SLICING (ACCESS)
├── 5. ARRAY TYPE CODES & MEMORY (EFFICIENCY)
├── 6. ARRAY VS LIST COMPARISON (PERFORMANCE)
├── 7. ARRAY ALGORITHMS & PATTERNS (ALGORITHMS)
├── 8. BUFFER PROTOCOL & MEMORYVIEW (ADVANCED)
├── 9. ARRAY SERIALIZATION & I/O (PERSISTENCE)
└── 10. REAL-WORLD ARRAY APPLICATIONS

🔍 CORE CONCEPT:
Python arrays (from the array module) are homogeneous, type-specific
collections optimized for memory efficiency and numeric operations,
distinct from lists and NumPy arrays.
"""

# =============================================================================
# 1. ARRAY FUNDAMENTALS & OVERVIEW - FOUNDATION
# =============================================================================

"""
PYTHON ARRAYS COMPLETE REFERENCE:
Understanding arrays, their purpose, and relationship to other data structures
"""

def demonstrate_array_fundamentals():
    """
    COMPREHENSIVE ARRAY FUNDAMENTALS OVERVIEW
    Master array concepts, characteristics, and comparisons
    """
    
    import array
    import sys
    
    # Array characteristics and properties
    def array_characteristics():
        """Demonstrate core array characteristics."""
        
        # Create different array types
        int_array = array.array('i', [1, 2, 3, 4, 5])
        float_array = array.array('f', [1.1, 2.2, 3.3])
        byte_array = array.array('B', [65, 66, 67, 68])
        
        characteristics = {
            'homogeneous_type': True,  # All elements must be same type
            'mutable': True,           # Can be modified after creation
            'ordered': True,           # Elements maintain order
            'indexed': True,           # Elements accessible by index
            'dynamic_size': True,      # Size can change
            'memory_efficient': True,  # More efficient than lists for numeric data
        }
        
        # Type information
        type_info = {
            'int_array_typecode': int_array.typecode,
            'float_array_typecode': float_array.typecode,
            'byte_array_typecode': byte_array.typecode,
            'int_array_itemsize': int_array.itemsize,      # Bytes per element
            'float_array_itemsize': float_array.itemsize,
            'byte_array_itemsize': byte_array.itemsize,
        }
        
        # Memory usage comparison
        def memory_comparison():
            """Compare memory usage of arrays vs lists."""
            
            # Create equivalent data structures
            data = list(range(1000))
            list_obj = data
            array_obj = array.array('i', data)
            
            # Calculate memory usage
            list_size = sys.getsizeof(list_obj) + sum(sys.getsizeof(item) for item in list_obj)
            array_size = sys.getsizeof(array_obj)  # Array stores data more efficiently
            
            return {
                'list_memory_bytes': list_size,
                'array_memory_bytes': array_size,
                'memory_ratio': list_size / array_size if array_size > 0 else 'N/A',
                'space_saved_percent': ((list_size - array_size) / list_size * 100) if list_size > 0 else 0
            }
        
        memory_info = memory_comparison()
        
        return {
            'core_characteristics': characteristics,
            'type_information': type_info,
            'memory_comparison': memory_info
        }
    
    # Array vs other data structures
    def array_comparisons():
        """Compare arrays with lists, tuples, and NumPy arrays."""
        
        # Feature comparison matrix
        feature_comparison = {
            'data_structure': ['array.array', 'list', 'tuple', 'numpy.array'],
            'homogeneous': [True, False, False, True],
            'mutable': [True, True, False, True],
            'memory_efficient': [True, False, False, True],
            'type_checking': [True, False, False, True],
            'mathematical_ops': [False, False, False, True],
            'multi_dimensional': [False, False, False, True],
            'built_in': [True, True, True, False],
        }
        
        # Performance characteristics
        performance_comparison = {
            'creation_speed': 'list > array > numpy.array',
            'memory_usage': 'array ≈ numpy < tuple < list',
            'element_access': 'list ≈ array ≈ tuple ≈ numpy',
            'mathematical_ops': 'numpy >> array > list',
            'append_operations': 'list ≈ array > tuple (immutable)',
        }
        
        # Use case recommendations
        use_cases = {
            'array.array': [
                'Homogeneous numeric data',
                'Memory-constrained environments', 
                'Simple numeric operations',
                'Data serialization/deserialization'
            ],
            'list': [
                'Heterogeneous data',
                'General-purpose collections',
                'Frequent insertions/deletions',
                'Mixed data types'
            ],
            'tuple': [
                'Immutable sequences',
                'Dictionary keys',
                'Function arguments',
                'Configuration data'
            ],
            'numpy.array': [
                'Scientific computing',
                'Mathematical operations',
                'Multi-dimensional data',
                'Broadcasting and vectorization'
            ]
        }
        
        return {
            'feature_comparison': feature_comparison,
            'performance_comparison': performance_comparison,
            'use_case_recommendations': use_cases
        }
    
    # Array limitations and constraints
    def array_limitations():
        """Demonstrate array limitations and constraints."""
        
        limitations = {
            'type_homogeneity': 'All elements must be same type',
            'limited_types': 'Only supports specific numeric types',
            'no_mixed_data': 'Cannot store strings, objects, etc. together',
            'no_native_math': 'No built-in mathematical operations',
            'single_dimension': 'Only 1D arrays (no matrices)',
            'platform_dependent': 'Some type sizes vary by platform'
        }
        
        # Demonstration of type constraints
        constraint_examples = []
        
        try:
            # This will work - homogeneous integers
            valid_array = array.array('i', [1, 2, 3, 4])
            constraint_examples.append({
                'operation': 'array.array("i", [1, 2, 3, 4])',
                'success': True,
                'result': str(valid_array)
            })
        except Exception as e:
            constraint_examples.append({
                'operation': 'homogeneous integers',
                'success': False,
                'error': str(e)
            })
        
        try:
            # This will fail - mixed types
            mixed_array = array.array('i', [1, 2.5, 3, 4])
            constraint_examples.append({
                'operation': 'array.array("i", [1, 2.5, 3, 4])',
                'success': True,
                'result': str(mixed_array)
            })
        except Exception as e:
            constraint_examples.append({
                'operation': 'mixed int and float',
                'success': False,
                'error': str(e)
            })
        
        try:
            # This will fail - wrong type for array
            string_array = array.array('i', ['hello', 'world'])
            constraint_examples.append({
                'operation': 'array.array("i", ["hello", "world"])',
                'success': True,
                'result': str(string_array)
            })
        except Exception as e:
            constraint_examples.append({
                'operation': 'strings in integer array',
                'success': False,
                'error': str(e)
            })
        
        return {
            'limitations_list': limitations,
            'constraint_examples': constraint_examples
        }
    
    # Execute all fundamental demonstrations
    characteristics = array_characteristics()
    comparisons = array_comparisons()
    limitations = array_limitations()
    
    return {
        'array_characteristics': characteristics,
        'comparisons_with_others': comparisons,
        'limitations_and_constraints': limitations
    }

# =============================================================================
# 2. ARRAY CREATION & INITIALIZATION - CREATION PATTERNS
# =============================================================================

"""
ARRAY CREATION MASTERY:
Comprehensive array creation and initialization techniques
"""

def demonstrate_array_creation():
    """
    COMPREHENSIVE ARRAY CREATION DEMONSTRATION
    Master all array creation patterns and initialization methods
    """
    
    import array
    import struct
    
    # Basic array creation patterns
    def basic_creation_patterns():
        """Demonstrate basic array creation methods."""
        
        # Empty arrays
        empty_arrays = {
            'empty_int': array.array('i'),
            'empty_float': array.array('f'),
            'empty_double': array.array('d'),
            'empty_byte': array.array('B'),
        }
        
        # Arrays with initial data
        initialized_arrays = {
            'from_list': array.array('i', [1, 2, 3, 4, 5]),
            'from_tuple': array.array('f', (1.1, 2.2, 3.3)),
            'from_range': array.array('i', range(10)),
            'from_generator': array.array('i', (x*2 for x in range(5))),
        }
        
        # String and bytes initialization
        string_byte_arrays = {
            'from_string': array.array('u', 'Hello'),  # Unicode characters
            'from_bytes': array.array('B', b'Hello'),   # Byte values
            'byte_values': array.array('B', [72, 101, 108, 108, 111]),  # ASCII values for "Hello"
        }
        
        # Convert to regular lists for display
        result = {}
        for category, arrays in [
            ('empty_arrays', empty_arrays),
            ('initialized_arrays', initialized_arrays), 
            ('string_byte_arrays', string_byte_arrays)
        ]:
            result[category] = {}
            for name, arr in arrays.items():
                result[category][name] = {
                    'typecode': arr.typecode,
                    'length': len(arr),
                    'data': list(arr) if len(arr) <= 20 else list(arr)[:20] + ['...'],
                    'itemsize': arr.itemsize
                }
        
        return result
    
    # Advanced creation patterns
    def advanced_creation_patterns():
        """Demonstrate advanced array creation techniques."""
        
        # Array from binary data
        def from_binary_data():
            """Create arrays from binary data."""
            
            # Pack data using struct
            binary_data = struct.pack('5i', 1, 2, 3, 4, 5)
            
            # Create array from binary data
            arr_from_binary = array.array('i')
            arr_from_binary.frombytes(binary_data)
            
            return {
                'binary_data_length': len(binary_data),
                'array_from_binary': list(arr_from_binary),
                'original_data': [1, 2, 3, 4, 5]
            }
        
        # Array copying and cloning
        def array_copying():
            """Demonstrate array copying techniques."""
            
            original = array.array('i', [1, 2, 3, 4, 5])
            
            # Different copying methods
            shallow_copy = array.array(original.typecode, original)
            slice_copy = original[:]
            
            # Modify original to test independence
            original.append(6)
            
            return {
                'original_after_modification': list(original),
                'shallow_copy': list(shallow_copy),
                'slice_copy': list(slice_copy),
                'copies_independent': list(shallow_copy) != list(original)
            }
        
        # Array from file
        def from_file_data():
            """Demonstrate creating arrays from file-like data."""
            
            # Simulate file data
            import io
            
            # Create binary data
            data = array.array('i', range(10))
            binary_buffer = io.BytesIO()
            data.tofile(binary_buffer)
            
            # Read back from buffer
            binary_buffer.seek(0)
            new_array = array.array('i')
            try:
                new_array.fromfile(binary_buffer, 10)
            except EOFError:
                # Handle case where less data available
                pass
            
            return {
                'original_data': list(data),
                'reconstructed_data': list(new_array),
                'data_matches': list(data) == list(new_array)
            }
        
        binary_result = from_binary_data()
        copying_result = array_copying()
        file_result = from_file_data()
        
        return {
            'from_binary_data': binary_result,
            'array_copying': copying_result,
            'from_file_data': file_result
        }
    
    # Type code comprehensive examples
    def type_code_examples():
        """Comprehensive examples of all array type codes."""
        
        # All available type codes with examples
        type_code_info = {
            'b': {'name': 'signed char', 'size': None, 'range': (-128, 127)},
            'B': {'name': 'unsigned char', 'size': None, 'range': (0, 255)},
            'u': {'name': 'unicode char', 'size': None, 'range': 'Unicode characters'},
            'h': {'name': 'signed short', 'size': None, 'range': (-32768, 32767)},
            'H': {'name': 'unsigned short', 'size': None, 'range': (0, 65535)},
            'i': {'name': 'signed int', 'size': None, 'range': 'Platform dependent'},
            'I': {'name': 'unsigned int', 'size': None, 'range': 'Platform dependent'},
            'l': {'name': 'signed long', 'size': None, 'range': 'Platform dependent'},
            'L': {'name': 'unsigned long', 'size': None, 'range': 'Platform dependent'},
            'q': {'name': 'signed long long', 'size': None, 'range': 'Platform dependent'},
            'Q': {'name': 'unsigned long long', 'size': None, 'range': 'Platform dependent'},
            'f': {'name': 'float', 'size': None, 'range': 'IEEE 754 single precision'},
            'd': {'name': 'double', 'size': None, 'range': 'IEEE 754 double precision'},
        }
        
        # Create example arrays for each type code
        type_examples = {}
        
        for typecode, info in type_code_info.items():
            try:
                if typecode == 'u':
                    # Unicode characters
                    example_array = array.array(typecode, 'Hello')
                    example_data = 'Hello'
                elif typecode in 'bBhHiIlLqQ':
                    # Integer types
                    example_array = array.array(typecode, [1, 2, 3, 4, 5])
                    example_data = [1, 2, 3, 4, 5]
                else:
                    # Float types
                    example_array = array.array(typecode, [1.1, 2.2, 3.3])
                    example_data = [1.1, 2.2, 3.3]
                
                info['size'] = example_array.itemsize
                type_examples[typecode] = {
                    'info': info,
                    'example_data': example_data,
                    'array_representation': str(example_array),
                    'itemsize': example_array.itemsize,
                    'length': len(example_array)
                }
                
            except (ValueError, OverflowError) as e:
                type_examples[typecode] = {
                    'info': info,
                    'error': str(e)
                }
        
        return type_examples
    
    # Execute all creation demonstrations
    basic_patterns = basic_creation_patterns()
    advanced_patterns = advanced_creation_patterns()
    type_codes = type_code_examples()
    
    return {
        'basic_creation_patterns': basic_patterns,
        'advanced_creation_patterns': advanced_patterns,
        'type_code_examples': type_codes
    }

# =============================================================================
# 3. ARRAY OPERATIONS & METHODS - MANIPULATION MASTERY
# =============================================================================

"""
ARRAY OPERATIONS COMPREHENSIVE GUIDE:
Master all array manipulation methods and operations
"""

def demonstrate_array_operations():
    """
    COMPREHENSIVE ARRAY OPERATIONS DEMONSTRATION
    Master array modification, manipulation, and method usage
    """
    
    import array
    import copy
    
    # Basic array methods
    def basic_array_methods():
        """Demonstrate basic array modification methods."""
        
        # Create test array
        arr = array.array('i', [1, 2, 3, 4, 5])
        operations_log = []
        
        # append() - Add element to end
        arr.append(6)
        operations_log.append({
            'operation': 'append(6)',
            'result': list(arr),
            'length': len(arr)
        })
        
        # insert() - Insert element at position
        arr.insert(2, 99)
        operations_log.append({
            'operation': 'insert(2, 99)',
            'result': list(arr),
            'length': len(arr)
        })
        
        # extend() - Add multiple elements
        arr.extend([7, 8, 9])
        operations_log.append({
            'operation': 'extend([7, 8, 9])',
            'result': list(arr),
            'length': len(arr)
        })
        
        # remove() - Remove first occurrence
        arr.remove(99)
        operations_log.append({
            'operation': 'remove(99)',
            'result': list(arr),
            'length': len(arr)
        })
        
        # pop() - Remove and return element
        popped_value = arr.pop()
        operations_log.append({
            'operation': 'pop()',
            'result': list(arr),
            'popped_value': popped_value,
            'length': len(arr)
        })
        
        # pop(index) - Remove and return element at index
        popped_value = arr.pop(2)
        operations_log.append({
            'operation': 'pop(2)',
            'result': list(arr),
            'popped_value': popped_value,
            'length': len(arr)
        })
        
        # reverse() - Reverse array in-place
        arr.reverse()
        operations_log.append({
            'operation': 'reverse()',
            'result': list(arr),
            'length': len(arr)
        })
        
        return {
            'initial_array': [1, 2, 3, 4, 5],
            'operations_log': operations_log,
            'final_array': list(arr)
        }
    
    # Advanced array operations
    def advanced_array_operations():
        """Demonstrate advanced array operations."""
        
        # Array slicing and indexing
        def slicing_operations():
            """Comprehensive slicing operations."""
            
            arr = array.array('i', list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            
            slicing_examples = {
                'full_array': list(arr[:]),
                'first_half': list(arr[:5]),
                'second_half': list(arr[5:]),
                'every_second': list(arr[::2]),
                'reverse': list(arr[::-1]),
                'middle_slice': list(arr[3:7]),
                'negative_indexing': list(arr[-3:]),
                'step_slice': list(arr[1:8:2])
            }
            
            # Slice assignment
            arr[2:5] = array.array('i', [99, 98, 97])
            slicing_examples['after_slice_assignment'] = list(arr)
            
            return slicing_examples
        
        # Array searching and counting
        def searching_operations():
            """Demonstrate search and count operations."""
            
            arr = array.array('i', [1, 2, 3, 2, 4, 2, 5])
            
            search_results = {
                'original_array': list(arr),
                'index_of_2': arr.index(2),  # First occurrence
                'count_of_2': arr.count(2),   # Total occurrences
                'length': len(arr),
                'max_element': max(arr),
                'min_element': min(arr),
                'sum_of_elements': sum(arr)
            }
            
            # Custom search functions
            def find_all_indices(arr, value):
                """Find all indices of a value."""
                indices = []
                for i, element in enumerate(arr):
                    if element == value:
                        indices.append(i)
                return indices
            
            search_results['all_indices_of_2'] = find_all_indices(arr, 2)
            
            return search_results
        
        # Array comparison and sorting
        def comparison_sorting():
            """Demonstrate comparison and sorting operations."""
            
            arr1 = array.array('i', [3, 1, 4, 1, 5, 9])
            arr2 = array.array('i', [3, 1, 4, 1, 5, 9])
            arr3 = array.array('i', [1, 2, 3, 4, 5])
            
            # Array comparisons
            comparison_results = {
                'arr1_equals_arr2': list(arr1) == list(arr2),
                'arr1_equals_arr3': list(arr1) == list(arr3),
                'element_wise_comparison': [a == b for a, b in zip(arr1, arr2)]
            }
            
            # Sorting (create copy first since arrays don't have sort method)
            sorted_data = sorted(arr1)
            
            # Manual sorting demonstration
            arr_copy = array.array('i', arr1)
            arr_copy_list = list(arr_copy)
            arr_copy_list.sort()
            
            sorting_results = {
                'original': list(arr1),
                'sorted_builtin': sorted_data,
                'manual_sort': arr_copy_list
            }
            
            return {
                'comparisons': comparison_results,
                'sorting': sorting_results
            }
        
        slicing_result = slicing_operations()
        searching_result = searching_operations()
        comparison_result = comparison_sorting()
        
        return {
            'slicing_operations': slicing_result,
            'searching_operations': searching_result,
            'comparison_sorting': comparison_result
        }
    
    # Array conversion and transformation
    def conversion_operations():
        """Demonstrate array conversion and transformation."""
        
        # Different conversion methods
        arr = array.array('i', [1, 2, 3, 4, 5])
        
        conversions = {
            'to_list': list(arr),
            'to_tuple': tuple(arr),
            'to_string': str(arr),
            'to_bytes': arr.tobytes(),
            'itemsize': arr.itemsize,
            'typecode': arr.typecode
        }
        
        # Convert to different array types
        type_conversions = {}
        
        # Float conversion
        float_arr = array.array('f', arr)
        type_conversions['to_float'] = {
            'data': list(float_arr),
            'itemsize': float_arr.itemsize,
            'typecode': float_arr.typecode
        }
        
        # Double conversion
        double_arr = array.array('d', arr)
        type_conversions['to_double'] = {
            'data': list(double_arr),
            'itemsize': double_arr.itemsize,
            'typecode': double_arr.typecode
        }
        
        # Reconstruct from bytes
        reconstructed = array.array('i')
        reconstructed.frombytes(arr.tobytes())
        
        reconstruction = {
            'original': list(arr),
            'reconstructed': list(reconstructed),
            'bytes_match': arr.tobytes() == reconstructed.tobytes()
        }
        
        return {
            'basic_conversions': conversions,
            'type_conversions': type_conversions,
            'byte_reconstruction': reconstruction
        }
    
    # Execute all operation demonstrations
    basic_methods = basic_array_methods()
    advanced_ops = advanced_array_operations()
    conversions = conversion_operations()
    
    return {
        'basic_array_methods': basic_methods,
        'advanced_operations': advanced_ops,
        'conversion_operations': conversions
    }

# =============================================================================
# 4. ARRAY INDEXING & SLICING - ACCESS PATTERNS
# =============================================================================

"""
ARRAY INDEXING MASTERY:
Comprehensive indexing, slicing, and element access patterns
"""

def demonstrate_array_indexing():
    """
    COMPREHENSIVE ARRAY INDEXING DEMONSTRATION
    Master array element access and manipulation patterns
    """
    
    import array
    
    # Basic indexing operations
    def basic_indexing():
        """Demonstrate basic array indexing patterns."""
        
        arr = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90])
        
        # Positive indexing
        positive_indexing = {
            'first_element': arr[0],
            'second_element': arr[1],
            'middle_element': arr[len(arr)//2],
            'last_element': arr[len(arr)-1]
        }
        
        # Negative indexing
        negative_indexing = {
            'last_element': arr[-1],
            'second_last': arr[-2],
            'third_last': arr[-3],
            'first_from_end': arr[-len(arr)]
        }
        
        # Index validation and bounds checking
        def safe_index_access(arr, index):
            """Safe array access with bounds checking."""
            try:
                if -len(arr) <= index < len(arr):
                    return {'success': True, 'value': arr[index], 'index': index}
                else:
                    return {'success': False, 'error': 'Index out of bounds', 'index': index}
            except IndexError as e:
                return {'success': False, 'error': str(e), 'index': index}
        
        bounds_checking = {
            'valid_positive': safe_index_access(arr, 3),
            'valid_negative': safe_index_access(arr, -2),
            'invalid_positive': safe_index_access(arr, 20),
            'invalid_negative': safe_index_access(arr, -20)
        }
        
        return {
            'array_data': list(arr),
            'positive_indexing': positive_indexing,
            'negative_indexing': negative_indexing,
            'bounds_checking': bounds_checking
        }
    
    # Advanced slicing patterns
    def advanced_slicing():
        """Demonstrate advanced slicing patterns."""
        
        arr = array.array('i', list(range(20)))  # [0, 1, 2, ..., 19]
        
        # Comprehensive slicing patterns
        slicing_patterns = {
            'full_copy': list(arr[:]),
            'first_n': list(arr[:5]),
            'last_n': list(arr[-5:]),
            'middle_range': list(arr[5:15]),
            'every_second': list(arr[::2]),
            'every_third': list(arr[::3]),
            'reverse_all': list(arr[::-1]),
            'reverse_range': list(arr[10:5:-1]),
            'skip_reverse': list(arr[::-2])
        }
        
        # Complex slicing combinations
        complex_slicing = {
            'first_half_reverse': list(arr[:10][::-1]),
            'second_half_every_second': list(arr[10::2]),
            'middle_third': list(arr[len(arr)//3:2*len(arr)//3]),
            'alternating_halves': list(arr[:10:2]) + list(arr[10::2])
        }
        
        # Slice assignment patterns
        arr_copy = array.array('i', arr)
        slice_assignment_log = []
        
        # Replace middle section
        arr_copy[5:10] = array.array('i', [99, 98, 97, 96, 95])
        slice_assignment_log.append({
            'operation': 'arr[5:10] = [99, 98, 97, 96, 95]',
            'result': list(arr_copy)
        })
        
        # Replace with different size
        arr_copy[2:5] = array.array('i', [88, 77])
        slice_assignment_log.append({
            'operation': 'arr[2:5] = [88, 77]',
            'result': list(arr_copy)
        })
        
        # Step-wise replacement
        arr_copy[::2] = array.array('i', [x*10 for x in range(len(arr_copy[::2]))])
        slice_assignment_log.append({
            'operation': 'arr[::2] = [0, 10, 20, ...]',
            'result': list(arr_copy)
        })
        
        return {
            'original_array': list(arr),
            'basic_slicing_patterns': slicing_patterns,
            'complex_slicing': complex_slicing,
            'slice_assignment_log': slice_assignment_log
        }
    
    # Multi-dimensional indexing simulation
    def multi_dimensional_simulation():
        """Simulate multi-dimensional indexing using 1D arrays."""
        
        # Simulate 2D array using 1D array
        rows, cols = 4, 5
        flat_array = array.array('i', range(rows * cols))
        
        def get_2d_index(row, col, cols):
            """Convert 2D coordinates to 1D index."""
            return row * cols + col
        
        def get_2d_coords(index, cols):
            """Convert 1D index to 2D coordinates."""
            return divmod(index, cols)
        
        # Access patterns
        access_patterns = {
            'element_at_2_3': flat_array[get_2d_index(2, 3, cols)],
            'first_row': list(flat_array[0:cols]),
            'last_row': list(flat_array[(rows-1)*cols:rows*cols]),
            'first_column': [flat_array[get_2d_index(r, 0, cols)] for r in range(rows)],
            'last_column': [flat_array[get_2d_index(r, cols-1, cols)] for r in range(rows)],
            'main_diagonal': [flat_array[get_2d_index(i, i, cols)] for i in range(min(rows, cols))]
        }
        
        # Matrix representation
        matrix_representation = []
        for r in range(rows):
            row_data = list(flat_array[r*cols:(r+1)*cols])
            matrix_representation.append(row_data)
        
        return {
            'flat_array': list(flat_array),
            'dimensions': {'rows': rows, 'cols': cols},
            'matrix_representation': matrix_representation,
            'access_patterns': access_patterns
        }
    
    # Performance comparison of access methods
    def access_performance_analysis():
        """Analyze performance of different access methods."""
        
        import time
        
        # Create large array for testing
        large_array = array.array('i', range(100000))
        
        # Test different access patterns
        def time_operation(operation_func):
            """Time an operation."""
            start_time = time.time()
            result = operation_func()
            end_time = time.time()
            return {
                'result_length': len(result) if hasattr(result, '__len__') else 1,
                'execution_time': end_time - start_time
            }
        
        performance_tests = {
            'single_element_access': time_operation(lambda: large_array[50000]),
            'slice_first_1000': time_operation(lambda: large_array[:1000]),
            'slice_last_1000': time_operation(lambda: large_array[-1000:]),
            'every_100th_element': time_operation(lambda: large_array[::100]),
            'reverse_slice': time_operation(lambda: large_array[::-1])
        }
        
        return {
            'array_size': len(large_array),
            'performance_tests': performance_tests,
            'notes': 'Times may vary based on system performance'
        }
    
# =============================================================================
# 5. ARRAY TYPE CODES & MEMORY - EFFICIENCY MASTERY
# =============================================================================

"""
ARRAY TYPE CODES AND MEMORY OPTIMIZATION:
Master array type selection and memory efficiency
"""

def demonstrate_array_type_codes():
    """
    COMPREHENSIVE TYPE CODE AND MEMORY DEMONSTRATION
    Master type code selection and memory optimization strategies
    """
    
    import array
    import sys
    import struct
    
    # Complete type code reference
    def complete_type_code_reference():
        """Complete reference of all array type codes."""
        
        # Type code specifications
        type_specifications = {
            'signed_integers': {
                'b': {'name': 'signed char', 'min': -128, 'max': 127},
                'h': {'name': 'signed short', 'min': -32768, 'max': 32767},
                'i': {'name': 'signed int', 'min': -2147483648, 'max': 2147483647},
                'l': {'name': 'signed long', 'min': None, 'max': None},  # Platform dependent
                'q': {'name': 'signed long long', 'min': None, 'max': None}  # Platform dependent
            },
            'unsigned_integers': {
                'B': {'name': 'unsigned char', 'min': 0, 'max': 255},
                'H': {'name': 'unsigned short', 'min': 0, 'max': 65535},
                'I': {'name': 'unsigned int', 'min': 0, 'max': 4294967295},
                'L': {'name': 'unsigned long', 'min': 0, 'max': None},  # Platform dependent
                'Q': {'name': 'unsigned long long', 'min': 0, 'max': None}  # Platform dependent
            },
            'floating_point': {
                'f': {'name': 'float', 'precision': 'single (IEEE 754)', 'bytes': 4},
                'd': {'name': 'double', 'precision': 'double (IEEE 754)', 'bytes': 8}
            },
            'character': {
                'u': {'name': 'unicode character', 'encoding': 'UTF-16 or UTF-32'}
            }
        }
        
        # Test actual sizes on current platform
        actual_sizes = {}
        for category, types in type_specifications.items():
            actual_sizes[category] = {}
            for typecode, info in types.items():
                try:
                    test_array = array.array(typecode)
                    actual_sizes[category][typecode] = {
                        'itemsize': test_array.itemsize,
                        'info': info
                    }
                except (ValueError, TypeError) as e:
                    actual_sizes[category][typecode] = {
                        'error': str(e),
                        'info': info
                    }
        
        return {
            'type_specifications': type_specifications,
            'actual_platform_sizes': actual_sizes
        }
    
    # Memory usage analysis
    def memory_usage_analysis():
        """Analyze memory usage patterns for different type codes."""
        
        # Test data for comparison
        test_data_int = list(range(1000))
        test_data_float = [float(x) for x in range(1000)]
        
        memory_comparison = {}
        
        # Integer type codes
        for typecode in ['b', 'h', 'i', 'l']:
            try:
                # Filter data to fit type range if needed
                if typecode == 'b':
                    filtered_data = [x for x in test_data_int if -128 <= x <= 127][:100]
                elif typecode == 'h':
                    filtered_data = [x for x in test_data_int if -32768 <= x <= 32767][:500]
                else:
                    filtered_data = test_data_int
                
                arr = array.array(typecode, filtered_data)
                list_equiv = list(filtered_data)
                
                memory_comparison[f'type_{typecode}'] = {
                    'array_memory': sys.getsizeof(arr),
                    'list_memory': sys.getsizeof(list_equiv) + sum(sys.getsizeof(item) for item in list_equiv),
                    'element_count': len(filtered_data),
                    'itemsize': arr.itemsize,
                    'total_data_bytes': len(filtered_data) * arr.itemsize
                }
                
            except (ValueError, OverflowError) as e:
                memory_comparison[f'type_{typecode}'] = {'error': str(e)}
        
        # Float type codes
        for typecode in ['f', 'd']:
            try:
                arr = array.array(typecode, test_data_float)
                list_equiv = test_data_float
                
                memory_comparison[f'type_{typecode}'] = {
                    'array_memory': sys.getsizeof(arr),
                    'list_memory': sys.getsizeof(list_equiv) + sum(sys.getsizeof(item) for item in list_equiv),
                    'element_count': len(test_data_float),
                    'itemsize': arr.itemsize,
                    'total_data_bytes': len(test_data_float) * arr.itemsize
                }
                
            except (ValueError, OverflowError) as e:
                memory_comparison[f'type_{typecode}'] = {'error': str(e)}
        
        return memory_comparison
    
    # Type selection guidelines
    def type_selection_guidelines():
        """Guidelines for choosing appropriate type codes."""
        
        selection_guide = {
            'data_range_considerations': {
                'small_integers_0_255': {
                    'recommended': 'B',
                    'reason': 'Unsigned char, 1 byte per element',
                    'use_cases': ['Image pixel values', 'ASCII codes', 'Boolean flags']
                },
                'small_signed_integers': {
                    'recommended': 'b',
                    'reason': 'Signed char, 1 byte per element',
                    'use_cases': ['Temperature readings', 'Small offsets', 'Status codes']
                },
                'standard_integers': {
                    'recommended': 'i',
                    'reason': 'Standard int, platform dependent size',
                    'use_cases': ['General numeric data', 'Counters', 'IDs']
                },
                'large_integers': {
                    'recommended': 'q',
                    'reason': 'Long long int, 8 bytes',
                    'use_cases': ['Timestamps', 'Large counters', 'Financial data']
                },
                'decimal_numbers': {
                    'recommended': 'f or d',
                    'reason': 'Float (4 bytes) or double (8 bytes)',
                    'use_cases': ['Scientific calculations', 'Graphics coordinates', 'Measurements']
                },
                'text_characters': {
                    'recommended': 'u',
                    'reason': 'Unicode characters',
                    'use_cases': ['Text processing', 'Character arrays', 'Unicode data']
                }
            },
            'memory_optimization_strategies': {
                'minimize_memory': 'Use smallest type that fits data range',
                'maximize_precision': 'Use double (d) for critical calculations',
                'balance_performance': 'Standard int (i) often has best performance',
                'consider_platform': 'Some types vary by platform (l, L, q, Q)'
            },
            'performance_considerations': {
                'cache_efficiency': 'Smaller types = more elements per cache line',
                'cpu_optimization': 'Native word size often fastest',
                'memory_bandwidth': 'Smaller types reduce memory traffic'
            }
        }
        
        # Practical examples
        practical_examples = {
            'image_processing': {
                'data_type': 'Pixel values (0-255)',
                'recommended_type': 'B',
                'example': array.array('B', [255, 128, 64, 32, 0])
            },
            'financial_data': {
                'data_type': 'Currency amounts (cents)',
                'recommended_type': 'q',
                'example': array.array('q', [100, 250, 1000, 50])
            },
            'scientific_measurements': {
                'data_type': 'Floating point measurements',
                'recommended_type': 'd',
                'example': array.array('d', [3.14159, 2.71828, 1.41421])
            },
            'sensor_readings': {
                'data_type': 'Temperature (-40 to 125 °C)',
                'recommended_type': 'b',
                'example': array.array('b', [-10, 0, 25, 50, 100])
            }
        }
        
        return {
            'selection_guidelines': selection_guide,
            'practical_examples': {k: {**v, 'array_data': list(v['example'])} 
                                   for k, v in practical_examples.items()}
        }
    
    # Platform dependency analysis
    def platform_dependency_analysis():
        """Analyze platform-dependent type behavior."""
        
        platform_info = {
            'system_info': {
                'platform': sys.platform,
                'byte_order': sys.byteorder,
                'pointer_size': struct.calcsize("P"),
                'int_size': struct.calcsize("i"),
                'long_size': struct.calcsize("l")
            }
        }
        
        # Test platform-dependent types
        platform_dependent_types = ['l', 'L', 'q', 'Q']
        type_analysis = {}
        
        for typecode in platform_dependent_types:
            try:
                test_arr = array.array(typecode)
                type_analysis[typecode] = {
                    'itemsize': test_arr.itemsize,
                    'available': True,
                    'description': f'Platform size: {test_arr.itemsize} bytes'
                }
            except ValueError as e:
                type_analysis[typecode] = {
                    'available': False,
                    'error': str(e)
                }
        
        platform_info['type_analysis'] = type_analysis
        
        # Portability recommendations
        portability_recommendations = {
            'cross_platform_safe': ['b', 'B', 'h', 'H', 'i', 'I', 'f', 'd'],
            'platform_dependent': ['l', 'L', 'q', 'Q'],
            'recommendations': {
                'portable_code': 'Use i, I, f, d for maximum portability',
                'specific_sizes': 'Use struct module for exact byte sizes',
                'testing': 'Test on target platforms for platform-dependent types'
            }
        }
        
        platform_info['portability'] = portability_recommendations
        
        return platform_info
    
    # Execute all type code demonstrations
    type_reference = complete_type_code_reference()
    memory_analysis = memory_usage_analysis()
    selection_guide = type_selection_guidelines()
    platform_analysis = platform_dependency_analysis()
    
    return {
        'complete_type_reference': type_reference,
        'memory_usage_analysis': memory_analysis,
        'type_selection_guidelines': selection_guide,
        'platform_dependency_analysis': platform_analysis
    }

# =============================================================================
# 6. ARRAY VS LIST COMPARISON - PERFORMANCE ANALYSIS
# =============================================================================

"""
COMPREHENSIVE ARRAY VS LIST COMPARISON:
Detailed performance and feature comparison
"""

def demonstrate_array_vs_list():
    """
    COMPREHENSIVE ARRAY VS LIST COMPARISON
    Analyze performance, memory, and feature differences
    """
    
    import array
    import time
    import sys
    import gc
    
    # Performance benchmarking
    def performance_benchmarks():
        """Compare performance of arrays vs lists."""
        
        # Test data sizes
        test_sizes = [1000, 10000, 100000]
        performance_results = {}
        
        for size in test_sizes:
            performance_results[f'size_{size}'] = {}
            
            # Creation performance
            def test_creation():
                data = list(range(size))
                
                # List creation
                start_time = time.time()
                test_list = data.copy()
                list_time = time.time() - start_time
                
                # Array creation
                start_time = time.time()
                test_array = array.array('i', data)
                array_time = time.time() - start_time
                
                return {
                    'list_creation_time': list_time,
                    'array_creation_time': array_time,
                    'array_vs_list_ratio': array_time / list_time if list_time > 0 else float('inf')
                }
            
            # Element access performance
            def test_element_access():
                data = list(range(size))
                test_list = data.copy()
                test_array = array.array('i', data)
                
                # Test random access
                import random
                indices = [random.randint(0, size-1) for _ in range(100)]
                
                # List access
                start_time = time.time()
                for idx in indices:
                    _ = test_list[idx]
                list_access_time = time.time() - start_time
                
                # Array access
                start_time = time.time()
                for idx in indices:
                    _ = test_array[idx]
                array_access_time = time.time() - start_time
                
                return {
                    'list_access_time': list_access_time,
                    'array_access_time': array_access_time,
                    'array_vs_list_ratio': array_access_time / list_access_time if list_access_time > 0 else float('inf')
                }
            
            # Append performance
            def test_append_performance():
                test_list = []
                test_array = array.array('i')
                
                # List append
                start_time = time.time()
                for i in range(1000):  # Smaller test for append
                    test_list.append(i)
                list_append_time = time.time() - start_time
                
                # Array append
                start_time = time.time()
                for i in range(1000):
                    test_array.append(i)
                array_append_time = time.time() - start_time
                
                return {
                    'list_append_time': list_append_time,
                    'array_append_time': array_append_time,
                    'array_vs_list_ratio': array_append_time / list_append_time if list_append_time > 0 else float('inf')
                }
            
            performance_results[f'size_{size}']['creation'] = test_creation()
            performance_results[f'size_{size}']['element_access'] = test_element_access()
            if size <= 10000:  # Only test append for smaller sizes
                performance_results[f'size_{size}']['append'] = test_append_performance()
        
        return performance_results
    
    # Memory usage comparison
    def memory_usage_comparison():
        """Compare memory usage between arrays and lists."""
        
        test_sizes = [100, 1000, 10000]
        memory_results = {}
        
        for size in test_sizes:
            # Create test data
            data = list(range(size))
            test_list = data.copy()
            test_array = array.array('i', data)
            
            # Calculate memory usage
            gc.collect()  # Force garbage collection for accurate measurement
            
            # List memory (object overhead + references)
            list_base_size = sys.getsizeof(test_list)
            list_element_size = sum(sys.getsizeof(item) for item in test_list)
            list_total = list_base_size + list_element_size
            
            # Array memory (more efficient storage)
            array_total = sys.getsizeof(test_array)
            
            memory_results[f'size_{size}'] = {
                'list_base_size': list_base_size,
                'list_element_overhead': list_element_size,
                'list_total_size': list_total,
                'array_total_size': array_total,
                'memory_ratio': list_total / array_total if array_total > 0 else float('inf'),
                'memory_saved': list_total - array_total,
                'efficiency_improvement': ((list_total - array_total) / list_total * 100) if list_total > 0 else 0
            }
        
        return memory_results
    
    # Feature comparison matrix
    def feature_comparison_matrix():
        """Comprehensive feature comparison."""
        
        feature_matrix = {
            'data_storage': {
                'list': 'Heterogeneous (mixed types)',
                'array': 'Homogeneous (single type only)',
                'winner': 'list (flexibility)'
            },
            'memory_efficiency': {
                'list': 'High overhead (object references)',
                'array': 'Low overhead (contiguous memory)',
                'winner': 'array'
            },
            'type_safety': {
                'list': 'No type checking',
                'array': 'Strict type checking',
                'winner': 'array (for numeric data)'
            },
            'mathematical_operations': {
                'list': 'No built-in math operations',
                'array': 'Basic operations only',
                'winner': 'neither (use NumPy)'
            },
            'element_access_speed': {
                'list': 'Very fast',
                'array': 'Very fast',
                'winner': 'tie'
            },
            'append_performance': {
                'list': 'Optimized',
                'array': 'Good',
                'winner': 'list (slightly)'
            },
            'slice_operations': {
                'list': 'Full support',
                'array': 'Full support',
                'winner': 'tie'
            },
            'serialization': {
                'list': 'Pickle, JSON (limited)',
                'array': 'Built-in binary methods',
                'winner': 'array (for binary data)'
            },
            'built_in_status': {
                'list': 'Built-in type',
                'array': 'Requires import',
                'winner': 'list'
            },
            'iteration_speed': {
                'list': 'Fast',
                'array': 'Fast',
                'winner': 'tie'
            }
        }
        
        return feature_matrix
    
    # Use case recommendations
    def use_case_recommendations():
        """Detailed use case recommendations."""
        
        recommendations = {
            'use_lists_when': {
                'mixed_data_types': {
                    'reason': 'Lists can store any combination of types',
                    'example': '[1, "hello", [2, 3], {"key": "value"}]'
                },
                'frequent_insertions': {
                    'reason': 'Lists optimized for dynamic operations',
                    'example': 'Building data structures with unknown final size'
                },
                'general_purpose': {
                    'reason': 'Lists are Python\'s general-purpose sequence',
                    'example': 'Most everyday programming tasks'
                },
                'object_storage': {
                    'reason': 'Storing complex objects and references',
                    'example': 'Collections of class instances'
                }
            },
            'use_arrays_when': {
                'numeric_data_only': {
                    'reason': 'Arrays optimized for homogeneous numeric data',
                    'example': 'Sensor readings, pixel values, mathematical data'
                },
                'memory_constrained': {
                    'reason': 'Arrays use significantly less memory',
                    'example': 'Embedded systems, large datasets'
                },
                'type_safety_needed': {
                    'reason': 'Arrays enforce type consistency',
                    'example': 'Critical numeric calculations'
                },
                'binary_io': {
                    'reason': 'Arrays have efficient binary serialization',
                    'example': 'File I/O, network protocols'
                },
                'interfacing_c': {
                    'reason': 'Arrays compatible with C APIs',
                    'example': 'Calling C libraries, system programming'
                }
            },
            'consider_alternatives': {
                'numpy_arrays': {
                    'when': 'Mathematical operations, multi-dimensional data',
                    'advantages': 'Vectorized operations, broadcasting, extensive math functions'
                },
                'bytes_bytearray': {
                    'when': 'Binary data manipulation',
                    'advantages': 'Specialized for byte operations'
                },
                'collections_deque': {
                    'when': 'Frequent additions/removals at both ends',
                    'advantages': 'Optimized double-ended operations'
                }
            }
        }
        
        return recommendations
    
    # Execute all comparison demonstrations
    performance = performance_benchmarks()
    memory = memory_usage_comparison()
    features = feature_comparison_matrix()
    use_cases = use_case_recommendations()
    
    return {
        'performance_benchmarks': performance,
        'memory_usage_comparison': memory,
        'feature_comparison_matrix': features,
        'use_case_recommendations': use_cases
    }

# =============================================================================
# 7. ARRAY ALGORITHMS & PATTERNS - ALGORITHMIC MASTERY
# =============================================================================

"""
ARRAY ALGORITHMS AND PATTERNS:
Master common array algorithms and programming patterns
"""

def demonstrate_array_algorithms():
    """
    COMPREHENSIVE ARRAY ALGORITHMS DEMONSTRATION
    Master common algorithms and patterns using arrays
    """
    
    import array
    import math
    import random
    
    # Sorting algorithms using arrays
    def sorting_algorithms():
        """Implement and demonstrate sorting algorithms with arrays."""
        
        # Test data
        original_data = [64, 34, 25, 12, 22, 11, 90]
        
        def bubble_sort_array(arr):
            """Bubble sort implementation for arrays."""
            arr_copy = array.array('i', arr)
            n = len(arr_copy)
            comparisons = 0
            swaps = 0
            
            for i in range(n):
                swapped = False
                for j in range(0, n-i-1):
                    comparisons += 1
                    if arr_copy[j] > arr_copy[j+1]:
                        arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                        swaps += 1
                        swapped = True
                if not swapped:
                    break
            
            return {
                'sorted_array': list(arr_copy),
                'comparisons': comparisons,
                'swaps': swaps
            }
        
        def selection_sort_array(arr):
            """Selection sort implementation for arrays."""
            arr_copy = array.array('i', arr)
            n = len(arr_copy)
            comparisons = 0
            swaps = 0
            
            for i in range(n):
                min_idx = i
                for j in range(i+1, n):
                    comparisons += 1
                    if arr_copy[j] < arr_copy[min_idx]:
                        min_idx = j
                if min_idx != i:
                    arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
                    swaps += 1
            
            return {
                'sorted_array': list(arr_copy),
                'comparisons': comparisons,
                'swaps': swaps
            }
        
        def insertion_sort_array(arr):
            """Insertion sort implementation for arrays."""
            arr_copy = array.array('i', arr)
            n = len(arr_copy)
            comparisons = 0
            shifts = 0
            
            for i in range(1, n):
                key = arr_copy[i]
                j = i - 1
                
                while j >= 0:
                    comparisons += 1
                    if arr_copy[j] > key:
                        arr_copy[j + 1] = arr_copy[j]
                        shifts += 1
                        j -= 1
                    else:
                        break
                
                arr_copy[j + 1] = key
            
            return {
                'sorted_array': list(arr_copy),
                'comparisons': comparisons,
                'shifts': shifts
            }
        
        sorting_results = {
            'original_data': original_data,
            'bubble_sort': bubble_sort_array(original_data),
            'selection_sort': selection_sort_array(original_data),
            'insertion_sort': insertion_sort_array(original_data)
        }
        
        return sorting_results
    
    # Search algorithms using arrays
    def searching_algorithms():
        """Implement and demonstrate search algorithms with arrays."""
        
        # Test data (sorted for binary search)
        sorted_data = list(range(0, 100, 2))  # [0, 2, 4, 6, ..., 98]
        arr = array.array('i', sorted_data)
        
        def linear_search(arr, target):
            """Linear search implementation."""
            comparisons = 0
            for i, value in enumerate(arr):
                comparisons += 1
                if value == target:
                    return {'found': True, 'index': i, 'comparisons': comparisons}
            return {'found': False, 'index': -1, 'comparisons': comparisons}
        
        def binary_search(arr, target):
            """Binary search implementation."""
            left, right = 0, len(arr) - 1
            comparisons = 0
            
            while left <= right:
                comparisons += 1
                mid = (left + right) // 2
                
                if arr[mid] == target:
                    return {'found': True, 'index': mid, 'comparisons': comparisons}
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return {'found': False, 'index': -1, 'comparisons': comparisons}
        
        def jump_search(arr, target):
            """Jump search implementation."""
            n = len(arr)
            step = int(math.sqrt(n))
            prev = 0
            comparisons = 0
            
            # Jump search phase
            while arr[min(step, n) - 1] < target:
                comparisons += 1
                prev = step
                step += int(math.sqrt(n))
                if prev >= n:
                    return {'found': False, 'index': -1, 'comparisons': comparisons}
            
            # Linear search phase
            while arr[prev] < target:
                comparisons += 1
                prev += 1
                if prev == min(step, n):
                    return {'found': False, 'index': -1, 'comparisons': comparisons}
            
            comparisons += 1
            if arr[prev] == target:
                return {'found': True, 'index': prev, 'comparisons': comparisons}
            
            return {'found': False, 'index': -1, 'comparisons': comparisons}
        
        # Test different targets
        test_targets = [42, 13, 0, 98, 101]  # Mix of existing and non-existing values
        search_results = {}
        
        for target in test_targets:
            search_results[f'target_{target}'] = {
                'linear_search': linear_search(arr, target),
                'binary_search': binary_search(arr, target),
                'jump_search': jump_search(arr, target)
            }
        
        return {
            'test_array': sorted_data[:10] + ['...'] + sorted_data[-10:],  # Show sample
            'array_size': len(sorted_data),
            'search_results': search_results
        }
    
    # Array manipulation patterns
    def manipulation_patterns():
        """Demonstrate common array manipulation patterns."""
        
        # Filtering patterns
        def filtering_patterns():
            """Array filtering techniques."""
            
            arr = array.array('i', range(-10, 11))  # [-10, -9, ..., 10]
            
            # Filter positive numbers
            positive_numbers = array.array('i', [x for x in arr if x > 0])
            
            # Filter even numbers
            even_numbers = array.array('i', [x for x in arr if x % 2 == 0])
            
            # Filter by absolute value
            large_abs_numbers = array.array('i', [x for x in arr if abs(x) >= 5])
            
            # Custom filter function
            def is_prime(n):
                """Check if number is prime."""
                if n < 2:
                    return False
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        return False
                return True
            
            prime_numbers = array.array('i', [x for x in arr if x > 1 and is_prime(x)])
            
            return {
                'original': list(arr),
                'positive_numbers': list(positive_numbers),
                'even_numbers': list(even_numbers),
                'large_absolute': list(large_abs_numbers),
                'prime_numbers': list(prime_numbers)
            }
        
        # Transformation patterns
        def transformation_patterns():
            """Array transformation techniques."""
            
            arr = array.array('i', [1, 2, 3, 4, 5])
            
            # Mathematical transformations
            squared = array.array('i', [x*x for x in arr])
            doubled = array.array('i', [x*2 for x in arr])
            incremented = array.array('i', [x+10 for x in arr])
            
            # Conditional transformations
            abs_values = array.array('i', [-5, -2, 0, 3, -7])
            absolute = array.array('i', [abs(x) for x in abs_values])
            
            # Complex transformation
            def transform_element(x):
                """Complex transformation function."""
                if x < 0:
                    return 0
                elif x == 0:
                    return 1
                else:
                    return x * 2
            
            complex_transform = array.array('i', [transform_element(x) for x in abs_values])
            
            return {
                'original': list(arr),
                'squared': list(squared),
                'doubled': list(doubled),
                'incremented': list(incremented),
                'negative_array': list(abs_values),
                'absolute_values': list(absolute),
                'complex_transformation': list(complex_transform)
            }
        
        # Aggregation patterns
        def aggregation_patterns():
            """Array aggregation techniques."""
            
            arr = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
            
            # Basic aggregations
            total_sum = sum(arr)
            count = len(arr)
            average = total_sum / count if count > 0 else 0
            minimum = min(arr)
            maximum = max(arr)
            
            # Statistical aggregations
            def median(arr):
                """Calculate median of array."""
                sorted_arr = sorted(arr)
                n = len(sorted_arr)
                if n % 2 == 0:
                    return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
                else:
                    return sorted_arr[n//2]
            
            def std_deviation(arr):
                """Calculate standard deviation."""
                mean = sum(arr) / len(arr)
                variance = sum((x - mean) ** 2 for x in arr) / len(arr)
                return variance ** 0.5
            
            median_val = median(arr)
            std_dev = std_deviation(arr)
            
            # Range and spread
            range_val = maximum - minimum
            
            return {
                'array_data': list(arr),
                'sum': total_sum,
                'count': count,
                'average': average,
                'minimum': minimum,
                'maximum': maximum,
                'median': median_val,
                'std_deviation': std_dev,
                'range': range_val
            }
        
        filtering = filtering_patterns()
        transformations = transformation_patterns()
        aggregations = aggregation_patterns()
        
        return {
            'filtering_patterns': filtering,
            'transformation_patterns': transformations,
            'aggregation_patterns': aggregations
        }
    
    # Advanced algorithm patterns
    def advanced_algorithm_patterns():
        """Demonstrate advanced algorithmic patterns with arrays."""
        
        # Sliding window pattern
        def sliding_window_algorithms():
            """Sliding window technique examples."""
            
            arr = array.array('i', [1, 3, 2, 6, -1, 4, 1, 8, 2])
            
            def max_sum_subarray(arr, k):
                """Find maximum sum of subarray of size k."""
                if len(arr) < k:
                    return None
                
                # Calculate sum of first window
                window_sum = sum(arr[:k])
                max_sum = window_sum
                
                # Slide window and update sum
                for i in range(k, len(arr)):
                    window_sum = window_sum - arr[i-k] + arr[i]
                    max_sum = max(max_sum, window_sum)
                
                return max_sum
            
            def avg_of_subarrays(arr, k):
                """Calculate average of all subarrays of size k."""
                if len(arr) < k:
                    return []
                
                averages = []
                window_sum = sum(arr[:k])
                averages.append(window_sum / k)
                
                for i in range(k, len(arr)):
                    window_sum = window_sum - arr[i-k] + arr[i]
                    averages.append(window_sum / k)
                
                return averages
            
            return {
                'array_data': list(arr),
                'max_sum_k3': max_sum_subarray(arr, 3),
                'max_sum_k4': max_sum_subarray(arr, 4),
                'averages_k3': avg_of_subarrays(arr, 3)
            }
        
        # Two pointer technique
        def two_pointer_algorithms():
            """Two pointer technique examples."""
            
            # Find pair with target sum (sorted array)
            sorted_arr = array.array('i', [1, 2, 3, 4, 6, 8, 9, 14, 15])
            target = 10
            
            def find_pair_with_sum(arr, target):
                """Find pair that sums to target using two pointers."""
                left, right = 0, len(arr) - 1
                
                while left < right:
                    current_sum = arr[left] + arr[right]
                    if current_sum == target:
                        return {'found': True, 'pair': [arr[left], arr[right]], 'indices': [left, right]}
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                
                return {'found': False, 'pair': None, 'indices': None}
            
            # Remove duplicates in sorted array
            def remove_duplicates(arr):
                """Remove duplicates from sorted array in-place."""
                if len(arr) <= 1:
                    return len(arr)
                
                arr_copy = array.array('i', arr)
                write_index = 1
                
                for read_index in range(1, len(arr_copy)):
                    if arr_copy[read_index] != arr_copy[read_index - 1]:
                        arr_copy[write_index] = arr_copy[read_index]
                        write_index += 1
                
                return {'new_length': write_index, 'array': list(arr_copy[:write_index])}
            
            duplicate_arr = array.array('i', [1, 1, 2, 2, 2, 3, 4, 4, 5])
            
            return {
                'sorted_array': list(sorted_arr),
                'target_sum': target,
                'pair_result': find_pair_with_sum(sorted_arr, target),
                'duplicate_array': list(duplicate_arr),
                'deduplicated': remove_duplicates(duplicate_arr)
            }
        
        sliding_window = sliding_window_algorithms()
        two_pointer = two_pointer_algorithms()
        
        return {
            'sliding_window_algorithms': sliding_window,
            'two_pointer_algorithms': two_pointer
        }
    
    # Execute all algorithm demonstrations
    sorting = sorting_algorithms()
    searching = searching_algorithms()
    manipulation = manipulation_patterns()
    advanced = advanced_algorithm_patterns()
    
    return {
        'sorting_algorithms': sorting,
        'searching_algorithms': searching,
        'manipulation_patterns': manipulation,
        'advanced_algorithm_patterns': advanced
    }

# =============================================================================
# 8. BUFFER PROTOCOL & MEMORYVIEW - ADVANCED OPERATIONS
# =============================================================================

"""
BUFFER PROTOCOL AND MEMORYVIEW MASTERY:
Advanced memory operations and buffer interface
"""

def demonstrate_buffer_operations():
    """
    COMPREHENSIVE BUFFER PROTOCOL DEMONSTRATION
    Master advanced memory operations and buffer interface
    """
    
    import array
    import struct
    import sys
    
    # Buffer protocol basics
    def buffer_protocol_basics():
        """Demonstrate basic buffer protocol concepts."""
        
        # Create arrays that support buffer protocol
        int_array = array.array('i', [1, 2, 3, 4, 5])
        float_array = array.array('f', [1.1, 2.2, 3.3])
        byte_array = array.array('B', [65, 66, 67, 68, 69])  # ASCII: ABCDE
        
        # Buffer information
        def get_buffer_info(arr, name):
            """Get comprehensive buffer information."""
            try:
                # Get buffer info
                buffer_info = arr.buffer_info()
                
                # Create memoryview
                mv = memoryview(arr)
                
                return {
                    'array_type': name,
                    'typecode': arr.typecode,
                    'itemsize': arr.itemsize,
                    'buffer_address': buffer_info[0],
                    'buffer_length': buffer_info[1],
                    'memoryview_format': mv.format,
                    'memoryview_itemsize': mv.itemsize,
                    'memoryview_ndim': mv.ndim,
                    'memoryview_shape': mv.shape,
                    'memoryview_strides': mv.strides,
                    'memoryview_readonly': mv.readonly,
                    'bytes_representation': arr.tobytes()
                }
            except Exception as e:
                return {'error': str(e), 'array_type': name}
        
        buffer_details = {
            'integer_array': get_buffer_info(int_array, 'integer'),
            'float_array': get_buffer_info(float_array, 'float'),
            'byte_array': get_buffer_info(byte_array, 'byte')
        }
        
        return buffer_details
    
    # Memoryview operations
    def memoryview_operations():
        """Demonstrate memoryview operations and capabilities."""
        
        # Create test array
        source_array = array.array('i', list(range(20)))
        
        # Basic memoryview operations
        def basic_memoryview_ops():
            """Basic memoryview operations."""
            
            mv = memoryview(source_array)
            
            # Slicing operations
            slice_operations = {
                'full_view': list(mv),
                'first_half': list(mv[:10]),
                'second_half': list(mv[10:]),
                'every_second': list(mv[::2]),
                'reverse_view': list(mv[::-1])
            }
            
            # View properties
            view_properties = {
                'format': mv.format,
                'itemsize': mv.itemsize,
                'ndim': mv.ndim,
                'shape': mv.shape,
                'strides': mv.strides,
                'readonly': mv.readonly,
                'c_contiguous': mv.c_contiguous,
                'f_contiguous': mv.f_contiguous,
                'contiguous': mv.contiguous
            }
            
            return {
                'slice_operations': slice_operations,
                'view_properties': view_properties
            }
        
        # Advanced memoryview operations
        def advanced_memoryview_ops():
            """Advanced memoryview operations."""
            
            mv = memoryview(source_array)
            
            # Cast operations (reinterpret data)
            cast_operations = {}
            
            try:
                # Cast to bytes
                byte_view = mv.cast('B')
                cast_operations['cast_to_bytes'] = {
                    'success': True,
                    'format': byte_view.format,
                    'itemsize': byte_view.itemsize,
                    'data_sample': list(byte_view[:20])  # First 20 bytes
                }
            except Exception as e:
                cast_operations['cast_to_bytes'] = {'success': False, 'error': str(e)}
            
            try:
                # Cast to different integer type
                short_view = mv.cast('h')
                cast_operations['cast_to_short'] = {
                    'success': True,
                    'format': short_view.format,
                    'itemsize': short_view.itemsize,
                    'data_sample': list(short_view[:10])
                }
            except Exception as e:
                cast_operations['cast_to_short'] = {'success': False, 'error': str(e)}
            
            # Memory sharing demonstration
            def memory_sharing_demo():
                """Demonstrate memory sharing between views."""
                
                # Create view and modify original
                view = mv[5:15]
                original_view_data = list(view)
                
                # Modify original array
                source_array[7] = 999
                updated_view_data = list(view)
                
                return {
                    'original_view_data': original_view_data,
                    'updated_view_data': updated_view_data,
                    'memory_shared': original_view_data != updated_view_data
                }
            
            memory_sharing = memory_sharing_demo()
            
            return {
                'cast_operations': cast_operations,
                'memory_sharing': memory_sharing
            }
        
        basic_ops = basic_memoryview_ops()
        advanced_ops = advanced_memoryview_ops()
        
        return {
            'source_array': list(source_array),
            'basic_operations': basic_ops,
            'advanced_operations': advanced_ops
        }
    
    # Zero-copy operations
    def zero_copy_operations():
        """Demonstrate zero-copy operations using buffer protocol."""
        
        # Create large array for demonstration
        large_array = array.array('i', range(1000))
        
        def demonstrate_zero_copy():
            """Show zero-copy operations."""
            
            # Traditional copy operations
            def traditional_copy_slice():
                """Traditional slicing creates copy."""
                slice_copy = large_array[100:200]  # Creates new array
                return {
                    'operation': 'array[100:200]',
                    'creates_copy': True,
                    'memory_usage': 'High (new array created)',
                    'data_sample': list(slice_copy[:5])
                }
            
            # Zero-copy view operations
            def zero_copy_view():
                """Memoryview creates zero-copy view."""
                mv = memoryview(large_array)
                view_slice = mv[100:200]  # Creates view, no copy
                return {
                    'operation': 'memoryview(array)[100:200]',
                    'creates_copy': False,
                    'memory_usage': 'Low (view only)',
                    'data_sample': list(view_slice[:5])
                }
            
            # Performance comparison simulation
            def performance_comparison():
                """Compare performance of copy vs view."""
                import time
                
                # Time traditional slicing
                start_time = time.time()
                for _ in range(100):
                    _ = large_array[100:900]  # Creates copy
                copy_time = time.time() - start_time
                
                # Time memoryview slicing
                mv = memoryview(large_array)
                start_time = time.time()
                for _ in range(100):
                    _ = mv[100:900]  # Creates view
                view_time = time.time() - start_time
                
                return {
                    'copy_operations_time': copy_time,
                    'view_operations_time': view_time,
                    'speed_improvement': copy_time / view_time if view_time > 0 else float('inf')
                }
            
            traditional = traditional_copy_slice()
            zero_copy = zero_copy_view()
            performance = performance_comparison()
            
            return {
                'traditional_copy': traditional,
                'zero_copy_view': zero_copy,
                'performance_comparison': performance
            }
        
        zero_copy_demo = demonstrate_zero_copy()
        
        return {
            'array_size': len(large_array),
            'zero_copy_demonstration': zero_copy_demo
        }
    
    # Buffer interface with other types
    def buffer_interface_compatibility():
        """Demonstrate buffer interface with different types."""
        
        # Different buffer-supporting types
        buffer_types = {}
        
        # Array
        test_array = array.array('i', [1, 2, 3, 4, 5])
        buffer_types['array'] = {
            'type': 'array.array',
            'supports_buffer': True,
            'data': list(test_array),
            'bytes': test_array.tobytes()
        }
        
        # Bytes
        test_bytes = b'Hello World'
        buffer_types['bytes'] = {
            'type': 'bytes',
            'supports_buffer': True,
            'data': list(test_bytes),
            'bytes': test_bytes
        }
        
        # Bytearray
        test_bytearray = bytearray(b'Mutable')
        buffer_types['bytearray'] = {
            'type': 'bytearray',
            'supports_buffer': True,
            'data': list(test_bytearray),
            'bytes': bytes(test_bytearray)
        }
        
        # Test memoryview compatibility
        compatibility_test = {}
        
        for name, info in buffer_types.items():
            try:
                if name == 'array':
                    obj = test_array
                elif name == 'bytes':
                    obj = test_bytes
                elif name == 'bytearray':
                    obj = test_bytearray
                
                mv = memoryview(obj)
                compatibility_test[name] = {
                    'memoryview_compatible': True,
                    'format': mv.format,
                    'itemsize': mv.itemsize,
                    'readonly': mv.readonly
                }
            except Exception as e:
                compatibility_test[name] = {
                    'memoryview_compatible': False,
                    'error': str(e)
                }
        
        return {
            'buffer_supporting_types': buffer_types,
            'memoryview_compatibility': compatibility_test
        }
    
    # Execute all buffer demonstrations
    buffer_basics = buffer_protocol_basics()
    memoryview_ops = memoryview_operations()
    zero_copy = zero_copy_operations()
    compatibility = buffer_interface_compatibility()
    
    return {
        'buffer_protocol_basics': buffer_basics,
        'memoryview_operations': memoryview_ops,
        'zero_copy_operations': zero_copy,
        'buffer_interface_compatibility': compatibility
    }

# =============================================================================
# 9. ARRAY SERIALIZATION & I/O - PERSISTENCE MASTERY
# =============================================================================

"""
ARRAY SERIALIZATION AND I/O OPERATIONS:
Master array persistence, serialization, and I/O operations
"""

def demonstrate_array_serialization():
    """
    COMPREHENSIVE ARRAY SERIALIZATION DEMONSTRATION
    Master array persistence and I/O operations
    """
    
    import array
    import pickle
    import json
    import io
    import base64
    import struct
    
    # Binary serialization methods
    def binary_serialization():
        """Demonstrate binary serialization methods for arrays."""
        
        # Test arrays
        int_array = array.array('i', [1, 2, 3, 4, 5])
        float_array = array.array('f', [1.1, 2.2, 3.3, 4.4])
        byte_array = array.array('B', [65, 66, 67, 68, 69])
        
        serialization_results = {}
        
        # Method 1: tobytes() and frombytes()
        def bytes_serialization():
            """Serialize using bytes methods."""
            
            results = {}
            
            for name, arr in [('int_array', int_array), ('float_array', float_array), ('byte_array', byte_array)]:
                # Serialize to bytes
                binary_data = arr.tobytes()
                
                # Deserialize from bytes
                restored_array = array.array(arr.typecode)
                restored_array.frombytes(binary_data)
                
                results[name] = {
                    'original': list(arr),
                    'typecode': arr.typecode,
                    'binary_size': len(binary_data),
                    'binary_data_sample': binary_data[:20],  # First 20 bytes
                    'restored': list(restored_array),
                    'restoration_successful': list(arr) == list(restored_array)
                }
            
            return results
        
        # Method 2: File I/O
        def file_serialization():
            """Serialize using file I/O methods."""
            
            results = {}
            
            for name, arr in [('int_array', int_array), ('float_array', float_array)]:
                # Serialize to file-like object
                buffer = io.BytesIO()
                arr.tofile(buffer)
                
                # Get binary data
                binary_data = buffer.getvalue()
                
                # Deserialize from file-like object
                buffer.seek(0)  # Reset position
                restored_array = array.array(arr.typecode)
                try:
                    restored_array.fromfile(buffer, len(arr))
                except EOFError:
                    pass  # Handle case where less data is available
                
                results[name] = {
                    'original': list(arr),
                    'typecode': arr.typecode,
                    'file_size': len(binary_data),
                    'restored': list(restored_array),
                    'restoration_successful': list(arr) == list(restored_array)
                }
            
            return results
        
        # Method 3: Struct packing
        def struct_serialization():
            """Serialize using struct module."""
            
            results = {}
            
            # Integer array
            int_format = f'{len(int_array)}i'
            int_packed = struct.pack(int_format, *int_array)
            int_unpacked = list(struct.unpack(int_format, int_packed))
            
            results['int_array'] = {
                'original': list(int_array),
                'format_string': int_format,
                'packed_size': len(int_packed),
                'unpacked': int_unpacked,
                'restoration_successful': list(int_array) == int_unpacked
            }
            
            # Float array  
            float_format = f'{len(float_array)}f'
            float_packed = struct.pack(float_format, *float_array)
            float_unpacked = list(struct.unpack(float_format, float_packed))
            
            results['float_array'] = {
                'original': list(float_array),
                'format_string': float_format,
                'packed_size': len(float_packed),
                'unpacked': float_unpacked,
                'restoration_successful': abs(sum(float_array) - sum(float_unpacked)) < 1e-6
            }
            
            return results
        
        serialization_results['bytes_method'] = bytes_serialization()
        serialization_results['file_method'] = file_serialization()
        serialization_results['struct_method'] = struct_serialization()
        
        return serialization_results
    
    # Text-based serialization
    def text_serialization():
        """Demonstrate text-based serialization methods."""
        
        test_array = array.array('i', [1, 2, 3, 4, 5])
        
        text_methods = {}
        
        # Method 1: JSON serialization (via list conversion)
        def json_serialization():
            """Serialize array as JSON."""
            
            # Convert to JSON-serializable format
            array_data = {
                'typecode': test_array.typecode,
                'data': list(test_array),
                'itemsize': test_array.itemsize
            }
            
            # Serialize to JSON
            json_string = json.dumps(array_data)
            
            # Deserialize from JSON
            restored_data = json.loads(json_string)
            restored_array = array.array(restored_data['typecode'], restored_data['data'])
            
            return {
                'original': list(test_array),
                'json_string': json_string,
                'json_size': len(json_string),
                'restored': list(restored_array),
                'restoration_successful': list(test_array) == list(restored_array)
            }
        
        # Method 2: Base64 encoding of binary data
        def base64_serialization():
            """Serialize array using Base64 encoding."""
            
            # Get binary data
            binary_data = test_array.tobytes()
            
            # Encode to Base64
            base64_string = base64.b64encode(binary_data).decode('ascii')
            
            # Create complete representation
            array_info = {
                'typecode': test_array.typecode,
                'data': base64_string,
                'itemsize': test_array.itemsize,
                'length': len(test_array)
            }
            
            # Serialize info to JSON
            serialized = json.dumps(array_info)
            
            # Deserialize
            restored_info = json.loads(serialized)
            decoded_binary = base64.b64decode(restored_info['data'])
            
            restored_array = array.array(restored_info['typecode'])
            restored_array.frombytes(decoded_binary)
            
            return {
                'original': list(test_array),
                'base64_string': base64_string,
                'serialized_size': len(serialized),
                'restored': list(restored_array),
                'restoration_successful': list(test_array) == list(restored_array)
            }
        
        # Method 3: String representation
        def string_representation():
            """Serialize using string representation."""
            
            # Convert to string
            string_repr = str(test_array)
            
            # For restoration, we'd need to parse the string
            # This is more complex and not recommended for actual use
            
            return {
                'original': list(test_array),
                'string_representation': string_repr,
                'string_size': len(string_repr),
                'note': 'String parsing for restoration is complex and not recommended'
            }
        
        text_methods['json_method'] = json_serialization()
        text_methods['base64_method'] = base64_serialization()
        text_methods['string_method'] = string_representation()
        
        return text_methods
    
    # Pickle serialization
    def pickle_serialization():
        """Demonstrate pickle serialization for arrays."""
        
        # Test arrays
        arrays_to_test = {
            'int_array': array.array('i', [1, 2, 3, 4, 5]),
            'float_array': array.array('f', [1.1, 2.2, 3.3]),
            'byte_array': array.array('B', [65, 66, 67, 68])
        }
        
        pickle_results = {}
        
        for name, arr in arrays_to_test.items():
            # Pickle the array
            pickled_data = pickle.dumps(arr)
            
            # Unpickle the array
            restored_array = pickle.loads(pickled_data)
            
            pickle_results[name] = {
                'original': list(arr),
                'original_type': type(arr).__name__,
                'pickled_size': len(pickled_data),
                'restored': list(restored_array),
                'restored_type': type(restored_array).__name__,
                'restoration_successful': (
                    list(arr) == list(restored_array) and
                    type(arr) == type(restored_array) and
                    arr.typecode == restored_array.typecode
                )
            }
        
        return pickle_results
    
    # Performance comparison of serialization methods
    def serialization_performance():
        """Compare performance of different serialization methods."""
        
        import time
        
        # Create larger array for meaningful performance testing
        large_array = array.array('i', range(10000))
        
        performance_results = {}
        
        # Test tobytes/frombytes
        def test_bytes_performance():
            """Test bytes serialization performance."""
            
            # Serialization
            start_time = time.time()
            binary_data = large_array.tobytes()
            serialize_time = time.time() - start_time
            
            # Deserialization
            start_time = time.time()
            restored = array.array('i')
            restored.frombytes(binary_data)
            deserialize_time = time.time() - start_time
            
            return {
                'serialize_time': serialize_time,
                'deserialize_time': deserialize_time,
                'total_time': serialize_time + deserialize_time,
                'data_size': len(binary_data)
            }
        
        # Test pickle performance
        def test_pickle_performance():
            """Test pickle serialization performance."""
            
            # Serialization
            start_time = time.time()
            pickled_data = pickle.dumps(large_array)
            serialize_time = time.time() - start_time
            
            # Deserialization
            start_time = time.time()
            restored = pickle.loads(pickled_data)
            deserialize_time = time.time() - start_time
            
            return {
                'serialize_time': serialize_time,
                'deserialize_time': deserialize_time,
                'total_time': serialize_time + deserialize_time,
                'data_size': len(pickled_data)
            }
        
        # Test JSON performance
        def test_json_performance():
            """Test JSON serialization performance."""
            
            array_data = {'typecode': large_array.typecode, 'data': list(large_array)}
            
            # Serialization
            start_time = time.time()
            json_string = json.dumps(array_data)
            serialize_time = time.time() - start_time
            
            # Deserialization
            start_time = time.time()
            restored_data = json.loads(json_string)
            restored = array.array(restored_data['typecode'], restored_data['data'])
            deserialize_time = time.time() - start_time
            
            return {
                'serialize_time': serialize_time,
                'deserialize_time': deserialize_time,
                'total_time': serialize_time + deserialize_time,
                'data_size': len(json_string)
            }
        
        performance_results['bytes_method'] = test_bytes_performance()
        performance_results['pickle_method'] = test_pickle_performance()
        performance_results['json_method'] = test_json_performance()
        
        # Performance summary
        performance_summary = {}
        for method, results in performance_results.items():
            performance_summary[method] = {
                'speed_rank': 0,  # Will be calculated
                'size_efficiency': results['data_size'],
                'total_time': results['total_time']
            }
        
        # Rank by speed
        sorted_by_speed = sorted(performance_summary.items(), key=lambda x: x[1]['total_time'])
        for i, (method, data) in enumerate(sorted_by_speed):
            performance_summary[method]['speed_rank'] = i + 1
        
        return {
            'array_size': len(large_array),
            'performance_details': performance_results,
            'performance_summary': performance_summary,
            'fastest_method': sorted_by_speed[0][0]
        }
    
    # Execute all serialization demonstrations
    binary_methods = binary_serialization()
    text_methods = text_serialization()
    pickle_method = pickle_serialization()
    performance = serialization_performance()
    
    return {
        'binary_serialization_methods': binary_methods,
        'text_serialization_methods': text_methods,
        'pickle_serialization': pickle_method,
        'serialization_performance': performance
    }

# =============================================================================
# 10. REAL-WORLD ARRAY APPLICATIONS - PRACTICAL MASTERY
# =============================================================================

"""
REAL-WORLD ARRAY APPLICATIONS:
Comprehensive practical applications and use cases
"""

def demonstrate_real_world_applications():
    """
    COMPREHENSIVE REAL-WORLD APPLICATIONS DEMONSTRATION
    Master practical array applications in real scenarios
    """
    
    import array
    import time
    import random
    import math
    
    # Data Processing Pipeline
    def data_processing_pipeline():
        """Complete data processing pipeline using arrays."""
        
        # Simulate sensor data (temperature readings)
        def generate_sensor_data():
            """Generate simulated sensor data."""
            # Temperature readings in Celsius (-40 to 125, typical sensor range)
            raw_data = [random.randint(-40, 125) for _ in range(1000)]
            return array.array('b', raw_data)  # Use signed byte for temperature
        
        # Data validation and cleaning
        def validate_and_clean_data(sensor_array):
            """Validate and clean sensor data."""
            
            valid_readings = array.array('b')
            invalid_count = 0
            outliers_removed = 0
            
            # Define valid range and outlier thresholds
            MIN_VALID = -30
            MAX_VALID = 100
            
            # Calculate basic statistics for outlier detection
            valid_for_stats = [x for x in sensor_array if MIN_VALID <= x <= MAX_VALID]
            if valid_for_stats:
                mean_temp = sum(valid_for_stats) / len(valid_for_stats)
                std_dev = math.sqrt(sum((x - mean_temp) ** 2 for x in valid_for_stats) / len(valid_for_stats))
                outlier_threshold = 2 * std_dev
            else:
                mean_temp = 0
                outlier_threshold = float('inf')
            
            for reading in sensor_array:
                if not (MIN_VALID <= reading <= MAX_VALID):
                    invalid_count += 1
                    continue
                
                if abs(reading - mean_temp) > outlier_threshold:
                    outliers_removed += 1
                    continue
                
                valid_readings.append(reading)
            
            return {
                'original_count': len(sensor_array),
                'valid_readings': valid_readings,
                'invalid_readings_removed': invalid_count,
                'outliers_removed': outliers_removed,
                'data_quality_percent': (len(valid_readings) / len(sensor_array)) * 100
            }
        
        # Data analysis and statistics
        def analyze_sensor_data(clean_array):
            """Analyze clean sensor data."""
            
            if not clean_array:
                return {'error': 'No valid data for analysis'}
            
            # Basic statistics
            readings = list(clean_array)
            n = len(readings)
            total = sum(readings)
            mean = total / n
            
            # Variance and standard deviation
            variance = sum((x - mean) ** 2 for x in readings) / n
            std_dev = math.sqrt(variance)
            
            # Min/max
            minimum = min(readings)
            maximum = max(readings)
            
            # Median
            sorted_readings = sorted(readings)
            median = (sorted_readings[n//2] + sorted_readings[(n-1)//2]) / 2
            
            # Temperature categories
            categories = {
                'freezing': sum(1 for x in readings if x <= 0),
                'cold': sum(1 for x in readings if 0 < x <= 10),
                'cool': sum(1 for x in readings if 10 < x <= 20),
                'comfortable': sum(1 for x in readings if 20 < x <= 30),
                'warm': sum(1 for x in readings if 30 < x <= 40),
                'hot': sum(1 for x in readings if x > 40)
            }
            
            return {
                'sample_count': n,
                'mean_temperature': mean,
                'median_temperature': median,
                'std_deviation': std_dev,
                'min_temperature': minimum,
                'max_temperature': maximum,
                'temperature_range': maximum - minimum,
                'temperature_categories': categories
            }
        
        # Execute pipeline
        sensor_data = generate_sensor_data()
        validation_results = validate_and_clean_data(sensor_data)
        analysis_results = analyze_sensor_data(validation_results['valid_readings'])
        
        return {
            'raw_data_sample': list(sensor_data[:20]),
            'validation_results': validation_results,
            'analysis_results': analysis_results,
            'pipeline_summary': f"Processed {len(sensor_data)} readings, {validation_results['data_quality_percent']:.1f}% valid"
        }
    
    # Signal Processing Application
    def signal_processing_application():
        """Signal processing using arrays."""
        
        # Generate synthetic signal
        def generate_signal():
            """Generate synthetic signal with noise."""
            
            # Parameters
            sample_rate = 1000  # Hz
            duration = 2.0      # seconds
            frequency1 = 50     # Hz - main signal
            frequency2 = 120    # Hz - secondary signal
            noise_amplitude = 0.1
            
            # Generate time samples
            samples = int(sample_rate * duration)
            signal_array = array.array('f')
            
            for i in range(samples):
                t = i / sample_rate
                
                # Composite signal: two sine waves + noise
                clean_signal = (
                    math.sin(2 * math.pi * frequency1 * t) +
                    0.5 * math.sin(2 * math.pi * frequency2 * t)
                )
                
                # Add random noise
                noise = noise_amplitude * (random.random() - 0.5) * 2
                noisy_signal = clean_signal + noise
                
                signal_array.append(noisy_signal)
            
            return signal_array
        
        # Simple moving average filter
        def moving_average_filter(signal_array, window_size):
            """Apply moving average filter to reduce noise."""
            
            filtered_signal = array.array('f')
            
            for i in range(len(signal_array)):
                # Determine window boundaries
                start_idx = max(0, i - window_size // 2)
                end_idx = min(len(signal_array), i + window_size // 2 + 1)
                
                # Calculate average
                window_sum = sum(signal_array[start_idx:end_idx])
                window_length = end_idx - start_idx
                average = window_sum / window_length if window_length > 0 else 0
                
                filtered_signal.append(average)
            
            return filtered_signal
        
        # Signal analysis
        def analyze_signal(signal_array):
            """Analyze signal characteristics."""
            
            readings = list(signal_array)
            n = len(readings)
            
            # Basic statistics
            mean = sum(readings) / n
            rms = math.sqrt(sum(x*x for x in readings) / n)
            peak_to_peak = max(readings) - min(readings)
            
            # Zero crossings (approximate frequency detection)
            zero_crossings = 0
            for i in range(1, len(readings)):
                if (readings[i-1] >= 0 and readings[i] < 0) or (readings[i-1] < 0 and readings[i] >= 0):
                    zero_crossings += 1
            
            return {
                'sample_count': n,
                'mean_value': mean,
                'rms_value': rms,
                'peak_to_peak': peak_to_peak,
                'zero_crossings': zero_crossings,
                'estimated_frequency_hz': zero_crossings / 4.0  # Rough estimate
            }
        
        # Execute signal processing
        original_signal = generate_signal()
        filtered_signal = moving_average_filter(original_signal, 10)
        
        original_analysis = analyze_signal(original_signal)
        filtered_analysis = analyze_signal(filtered_signal)
        
        return {
            'signal_length': len(original_signal),
            'original_sample': list(original_signal[:20]),
            'filtered_sample': list(filtered_signal[:20]),
            'original_analysis': original_analysis,
            'filtered_analysis': filtered_analysis,
            'noise_reduction': {
                'rms_improvement': original_analysis['rms_value'] - filtered_analysis['rms_value'],
                'peak_to_peak_reduction': original_analysis['peak_to_peak'] - filtered_analysis['peak_to_peak']
            }
        }
    
    # Image Processing Simulation
    def image_processing_simulation():
        """Simulate basic image processing using arrays."""
        
        # Create synthetic "image" data
        def create_test_image():
            """Create synthetic 8-bit grayscale image data."""
            
            width, height = 32, 32  # Small image for demonstration
            image_array = array.array('B')  # Unsigned bytes (0-255)
            
            # Generate gradient pattern with some noise
            for y in range(height):
                for x in range(width):
                    # Create radial gradient
                    center_x, center_y = width // 2, height // 2
                    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                    max_distance = math.sqrt(center_x**2 + center_y**2)
                    
                    # Normalize to 0-255
                    base_value = int((1 - distance / max_distance) * 255)
                    
                    # Add some random noise
                    noise = random.randint(-20, 20)
                    pixel_value = max(0, min(255, base_value + noise))
                    
                    image_array.append(pixel_value)
            
            return image_array, width, height
        
        # Image filtering operations
        def apply_image_filters(image_array, width, height):
            """Apply basic image filtering operations."""
            
            def get_pixel(x, y):
                """Get pixel value with bounds checking."""
                if 0 <= x < width and 0 <= y < height:
                    return image_array[y * width + x]
                return 0
            
            # Brightness adjustment
            def adjust_brightness(factor):
                """Adjust image brightness."""
                bright_array = array.array('B')
                for pixel in image_array:
                    new_value = int(pixel * factor)
                    bright_array.append(max(0, min(255, new_value)))
                return bright_array
            
            # Simple blur filter (3x3 average)
            def blur_filter():
                """Apply 3x3 blur filter."""
                blurred_array = array.array('B')
                
                for y in range(height):
                    for x in range(width):
                        # 3x3 neighborhood
                        total = 0
                        count = 0
                        
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                px, py = x + dx, y + dy
                                if 0 <= px < width and 0 <= py < height:
                                    total += get_pixel(px, py)
                                    count += 1
                        
                        average = total // count if count > 0 else 0
                        blurred_array.append(average)
                
                return blurred_array
            
            # Edge detection (simple gradient)
            def edge_detection():
                """Simple edge detection filter."""
                edge_array = array.array('B')
                
                for y in range(height):
                    for x in range(width):
                        if x == 0 or y == 0 or x == width-1 or y == height-1:
                            edge_array.append(0)
                            continue
                        
                        # Sobel-like operation (simplified)
                        gx = (get_pixel(x+1, y-1) + 2*get_pixel(x+1, y) + get_pixel(x+1, y+1) -
                              get_pixel(x-1, y-1) - 2*get_pixel(x-1, y) - get_pixel(x-1, y+1))
                        
                        gy = (get_pixel(x-1, y+1) + 2*get_pixel(x, y+1) + get_pixel(x+1, y+1) -
                              get_pixel(x-1, y-1) - 2*get_pixel(x, y-1) - get_pixel(x+1, y-1))
                        
                        magnitude = int(math.sqrt(gx*gx + gy*gy))
                        edge_array.append(min(255, magnitude))
                
                return edge_array
            
            return {
                'brightness_increased': adjust_brightness(1.3),
                'brightness_decreased': adjust_brightness(0.7),
                'blurred': blur_filter(),
                'edges': edge_detection()
            }
        
        # Image statistics
        def calculate_image_stats(image_array):
            """Calculate image statistics."""
            
            pixels = list(image_array)
            n = len(pixels)
            
            # Histogram (simplified - 8 bins)
            histogram = [0] * 8
            for pixel in pixels:
                bin_index = min(pixel // 32, 7)  # 32 values per bin
                histogram[bin_index] += 1
            
            return {
                'pixel_count': n,
                'min_intensity': min(pixels),
                'max_intensity': max(pixels),
                'mean_intensity': sum(pixels) / n,
                'histogram': histogram,
                'dynamic_range': max(pixels) - min(pixels)
            }
        
        # Execute image processing
        original_image, width, height = create_test_image()
        filtered_images = apply_image_filters(original_image, width, height)
        original_stats = calculate_image_stats(original_image)
        
        # Stats for processed images
        processed_stats = {}
        for filter_name, filtered_image in filtered_images.items():
            processed_stats[filter_name] = calculate_image_stats(filtered_image)
        
        return {
            'image_dimensions': {'width': width, 'height': height},
            'original_stats': original_stats,
            'original_sample': list(original_image[:20]),
            'processed_samples': {name: list(img[:20]) for name, img in filtered_images.items()},
            'processed_stats': processed_stats
        }
    
    # Performance optimization case study
    def performance_optimization_case():
        """Demonstrate performance optimization using arrays."""
        
        # Problem: Process large dataset efficiently
        data_size = 100000
        
        # Method 1: Using lists (less efficient)
        def process_with_lists():
            """Process data using regular Python lists."""
            
            start_time = time.time()
            
            # Create data
            data_list = list(range(data_size))
            
            # Process data (square each element, filter evens)
            squared = [x*x for x in data_list]
            evens = [x for x in squared if x % 2 == 0]
            
            processing_time = time.time() - start_time
            
            return {
                'method': 'Python lists',
                'processing_time': processing_time,
                'memory_efficient': False,
                'result_count': len(evens),
                'result_sample': evens[:10]
            }
        
        # Method 2: Using arrays (more efficient)
        def process_with_arrays():
            """Process data using arrays."""
            
            start_time = time.time()
            
            # Create data
            data_array = array.array('i', range(data_size))
            
            # Process data
            squared_array = array.array('L')  # Unsigned long for squares
            for x in data_array:
                squared = x * x
                if squared % 2 == 0:
                    squared_array.append(squared)
            
            processing_time = time.time() - start_time
            
            return {
                'method': 'Arrays',
                'processing_time': processing_time,
                'memory_efficient': True,
                'result_count': len(squared_array),
                'result_sample': list(squared_array[:10])
            }
        
        # Method 3: Generator-based processing (memory efficient)
        def process_with_generators():
            """Process data using generators for memory efficiency."""
            
            start_time = time.time()
            
            # Generator pipeline
            def data_generator():
                for x in range(data_size):
                    yield x
            
            def square_generator(data_gen):
                for x in data_gen:
                    yield x * x
            
            def filter_evens(squared_gen):
                for x in squared_gen:
                    if x % 2 == 0:
                        yield x
            
            # Process and collect results
            pipeline = filter_evens(square_generator(data_generator()))
            results = array.array('L', pipeline)
            
            processing_time = time.time() - start_time
            
            return {
                'method': 'Generator pipeline',
                'processing_time': processing_time,
                'memory_efficient': True,
                'result_count': len(results),
                'result_sample': list(results[:10])
            }
        
        # Execute all methods
        list_result = process_with_lists()
        array_result = process_with_arrays()
        generator_result = process_with_generators()
        
        # Compare performance
        methods = [list_result, array_result, generator_result]
        fastest = min(methods, key=lambda x: x['processing_time'])
        
        return {
            'data_size': data_size,
            'list_method': list_result,
            'array_method': array_result,
            'generator_method': generator_result,
            'performance_comparison': {
                'fastest_method': fastest['method'],
                'speed_improvements': {
                    method['method']: fastest['processing_time'] / method['processing_time']
                    for method in methods
                }
            }
        }
    
    # Execute all real-world applications
    data_pipeline = data_processing_pipeline()
    signal_processing = signal_processing_application()
    image_processing = image_processing_simulation()
    performance_optimization = performance_optimization_case()
    
    return {
        'data_processing_pipeline': data_pipeline,
        'signal_processing_application': signal_processing,
        'image_processing_simulation': image_processing,
        'performance_optimization_case': performance_optimization
    }

# =============================================================================
# COMPREHENSIVE ARRAY MASTERY SUMMARY
# =============================================================================

def array_mastery_summary():
    """
    Complete summary of Python arrays mastery
    """
    
    summary = {
        'learning_path_completed': [
            '✓ Array Fundamentals & Overview',
            '✓ Array Creation & Initialization',
            '✓ Array Operations & Methods', 
            '✓ Array Indexing & Slicing',
            '✓ Array Type Codes & Memory',
            '✓ Array vs List Comparison',
            '✓ Array Algorithms & Patterns',
            '✓ Buffer Protocol & Memoryview',
            '✓ Array Serialization & I/O',
            '✓ Real-World Applications'
        ],
        'key_concepts_mastered': {
            'core_concepts': [
                'Homogeneous data storage',
                'Memory efficiency',
                'Type code selection',
                'Buffer protocol'
            ],
            'practical_skills': [
                'Performance optimization',
                'Data processing pipelines', 
                'Signal processing',
                'Serialization techniques'
            ],
            'advanced_topics': [
                'Zero-copy operations',
                'Memory views',
                'Algorithm implementation',
                'Real-world applications'
            ]
        },
        'best_practices': [
            'Choose appropriate type codes for data range',
            'Use arrays for homogeneous numeric data',
            'Leverage memoryview for zero-copy operations',
            'Consider memory efficiency in large datasets',
            'Use proper serialization methods for persistence',
            'Implement efficient algorithms for array processing'
        ],
        'next_steps': [
            'Explore NumPy for advanced mathematical operations',
            'Study computer graphics applications',
            'Learn about real-time signal processing',
            'Investigate scientific computing libraries',
            'Apply arrays in machine learning contexts'
        ]
    }
    
    return summary

# =============================================================================
# DEMONSTRATION EXECUTION
# =============================================================================

if __name__ == "__main__":
    """
    Execute comprehensive array demonstrations
    Run this section to see all array concepts in action
    """
    
    print("🎯 PYTHON ARRAYS - COMPLETE MASTERY DEMONSTRATION")
    print("=" * 60)
    
    # Execute each section
    sections = [
        ("Array Fundamentals", demonstrate_array_fundamentals),
        ("Array Creation", demonstrate_array_creation),
        ("Array Operations", demonstrate_array_operations),
        ("Array Indexing", demonstrate_array_indexing),
        ("Type Codes & Memory", demonstrate_array_type_codes),
        ("Array vs List", demonstrate_array_vs_list),
        ("Array Algorithms", demonstrate_array_algorithms),
        ("Buffer Operations", demonstrate_buffer_operations),
        ("Array Serialization", demonstrate_array_serialization),
        ("Real-World Applications", demonstrate_real_world_applications)
    ]
    
    for section_name, demo_function in sections:
        print(f"\n📋 {section_name.upper()}")
        print("-" * 50)
        
        try:
            results = demo_function()
            print(f"✅ {section_name} demonstration completed successfully")
            print(f"   Results: {len(results)} categories demonstrated")
            
        except Exception as e:
            print(f"❌ Error in {section_name}: {str(e)}")
    
    # Display mastery summary
    print(f"\n🏆 ARRAY MASTERY SUMMARY")
    print("-" * 50)
    
    summary = array_mastery_summary()
    print("✅ Learning Path Completed:")
    for item in summary['learning_path_completed']:
        print(f"   {item}")
    
    print(f"\n🎯 Ready for advanced Python data structures and NumPy!")
    print("=" * 60)
# You can access individual elements by referring to their index number.
#   The first element (counting left to right) is at index 0, the second at index 1, and so on.
#   The last element can also be accessed with negative indexing: -1 for last, -2 for second to last, etc.

"""
Example with array('i', [10, 20, 30, 40, 50]):
 +----+----+----+----+----+
 | 10 | 20 | 30 | 40 | 50 |
 +----+----+----+----+----+
  0    1    2    3    4   
 -5   -4   -3   -2   -1
"""

""" Array Slicing"""
# Arrays can be sliced, allowing you to obtain a sub-array.
#   The slice is defined by two indices, the start and the end.
#       The start index is included in the slice, while the end index is excluded.
#           The slice is defined by the syntax [start:end].
#               Following the logical array recomposition rule: arr[:i] + arr[i:]
#                   The length of a slice is the difference of the indices
#                       my_array[1:3] length equals 2

# Example array for slicing
arr_example = array.array('i', [10, 20, 30, 40, 50])

arr_example[:2]   # Slice from the beginning of the array to index 2 (excluding index 2)
# array('i', [10, 20])

arr_example[2:]   # Slice from index 2 to the end of the array
# array('i', [30, 40, 50])

arr_example[0:2]  # Slice from index 0 to index 2 (excluding index 2)
# array('i', [10, 20])

arr_example[2:5]  # Slice from index 2 to index 5 (excluding index 5)
# array('i', [30, 40, 50])

arr_example[:]    # Slice the entire array
# array('i', [10, 20, 30, 40, 50])

arr_example[::2]  # Slice the array with a step of 2
# array('i', [10, 30, 50])

arr_example[::-1] # Slice the array in reverse order
# array('i', [50, 40, 30, 20, 10])

arr_example[-2:]  # Slice the last two elements of the array
# array('i', [40, 50])

arr_example[-2:-1] # Slice from index -2 to index -1 (excluding index -1)
# array('i', [40])

""" Array slice out of range can be handled without error. """
#   The slice will be empty if the start index is greater than the array length.

arr_example[42:]  # Slice from index 42 to the end of the array
# array('i', [])             # Empty array

arr_example[:42]  # Slice from index 0 to index 42 (excluding index 42)
# array('i', [10, 20, 30, 40, 50])      # The entire array, since 42 is beyond the array length

# ----------

"""Modify Array Elements"""
#   Arrays are mutable, meaning you can change the value of an element in an array.
#       You can change the value of an element in an array by
#           assigning a new value to the index of the element.

""" Change the value of an element in an Array """
#  You can change the value of an element in an array by assigning a new value to the index of the element.

arr_modify = array.array('i', [100, 200, 300])

arr_modify[1] = 250
print(arr_modify)
# array('i', [100, 250, 300])

""" Add an element to an Array """
# You can add an element to an array by using the append() method.

arr_modify = array.array('i', [100, 200, 300])

arr_modify.append(400)
print(arr_modify)
# array('i', [100, 200, 300, 400])

""" Remove an element from an Array """
# You can remove an element from an array by using the remove() method.

arr_modify = array.array('i', [100, 200, 300])

arr_modify.remove(200)
print(arr_modify)
# array('i', [100, 300])

""" Insert element at specific position """
# You can insert an element at a specific position using the insert() method.

arr_modify = array.array('i', [100, 300])

arr_modify.insert(1, 200)
print(arr_modify)
# array('i', [100, 200, 300])

""" Pop element from Array """
# You can remove and return an element from the array using pop().

arr_modify = array.array('i', [100, 200, 300])

popped_element = arr_modify.pop()
print(f"Popped: {popped_element}")
# Popped: 300
print(arr_modify)
# array('i', [100, 200])

# ----------

""" Array Methods """
# Array methods are functions that can be used to manipulate arrays.
#   They are called on an array object and can be used to perform various operations on the array.

#  append()    Adds an element at the end of the array
#  buffer_info() Returns a tuple (address, length) giving the current memory info
#  byteswap()  Byteswaps all items of the array
#  count()     Returns the number of elements with the specified value
#  extend()    Add the elements of an array (or any iterable), to the end of the current array
#  frombytes() Appends items from the string, interpreting as machine values
#  fromfile()  Read n items from the file object and append them to the end of the array
#  fromlist()  Append items from the list to the array
#  index()     Returns the index of the first element with the specified value
#  insert()    Adds an element at the specified position
#  pop()       Removes the element at the specified position
#  remove()    Removes the item with the specified value
#  reverse()   Reverses the order of the array
#  tobytes()   Convert the array to a bytes object
#  tofile()    Write all items to a file object
#  tolist()    Convert the array to a list

""" Additional Array Operations """

# Get array information
arr_info = array.array('i', [1, 2, 3, 4, 5])

# Convert array to list
arr_as_list = arr_info.tolist()
print(f"Array as list: {arr_as_list}")
# Array as list: [1, 2, 3, 4, 5]

# Count occurrences of a value
arr_count = array.array('i', [1, 2, 2, 3, 2])
count_twos = arr_count.count(2)
print(f"Number of 2s: {count_twos}")
# Number of 2s: 3

# Get index of a value
index_of_three = arr_count.index(3)
print(f"Index of 3: {index_of_three}")
# Index of 3: 3

# Extend array with another array
arr1 = array.array('i', [1, 2, 3])
arr2 = array.array('i', [4, 5, 6])
arr1.extend(arr2)
print(f"Extended array: {arr1}")
# Extended array: array('i', [1, 2, 3, 4, 5, 6])

# Reverse an array
arr_reverse = array.array('i', [1, 2, 3, 4, 5])
arr_reverse.reverse()
print(f"Reversed array: {arr_reverse}")
# Reversed array: array('i', [5, 4, 3, 2, 1])

# ----------

""" PRACTICAL EXAMPLES: WHEN TO USE ARRAYS VS LISTS """

# 🎯 Example 1: Temperature Sensor Data (Arrays are better)
# When storing large amounts of numeric data from sensors
print("=== Temperature Monitoring System ===")
import array

# Store 1000 temperature readings (more memory efficient with arrays)
temperatures = array.array('f')  # Float array for decimal temperatures

# Simulate adding temperature readings
sample_temps = [20.5, 21.2, 22.1, 20.8, 19.9, 21.5, 22.3, 20.1, 21.9, 20.4]
for temp in sample_temps:
    temperatures.append(temp)

print(f"Temperatures recorded: {len(temperatures)}")
print(f"First 5 readings: {temperatures[:5].tolist()}")
print(f"Average temperature: {sum(temperatures) / len(temperatures):.1f}°C")

# Memory usage comparison
import sys
list_temps = list(temperatures)
print(f"\nMemory usage:")
print(f"Array: {sys.getsizeof(temperatures)} bytes")
print(f"List:  {sys.getsizeof(list_temps)} bytes")
print(f"Array is {sys.getsizeof(list_temps) / sys.getsizeof(temperatures):.1f}x more memory efficient!")

# 🎯 Example 2: RGB Color Values (Arrays are perfect)
print("\n=== Image Processing: RGB Values ===")
# RGB values are always integers 0-255, perfect for arrays

# Create RGB array for a small image (3x3 pixels, RGB values)
rgb_data = array.array('B')  # Unsigned char (0-255)
rgb_pixels = [
    255, 0, 0,    # Red pixel
    0, 255, 0,    # Green pixel  
    0, 0, 255,    # Blue pixel
    255, 255, 0,  # Yellow pixel
    255, 0, 255,  # Magenta pixel
    0, 255, 255,  # Cyan pixel
    128, 128, 128, # Gray pixel
    255, 255, 255, # White pixel
    0, 0, 0       # Black pixel
]

rgb_data.extend(rgb_pixels)
print(f"Image data: {len(rgb_data)} color values")
print(f"First pixel RGB: ({rgb_data[0]}, {rgb_data[1]}, {rgb_data[2]})")

# 🎯 Example 3: Scientific Computing (Arrays excel here)
print("\n=== Scientific Data: Experimental Measurements ===")

# Store measurement data efficiently
measurements = array.array('d')  # Double precision for scientific accuracy
sample_data = [1.23456789, 2.34567890, 3.45678901, 4.56789012, 5.67890123]
measurements.extend(sample_data)

print(f"High-precision measurements: {measurements.tolist()}")

# Statistical calculations
mean = sum(measurements) / len(measurements)
variance = sum((x - mean) ** 2 for x in measurements) / len(measurements)
print(f"Mean: {mean:.8f}")
print(f"Variance: {variance:.8f}")

# 🎯 Example 4: When Lists Are Better
print("\n=== When to Use Lists Instead ===")

# Mixed data types - arrays can't handle this
student_record = ["Alice", 20, 85.5, True, ["Math", "Physics", "Chemistry"]]
print(f"Student record: {student_record}")
print("^ This MUST be a list - arrays can't store mixed types")

# Frequent insertions/deletions - lists are more flexible
dynamic_data = [1, 2, 3]
dynamic_data.insert(1, "new_item")  # Easy with lists
dynamic_data.append({"key": "value"})  # Mix types freely
print(f"Dynamic data: {dynamic_data}")

# 📊 PERFORMANCE COMPARISON
print("\n=== Performance Comparison Demo ===")
import time

# Time array creation vs list creation
print("Creating 100,000 integers...")

# Array creation
start_time = time.time()
large_array = array.array('i', range(100000))
array_time = time.time() - start_time

# List creation  
start_time = time.time()
large_list = list(range(100000))
list_time = time.time() - start_time

print(f"Array creation: {array_time:.6f} seconds")
print(f"List creation:  {list_time:.6f} seconds")

# Memory comparison
print(f"\nMemory usage for 100,000 integers:")
print(f"Array: {sys.getsizeof(large_array):,} bytes")
print(f"List:  {sys.getsizeof(large_list):,} bytes")
print(f"Memory savings: {(sys.getsizeof(large_list) - sys.getsizeof(large_array)):,} bytes")

# 🎯 BEST PRACTICES SUMMARY
print("\n" + "="*50)
print("ARRAYS vs LISTS - DECISION GUIDE")
print("="*50)
print("✅ Use ARRAYS when:")
print("  • Large amounts of numeric data")
print("  • Memory efficiency is important")  
print("  • All elements are the same type")
print("  • Interfacing with C libraries")
print("  • Scientific computing")
print("  • Image/audio processing")

print("\n✅ Use LISTS when:")
print("  • Mixed data types needed")
print("  • Flexibility is more important than memory")
print("  • Frequent insertions/deletions")
print("  • General-purpose data storage")
print("  • Working with objects, not just numbers")
print("  • You need built-in methods like sort(), reverse(), etc.")

# ---------