""" 3.10.0_Python_INDEX.py """

# =============================================================================
# PYTHON INDEXING & SLICING - COMPLETE MASTERY GUIDE
# =============================================================================
# Version: 3.10.0 | Educational Excellence Target: 9.5/10
# Purpose: Master Python indexing, slicing, and sequence manipulation
# Target: Beginner to Advanced Python programmers
# =============================================================================

"""
🎯 LEARNING OBJECTIVES:
By mastering Python indexing and slicing, you will:
✓ Understand positive and negative indexing systems
✓ Master slicing syntax and advanced slice operations
✓ Apply indexing to strings, lists, tuples, and sequences
✓ Implement efficient sequence manipulation techniques
✓ Use advanced slicing patterns for data processing
✓ Optimize sequence operations for performance

🚀 QUICK NAVIGATION:
├── 1. INDEXING FUNDAMENTALS & CONCEPTS (FOUNDATION)
├── 2. POSITIVE & NEGATIVE INDEXING (BASICS)
├── 3. SLICING SYNTAX & OPERATIONS (CORE)
├── 4. ADVANCED SLICING PATTERNS (TECHNIQUES)
├── 5. SEQUENCE MODIFICATION & MANIPULATION (EDITING)
├── 6. MULTI-DIMENSIONAL INDEXING (ADVANCED)
├── 7. INDEXING PERFORMANCE & OPTIMIZATION (EFFICIENCY)
├── 8. ERROR HANDLING & BOUNDS CHECKING (SAFETY)
├── 9. PRACTICAL INDEXING APPLICATIONS (REAL-WORLD)
└── 10. MASTERY PATTERNS & BEST PRACTICES

🔍 CORE CONCEPT:
Python indexing provides zero-based access to sequence elements,
while slicing enables powerful sub-sequence extraction and manipulation
with start:stop:step syntax for comprehensive data processing.
"""

# =============================================================================
# 1. INDEXING FUNDAMENTALS & CONCEPTS - FOUNDATION
# =============================================================================

"""
INDEXING FUNDAMENTALS COMPLETE REFERENCE:
Understanding Python's indexing system and sequence access patterns
"""

def demonstrate_indexing_fundamentals():
    """
    COMPREHENSIVE INDEXING FUNDAMENTALS OVERVIEW
    Master the core concepts of Python indexing systems
    """
    
    # Indexing concept demonstration
    def indexing_concept_overview():
        """Demonstrate core indexing concepts."""
        
        # Visual representation of indexing
        text = "Python"
        numbers = [10, 20, 30, 40, 50]
        
        # Positive indexing (left to right, starting from 0)
        positive_indexing = {
            'string_example': text,
            'string_indices': {i: char for i, char in enumerate(text)},
            'list_example': numbers,
            'list_indices': {i: value for i, value in enumerate(numbers)}
        }
        
        # Negative indexing (right to left, starting from -1)
        negative_indexing = {
            'string_negative': {-i-1: char for i, char in enumerate(reversed(text))},
            'list_negative': {-i-1: value for i, value in enumerate(reversed(numbers))}
        }
        
        # Index mapping demonstration
        def create_index_mapping(sequence):
            """Create comprehensive index mapping."""
            mapping = {}
            for i, item in enumerate(sequence):
                mapping[f'positive_{i}'] = item
                mapping[f'negative_{-len(sequence)+i}'] = item
            return mapping
        
        index_mappings = {
            'string_mapping': create_index_mapping(text),
            'list_mapping': create_index_mapping(numbers)
        }
        
        # Indexing properties
        indexing_properties = {
            'zero_based': 'Python uses 0-based indexing',
            'inclusive_access': 'Index directly accesses the element',
            'negative_support': 'Negative indices count from the end',
            'bounds_checking': 'IndexError raised for invalid indices',
            'universal_application': 'Works with all sequence types'
        }
        
        return {
            'positive_indexing': positive_indexing,
            'negative_indexing': negative_indexing,
            'index_mappings': index_mappings,
            'indexing_properties': indexing_properties
        }
    
    # Sequence type indexing compatibility
    def sequence_type_compatibility():
        """Demonstrate indexing across different sequence types."""
        
        # Different sequence types
        sequences = {
            'string': "Hello",
            'list': [1, 2, 3, 4, 5],
            'tuple': (10, 20, 30, 40),
            'range': range(5, 10),
            'bytes': b'abcde',
            'bytearray': bytearray(b'vwxyz')
        }
        
        # Test indexing operations on each type
        indexing_tests = {}
        
        for seq_type, sequence in sequences.items():
            try:
                # Convert range and bytes/bytearray for consistent display
                if seq_type == 'range':
                    display_seq = list(sequence)
                elif seq_type in ['bytes', 'bytearray']:
                    display_seq = [chr(b) if isinstance(b, int) else b for b in sequence]
                else:
                    display_seq = list(sequence)
                
                indexing_tests[seq_type] = {
                    'sequence': display_seq,
                    'length': len(sequence),
                    'first_element': sequence[0],
                    'last_element': sequence[-1],
                    'middle_element': sequence[len(sequence)//2] if len(sequence) > 0 else None,
                    'supports_indexing': True,
                    'type_info': type(sequence).__name__
                }
                
            except Exception as e:
                indexing_tests[seq_type] = {
                    'sequence': str(sequence),
                    'supports_indexing': False,
                    'error': str(e),
                    'type_info': type(sequence).__name__
                }
        
        return indexing_tests
    
    # Index bounds and validation
    def index_bounds_validation():
        """Demonstrate index bounds checking and validation."""
        
        test_sequence = [10, 20, 30, 40, 50]
        
        def safe_index_access(sequence, index):
            """Safely access sequence element with bounds checking."""
            try:
                if isinstance(index, int):
                    # Check bounds
                    if -len(sequence) <= index < len(sequence):
                        return {
                            'success': True,
                            'value': sequence[index],
                            'index': index,
                            'bounds_status': 'within_bounds'
                        }
                    else:
                        return {
                            'success': False,
                            'error': 'Index out of bounds',
                            'index': index,
                            'bounds_status': 'out_of_bounds',
                            'valid_range': f'[{-len(sequence)}, {len(sequence)-1}]'
                        }
                else:
                    return {
                        'success': False,
                        'error': 'Index must be integer',
                        'index': index,
                        'bounds_status': 'invalid_type'
                    }
            except Exception as e:
                return {
                    'success': False,
                    'error': str(e),
                    'index': index,
                    'bounds_status': 'exception_occurred'
                }
        
        # Test various index scenarios
        test_indices = [0, 2, 4, -1, -3, -5, 5, 10, -6, -10, 'invalid']
        
        bounds_test_results = {
            'sequence': test_sequence,
            'sequence_length': len(test_sequence),
            'valid_positive_range': f'[0, {len(test_sequence)-1}]',
            'valid_negative_range': f'[{-len(test_sequence)}, -1]',
            'test_results': {}
        }
        
        for index in test_indices:
            bounds_test_results['test_results'][f'index_{index}'] = safe_index_access(test_sequence, index)
        
        return bounds_test_results
    
    # Execute all fundamental demonstrations
    concepts = indexing_concept_overview()
    compatibility = sequence_type_compatibility()
    bounds_validation = index_bounds_validation()
    
    return {
        'indexing_concepts': concepts,
        'sequence_compatibility': compatibility,
        'bounds_validation': bounds_validation
    }

# =============================================================================
# 2. POSITIVE & NEGATIVE INDEXING - BASICS MASTERY
# =============================================================================

"""
POSITIVE AND NEGATIVE INDEXING MASTERY:
Complete understanding of both indexing directions
"""

def demonstrate_positive_negative_indexing():
    """
    COMPREHENSIVE POSITIVE AND NEGATIVE INDEXING DEMONSTRATION
    Master both indexing directions and their applications
    """
    
    # Positive indexing patterns
    def positive_indexing_patterns():
        """Demonstrate positive indexing patterns and usage."""
        
        # Test sequences
        sequences = {
            'short_string': "Hi",
            'medium_string': "Python",
            'long_string': "Programming",
            'small_list': [1, 2, 3],
            'medium_list': [10, 20, 30, 40, 50],
            'large_list': list(range(20))
        }
        
        positive_patterns = {}
        
        for name, sequence in sequences.items():
            # Common positive indexing patterns
            patterns = {
                'first_element': sequence[0] if len(sequence) > 0 else None,
                'second_element': sequence[1] if len(sequence) > 1 else None,
                'third_element': sequence[2] if len(sequence) > 2 else None,
                'middle_element': sequence[len(sequence)//2] if len(sequence) > 0 else None,
                'second_to_last': sequence[-2] if len(sequence) > 1 else None,
                'last_element': sequence[-1] if len(sequence) > 0 else None
            }
            
            # Index enumeration
            enumeration = {f'index_{i}': item for i, item in enumerate(sequence)}
            
            positive_patterns[name] = {
                'sequence': list(sequence) if not isinstance(sequence, list) else sequence,
                'length': len(sequence),
                'common_patterns': patterns,
                'full_enumeration': enumeration
            }
        
        return positive_patterns
    
    # Negative indexing patterns
    def negative_indexing_patterns():
        """Demonstrate negative indexing patterns and usage."""
        
        test_sequence = "Programming"
        
        # Comprehensive negative indexing demonstration
        def demonstrate_negative_access(sequence):
            """Demonstrate various negative indexing patterns."""
            
            negative_access = {}
            
            # Map each negative index to its value
            for i in range(len(sequence)):
                negative_index = -(len(sequence) - i)
                positive_index = i
                value = sequence[negative_index]
                
                negative_access[f'neg_{negative_index}'] = {
                    'negative_index': negative_index,
                    'equivalent_positive': positive_index,
                    'value': value,
                    'position_description': f'{i+1} from start, {len(sequence)-i} from end'
                }
            
            return negative_access
        
        # Common negative indexing patterns
        def common_negative_patterns(sequence):
            """Common negative indexing use cases."""
            
            patterns = {
                'last_element': {
                    'index': -1,
                    'value': sequence[-1],
                    'use_case': 'Most recent item, file extension, etc.'
                },
                'second_last': {
                    'index': -2,
                    'value': sequence[-2] if len(sequence) > 1 else None,
                    'use_case': 'Previous item, backup value, etc.'
                },
                'third_last': {
                    'index': -3,
                    'value': sequence[-3] if len(sequence) > 2 else None,
                    'use_case': 'Pattern matching, rollback scenarios'
                },
                'last_n_elements': {
                    'pattern': 'sequence[-n:]',
                    'example': list(sequence[-3:]),
                    'use_case': 'Recent history, tail of data'
                },
                'all_but_last': {
                    'pattern': 'sequence[:-1]',
                    'example': list(sequence[:-1]),
                    'use_case': 'Remove file extension, trim data'
                }
            }
            
            return patterns
        
        # Negative vs positive equivalence
        def negative_positive_equivalence(sequence):
            """Show equivalence between negative and positive indices."""
            
            equivalences = []
            
            for i in range(len(sequence)):
                positive_idx = i
                negative_idx = i - len(sequence)
                value = sequence[i]
                
                equivalences.append({
                    'positive_index': positive_idx,
                    'negative_index': negative_idx,
                    'value': value,
                    'verification': sequence[positive_idx] == sequence[negative_idx]
                })
            
            return equivalences
        
        negative_access = demonstrate_negative_access(test_sequence)
        common_patterns = common_negative_patterns(test_sequence)
        equivalence = negative_positive_equivalence(test_sequence)
        
        return {
            'test_sequence': test_sequence,
            'negative_index_mapping': negative_access,
            'common_patterns': common_patterns,
            'positive_negative_equivalence': equivalence
        }
    
    # Index calculation and conversion
    def index_calculation_conversion():
        """Demonstrate index calculations and conversions."""
        
        def calculate_indices(sequence_length):
            """Calculate all valid indices for a sequence."""
            
            calculations = {
                'sequence_length': sequence_length,
                'positive_indices': list(range(sequence_length)),
                'negative_indices': list(range(-sequence_length, 0)),
                'index_pairs': [(i, i - sequence_length) for i in range(sequence_length)]
            }
            
            return calculations
        
        def convert_negative_to_positive(negative_index, sequence_length):
            """Convert negative index to positive equivalent."""
            
            if negative_index >= 0:
                return {
                    'input_index': negative_index,
                    'is_negative': False,
                    'converted_index': negative_index,
                    'note': 'Already positive'
                }
            
            converted = sequence_length + negative_index
            
            return {
                'input_index': negative_index,
                'is_negative': True,
                'converted_index': converted,
                'valid': 0 <= converted < sequence_length,
                'formula': f'{sequence_length} + ({negative_index}) = {converted}'
            }
        
        def convert_positive_to_negative(positive_index, sequence_length):
            """Convert positive index to negative equivalent."""
            
            if positive_index < 0:
                return {
                    'input_index': positive_index,
                    'is_positive': False,
                    'converted_index': positive_index,
                    'note': 'Already negative'
                }
            
            converted = positive_index - sequence_length
            
            return {
                'input_index': positive_index,
                'is_positive': True,
                'converted_index': converted,
                'valid': -sequence_length <= converted < 0,
                'formula': f'{positive_index} - {sequence_length} = {converted}'
            }
        
        # Test with different sequence lengths
        test_lengths = [3, 5, 10, 1]
        calculations_results = {}
        
        for length in test_lengths:
            calculations_results[f'length_{length}'] = calculate_indices(length)
        
        # Test conversions
        conversion_tests = {
            'negative_to_positive': [
                convert_negative_to_positive(-1, 5),
                convert_negative_to_positive(-3, 5),
                convert_negative_to_positive(-5, 5),
                convert_negative_to_positive(2, 5)  # Already positive
            ],
            'positive_to_negative': [
                convert_positive_to_negative(0, 5),
                convert_positive_to_negative(2, 5),
                convert_positive_to_negative(4, 5),
                convert_positive_to_negative(-2, 5)  # Already negative
            ]
        }
        
        return {
            'index_calculations': calculations_results,
            'conversion_examples': conversion_tests
        }
    
    # Execute all positive/negative indexing demonstrations
    positive_patterns = positive_indexing_patterns()
    negative_patterns = negative_indexing_patterns()
    calculations = index_calculation_conversion()
    
    return {
        'positive_indexing_patterns': positive_patterns,
        'negative_indexing_patterns': negative_patterns,
        'index_calculations': calculations
    }

# =============================================================================
# 3. SLICING SYNTAX & OPERATIONS - CORE MASTERY
# =============================================================================

"""
COMPREHENSIVE SLICING SYNTAX AND OPERATIONS:
Master Python's powerful slicing capabilities
"""

def demonstrate_slicing_operations():
    """
    COMPREHENSIVE SLICING DEMONSTRATION
    Master all aspects of Python slicing syntax and operations
    """
    
    # Basic slicing syntax patterns
    def basic_slicing_syntax():
        """Demonstrate fundamental slicing syntax patterns."""
        
        test_sequence = "Programming"
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # Basic slicing patterns with explanations
        slicing_patterns = {
            'full_copy': {
                'syntax': '[:]',
                'string_result': test_sequence[:],
                'list_result': test_list[:],
                'explanation': 'Creates a shallow copy of entire sequence'
            },
            'from_start': {
                'syntax': '[:n]',
                'string_result': test_sequence[:5],
                'list_result': test_list[:5],
                'explanation': 'Elements from start up to (but not including) index n'
            },
            'to_end': {
                'syntax': '[n:]',
                'string_result': test_sequence[4:],
                'list_result': test_list[4:],
                'explanation': 'Elements from index n to end of sequence'
            },
            'middle_slice': {
                'syntax': '[start:end]',
                'string_result': test_sequence[2:7],
                'list_result': test_list[2:7],
                'explanation': 'Elements from start index to end index (exclusive)'
            },
            'negative_start': {
                'syntax': '[-n:]',
                'string_result': test_sequence[-4:],
                'list_result': test_list[-4:],
                'explanation': 'Last n elements of sequence'
            },
            'negative_end': {
                'syntax': '[:-n]',
                'string_result': test_sequence[:-2],
                'list_result': test_list[:-2],
                'explanation': 'All elements except last n elements'
            },
            'both_negative': {
                'syntax': '[-n:-m]',
                'string_result': test_sequence[-6:-2],
                'list_result': test_list[-6:-2],
                'explanation': 'Slice using negative indices for both bounds'
            }
        }
        
        return {
            'test_string': test_sequence,
            'test_list': test_list,
            'slicing_patterns': slicing_patterns
        }
    
    # Step slicing patterns
    def step_slicing_patterns():
        """Demonstrate step-based slicing patterns."""
        
        sequence = list(range(20))  # [0, 1, 2, ..., 19]
        
        step_patterns = {
            'every_second': {
                'syntax': '[::2]',
                'result': sequence[::2],
                'explanation': 'Every second element starting from beginning'
            },
            'every_third': {
                'syntax': '[::3]',
                'result': sequence[::3],
                'explanation': 'Every third element starting from beginning'
            },
            'reverse_all': {
                'syntax': '[::-1]',
                'result': sequence[::-1],
                'explanation': 'Reverse the entire sequence'
            },
            'reverse_every_second': {
                'syntax': '[::-2]',
                'result': sequence[::-2],
                'explanation': 'Every second element in reverse order'
            },
            'range_with_step': {
                'syntax': '[start:end:step]',
                'result': sequence[2:15:3],
                'explanation': 'Every 3rd element from index 2 to 15'
            },
            'negative_range_step': {
                'syntax': '[start:end:-step]',
                'result': sequence[15:5:-2],
                'explanation': 'Every 2nd element from 15 down to 5 (reverse)'
            },
            'partial_reverse': {
                'syntax': '[start:end:-1]',
                'result': sequence[10:3:-1],
                'explanation': 'Reverse slice from start to end'
            }
        }
        
        # Advanced step combinations
        advanced_patterns = {
            'skip_first_last': {
                'syntax': '[1:-1:2]',
                'result': sequence[1:-1:2],
                'explanation': 'Every 2nd element, excluding first and last'
            },
            'middle_third_reverse': {
                'syntax': '[2*len//3:len//3:-1]',
                'result': sequence[2*len(sequence)//3:len(sequence)//3:-1],
                'explanation': 'Middle third of sequence in reverse'
            },
            'alternating_halves': {
                'syntax': 'first[::2] + second[::2]',
                'result': sequence[:10:2] + sequence[10::2],
                'explanation': 'Alternating pattern from both halves'
            }
        }
        
        return {
            'test_sequence': sequence,
            'basic_step_patterns': step_patterns,
            'advanced_step_patterns': advanced_patterns
        }
    
    # Slice bounds and edge cases
    def slice_bounds_edge_cases():
        """Demonstrate slice bounds behavior and edge cases."""
        
        test_list = [10, 20, 30, 40, 50]
        
        # Out of bounds slicing (Python handles gracefully)
        edge_cases = {
            'start_beyond_end': {
                'slice': test_list[10:15],
                'explanation': 'Start index beyond sequence length returns empty',
                'result': test_list[10:15]
            },
            'end_beyond_length': {
                'slice': test_list[2:100],
                'explanation': 'End index beyond length returns to actual end',
                'result': test_list[2:100]
            },
            'negative_beyond_start': {
                'slice': test_list[-100:3],
                'explanation': 'Negative start beyond length starts from beginning',
                'result': test_list[-100:3]
            },
            'start_equals_end': {
                'slice': test_list[2:2],
                'explanation': 'Start equals end returns empty slice',
                'result': test_list[2:2]
            },
            'start_greater_than_end': {
                'slice': test_list[4:2],
                'explanation': 'Start > end with positive step returns empty',
                'result': test_list[4:2]
            },
            'empty_sequence_slice': {
                'slice': [][0:5],
                'explanation': 'Slicing empty sequence returns empty',
                'result': [][0:5]
            }
        }
        
        # Step edge cases
        step_edge_cases = {
            'zero_step_error': {
                'explanation': 'Step of 0 raises ValueError',
                'error_demo': 'slice(None, None, 0) raises ValueError'
            },
            'large_positive_step': {
                'slice': test_list[::100],
                'explanation': 'Large step returns first element only',
                'result': test_list[::100]
            },
            'large_negative_step': {
                'slice': test_list[::-100],
                'explanation': 'Large negative step returns last element only',
                'result': test_list[::-100]
            }
        }
        
        # Slice object demonstration
        def slice_object_demo():
            """Demonstrate slice objects and their properties."""
            
            slice_objects = {
                'basic_slice': slice(2, 7),
                'step_slice': slice(1, 10, 2),
                'negative_slice': slice(-5, -1),
                'reverse_slice': slice(None, None, -1)
            }
            
            slice_info = {}
            for name, slice_obj in slice_objects.items():
                slice_info[name] = {
                    'slice_object': str(slice_obj),
                    'start': slice_obj.start,
                    'stop': slice_obj.stop,
                    'step': slice_obj.step,
                    'result_on_test_list': test_list[slice_obj]
                }
            
            return slice_info
        
        slice_objects = slice_object_demo()
        
        return {
            'test_list': test_list,
            'bounds_edge_cases': edge_cases,
            'step_edge_cases': step_edge_cases,
            'slice_objects': slice_objects
        }
    
    # Slice assignment and modification
    def slice_assignment_modification():
        """Demonstrate slice assignment for sequence modification."""
        
        # Note: Only works with mutable sequences (lists)
        def demonstrate_slice_assignment():
            """Show various slice assignment patterns."""
            
            assignment_examples = []
            
            # Replace slice with same length
            test_list = [1, 2, 3, 4, 5]
            original = test_list.copy()
            test_list[1:4] = [20, 30, 40]
            assignment_examples.append({
                'operation': 'Replace slice with same length',
                'original': original,
                'assignment': 'list[1:4] = [20, 30, 40]',
                'result': test_list.copy()
            })
            
            # Replace slice with different length
            test_list = [1, 2, 3, 4, 5]
            original = test_list.copy()
            test_list[1:4] = [100, 200]
            assignment_examples.append({
                'operation': 'Replace slice with shorter sequence',
                'original': original,
                'assignment': 'list[1:4] = [100, 200]',
                'result': test_list.copy()
            })
            
            # Insert elements using empty slice
            test_list = [1, 2, 3, 4, 5]
            original = test_list.copy()
            test_list[2:2] = [25, 26, 27]
            assignment_examples.append({
                'operation': 'Insert elements using empty slice',
                'original': original,
                'assignment': 'list[2:2] = [25, 26, 27]',
                'result': test_list.copy()
            })
            
            # Delete elements using empty assignment
            test_list = [1, 2, 3, 4, 5]
            original = test_list.copy()
            test_list[1:3] = []
            assignment_examples.append({
                'operation': 'Delete elements using empty assignment',
                'original': original,
                'assignment': 'list[1:3] = []',
                'result': test_list.copy()
            })
            
            # Step slice assignment
            test_list = [1, 2, 3, 4, 5, 6]
            original = test_list.copy()
            test_list[::2] = [10, 30, 50]
            assignment_examples.append({
                'operation': 'Step slice assignment',
                'original': original,
                'assignment': 'list[::2] = [10, 30, 50]',
                'result': test_list.copy()
            })
            
            return assignment_examples
        
        # Immutable sequence behavior
        def immutable_sequence_behavior():
            """Show behavior with immutable sequences."""
            
            immutable_examples = {
                'string_slice': {
                    'sequence': "Hello",
                    'slice_result': "Hello"[1:4],
                    'assignment_possible': False,
                    'note': 'Strings are immutable - cannot assign to slices'
                },
                'tuple_slice': {
                    'sequence': (1, 2, 3, 4, 5),
                    'slice_result': (1, 2, 3, 4, 5)[1:4],
                    'assignment_possible': False,
                    'note': 'Tuples are immutable - cannot assign to slices'
                },
                'list_slice': {
                    'sequence': [1, 2, 3, 4, 5],
                    'slice_result': [1, 2, 3, 4, 5][1:4],
                    'assignment_possible': True,
                    'note': 'Lists are mutable - slice assignment works'
                }
            }
            
            return immutable_examples
        
        assignment_examples = demonstrate_slice_assignment()
        immutable_behavior = immutable_sequence_behavior()
        
        return {
            'slice_assignment_examples': assignment_examples,
            'immutable_sequence_behavior': immutable_behavior
        }
    
    # Execute all slicing demonstrations
    basic_syntax = basic_slicing_syntax()
    step_patterns = step_slicing_patterns()
    edge_cases = slice_bounds_edge_cases()
    assignment = slice_assignment_modification()
    
    return {
        'basic_slicing_syntax': basic_syntax,
        'step_slicing_patterns': step_patterns,
        'slice_bounds_edge_cases': edge_cases,
        'slice_assignment': assignment
    }

# =============================================================================
# 4. ADVANCED SLICING PATTERNS - TECHNIQUES MASTERY
# =============================================================================

"""
ADVANCED SLICING PATTERNS AND TECHNIQUES:
Master sophisticated slicing patterns for data manipulation
"""

def demonstrate_advanced_slicing():
    """
    COMPREHENSIVE ADVANCED SLICING DEMONSTRATION
    Master sophisticated slicing techniques and patterns
    """
    
    import random
    
    # Multi-dimensional slicing simulation
    def multi_dimensional_slicing():
        """Simulate multi-dimensional slicing using 1D sequences."""
        
        # Create 2D matrix simulation using flat list
        rows, cols = 5, 4
        matrix_data = list(range(rows * cols))  # [0, 1, 2, ..., 19]
        
        def get_2d_index(row, col):
            """Convert 2D coordinates to 1D index."""
            return row * cols + col
        
        def get_row_slice(row):
            """Extract a complete row."""
            start_idx = row * cols
            end_idx = start_idx + cols
            return matrix_data[start_idx:end_idx]
        
        def get_column_slice(col):
            """Extract a complete column."""
            return [matrix_data[get_2d_index(row, col)] for row in range(rows)]
        
        def get_diagonal_slice():
            """Extract main diagonal elements."""
            return [matrix_data[get_2d_index(i, i)] for i in range(min(rows, cols))]
        
        def get_submatrix(start_row, end_row, start_col, end_col):
            """Extract submatrix."""
            submatrix = []
            for row in range(start_row, end_row):
                row_data = []
                for col in range(start_col, end_col):
                    row_data.append(matrix_data[get_2d_index(row, col)])
                submatrix.append(row_data)
            return submatrix
        
        # Matrix representation for display
        matrix_2d = []
        for row in range(rows):
            matrix_2d.append(get_row_slice(row))
        
        multi_dim_examples = {
            'matrix_dimensions': {'rows': rows, 'cols': cols},
            'flat_representation': matrix_data,
            'matrix_2d_representation': matrix_2d,
            'row_extractions': {
                'first_row': get_row_slice(0),
                'middle_row': get_row_slice(2),
                'last_row': get_row_slice(rows-1)
            },
            'column_extractions': {
                'first_column': get_column_slice(0),
                'middle_column': get_column_slice(1),
                'last_column': get_column_slice(cols-1)
            },
            'diagonal_extraction': get_diagonal_slice(),
            'submatrix_example': get_submatrix(1, 4, 1, 3)
        }
        
        return multi_dim_examples
    
    # Pattern-based slicing
    def pattern_based_slicing():
        """Demonstrate pattern-based slicing techniques."""
        
        # Test data: mixed content
        data = list(range(50))  # [0, 1, 2, ..., 49]
        
        # Conditional slicing patterns
        def conditional_slicing_patterns():
            """Apply slicing based on conditions."""
            
            patterns = {
                'first_n_percent': {
                    'description': 'First 20% of elements',
                    'slice': data[:len(data)//5],
                    'formula': 'data[:len(data)//5]'
                },
                'middle_third': {
                    'description': 'Middle third of elements',
                    'slice': data[len(data)//3:2*len(data)//3],
                    'formula': 'data[len(data)//3:2*len(data)//3]'
                },
                'last_quarter': {
                    'description': 'Last 25% of elements',
                    'slice': data[3*len(data)//4:],
                    'formula': 'data[3*len(data)//4:]'
                },
                'even_positions': {
                    'description': 'Elements at even positions',
                    'slice': data[::2],
                    'formula': 'data[::2]'
                },
                'odd_positions': {
                    'description': 'Elements at odd positions',
                    'slice': data[1::2],
                    'formula': 'data[1::2]'
                },
                'every_fifth': {
                    'description': 'Every fifth element',
                    'slice': data[::5],
                    'formula': 'data[::5]'
                }
            }
            
            return patterns
        
        # Overlapping slice patterns
        def overlapping_slice_patterns():
            """Create overlapping slices for sliding window effects."""
            
            window_size = 5
            step = 2
            
            overlapping_slices = []
            for start in range(0, len(data) - window_size + 1, step):
                end = start + window_size
                overlapping_slices.append({
                    'start': start,
                    'end': end,
                    'slice': data[start:end],
                    'overlap_with_previous': start < (start - step + window_size) if overlapping_slices else False
                })
            
            return {
                'window_size': window_size,
                'step_size': step,
                'total_windows': len(overlapping_slices),
                'overlapping_slices': overlapping_slices[:10]  # Show first 10
            }
        
        # Reverse pattern slicing
        def reverse_pattern_slicing():
            """Various reverse slicing patterns."""
            
            reverse_patterns = {
                'complete_reverse': {
                    'description': 'Complete sequence reversed',
                    'slice': data[::-1],
                    'formula': 'data[::-1]'
                },
                'reverse_first_half': {
                    'description': 'First half reversed',
                    'slice': data[:len(data)//2][::-1],
                    'formula': 'data[:len(data)//2][::-1]'
                },
                'reverse_second_half': {
                    'description': 'Second half reversed',
                    'slice': data[len(data)//2:][::-1],
                    'formula': 'data[len(data)//2:][::-1]'
                },
                'reverse_every_third': {
                    'description': 'Every third element in reverse',
                    'slice': data[::-3],
                    'formula': 'data[::-3]'
                },
                'interleaved_reverse': {
                    'description': 'Interleave forward and reverse',
                    'slice': data[:len(data)//2] + data[len(data)//2:][::-1],
                    'formula': 'data[:half] + data[half:][::-1]'
                }
            }
            
            return reverse_patterns
        
        conditional = conditional_slicing_patterns()
        overlapping = overlapping_slice_patterns()
        reverse = reverse_pattern_slicing()
        
        return {
            'test_data_size': len(data),
            'conditional_patterns': conditional,
            'overlapping_patterns': overlapping,
            'reverse_patterns': reverse
        }
    
    # Dynamic slicing techniques
    def dynamic_slicing_techniques():
        """Demonstrate dynamic slicing based on runtime conditions."""
        
        # Sample data
        sample_data = list(range(100))
        
        # Dynamic slice calculation functions
        def calculate_dynamic_slice(sequence, pattern_type):
            """Calculate slice parameters dynamically."""
            
            length = len(sequence)
            
            patterns = {
                'adaptive_window': {
                    'description': 'Window size adapts to sequence length',
                    'start': 0,
                    'end': max(10, length // 10),
                    'step': 1
                },
                'golden_ratio': {
                    'description': 'Use golden ratio for slice points',
                    'start': int(length * 0.382),  # 1 - golden ratio
                    'end': int(length * 0.618),    # golden ratio
                    'step': 1
                },
                'fibonacci_step': {
                    'description': 'Use Fibonacci sequence for step',
                    'start': 0,
                    'end': length,
                    'step': 8  # 8th Fibonacci number
                },
                'logarithmic': {
                    'description': 'Logarithmic distribution',
                    'start': 0,
                    'end': length,
                    'step': max(1, int(length ** 0.5))
                }
            }
            
            if pattern_type not in patterns:
                return None
            
            pattern = patterns[pattern_type]
            start, end, step = pattern['start'], pattern['end'], pattern['step']
            
            return {
                'pattern_type': pattern_type,
                'description': pattern['description'],
                'slice_params': {'start': start, 'end': end, 'step': step},
                'slice_result': sequence[start:end:step],
                'result_length': len(sequence[start:end:step])
            }
        
        # Test dynamic patterns
        dynamic_results = {}
        for pattern in ['adaptive_window', 'golden_ratio', 'fibonacci_step', 'logarithmic']:
            dynamic_results[pattern] = calculate_dynamic_slice(sample_data, pattern)
        
        # Conditional slicing based on data properties
        def conditional_data_slicing(sequence):
            """Apply slicing based on data characteristics."""
            
            # Analyze data properties
            total_sum = sum(sequence)
            average = total_sum / len(sequence)
            maximum = max(sequence)
            minimum = min(sequence)
            
            # Apply conditional slicing
            conditions = {
                'above_average_positions': {
                    'description': 'Positions where value > average',
                    'indices': [i for i, val in enumerate(sequence) if val > average],
                    'values': [val for val in sequence if val > average]
                },
                'top_quartile': {
                    'description': 'Top 25% of values by position',
                    'slice': sequence[3*len(sequence)//4:],
                    'values': sequence[3*len(sequence)//4:]
                },
                'outliers': {
                    'description': 'Values significantly different from average',
                    'threshold': average + (maximum - minimum) * 0.3,
                    'indices': [i for i, val in enumerate(sequence) if abs(val - average) > (maximum - minimum) * 0.3],
                    'values': [val for val in sequence if abs(val - average) > (maximum - minimum) * 0.3]
                }
            }
            
            return {
                'data_stats': {
                    'length': len(sequence),
                    'sum': total_sum,
                    'average': average,
                    'min': minimum,
                    'max': maximum
                },
                'conditional_slices': conditions
            }
        
        conditional_results = conditional_data_slicing(sample_data[:20])  # Use subset for clear example
        
        return {
            'sample_data_size': len(sample_data),
            'dynamic_pattern_results': dynamic_results,
            'conditional_slicing_results': conditional_results
        }
    
    # Execute all advanced slicing demonstrations
    multi_dim = multi_dimensional_slicing()
    pattern_based = pattern_based_slicing()
    dynamic = dynamic_slicing_techniques()
    
    return {
        'multi_dimensional_slicing': multi_dim,
        'pattern_based_slicing': pattern_based,
        'dynamic_slicing_techniques': dynamic
    }

# =============================================================================
# 5. SEQUENCE MODIFICATION & MANIPULATION - EDITING MASTERY
# =============================================================================

"""
SEQUENCE MODIFICATION AND MANIPULATION:
Master sequence editing through indexing and slicing
"""

def demonstrate_sequence_modification():
    """
    COMPREHENSIVE SEQUENCE MODIFICATION DEMONSTRATION
    Master sequence editing and manipulation techniques
    """
    
    # Single element modification
    def single_element_modification():
        """Demonstrate single element modification techniques."""
        
        # Mutable sequence modifications
        test_list = [10, 20, 30, 40, 50]
        modification_log = []
        
        # Direct index assignment
        original = test_list.copy()
        test_list[2] = 99
        modification_log.append({
            'operation': 'Direct index assignment',
            'code': 'list[2] = 99',
            'before': original,
            'after': test_list.copy()
        })
        
        # Negative index assignment
        original = test_list.copy()
        test_list[-1] = 100
        modification_log.append({
            'operation': 'Negative index assignment',
            'code': 'list[-1] = 100',
            'before': original,
            'after': test_list.copy()
        })
        
        # Conditional modification
        original = test_list.copy()
        for i in range(len(test_list)):
            if test_list[i] > 50:
                test_list[i] = test_list[i] * 2
        modification_log.append({
            'operation': 'Conditional modification',
            'code': 'Double values > 50',
            'before': original,
            'after': test_list.copy()
        })
        
        # Function-based modification
        original = test_list.copy()
        def modify_element(value):
            return value + 5 if value < 50 else value - 5
        
        for i in range(len(test_list)):
            test_list[i] = modify_element(test_list[i])
        modification_log.append({
            'operation': 'Function-based modification',
            'code': '+5 if <50, else -5',
            'before': original,
            'after': test_list.copy()
        })
        
        return {
            'modification_examples': modification_log,
            'final_list': test_list
        }
    
    # Slice-based modification
    def slice_based_modification():
        """Demonstrate slice-based modification techniques."""
        
        modification_examples = []
        
        # Replace slice with same length
        test_list = list(range(10))  # [0, 1, 2, ..., 9]
        original = test_list.copy()
        test_list[2:5] = [22, 33, 44]
        modification_examples.append({
            'operation': 'Replace slice - same length',
            'original': original,
            'assignment': 'list[2:5] = [22, 33, 44]',
            'result': test_list.copy(),
            'length_change': len(test_list) - len(original)
        })
        
        # Replace slice with longer sequence
        test_list = list(range(10))
        original = test_list.copy()
        test_list[3:6] = [30, 31, 32, 33, 34]
        modification_examples.append({
            'operation': 'Replace slice - longer sequence',
            'original': original,
            'assignment': 'list[3:6] = [30, 31, 32, 33, 34]',
            'result': test_list.copy(),
            'length_change': len(test_list) - len(original)
        })
        
        # Replace slice with shorter sequence
        test_list = list(range(10))
        original = test_list.copy()
        test_list[1:7] = [100, 200]
        modification_examples.append({
            'operation': 'Replace slice - shorter sequence',
            'original': original,
            'assignment': 'list[1:7] = [100, 200]',
            'result': test_list.copy(),
            'length_change': len(test_list) - len(original)
        })
        
        # Insert using empty slice
        test_list = list(range(5))
        original = test_list.copy()
        test_list[2:2] = [88, 89]
        modification_examples.append({
            'operation': 'Insert using empty slice',
            'original': original,
            'assignment': 'list[2:2] = [88, 89]',
            'result': test_list.copy(),
            'length_change': len(test_list) - len(original)
        })
        
        # Delete using empty assignment
        test_list = list(range(10))
        original = test_list.copy()
        test_list[3:7] = []
        modification_examples.append({
            'operation': 'Delete using empty assignment',
            'original': original,
            'assignment': 'list[3:7] = []',
            'result': test_list.copy(),
            'length_change': len(test_list) - len(original)
        })
        
        # Step slice modification
        test_list = list(range(10))
        original = test_list.copy()
        test_list[::2] = [x * 10 for x in range(len(test_list[::2]))]
        modification_examples.append({
            'operation': 'Step slice modification',
            'original': original,
            'assignment': 'list[::2] = [0, 10, 20, 30, 40]',
            'result': test_list.copy(),
            'length_change': len(test_list) - len(original)
        })
        
        return modification_examples
    
    # Advanced modification patterns
    def advanced_modification_patterns():
        """Demonstrate advanced modification patterns."""
        
        # Swap elements using indexing
        def element_swapping():
            """Various element swapping techniques."""
            
            test_list = [1, 2, 3, 4, 5]
            swapping_examples = []
            
            # Basic swap
            original = test_list.copy()
            test_list[0], test_list[4] = test_list[4], test_list[0]
            swapping_examples.append({
                'method': 'Basic swap',
                'code': 'list[0], list[4] = list[4], list[0]',
                'before': original,
                'after': test_list.copy()
            })
            
            # Reverse pairs
            test_list = [1, 2, 3, 4, 5, 6]
            original = test_list.copy()
            for i in range(0, len(test_list)-1, 2):
                test_list[i], test_list[i+1] = test_list[i+1], test_list[i]
            swapping_examples.append({
                'method': 'Reverse adjacent pairs',
                'code': 'Swap each pair: (0,1), (2,3), (4,5)',
                'before': original,
                'after': test_list.copy()
            })
            
            # Circular rotation
            test_list = [1, 2, 3, 4, 5]
            original = test_list.copy()
            test_list[:] = test_list[1:] + test_list[:1]  # Rotate left
            swapping_examples.append({
                'method': 'Circular rotation left',
                'code': 'list[:] = list[1:] + list[:1]',
                'before': original,
                'after': test_list.copy()
            })
            
            return swapping_examples
        
        # Pattern-based modifications
        def pattern_modifications():
            """Apply modifications based on patterns."""
            
            test_data = list(range(20))
            pattern_examples = []
            
            # Modify every nth element
            original = test_data.copy()
            for i in range(0, len(test_data), 3):
                test_data[i] = test_data[i] * -1
            pattern_examples.append({
                'pattern': 'Every 3rd element negative',
                'original': original,
                'modified': test_data.copy()
            })
            
            # Modify based on position characteristics
            test_data = list(range(20))
            original = test_data.copy()
            for i in range(len(test_data)):
                if i % 2 == 0:  # Even positions
                    test_data[i] = test_data[i] ** 2
                else:  # Odd positions
                    test_data[i] = test_data[i] + 100
            pattern_examples.append({
                'pattern': 'Even positions squared, odd positions +100',
                'original': original,
                'modified': test_data.copy()
            })
            
            # Modify based on value characteristics
            test_data = list(range(20))
            original = test_data.copy()
            average = sum(test_data) / len(test_data)
            for i in range(len(test_data)):
                if test_data[i] > average:
                    test_data[i] = int(test_data[i] * 0.8)  # Reduce high values
                elif test_data[i] < average:
                    test_data[i] = int(test_data[i] * 1.2)  # Boost low values
            pattern_examples.append({
                'pattern': 'Normalize around average',
                'original': original,
                'modified': test_data.copy(),
                'average_used': average
            })
            
            return pattern_examples
        
        # In-place vs copy modifications
        def inplace_vs_copy():
            """Compare in-place vs copy-based modifications."""
            
            original_list = [1, 2, 3, 4, 5]
            
            # In-place modification
            inplace_list = original_list.copy()
            inplace_list.reverse()  # Modifies original
            inplace_result = {
                'method': 'In-place modification',
                'original': original_list,
                'modified': inplace_list,
                'same_object': inplace_list is original_list  # False, because we used copy()
            }
            
            # Copy-based modification
            copy_result = original_list[::-1]  # Creates new list
            copy_result_info = {
                'method': 'Copy-based modification',
                'original': original_list,
                'modified': copy_result,
                'same_object': copy_result is original_list  # False
            }
            
            # Slice assignment (in-place)
            slice_list = original_list.copy()
            slice_list[:] = original_list[::-1]  # Modifies existing list
            slice_result = {
                'method': 'Slice assignment (in-place)',
                'original': original_list,
                'modified': slice_list,
                'technique': 'list[:] = new_content'
            }
            
            return {
                'inplace_modification': inplace_result,
                'copy_modification': copy_result_info,
                'slice_assignment': slice_result
            }
        
        swapping = element_swapping()
        patterns = pattern_modifications()
        inplace_vs_copy = inplace_vs_copy()
        
        return {
            'element_swapping': swapping,
            'pattern_modifications': patterns,
            'inplace_vs_copy_comparison': inplace_vs_copy
        }
    
    # Execute all modification demonstrations
    single_element = single_element_modification()
    slice_based = slice_based_modification()
    advanced = advanced_modification_patterns()
    
    return {
        'single_element_modification': single_element,
        'slice_based_modification': slice_based,
        'advanced_modification_patterns': advanced
    }

# =============================================================================
# 6. MULTI-DIMENSIONAL INDEXING - ADVANCED PATTERNS
# =============================================================================

"""
MULTI-DIMENSIONAL INDEXING PATTERNS:
Advanced techniques for complex data structures
"""

def demonstrate_multidimensional_indexing():
    """
    COMPREHENSIVE MULTI-DIMENSIONAL INDEXING DEMONSTRATION
    Master advanced indexing patterns for complex data structures
    """
    
    # Nested list indexing
    def nested_list_indexing():
        """Demonstrate indexing in nested list structures."""
        
        # Create nested structure
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        
        # Basic nested indexing
        basic_access = {
            'element_0_0': matrix[0][0],     # First element of first row
            'element_1_2': matrix[1][2],     # Third element of second row
            'element_-1_-1': matrix[-1][-1], # Last element of last row
            'entire_first_row': matrix[0],    # Entire first row
            'entire_last_row': matrix[-1]     # Entire last row
        }
        
        # Column extraction (manual)
        def extract_column(matrix, col_index):
            """Extract a column from 2D matrix."""
            return [row[col_index] for row in matrix]
        
        column_access = {
            'first_column': extract_column(matrix, 0),
            'second_column': extract_column(matrix, 1),
            'last_column': extract_column(matrix, -1)
        }
        
        # Diagonal extraction
        def extract_diagonal(matrix):
            """Extract main diagonal from square matrix."""
            return [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
        
        def extract_anti_diagonal(matrix):
            """Extract anti-diagonal from square matrix."""
            n = len(matrix)
            return [matrix[i][n-1-i] for i in range(n)]
        
        diagonal_access = {
            'main_diagonal': extract_diagonal(matrix),
            'anti_diagonal': extract_anti_diagonal(matrix)
        }
        
        # Submatrix extraction
        def extract_submatrix(matrix, start_row, end_row, start_col, end_col):
            """Extract submatrix from larger matrix."""
            return [row[start_col:end_col] for row in matrix[start_row:end_row]]
        
        submatrix_examples = {
            'top_left_2x2': extract_submatrix(matrix, 0, 2, 0, 2),
            'center_2x2': extract_submatrix(matrix, 1, 3, 1, 3),
            'bottom_right_2x2': extract_submatrix(matrix, 2, 4, 2, 4)
        }
        
        return {
            'original_matrix': matrix,
            'basic_element_access': basic_access,
            'column_access': column_access,
            'diagonal_access': diagonal_access,
            'submatrix_examples': submatrix_examples
        }
    
    # Complex nested structure indexing
    def complex_nested_indexing():
        """Handle complex nested data structures."""
        
        # Complex nested structure
        complex_data = {
            'users': [
                {
                    'id': 1,
                    'name': 'Alice',
                    'scores': [85, 92, 78, 88],
                    'metadata': {'active': True, 'level': 'advanced'}
                },
                {
                    'id': 2,
                    'name': 'Bob',
                    'scores': [76, 81, 85, 79],
                    'metadata': {'active': True, 'level': 'intermediate'}
                },
                {
                    'id': 3,
                    'name': 'Charlie',
                    'scores': [91, 89, 94, 87],
                    'metadata': {'active': False, 'level': 'advanced'}
                }
            ],
            'courses': ['Math', 'Science', 'History', 'English']
        }
        
        # Deep indexing examples
        deep_access = {
            'first_user_name': complex_data['users'][0]['name'],
            'second_user_first_score': complex_data['users'][1]['scores'][0],
            'last_user_metadata_level': complex_data['users'][-1]['metadata']['level'],
            'first_course': complex_data['courses'][0]
        }
        
        # Extracting patterns from complex structure
        def extract_all_names(data):
            """Extract all user names."""
            return [user['name'] for user in data['users']]
        
        def extract_all_scores(data):
            """Extract all scores as flat list."""
            all_scores = []
            for user in data['users']:
                all_scores.extend(user['scores'])
            return all_scores
        
        def extract_active_users(data):
            """Extract only active users."""
            return [user for user in data['users'] if user['metadata']['active']]
        
        def extract_score_by_course(data, course_index):
            """Extract all scores for specific course."""
            return [user['scores'][course_index] for user in data['users']]
        
        pattern_extraction = {
            'all_names': extract_all_names(complex_data),
            'all_scores': extract_all_scores(complex_data),
            'active_users': len(extract_active_users(complex_data)),
            'math_scores': extract_score_by_course(complex_data, 0),
            'english_scores': extract_score_by_course(complex_data, 3)
        }
        
        return {
            'complex_structure_sample': {
                'total_users': len(complex_data['users']),
                'total_courses': len(complex_data['courses']),
                'structure_depth': '3 levels deep'
            },
            'deep_access_examples': deep_access,
            'pattern_extraction': pattern_extraction
        }
    
    # Flattened indexing for multi-dimensional data
    def flattened_indexing():
        """Convert multi-dimensional indices to flat indices."""
        
        # 3D array simulation using 1D list
        dims = (3, 4, 5)  # 3x4x5 array
        total_size = dims[0] * dims[1] * dims[2]
        flat_array = list(range(total_size))  # [0, 1, 2, ..., 59]
        
        def coords_to_flat_index(x, y, z, dims):
            """Convert 3D coordinates to flat index."""
            return x * dims[1] * dims[2] + y * dims[2] + z
        
        def flat_index_to_coords(flat_index, dims):
            """Convert flat index to 3D coordinates."""
            x = flat_index // (dims[1] * dims[2])
            remainder = flat_index % (dims[1] * dims[2])
            y = remainder // dims[2]
            z = remainder % dims[2]
            return (x, y, z)
        
        # Test coordinate conversions
        test_coordinates = [(0, 0, 0), (1, 2, 3), (2, 3, 4), (0, 1, 4)]
        conversion_tests = []
        
        for coords in test_coordinates:
            flat_idx = coords_to_flat_index(*coords, dims)
            back_to_coords = flat_index_to_coords(flat_idx, dims)
            value = flat_array[flat_idx]
            
            conversion_tests.append({
                'original_coords': coords,
                'flat_index': flat_idx,
                'converted_back': back_to_coords,
                'conversion_correct': coords == back_to_coords,
                'value': value
            })
        
        # Slice operations on flattened data
        def get_3d_slice(flat_array, dims, x_slice=None, y_slice=None, z_slice=None):
            """Extract 3D slice from flattened array."""
            x_range = range(*x_slice.indices(dims[0])) if x_slice else range(dims[0])
            y_range = range(*y_slice.indices(dims[1])) if y_slice else range(dims[1])
            z_range = range(*z_slice.indices(dims[2])) if z_slice else range(dims[2])
            
            result = []
            for x in x_range:
                for y in y_range:
                    for z in z_range:
                        flat_idx = coords_to_flat_index(x, y, z, dims)
                        result.append(flat_array[flat_idx])
            
            return result
        
        # Test 3D slicing
        slice_examples = {
            'first_xy_plane': get_3d_slice(flat_array, dims, slice(0, 1), None, None),
            'middle_z_column': get_3d_slice(flat_array, dims, None, None, slice(2, 3)),
            'corner_cube': get_3d_slice(flat_array, dims, slice(0, 2), slice(0, 2), slice(0, 2))
        }
        
        return {
            'array_dimensions': dims,
            'total_elements': total_size,
            'coordinate_conversion_tests': conversion_tests,
            'slice_examples': slice_examples
        }
    
    # Execute all multi-dimensional demonstrations
    nested_lists = nested_list_indexing()
    complex_nested = complex_nested_indexing()
    flattened = flattened_indexing()
    
    return {
        'nested_list_indexing': nested_lists,
        'complex_nested_indexing': complex_nested,
        'flattened_indexing': flattened
    }

# =============================================================================
# 7. INDEXING PERFORMANCE & OPTIMIZATION - EFFICIENCY MASTERY
# =============================================================================

"""
INDEXING PERFORMANCE AND OPTIMIZATION:
Master performance characteristics and optimization techniques
"""

def demonstrate_indexing_performance():
    """
    COMPREHENSIVE INDEXING PERFORMANCE DEMONSTRATION
    Master performance optimization for indexing operations
    """
    
    import time
    import random
    
    # Basic indexing performance comparison
    def basic_indexing_performance():
        """Compare performance of different indexing methods."""
        
        # Create test data
        small_list = list(range(1000))
        large_list = list(range(100000))
        
        performance_results = {}
        
        # Single element access performance
        def test_single_access(test_list, iterations=1000):
            """Test single element access performance."""
            
            # Random access test
            indices = [random.randint(0, len(test_list)-1) for _ in range(iterations)]
            
            start_time = time.time()
            for idx in indices:
                _ = test_list[idx]
            random_access_time = time.time() - start_time
            
            # Sequential access test
            start_time = time.time()
            for i in range(min(iterations, len(test_list))):
                _ = test_list[i]
            sequential_access_time = time.time() - start_time
            
            # Negative indexing test
            start_time = time.time()
            for i in range(min(iterations, len(test_list))):
                _ = test_list[-(i+1)]
            negative_access_time = time.time() - start_time
            
            return {
                'random_access_time': random_access_time,
                'sequential_access_time': sequential_access_time,
                'negative_access_time': negative_access_time,
                'iterations': iterations
            }
        
        performance_results['small_list'] = {
            'size': len(small_list),
            'performance': test_single_access(small_list)
        }
        
        performance_results['large_list'] = {
            'size': len(large_list),
            'performance': test_single_access(large_list, iterations=100)  # Fewer iterations for large list
        }
        
        return performance_results
    
    # Slicing performance analysis
    def slicing_performance_analysis():
        """Analyze performance of different slicing operations."""
        
        test_list = list(range(50000))
        
        def time_slicing_operation(operation_func, description):
            """Time a slicing operation."""
            start_time = time.time()
            result = operation_func()
            end_time = time.time()
            
            return {
                'description': description,
                'execution_time': end_time - start_time,
                'result_size': len(result) if hasattr(result, '__len__') else 1
            }
        
        # Different slicing operations
        slicing_tests = {
            'small_slice': time_slicing_operation(
                lambda: test_list[100:200],
                'Small slice (100 elements)'
            ),
            'large_slice': time_slicing_operation(
                lambda: test_list[:10000],
                'Large slice (10000 elements)'
            ),
            'step_slice': time_slicing_operation(
                lambda: test_list[::100],
                'Step slice (every 100th element)'
            ),
            'reverse_slice': time_slicing_operation(
                lambda: test_list[::-1],
                'Complete reverse slice'
            ),
            'negative_slice': time_slicing_operation(
                lambda: test_list[-1000:],
                'Negative indexing slice (last 1000)'
            ),
            'copy_slice': time_slicing_operation(
                lambda: test_list[:],
                'Complete copy via slicing'
            )
        }
        
        # Performance comparison
        fastest = min(slicing_tests.values(), key=lambda x: x['execution_time'])
        slowest = max(slicing_tests.values(), key=lambda x: x['execution_time'])
        
        return {
            'test_list_size': len(test_list),
            'slicing_performance': slicing_tests,
            'performance_summary': {
                'fastest_operation': fastest['description'],
                'fastest_time': fastest['execution_time'],
                'slowest_operation': slowest['description'],
                'slowest_time': slowest['execution_time'],
                'speed_ratio': slowest['execution_time'] / fastest['execution_time'] if fastest['execution_time'] > 0 else float('inf')
            }
        }
    
    # Memory efficiency analysis
    def memory_efficiency_analysis():
        """Analyze memory usage of different indexing approaches."""
        
        import sys
        
        # Create test data
        original_list = list(range(10000))
        
        def measure_memory_usage(operation_func, description):
            """Measure memory usage of an operation."""
            
            # Force garbage collection before measurement
            import gc
            gc.collect()
            
            # Perform operation
            result = operation_func()
            
            # Measure memory
            if hasattr(result, '__len__'):
                memory_usage = sys.getsizeof(result)
                if isinstance(result, list) and len(result) > 0:
                    # Add overhead of list elements for lists
                    memory_usage += sum(sys.getsizeof(item) for item in result[:100])  # Sample first 100
                    if len(result) > 100:
                        memory_usage = memory_usage * len(result) // 100  # Estimate total
            else:
                memory_usage = sys.getsizeof(result)
            
            return {
                'description': description,
                'memory_usage': memory_usage,
                'result_type': type(result).__name__,
                'result_size': len(result) if hasattr(result, '__len__') else 1
            }
        
        memory_tests = {
            'original_list': measure_memory_usage(
                lambda: original_list,
                'Original list (reference)'
            ),
            'slice_copy': measure_memory_usage(
                lambda: original_list[:5000],
                'Slice copy (5000 elements)'
            ),
            'step_slice': measure_memory_usage(
                lambda: original_list[::10],
                'Step slice (every 10th element)'
            ),
            'single_element': measure_memory_usage(
                lambda: original_list[5000],
                'Single element access'
            ),
            'list_comprehension': measure_memory_usage(
                lambda: [x for x in original_list[:1000]],
                'List comprehension (1000 elements)'
            )
        }
        
        return {
            'original_list_size': len(original_list),
            'memory_analysis': memory_tests,
            'memory_efficiency_tips': [
                'Use slicing instead of list comprehension for simple copies',
                'Prefer single element access over slicing when possible',
                'Step slicing can significantly reduce memory usage',
                'Consider generators for memory-efficient iteration'
            ]
        }
    
    # Optimization techniques
    def optimization_techniques():
        """Demonstrate indexing optimization techniques."""
        
        # Cache-friendly access patterns
        def cache_friendly_patterns():
            """Demonstrate cache-friendly indexing patterns."""
            
            large_matrix = [[i * 100 + j for j in range(100)] for i in range(100)]
            
            def row_major_access():
                """Row-major access pattern (cache-friendly)."""
                start_time = time.time()
                total = 0
                for i in range(100):
                    for j in range(100):
                        total += large_matrix[i][j]
                return time.time() - start_time, total
            
            def column_major_access():
                """Column-major access pattern (cache-unfriendly)."""
                start_time = time.time()
                total = 0
                for j in range(100):
                    for i in range(100):
                        total += large_matrix[i][j]
                return time.time() - start_time, total
            
            row_time, row_total = row_major_access()
            col_time, col_total = column_major_access()
            
            return {
                'row_major': {'time': row_time, 'total': row_total},
                'column_major': {'time': col_time, 'total': col_total},
                'performance_difference': col_time / row_time if row_time > 0 else float('inf'),
                'totals_match': row_total == col_total
            }
        
        # Batch operations
        def batch_operations():
            """Demonstrate batch indexing operations."""
            
            test_data = list(range(10000))
            indices_to_access = [random.randint(0, len(test_data)-1) for _ in range(1000)]
            
            # Individual access
            start_time = time.time()
            individual_results = []
            for idx in indices_to_access:
                individual_results.append(test_data[idx])
            individual_time = time.time() - start_time
            
            # Batch access using list comprehension
            start_time = time.time()
            batch_results = [test_data[idx] for idx in indices_to_access]
            batch_time = time.time() - start_time
            
            # Sorted batch access (more cache-friendly)
            sorted_indices = sorted(indices_to_access)
            start_time = time.time()
            sorted_batch_results = [test_data[idx] for idx in sorted_indices]
            sorted_batch_time = time.time() - start_time
            
            return {
                'individual_access': {
                    'time': individual_time,
                    'method': 'Loop with individual appends'
                },
                'batch_access': {
                    'time': batch_time,
                    'method': 'List comprehension'
                },
                'sorted_batch_access': {
                    'time': sorted_batch_time,
                    'method': 'Sorted indices list comprehension'
                },
                'results_match': (
                    len(individual_results) == len(batch_results) == len(sorted_batch_results)
                )
            }
        
        # Pre-computation strategies
        def precomputation_strategies():
            """Demonstrate pre-computation for repeated access."""
            
            data = list(range(1000))
            
            # Scenario: Frequently access last N elements
            def frequent_tail_access_naive(data, n, iterations=100):
                """Naive approach - compute slice each time."""
                start_time = time.time()
                for _ in range(iterations):
                    tail = data[-n:]
                    _ = sum(tail)  # Some operation on tail
                return time.time() - start_time
            
            def frequent_tail_access_optimized(data, n, iterations=100):
                """Optimized approach - pre-compute slice."""
                tail = data[-n:]  # Pre-compute once
                start_time = time.time()
                for _ in range(iterations):
                    _ = sum(tail)  # Same operation on pre-computed slice
                return time.time() - start_time
            
            n = 100
            naive_time = frequent_tail_access_naive(data, n)
            optimized_time = frequent_tail_access_optimized(data, n)
            
            return {
                'scenario': f'Frequent access to last {n} elements',
                'naive_approach': naive_time,
                'optimized_approach': optimized_time,
                'improvement_factor': naive_time / optimized_time if optimized_time > 0 else float('inf'),
                'optimization_technique': 'Pre-computation of frequently accessed slices'
            }
        
        cache_patterns = cache_friendly_patterns()
        batch_ops = batch_operations()
        precomputation = precomputation_strategies()
        
        return {
            'cache_friendly_patterns': cache_patterns,
            'batch_operations': batch_ops,
            'precomputation_strategies': precomputation
        }
    
    # Execute all performance demonstrations
    basic_performance = basic_indexing_performance()
    slicing_performance = slicing_performance_analysis()
    memory_efficiency = memory_efficiency_analysis()
    optimization = optimization_techniques()
    
    return {
        'basic_indexing_performance': basic_performance,
        'slicing_performance_analysis': slicing_performance,
        'memory_efficiency_analysis': memory_efficiency,
        'optimization_techniques': optimization
    }

# =============================================================================
# 8. ERROR HANDLING & BOUNDS CHECKING - SAFETY MASTERY
# =============================================================================

"""
ERROR HANDLING AND BOUNDS CHECKING:
Master safe indexing practices and error prevention
"""

def demonstrate_error_handling():
    """
    COMPREHENSIVE ERROR HANDLING DEMONSTRATION
    Master safe indexing and error prevention techniques
    """
    
    # Common indexing errors
    def common_indexing_errors():
        """Demonstrate common indexing errors and their causes."""
        
        test_list = [1, 2, 3, 4, 5]
        test_string = "Python"
        
        error_examples = []
        
        # IndexError scenarios
        index_error_cases = [
            {'operation': 'test_list[5]', 'description': 'Positive index beyond range'},
            {'operation': 'test_list[10]', 'description': 'Far beyond range'},
            {'operation': 'test_list[-6]', 'description': 'Negative index beyond range'},
            {'operation': 'test_string[10]', 'description': 'String index beyond length'},
            {'operation': '[][0]', 'description': 'Index into empty sequence'}
        ]
        
        for case in index_error_cases:
            try:
                if 'test_list[5]' in case['operation']:
                    result = test_list[5]
                elif 'test_list[10]' in case['operation']:
                    result = test_list[10]
                elif 'test_list[-6]' in case['operation']:
                    result = test_list[-6]
                elif 'test_string[10]' in case['operation']:
                    result = test_string[10]
                elif '[][0]' in case['operation']:
                    result = [][0]
                
                error_examples.append({
                    'operation': case['operation'],
                    'description': case['description'],
                    'error_occurred': False,
                    'result': result
                })
            except Exception as e:
                error_examples.append({
                    'operation': case['operation'],
                    'description': case['description'],
                    'error_occurred': True,
                    'error_type': type(e).__name__,
                    'error_message': str(e)
                })
        
        # TypeError scenarios
        type_error_cases = [
            {'operation': 'test_list["invalid"]', 'description': 'String index on list'},
            {'operation': 'test_list[1.5]', 'description': 'Float index'},
            {'operation': 'test_list[None]', 'description': 'None as index'}
        ]
        
        for case in type_error_cases:
            try:
                if '"invalid"' in case['operation']:
                    result = test_list["invalid"]
                elif '1.5' in case['operation']:
                    result = test_list[1.5]
                elif 'None' in case['operation']:
                    result = test_list[None]
                
                error_examples.append({
                    'operation': case['operation'],
                    'description': case['description'],
                    'error_occurred': False,
                    'result': result
                })
            except Exception as e:
                error_examples.append({
                    'operation': case['operation'],
                    'description': case['description'],
                    'error_occurred': True,
                    'error_type': type(e).__name__,
                    'error_message': str(e)
                })
        
        return {
            'test_sequences': {
                'test_list': test_list,
                'test_string': test_string
            },
            'error_examples': error_examples
        }
    
    # Safe indexing techniques
    def safe_indexing_techniques():
        """Demonstrate safe indexing practices."""
        
        def safe_get(sequence, index, default=None):
            """Safely get element with default value."""
            try:
                return sequence[index]
            except (IndexError, TypeError):
                return default
        
        def safe_slice(sequence, start=None, end=None, step=None, default=None):
            """Safely slice sequence with bounds checking."""
            try:
                if sequence:
                    return sequence[start:end:step]
                else:
                    return default if default is not None else []
            except (IndexError, TypeError, ValueError):
                return default if default is not None else []
        
        def bounds_checked_access(sequence, index):
            """Access with explicit bounds checking."""
            if not sequence:
                return {'success': False, 'error': 'Empty sequence'}
            
            if not isinstance(index, int):
                return {'success': False, 'error': 'Index must be integer'}
            
            if -len(sequence) <= index < len(sequence):
                return {'success': True, 'value': sequence[index]}
            else:
                return {
                    'success': False,
                    'error': f'Index {index} out of bounds for length {len(sequence)}'
                }
        
        # Test safe techniques
        test_sequences = [
            [1, 2, 3, 4, 5],
            "Hello",
            [],
            tuple(range(3))
        ]
        
        safe_technique_results = []
        
        for i, sequence in enumerate(test_sequences):
            test_indices = [0, 2, -1, 10, -10, "invalid"]
            
            sequence_results = {
                'sequence': list(sequence) if sequence else [],
                'sequence_type': type(sequence).__name__,
                'tests': {}
            }
            
            for index in test_indices:
                if index == "invalid":
                    sequence_results['tests'][f'index_{index}'] = {
                        'safe_get': safe_get(sequence, index, 'DEFAULT'),
                        'bounds_checked': bounds_checked_access(sequence, index)
                    }
                else:
                    sequence_results['tests'][f'index_{index}'] = {
                        'safe_get': safe_get(sequence, index, 'DEFAULT'),
                        'bounds_checked': bounds_checked_access(sequence, index),
                        'safe_slice': safe_slice(sequence, index, index+2, default=['EMPTY'])
                    }
            
            safe_technique_results.append(sequence_results)
        
        return {
            'safe_indexing_functions': {
                'safe_get': 'Returns default value on error',
                'safe_slice': 'Returns default slice on error',
                'bounds_checked_access': 'Explicit bounds checking with error info'
            },
            'test_results': safe_technique_results
        }
    
    # Input validation strategies
    def input_validation_strategies():
        """Demonstrate input validation for indexing operations."""
        
        def validate_index_input(sequence, index):
            """Comprehensive index validation."""
            validation_result = {
                'valid': True,
                'errors': [],
                'warnings': [],
                'normalized_index': None
            }
            
            # Check sequence
            if not hasattr(sequence, '__getitem__'):
                validation_result['valid'] = False
                validation_result['errors'].append('Object is not indexable')
                return validation_result
            
            if len(sequence) == 0:
                validation_result['valid'] = False
                validation_result['errors'].append('Cannot index empty sequence')
                return validation_result
            
            # Check index type
            if not isinstance(index, int):
                validation_result['valid'] = False
                validation_result['errors'].append(f'Index must be integer, got {type(index).__name__}')
                return validation_result
            
            # Check bounds
            seq_length = len(sequence)
            if index >= seq_length:
                validation_result['valid'] = False
                validation_result['errors'].append(f'Index {index} >= sequence length {seq_length}')
            elif index < -seq_length:
                validation_result['valid'] = False
                validation_result['errors'].append(f'Negative index {index} exceeds sequence length {seq_length}')
            else:
                # Valid index - normalize negative indices
                validation_result['normalized_index'] = index if index >= 0 else seq_length + index
                
                # Add warnings for potentially problematic cases
                if index < 0:
                    validation_result['warnings'].append('Using negative indexing')
                
                if abs(index) > seq_length * 0.8:
                    validation_result['warnings'].append('Index near sequence boundary')
            
            return validation_result
        
        def validate_slice_input(sequence, start, stop, step):
            """Comprehensive slice validation."""
            validation_result = {
                'valid': True,
                'errors': [],
                'warnings': [],
                'normalized_slice': None
            }
            
            # Check sequence
            if not hasattr(sequence, '__getitem__'):
                validation_result['valid'] = False
                validation_result['errors'].append('Object is not sliceable')
                return validation_result
            
            # Check step
            if step is not None:
                if not isinstance(step, int):
                    validation_result['valid'] = False
                    validation_result['errors'].append('Step must be integer or None')
                    return validation_result
                
                if step == 0:
                    validation_result['valid'] = False
                    validation_result['errors'].append('Step cannot be zero')
                    return validation_result
                
                if abs(step) > len(sequence):
                    validation_result['warnings'].append('Step size larger than sequence length')
            
            # Check start and stop
            seq_length = len(sequence)
            
            for param, value in [('start', start), ('stop', stop)]:
                if value is not None:
                    if not isinstance(value, int):
                        validation_result['valid'] = False
                        validation_result['errors'].append(f'{param} must be integer or None')
                        return validation_result
            
            # Create normalized slice object
            try:
                slice_obj = slice(start, stop, step)
                validation_result['normalized_slice'] = slice_obj
                
                # Test slice validity
                test_result = sequence[slice_obj]
                validation_result['slice_length'] = len(test_result)
                
            except Exception as e:
                validation_result['valid'] = False
                validation_result['errors'].append(f'Slice validation failed: {str(e)}')
            
            return validation_result
        
        # Test validation
        test_cases = [
            {'sequence': [1, 2, 3, 4, 5], 'index': 2},
            {'sequence': [1, 2, 3, 4, 5], 'index': -1},
            {'sequence': [1, 2, 3, 4, 5], 'index': 10},
            {'sequence': [], 'index': 0},
            {'sequence': "Hello", 'index': 2},
            {'sequence': [1, 2, 3], 'index': 'invalid'}
        ]
        
        validation_results = []
        for case in test_cases:
            result = validate_index_input(case['sequence'], case['index'])
            validation_results.append({
                'test_case': case,
                'validation_result': result
            })
        
        # Test slice validation
        slice_test_cases = [
            {'sequence': list(range(10)), 'start': 2, 'stop': 7, 'step': 1},
            {'sequence': list(range(10)), 'start': None, 'stop': 5, 'step': 2},
            {'sequence': list(range(10)), 'start': -3, 'stop': None, 'step': -1},
            {'sequence': list(range(10)), 'start': 0, 'stop': 10, 'step': 0},  # Invalid
        ]
        
        slice_validation_results = []
        for case in slice_test_cases:
            result = validate_slice_input(case['sequence'], case['start'], case['stop'], case['step'])
            slice_validation_results.append({
                'test_case': case,
                'validation_result': result
            })
        
        return {
            'index_validation_tests': validation_results,
            'slice_validation_tests': slice_validation_results,
            'validation_best_practices': [
                'Always validate input types before indexing',
                'Check sequence length before accessing',
                'Normalize negative indices for clarity',
                'Provide meaningful error messages',
                'Use try-catch as last resort, not first line of defense'
            ]
        }
    
    # Execute all error handling demonstrations
    common_errors = common_indexing_errors()
    safe_techniques = safe_indexing_techniques()
    validation = input_validation_strategies()
    
    return {
        'common_indexing_errors': common_errors,
        'safe_indexing_techniques': safe_techniques,
# =============================================================================
# 9. PRACTICAL APPLICATIONS & REAL-WORLD USAGE - MASTERY IN ACTION
# =============================================================================

"""
PRACTICAL APPLICATIONS AND REAL-WORLD USAGE:
Master indexing and slicing in real-world programming scenarios
"""

def demonstrate_practical_applications():
    """
    COMPREHENSIVE PRACTICAL APPLICATIONS DEMONSTRATION
    Master real-world indexing and slicing techniques
    """
    
    # Data processing applications
    def data_processing_applications():
        """Demonstrate indexing in data processing scenarios."""
        
        # CSV-like data processing
        def csv_data_processing():
            """Process CSV-like data using indexing."""
            
            # Simulate CSV data (header + rows)
            csv_data = [
                ['Name', 'Age', 'City', 'Salary'],
                ['Alice', '25', 'New York', '50000'],
                ['Bob', '30', 'Los Angeles', '60000'],
                ['Charlie', '35', 'Chicago', '55000'],
                ['Diana', '28', 'Houston', '52000'],
                ['Eve', '32', 'Phoenix', '58000']
            ]
            
            # Extract header
            header = csv_data[0]
            
            # Extract data rows
            data_rows = csv_data[1:]
            
            # Column-based operations using indexing
            def get_column_by_index(data, col_index):
                """Extract column by index."""
                return [row[col_index] for row in data]
            
            def get_column_by_name(data, header, col_name):
                """Extract column by name."""
                try:
                    col_index = header.index(col_name)
                    return get_column_by_index(data, col_index)
                except ValueError:
                    return None
            
            # Extract specific columns
            names = get_column_by_name(data_rows, header, 'Name')
            ages = get_column_by_name(data_rows, header, 'Age')
            salaries = get_column_by_name(data_rows, header, 'Salary')
            
            # Row-based operations
            def get_rows_by_slice(data, start, end=None, step=None):
                """Get rows using slicing."""
                return data[start:end:step]
            
            # Get first 3 employees
            first_three = get_rows_by_slice(data_rows, 0, 3)
            
            # Get every other employee
            every_other = get_rows_by_slice(data_rows, 0, None, 2)
            
            # Get last 2 employees
            last_two = get_rows_by_slice(data_rows, -2, None)
            
            # Data filtering using indexing
            def filter_rows_by_condition(data, header, condition_func):
                """Filter rows based on condition."""
                filtered_rows = []
                for row in data:
                    if condition_func(row, header):
                        filtered_rows.append(row)
                return filtered_rows
            
            # Filter high earners (salary > 55000)
            def high_earner_condition(row, header):
                salary_index = header.index('Salary')
                return int(row[salary_index]) > 55000
            
            high_earners = filter_rows_by_condition(data_rows, header, high_earner_condition)
            
            return {
                'original_data': csv_data,
                'header': header,
                'data_rows': data_rows,
                'column_extractions': {
                    'names': names,
                    'ages': ages,
                    'salaries': salaries
                },
                'row_slicing': {
                    'first_three': first_three,
                    'every_other': every_other,
                    'last_two': last_two
                },
                'filtered_data': {
                    'high_earners': high_earners
                }
            }
        
        # Time series data processing
        def time_series_processing():
            """Process time series data using indexing."""
            
            import datetime
            
            # Generate sample time series data
            base_date = datetime.date(2023, 1, 1)
            dates = [base_date + datetime.timedelta(days=i) for i in range(30)]
            values = [100 + i * 2 + (i % 7) * 5 for i in range(30)]  # Trend with weekly pattern
            
            time_series = list(zip(dates, values))
            
            # Extract different time periods
            def get_date_range(data, start_index, end_index=None):
                """Get data for specific date range by index."""
                return data[start_index:end_index]
            
            # First week (0-6)
            first_week = get_date_range(time_series, 0, 7)
            
            # Last week
            last_week = get_date_range(time_series, -7)
            
            # Every 3rd day
            every_third_day = time_series[::3]
            
            # Middle 50% of data
            quarter_point = len(time_series) // 4
            middle_50_percent = time_series[quarter_point:-quarter_point]
            
            # Moving window analysis using slicing
            def calculate_moving_average(data, window_size):
                """Calculate moving average using slicing."""
                moving_averages = []
                for i in range(len(data) - window_size + 1):
                    window_values = [item[1] for item in data[i:i+window_size]]
                    avg = sum(window_values) / len(window_values)
                    moving_averages.append((data[i+window_size-1][0], avg))
                return moving_averages
            
            # 7-day moving average
            moving_avg_7day = calculate_moving_average(time_series, 7)
            
            return {
                'time_series_data': time_series[:10],  # First 10 for display
                'date_range_extractions': {
                    'first_week': first_week,
                    'last_week': last_week,
                    'every_third_day': every_third_day,
                    'middle_50_percent': middle_50_percent
                },
                'moving_averages': {
                    'window_size': 7,
                    'moving_avg_sample': moving_avg_7day[:5]  # First 5 for display
                }
            }
        
        csv_processing = csv_data_processing()
        time_series = time_series_processing()
        
        return {
            'csv_data_processing': csv_processing,
            'time_series_processing': time_series
        }
    
    # String processing applications
    def string_processing_applications():
        """Demonstrate indexing in string processing scenarios."""
        
        # Text parsing and extraction
        def text_parsing_examples():
            """Parse and extract text using indexing."""
            
            # Sample text data
            email_text = "Contact us at support@company.com or sales@company.com"
            log_entry = "2023-10-15 14:30:22 [ERROR] Database connection failed"
            csv_line = "John,Doe,30,Engineer,New York"
            html_tag = "<a href='https://example.com' class='link'>Click here</a>"
            
            # Email extraction using string indexing
            def extract_emails(text):
                """Extract emails using string searching and slicing."""
                emails = []
                i = 0
                while i < len(text):
                    at_pos = text.find('@', i)
                    if at_pos == -1:
                        break
                    
                    # Find start of email (work backwards)
                    email_start = at_pos
                    while email_start > 0 and text[email_start - 1].isalnum():
                        email_start -= 1
                    
                    # Find end of email (work forwards)
                    email_end = at_pos + 1
                    while email_end < len(text) and (text[email_end].isalnum() or text[email_end] == '.'):
                        email_end += 1
                    
                    # Extract domain extension
                    dot_pos = text.find('.', at_pos)
                    if dot_pos != -1 and dot_pos < email_end + 10:
                        while email_end < len(text) and text[email_end].isalpha():
                            email_end += 1
                    
                    email = text[email_start:email_end]
                    if '.' in email and '@' in email:
                        emails.append(email)
                    
                    i = email_end
                
                return emails
            
            # Log parsing using indexing
            def parse_log_entry(log_line):
                """Parse log entry using string indexing."""
                
                # Extract timestamp (first 19 characters for "YYYY-MM-DD HH:MM:SS")
                timestamp = log_line[:19] if len(log_line) >= 19 else ""
                
                # Find log level (between square brackets)
                level_start = log_line.find('[')
                level_end = log_line.find(']')
                log_level = log_line[level_start+1:level_end] if level_start != -1 and level_end != -1 else ""
                
                # Extract message (everything after level)
                message_start = level_end + 1 if level_end != -1 else 0
                message = log_line[message_start:].strip()
                
                return {
                    'timestamp': timestamp,
                    'level': log_level,
                    'message': message,
                    'original': log_line
                }
            
            # CSV parsing using indexing
            def parse_csv_line(csv_line, delimiter=','):
                """Parse CSV line using string indexing."""
                
                fields = []
                current_field = ""
                in_quotes = False
                i = 0
                
                while i < len(csv_line):
                    char = csv_line[i]
                    
                    if char == '"':
                        in_quotes = not in_quotes
                    elif char == delimiter and not in_quotes:
                        fields.append(current_field.strip())
                        current_field = ""
                    else:
                        current_field += char
                    
                    i += 1
                
                # Add last field
                if current_field:
                    fields.append(current_field.strip())
                
                return fields
            
            # HTML attribute extraction
            def extract_html_attributes(html_tag):
                """Extract HTML attributes using string indexing."""
                
                # Find tag name
                tag_start = html_tag.find('<') + 1
                tag_name_end = html_tag.find(' ', tag_start)
                if tag_name_end == -1:
                    tag_name_end = html_tag.find('>', tag_start)
                
                tag_name = html_tag[tag_start:tag_name_end]
                
                # Extract attributes
                attributes = {}
                attr_section = html_tag[tag_name_end:html_tag.find('>')]
                
                i = 0
                while i < len(attr_section):
                    # Skip whitespace
                    while i < len(attr_section) and attr_section[i].isspace():
                        i += 1
                    
                    if i >= len(attr_section):
                        break
                    
                    # Find attribute name
                    attr_start = i
                    while i < len(attr_section) and attr_section[i] not in '= \t\n':
                        i += 1
                    
                    attr_name = attr_section[attr_start:i]
                    
                    # Skip to value
                    while i < len(attr_section) and attr_section[i] in '= \t\n':
                        i += 1
                    
                    # Extract value
                    if i < len(attr_section):
                        quote_char = attr_section[i] if attr_section[i] in '"\'\'""' else None
                        if quote_char:
                            i += 1  # Skip opening quote
                            value_start = i
                            while i < len(attr_section) and attr_section[i] != quote_char:
                                i += 1
                            attr_value = attr_section[value_start:i]
                            i += 1  # Skip closing quote
                        else:
                            value_start = i
                            while i < len(attr_section) and not attr_section[i].isspace():
                                i += 1
                            attr_value = attr_section[value_start:i]
                        
                        attributes[attr_name] = attr_value
                
                return {
                    'tag_name': tag_name,
                    'attributes': attributes
                }
            
            # Process all examples
            extracted_emails = extract_emails(email_text)
            parsed_log = parse_log_entry(log_entry)
            csv_fields = parse_csv_line(csv_line)
            html_attrs = extract_html_attributes(html_tag)
            
            return {
                'email_extraction': {
                    'original_text': email_text,
                    'extracted_emails': extracted_emails
                },
                'log_parsing': {
                    'original_log': log_entry,
                    'parsed_components': parsed_log
                },
                'csv_parsing': {
                    'original_line': csv_line,
                    'parsed_fields': csv_fields
                },
                'html_parsing': {
                    'original_html': html_tag,
                    'parsed_attributes': html_attrs
                }
            }
        
        # String manipulation patterns
        def string_manipulation_patterns():
            """Demonstrate string manipulation using indexing."""
            
            sample_text = "The Quick Brown Fox Jumps Over The Lazy Dog"
            
            # Case transformation patterns
            def title_case_custom(text):
                """Custom title case using indexing."""
                if not text:
                    return text
                
                result = text.lower()
                result = result[0].upper() + result[1:] if len(result) > 1 else result.upper()
                
                # Capitalize after spaces
                for i in range(1, len(result)):
                    if result[i-1] == ' ':
                        result = result[:i] + result[i].upper() + result[i+1:]
                
                return result
            
            # Word extraction and manipulation
            def extract_words_with_positions(text):
                """Extract words with their positions."""
                words_info = []
                word_start = 0
                i = 0
                
                while i <= len(text):
                    if i == len(text) or text[i].isspace():
                        if word_start < i:
                            word = text[word_start:i]
                            words_info.append({
                                'word': word,
                                'start_pos': word_start,
                                'end_pos': i,
                                'length': len(word)
                            })
                        
                        # Skip spaces
                        while i < len(text) and text[i].isspace():
                            i += 1
                        word_start = i
                    else:
                        i += 1
                
                return words_info
            
            # Character frequency using indexing
            def analyze_character_frequency(text):
                """Analyze character frequency using indexing."""
                char_count = {}
                
                for i in range(len(text)):
                    char = text[i].lower()
                    if char.isalpha():
                        char_count[char] = char_count.get(char, 0) + 1
                
                # Sort by frequency
                sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
                
                return {
                    'character_counts': char_count,
                    'sorted_by_frequency': sorted_chars,
                    'most_common': sorted_chars[0] if sorted_chars else None,
                    'total_letters': sum(char_count.values())
                }
            
            # String reversal patterns
            def reverse_words_preserve_spaces(text):
                """Reverse words while preserving space positions."""
                chars = list(text)
                
                # Reverse non-space characters
                non_space_chars = [char for char in chars if char != ' ']
                non_space_chars.reverse()
                
                # Place reversed chars back, preserving spaces
                non_space_index = 0
                for i in range(len(chars)):
                    if chars[i] != ' ':
                        chars[i] = non_space_chars[non_space_index]
                        non_space_index += 1
                
                return ''.join(chars)
            
            # Process sample text
            title_cased = title_case_custom(sample_text)
            words_info = extract_words_with_positions(sample_text)
            char_analysis = analyze_character_frequency(sample_text)
            reversed_words = reverse_words_preserve_spaces(sample_text)
            
            return {
                'original_text': sample_text,
                'title_case_custom': title_cased,
                'words_with_positions': words_info,
                'character_analysis': char_analysis,
                'reversed_words_preserve_spaces': reversed_words
            }
        
        text_parsing = text_parsing_examples()
        string_manipulation = string_manipulation_patterns()
        
        return {
            'text_parsing_examples': text_parsing,
            'string_manipulation_patterns': string_manipulation
        }
    
    # Algorithm implementations
    def algorithm_implementations():
        """Demonstrate indexing in algorithm implementations."""
        
        # Searching algorithms
        def searching_algorithms():
            """Implement searching algorithms using indexing."""
            
            def linear_search(arr, target):
                """Linear search with detailed indexing information."""
                search_info = {
                    'target': target,
                    'comparisons': 0,
                    'indices_checked': [],
                    'found': False,
                    'position': -1
                }
                
                for i in range(len(arr)):
                    search_info['comparisons'] += 1
                    search_info['indices_checked'].append(i)
                    
                    if arr[i] == target:
                        search_info['found'] = True
                        search_info['position'] = i
                        break
                
                return search_info
            
            def binary_search(arr, target):
                """Binary search with detailed indexing information."""
                search_info = {
                    'target': target,
                    'comparisons': 0,
                    'search_path': [],
                    'found': False,
                    'position': -1
                }
                
                left, right = 0, len(arr) - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    search_info['comparisons'] += 1
                    search_info['search_path'].append({
                        'left': left,
                        'right': right,
                        'mid': mid,
                        'mid_value': arr[mid],
                        'comparison': 'equal' if arr[mid] == target else 
                                      'less' if arr[mid] < target else 'greater'
                    })
                    
                    if arr[mid] == target:
                        search_info['found'] = True
                        search_info['position'] = mid
                        break
                    elif arr[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                return search_info
            
            # Test data
            test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
            search_targets = [7, 12, 1, 19]
            
            search_results = {}
            for target in search_targets:
                search_results[f'target_{target}'] = {
                    'linear_search': linear_search(test_array, target),
                    'binary_search': binary_search(test_array, target)
                }
            
            return {
                'test_array': test_array,
                'search_results': search_results
            }
        
        # Sorting with indexing
        def sorting_algorithms():
            """Implement sorting algorithms using detailed indexing."""
            
            def bubble_sort_with_tracking(arr):
                """Bubble sort with detailed swap tracking."""
                arr_copy = arr.copy()
                sort_info = {
                    'original_array': arr,
                    'passes': [],
                    'total_swaps': 0,
                    'total_comparisons': 0
                }
                
                n = len(arr_copy)
                for i in range(n):
                    pass_info = {
                        'pass_number': i + 1,
                        'swaps_this_pass': 0,
                        'comparisons_this_pass': 0,
                        'array_state': arr_copy.copy()
                    }
                    
                    for j in range(0, n - i - 1):
                        pass_info['comparisons_this_pass'] += 1
                        sort_info['total_comparisons'] += 1
                        
                        if arr_copy[j] > arr_copy[j + 1]:
                            # Swap elements
                            arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                            pass_info['swaps_this_pass'] += 1
                            sort_info['total_swaps'] += 1
                    
                    pass_info['array_after_pass'] = arr_copy.copy()
                    sort_info['passes'].append(pass_info)
                    
                    # Early termination if no swaps
                    if pass_info['swaps_this_pass'] == 0:
                        break
                
                sort_info['final_array'] = arr_copy
                return sort_info
            
            def selection_sort_with_tracking(arr):
                """Selection sort with detailed selection tracking."""
                arr_copy = arr.copy()
                sort_info = {
                    'original_array': arr,
                    'selections': [],
                    'total_swaps': 0,
                    'total_comparisons': 0
                }
                
                n = len(arr_copy)
                for i in range(n):
                    selection_info = {
                        'selection_round': i + 1,
                        'searching_range': f'[{i}:{n}]',
                        'min_index': i,
                        'min_value': arr_copy[i],
                        'comparisons_this_round': 0
                    }
                    
                    # Find minimum in remaining array
                    min_idx = i
                    for j in range(i + 1, n):
                        selection_info['comparisons_this_round'] += 1
                        sort_info['total_comparisons'] += 1
                        
                        if arr_copy[j] < arr_copy[min_idx]:
                            min_idx = j
                    
                    selection_info['final_min_index'] = min_idx
                    selection_info['final_min_value'] = arr_copy[min_idx]
                    
                    # Swap if necessary
                    if min_idx != i:
                        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
                        sort_info['total_swaps'] += 1
                        selection_info['swap_performed'] = True
                    else:
                        selection_info['swap_performed'] = False
                    
                    selection_info['array_after_selection'] = arr_copy.copy()
                    sort_info['selections'].append(selection_info)
                
                sort_info['final_array'] = arr_copy
                return sort_info
            
            # Test with sample data
            test_array = [64, 34, 25, 12, 22, 11, 90]
            
            bubble_result = bubble_sort_with_tracking(test_array)
            selection_result = selection_sort_with_tracking(test_array)
            
            return {
                'test_array': test_array,
                'bubble_sort_tracking': bubble_result,
                'selection_sort_tracking': selection_result
            }
        
        searching = searching_algorithms()
        sorting = sorting_algorithms()
        
        return {
            'searching_algorithms': searching,
            'sorting_algorithms': sorting
        }
    
    # Execute all practical applications
    data_processing = data_processing_applications()
    string_processing = string_processing_applications()
    algorithms = algorithm_implementations()
    
    return {
        'data_processing_applications': data_processing,
        'string_processing_applications': string_processing,
        'algorithm_implementations': algorithms
    }

# =============================================================================
# 10. ADVANCED PATTERNS & MASTERY TECHNIQUES - EXPERT LEVEL
# =============================================================================

"""
ADVANCED PATTERNS AND MASTERY TECHNIQUES:
Master expert-level indexing patterns and advanced techniques
"""

def demonstrate_mastery_techniques():
    """
    COMPREHENSIVE MASTERY TECHNIQUES DEMONSTRATION
    Expert-level indexing patterns and advanced applications
    """
    
    # Advanced slicing patterns
    def advanced_slicing_patterns():
        """Master advanced slicing techniques."""
        
        # Complex stride patterns
        def complex_stride_patterns():
            """Demonstrate complex stride and step patterns."""
            
            data = list(range(20))
            
            # Fibonacci-like stride pattern
            def fibonacci_stride_access(sequence, max_terms=10):
                """Access elements using Fibonacci-like strides."""
                fib_a, fib_b = 1, 1
                accessed_elements = []
                
                index = 0
                while index < len(sequence) and len(accessed_elements) < max_terms:
                    accessed_elements.append({
                        'index': index,
                        'value': sequence[index],
                        'stride': fib_a
                    })
                    
                    index += fib_a
                    fib_a, fib_b = fib_b, fib_a + fib_b
                
                return accessed_elements
            
            # Prime number indexing
            def prime_number_indexing(sequence):
                """Access elements at prime number indices."""
                def is_prime(n):
                    if n < 2:
                        return False
                    for i in range(2, int(n**0.5) + 1):
                        if n % i == 0:
                            return False
                    return True
                
                prime_elements = []
                for i in range(len(sequence)):
                    if is_prime(i):
                        prime_elements.append({
                            'prime_index': i,
                            'value': sequence[i]
                        })
                
                return prime_elements
            
            # Spiral access pattern (for 2D-like access on 1D array)
            def spiral_access_pattern(sequence, width):
                """Access 1D sequence in spiral pattern as if 2D."""
                if len(sequence) != width * width:
                    # Pad or truncate to make square
                    target_size = width * width
                    if len(sequence) < target_size:
                        padded_sequence = sequence + [0] * (target_size - len(sequence))
                    else:
                        padded_sequence = sequence[:target_size]
                else:
                    padded_sequence = sequence
                
                # Create 2D representation
                matrix = []
                for i in range(width):
                    row = padded_sequence[i*width:(i+1)*width]
                    matrix.append(row)
                
                # Spiral access
                spiral_elements = []
                top, bottom = 0, width - 1
                left, right = 0, width - 1
                
                while top <= bottom and left <= right:
                    # Top row
                    for col in range(left, right + 1):
                        spiral_elements.append({
                            '2d_position': (top, col),
                            '1d_index': top * width + col,
                            'value': matrix[top][col]
                        })
                    top += 1
                    
                    # Right column
                    for row in range(top, bottom + 1):
                        spiral_elements.append({
                            '2d_position': (row, right),
                            '1d_index': row * width + right,
                            'value': matrix[row][right]
                        })
                    right -= 1
                    
                    # Bottom row (if exists)
                    if top <= bottom:
                        for col in range(right, left - 1, -1):
                            spiral_elements.append({
                                '2d_position': (bottom, col),
                                '1d_index': bottom * width + col,
                                'value': matrix[bottom][col]
                            })
                        bottom -= 1
                    
                    # Left column (if exists)
                    if left <= right:
                        for row in range(bottom, top - 1, -1):
                            spiral_elements.append({
                                '2d_position': (row, left),
                                '1d_index': row * width + left,
                                'value': matrix[row][left]
                            })
                        left += 1
                
                return {
                    'matrix_representation': matrix,
                    'spiral_access_order': spiral_elements
                }
            
            # Test complex patterns
            fibonacci_access = fibonacci_stride_access(data)
            prime_access = prime_number_indexing(data)
            spiral_access = spiral_access_pattern(data, 4)  # 4x4 spiral
            
            return {
                'test_data': data,
                'fibonacci_stride_access': fibonacci_access,
                'prime_number_indexing': prime_access,
                'spiral_access_pattern': spiral_access
            }
        
        # Conditional slicing
        def conditional_slicing():
            """Advanced conditional slicing techniques."""
            
            data = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12]
            
            # Dynamic slice bounds based on content
            def find_slice_by_condition(sequence, start_condition, end_condition):
                """Find slice bounds based on conditions."""
                start_index = None
                end_index = None
                
                # Find start
                for i, value in enumerate(sequence):
                    if start_condition(value, i):
                        start_index = i
                        break
                
                # Find end (search from start)
                if start_index is not None:
                    for i in range(start_index + 1, len(sequence)):
                        if end_condition(sequence[i], i):
                            end_index = i + 1  # Exclusive end
                            break
                    
                    if end_index is None:
                        end_index = len(sequence)
                
                return {
                    'start_index': start_index,
                    'end_index': end_index,
                    'slice_result': sequence[start_index:end_index] if start_index is not None else []
                }
            
            # Find slice from first positive to first negative after it
            pos_to_neg = find_slice_by_condition(
                data,
                lambda val, idx: val > 0,  # Start: first positive
                lambda val, idx: val < 0   # End: first negative after start
            )
            
            # Find slice from largest value to next largest
            def find_top_values_slice(sequence, n=2):
                """Find slice between top N values."""
                indexed_values = [(val, idx) for idx, val in enumerate(sequence)]
                sorted_values = sorted(indexed_values, key=lambda x: x[0], reverse=True)
                
                top_indices = [item[1] for item in sorted_values[:n]]
                top_indices.sort()
                
                if len(top_indices) >= 2:
                    return {
                        'top_values': [sequence[i] for i in top_indices],
                        'top_indices': top_indices,
                        'slice_between': sequence[top_indices[0]:top_indices[-1]+1]
                    }
                
                return {'error': 'Not enough values to create slice'}
            
            top_values_slice = find_top_values_slice(data)
            
            # Alternating pattern slicing
            def alternating_pattern_slice(sequence, pattern_func):
                """Create slice based on alternating pattern."""
                selected_indices = []
                
                for i, value in enumerate(sequence):
                    if pattern_func(value, i):
                        selected_indices.append(i)
                
                # Group consecutive indices
                groups = []
                current_group = []
                
                for i in selected_indices:
                    if not current_group or i == current_group[-1] + 1:
                        current_group.append(i)
                    else:
                        groups.append(current_group)
                        current_group = [i]
                
                if current_group:
                    groups.append(current_group)
                
                return {
                    'selected_indices': selected_indices,
                    'consecutive_groups': groups,
                    'group_slices': [sequence[group[0]:group[-1]+1] for group in groups]
                }
            
            # Even values pattern
            even_pattern = alternating_pattern_slice(data, lambda val, idx: val % 2 == 0)
            
            return {
                'test_data': data,
                'positive_to_negative_slice': pos_to_neg,
                'top_values_slice': top_values_slice,
                'even_pattern_slice': even_pattern
            }
        
        complex_strides = complex_stride_patterns()
        conditional = conditional_slicing()
        
        return {
            'complex_stride_patterns': complex_strides,
            'conditional_slicing': conditional
        }
    
    # Memory-efficient techniques
    def memory_efficient_techniques():
        """Master memory-efficient indexing techniques."""
        
        # Generator-based indexing
        def generator_based_indexing():
            """Use generators for memory-efficient indexing."""
            
            def indexed_generator(sequence, indices):
                """Generate values at specific indices."""
                for index in indices:
                    if 0 <= index < len(sequence):
                        yield (index, sequence[index])
            
            def slice_generator(sequence, start=None, stop=None, step=None):
                """Generate slice elements without creating intermediate list."""
                slice_obj = slice(start, stop, step)
                indices = range(*slice_obj.indices(len(sequence)))
                
                for i in indices:
                    yield (i, sequence[i])
            
            def windowed_generator(sequence, window_size, step=1):
                """Generate sliding windows efficiently."""
                for start in range(0, len(sequence) - window_size + 1, step):
                    window_indices = range(start, start + window_size)
                    window_data = [sequence[i] for i in window_indices]
                    yield (start, window_data)
            
            # Test generators
            test_data = list(range(100))
            
            # Sample a few results from generators
            indexed_results = list(indexed_generator(test_data, [5, 10, 15, 20]))
            slice_results = list(slice_generator(test_data, 10, 20, 2))
            windowed_results = list(windowed_generator(test_data, 5, 3))[:10]  # First 10 windows
            
            return {
                'indexed_generator_sample': indexed_results,
                'slice_generator_sample': slice_results,
                'windowed_generator_sample': windowed_results
            }
        
        # Lazy evaluation techniques
        def lazy_evaluation_techniques():
            """Implement lazy evaluation for indexing."""
            
            class LazyIndexedSequence:
                """Lazy sequence that computes values on demand."""
                
                def __init__(self, compute_func, length):
                    self.compute_func = compute_func
                    self._length = length
                    self._cache = {}
                
                def __len__(self):
                    return self._length
                
                def __getitem__(self, key):
                    if isinstance(key, slice):
                        indices = range(*key.indices(len(self)))
                        return [self[i] for i in indices]
                    
                    if key not in self._cache:
                        self._cache[key] = self.compute_func(key)
                    
                    return self._cache[key]
                
                def cache_info(self):
                    return {
                        'cache_size': len(self._cache),
                        'cached_indices': list(self._cache.keys()),
                        'total_length': self._length
                    }
            
            # Example: Fibonacci sequence with lazy evaluation
            def fibonacci_computer(n):
                """Compute nth Fibonacci number."""
                if n <= 1:
                    return n
                
                a, b = 0, 1
                for _ in range(2, n + 1):
                    a, b = b, a + b
                
                return b
            
            # Create lazy Fibonacci sequence
            lazy_fib = LazyIndexedSequence(fibonacci_computer, 50)
            
            # Access some values
            fib_sample = [lazy_fib[i] for i in [5, 10, 15, 7, 12]]  # Note: 7 and 12 will use cache
            cache_info_after_access = lazy_fib.cache_info()
            
            # Slice access
            fib_slice = lazy_fib[20:25]
            cache_info_after_slice = lazy_fib.cache_info()
            
            return {
                'fibonacci_sample_access': {
                    'accessed_indices': [5, 10, 15, 7, 12],
                    'computed_values': fib_sample
                },
                'cache_info_after_individual_access': cache_info_after_access,
                'fibonacci_slice_access': {
                    'slice_range': '20:25',
                    'slice_values': fib_slice
                },
                'cache_info_after_slice_access': cache_info_after_slice
            }
        
        generator_techniques = generator_based_indexing()
        lazy_evaluation = lazy_evaluation_techniques()
        
        return {
            'generator_based_indexing': generator_techniques,
            'lazy_evaluation_techniques': lazy_evaluation
        }
    
    # Parallel and concurrent indexing
    def parallel_indexing_techniques():
        """Explore parallel indexing techniques."""
        
        # Concurrent access patterns
        def concurrent_access_patterns():
            """Demonstrate thread-safe indexing patterns."""
            
            import threading
            import time
            
            # Thread-safe indexed access
            class ThreadSafeIndexedContainer:
                """Thread-safe container with indexed access."""
                
                def __init__(self, data):
                    self._data = data.copy()
                    self._lock = threading.RLock()
                    self._access_log = []
                
                def __getitem__(self, key):
                    with self._lock:
                        access_info = {
                            'thread_id': threading.get_ident(),
                            'access_time': time.time(),
                            'key': key,
                            'key_type': type(key).__name__
                        }
                        
                        result = self._data[key]
                        access_info['result'] = result
                        self._access_log.append(access_info)
                        
                        return result
                
                def __setitem__(self, key, value):
                    with self._lock:
                        self._data[key] = value
                        self._access_log.append({
                            'thread_id': threading.get_ident(),
                            'access_time': time.time(),
                            'operation': 'set',
                            'key': key,
                            'value': value
                        })
                
                def get_access_log(self):
                    with self._lock:
                        return self._access_log.copy()
                
                def __len__(self):
                    return len(self._data)
            
            # Simulate concurrent access
            container = ThreadSafeIndexedContainer(list(range(20)))
            
            def worker_function(container, worker_id, access_pattern):
                """Worker function for concurrent access."""
                for index in access_pattern:
                    value = container[index]
                    time.sleep(0.001)  # Small delay to simulate work
                    if worker_id % 2 == 0:  # Even workers modify data
                        container[index] = value * 10
            
            # Define access patterns for different workers
            access_patterns = {
                0: [0, 2, 4, 6, 8],      # Even indices
                1: [1, 3, 5, 7, 9],      # Odd indices
                2: [10, 12, 14, 16, 18], # High even indices
                3: [11, 13, 15, 17, 19]  # High odd indices
            }
            
            # Create and start threads
            threads = []
            for worker_id, pattern in access_patterns.items():
                thread = threading.Thread(
                    target=worker_function,
                    args=(container, worker_id, pattern)
                )
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            # Analyze access log
            access_log = container.get_access_log()
            
            return {
                'final_container_state': list(container._data),
                'access_log_summary': {
                    'total_accesses': len(access_log),
                    'unique_threads': len(set(log['thread_id'] for log in access_log)),
                    'access_log_sample': access_log[:10]  # First 10 for brevity
                }
            }
        
        # Batch processing techniques
        def batch_processing_techniques():
            """Advanced batch processing using indexing."""
            
            def process_in_batches(sequence, batch_size, processing_func):
                """Process sequence in batches using slicing."""
                results = []
                batch_info = []
                
                for start_idx in range(0, len(sequence), batch_size):
                    end_idx = min(start_idx + batch_size, len(sequence))
                    batch = sequence[start_idx:end_idx]
                    
                    batch_result = processing_func(batch)
                    
                    batch_info.append({
                        'batch_number': len(batch_info) + 1,
                        'start_index': start_idx,
                        'end_index': end_idx,
                        'batch_size': len(batch),
                        'processing_result': batch_result
                    })
                    
                    results.extend(batch_result if isinstance(batch_result, list) else [batch_result])
                
                return {
                    'processed_results': results,
                    'batch_processing_info': batch_info
                }
            
            # Example processing functions
            def square_batch(batch):
                """Square all values in batch."""
                return [x ** 2 for x in batch]
            
            def sum_batch(batch):
                """Sum all values in batch."""
                return sum(batch)
            
            def analyze_batch(batch):
                """Analyze batch statistics."""
                return {
                    'count': len(batch),
                    'sum': sum(batch),
                    'avg': sum(batch) / len(batch) if batch else 0,
                    'min': min(batch) if batch else None,
                    'max': max(batch) if batch else None
                }
            
            # Test data
            test_data = list(range(1, 51))  # 1 to 50
            
            # Process with different batch sizes and functions
            squared_batches = process_in_batches(test_data, 10, square_batch)
            summed_batches = process_in_batches(test_data, 8, sum_batch)
            analyzed_batches = process_in_batches(test_data, 12, analyze_batch)
            
            return {
                'test_data_size': len(test_data),
                'squared_processing': {
                    'batch_size': 10,
                    'result_sample': squared_batches['processed_results'][:20],
                    'batch_info_sample': squared_batches['batch_processing_info'][:2]
                },
                'summed_processing': {
                    'batch_size': 8,
                    'results': summed_batches['processed_results'],
                    'batch_info': summed_batches['batch_processing_info']
                },
                'analyzed_processing': {
                    'batch_size': 12,
                    'analysis_results': analyzed_batches['processed_results'][:3],
                    'batch_info': analyzed_batches['batch_processing_info'][:3]
                }
            }
        
        concurrent_access = concurrent_access_patterns()
        batch_processing = batch_processing_techniques()
        
        return {
            'concurrent_access_patterns': concurrent_access,
            'batch_processing_techniques': batch_processing
        }
    
    # Execute all mastery techniques
    advanced_slicing = advanced_slicing_patterns()
    memory_efficient = memory_efficient_techniques()
    parallel_indexing = parallel_indexing_techniques()
    
    return {
        'advanced_slicing_patterns': advanced_slicing,
        'memory_efficient_techniques': memory_efficient,
# =============================================================================
# DEMONSTRATION AND TESTING EXECUTION
# =============================================================================

"""
COMPREHENSIVE DEMONSTRATION EXECUTION:
Execute all indexing and slicing demonstrations
"""

if __name__ == "__main__":
    print("=" * 80)
    print("PYTHON INDEXING & SLICING - COMPLETE MASTERY GUIDE")
    print("=" * 80)
    
    # Execute all major sections
    try:
        print("\n" + "=" * 60)
        print("1. INDEXING FUNDAMENTALS & CONCEPTS")
        print("=" * 60)
        fundamentals = demonstrate_indexing_fundamentals()
        print("✓ Indexing concepts and compatibility demonstrated")
        print(f"  - Sequence types tested: {len(fundamentals['concept_overview']['sequence_compatibility']['compatibility_results'])}")
        print(f"  - Bounds validation scenarios: {len(fundamentals['bounds_validation']['bounds_test_results'])}")
        
        print("\n" + "=" * 60)
        print("2. POSITIVE & NEGATIVE INDEXING")
        print("=" * 60)
        positive_negative = demonstrate_positive_negative_indexing()
        print("✓ Positive and negative indexing patterns demonstrated")
        print(f"  - Index conversion examples: {len(positive_negative['negative_indexing']['conversion_calculations'])}")
        print(f"  - Equivalence mappings verified: {len(positive_negative['negative_indexing']['equivalence_mapping']['test_sequence'])}")
        
        print("\n" + "=" * 60)
        print("3. SLICING SYNTAX & OPERATIONS")
        print("=" * 60)
        slicing_syntax = demonstrate_slicing_syntax()
        print("✓ Comprehensive slicing syntax demonstrated")
        print(f"  - Basic slicing patterns: {len(slicing_syntax['basic_slicing_patterns']['slicing_examples'])}")
        print(f"  - Step slicing examples: {len(slicing_syntax['step_slicing_patterns']['step_examples'])}")
        
        print("\n" + "=" * 60)
        print("4. ADVANCED SLICING PATTERNS")
        print("=" * 60)
        advanced_slicing = demonstrate_advanced_slicing()
        print("✓ Advanced slicing techniques demonstrated")
        print(f"  - Multi-dimensional simulation examples: Available")
        print(f"  - Pattern-based slicing techniques: Available")
        print(f"  - Dynamic slicing conditions: Available")
        
        print("\n" + "=" * 60)
        print("5. SEQUENCE MODIFICATION & MANIPULATION")
        print("=" * 60)
        sequence_modification = demonstrate_sequence_modification()
        print("✓ Sequence modification patterns demonstrated")
        print(f"  - Single element modification examples: Available")
        print(f"  - Slice-based modification patterns: Available")
        print(f"  - Advanced manipulation techniques: Available")
        
        print("\n" + "=" * 60)
        print("6. MULTI-DIMENSIONAL INDEXING")
        print("=" * 60)
        multidimensional = demonstrate_multidimensional_indexing()
        print("✓ Multi-dimensional indexing demonstrated")
        print(f"  - Nested list examples: Available")
        print(f"  - Complex structure handling: Available")
        print(f"  - Flattened indexing techniques: Available")
        
        print("\n" + "=" * 60)
        print("7. INDEXING PERFORMANCE & OPTIMIZATION")
        print("=" * 60)
        performance = demonstrate_indexing_performance()
        print("✓ Performance analysis and optimization demonstrated")
        print(f"  - Basic indexing performance: Available")
        print(f"  - Slicing performance analysis: Available")
        print(f"  - Memory efficiency analysis: Available")
        print(f"  - Optimization techniques: Available")
        
        print("\n" + "=" * 60)
        print("8. ERROR HANDLING & BOUNDS CHECKING")
        print("=" * 60)
        error_handling = demonstrate_error_handling()
        print("✓ Error handling and safety techniques demonstrated")
        print(f"  - Common error scenarios: {len(error_handling['common_indexing_errors']['error_examples'])}")
        print(f"  - Safe indexing techniques: Available")
        print(f"  - Input validation strategies: Available")
        
        print("\n" + "=" * 60)
        print("9. PRACTICAL APPLICATIONS & REAL-WORLD USAGE")
        print("=" * 60)
        practical = demonstrate_practical_applications()
        print("✓ Practical applications demonstrated")
        print(f"  - Data processing applications: Available")
        print(f"  - String processing applications: Available")
        print(f"  - Algorithm implementations: Available")
        
        print("\n" + "=" * 60)
        print("10. ADVANCED PATTERNS & MASTERY TECHNIQUES")
        print("=" * 60)
        mastery = demonstrate_mastery_techniques()
        print("✓ Expert-level mastery techniques demonstrated")
        print(f"  - Advanced slicing patterns: Available")
        print(f"  - Memory-efficient techniques: Available")
        print(f"  - Parallel indexing techniques: Available")
        
        print("\n" + "=" * 80)
        print("COMPREHENSIVE MASTERY SUMMARY")
        print("=" * 80)
        print("✓ All 10 sections successfully demonstrated")
        print("✓ Complete indexing and slicing mastery achieved")
        print("✓ Expert-level techniques and patterns covered")
        print("✓ Real-world applications and optimizations included")
        print("✓ Error handling and safety practices mastered")
        print("✓ Performance analysis and memory efficiency addressed")
        print("\nThis comprehensive guide covers every aspect of Python")
        print("indexing and slicing from basic concepts to expert-level")
        print("mastery techniques, providing practical examples and")
        print("real-world applications for professional development.")
        
    except Exception as e:
        print(f"\nError during demonstration: {str(e)}")
        print("Some advanced features may require specific Python versions or additional modules.")
    
    print("\n" + "=" * 80)
    print("END OF PYTHON INDEXING & SLICING MASTERY GUIDE")
    print("=" * 80)

p1[-2:-1] # Slice from index -2 to index -1 (excluding index -1)
# [2]

""" Slice out of range can be handled without error. """
#   The slice will be empty if the start index is greater than the sequence length.

p1[42:]  # Slice from index 42 to the end of the list
# []             # Empty list

p1[:42]  # Slice from index 0 to index 42 (excluding index 42)
# [1, 2, 3]       # The entire list, since 42 is beyond the list length

# ----------

"""Modify List Items"""
#   Lists are mutable, meaning you can change the value of an item in a list.
#       You can change the value of an item in a list by
#           assigning a new value to the index of the item.

""" Change the value of an item in a List """
#  You can change the value of an item in a list by assigning a new value to the index of the item.

p10 = [10, 22, 30]

p10[1] = 20
print(p10)
# [10, 20, 30]

""" Add an item to a List """
# You can add an item to a list by using the append() method.

p10 = [10, 20, 30]

p10.append(40)
print(p10)
# [10, 20, 30, 40]

""" Remove an item from a List """
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