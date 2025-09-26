"""
=============================================================================
PYTHON TEXT PROCESSING & STRING MANIPULATION - COMPLETE MASTERY GUIDE
=============================================================================

COMPREHENSIVE GUIDE TO PYTHON STRING OPERATIONS AND TEXT PROCESSING

This comprehensive guide covers every aspect of Python text processing from basic
string operations to advanced text manipulation techniques, real-world applications,
and professional text processing patterns.

Topics Covered:
1. String Fundamentals & Creation - Core string concepts and creation methods
2. String Properties & Characteristics - Immutability, encoding, and string behavior  
3. String Indexing & Slicing Mastery - Advanced indexing and slicing techniques
4. String Methods & Operations - Complete method reference with examples
5. String Formatting & Interpolation - Modern formatting techniques and best practices
6. Text Searching & Pattern Matching - Search algorithms and pattern recognition
7. String Manipulation & Transformation - Advanced modification and conversion techniques
8. Regular Expressions & Advanced Patterns - Regex mastery for complex text processing
9. Real-World Text Processing Applications - Practical text processing scenarios
10. Performance Optimization & Best Practices - Efficient text processing techniques

Educational Approach:
- Comprehensive examples with detailed explanations
- Real-world applications and practical use cases
- Performance considerations and optimization techniques
- Professional coding patterns and best practices
- Error handling and edge case management
- Cross-platform compatibility considerations

Target Audience: Beginner to Expert Level
Learning Objectives: Complete mastery of Python text processing capabilities
"""

# =============================================================================
# 1. STRING FUNDAMENTALS & CREATION - CORE CONCEPTS MASTERY
# =============================================================================

"""
STRING FUNDAMENTALS AND CREATION METHODS:
Master all aspects of string creation and fundamental concepts
"""

def demonstrate_string_fundamentals():
    """
    COMPREHENSIVE STRING FUNDAMENTALS DEMONSTRATION
    Master string creation methods and fundamental concepts
    """
    
    # Basic string creation methods
    def basic_string_creation():
        """Demonstrate all string creation methods."""
        
        creation_methods = {
            'single_quotes': 'Hello World',
            'double_quotes': "Hello World",
            'triple_single_quotes': '''Hello World''',
            'triple_double_quotes': """Hello World""",
            'raw_strings': r'Hello\nWorld',  # Backslashes treated literally
            'byte_strings': b'Hello World',  # Bytes object, not string
            'unicode_strings': u'Hello World',  # Unicode (default in Python 3)
            'formatted_strings': f'Hello {"World"}',  # f-strings
            'constructor_method': str('Hello World'),  # Using str() constructor
            'constructor_from_number': str(42),
            'constructor_from_list': str([1, 2, 3]),
            'empty_string': '',
            'single_character': 'A',
            'multiline_string': """Line 1
Line 2
Line 3"""
        }
        
        # Analyze each creation method
        creation_analysis = {}
        for method, string_value in creation_methods.items():
            creation_analysis[method] = {
                'value': string_value,
                'type': type(string_value).__name__,
                'length': len(string_value) if hasattr(string_value, '__len__') else 'N/A',
                'is_string': isinstance(string_value, str),
                'repr': repr(string_value)
            }
        
        return {
            'creation_methods': creation_methods,
            'creation_analysis': creation_analysis
        }
    
    # String literal types and behaviors
    def string_literal_types():
        """Explore different string literal types and their behaviors."""
        
        # Quote handling examples
        quote_examples = {
            'single_in_double': "It's a beautiful day",
            'double_in_single': 'He said "Hello"',
            'mixed_quotes': """She said "It's wonderful!" """,
            'escaped_single': 'It\'s a beautiful day',
            'escaped_double': "He said \"Hello\"",
            'multiple_escapes': "Quote: \"It's a 'test'\" example"
        }
        
        # Raw string comparisons
        raw_string_comparisons = {
            'regular_string': 'C:\new\folder\test.txt',
            'raw_string': r'C:\new\folder\test.txt',
            'regular_with_escapes': 'C:\\new\\folder\\test.txt',
            'newline_regular': 'Line 1\nLine 2',
            'newline_raw': r'Line 1\nLine 2'
        }
        
        # Multi-line string variations
        multiline_variations = {
            'triple_quotes_basic': """First line
Second line
Third line""",
            'triple_quotes_indented': """
            First line
            Second line
            Third line
            """,
            'triple_quotes_no_initial_newline': """\
First line
Second line
Third line""",
            'concatenated_lines': (
                "First line "
                "Second line "
                "Third line"
            ),
            'explicit_newlines': "First line\nSecond line\nThird line"
        }
        
        return {
            'quote_handling_examples': quote_examples,
            'raw_string_comparisons': raw_string_comparisons,
            'multiline_variations': multiline_variations
        }
    
    # String encoding and Unicode
    def string_encoding_unicode():
        """Demonstrate string encoding and Unicode handling."""
        
        # Unicode examples
        unicode_examples = {
            'basic_ascii': 'Hello World',
            'accented_characters': 'café, naïve, résumé',
            'special_symbols': '© ® ™ § ¶ † ‡',
            'mathematical_symbols': 'π ≈ ∞ ∑ ∆ √ ∫',
            'arrows_and_shapes': '→ ← ↑ ↓ ◆ ◇ ● ○',
            'emoji_characters': '🐍 🚀 💻 📊 ✨',
            'foreign_languages': {
                'spanish': '¡Hola mundo!',
                'french': 'Bonjour le monde!',
                'german': 'Hallo Welt!',
                'russian': 'Привет мир!',
                'chinese': '你好世界!',
                'japanese': 'こんにちは世界!',
                'arabic': 'مرحبا بالعالم!'
            }
        }
        
        # Encoding operations
        def demonstrate_encoding_operations():
            """Show encoding and decoding operations."""
            
            text = "Hello, 世界! 🌍"
            
            encoding_results = {}
            
            # Try different encodings
            encodings = ['utf-8', 'utf-16', 'utf-32', 'ascii', 'latin-1']
            
            for encoding in encodings:
                try:
                    encoded = text.encode(encoding)
                    decoded = encoded.decode(encoding)
                    
                    encoding_results[encoding] = {
                        'original': text,
                        'encoded_bytes': encoded,
                        'encoded_length': len(encoded),
                        'decoded': decoded,
                        'encoding_successful': True,
                        'round_trip_successful': text == decoded
                    }
                except Exception as e:
                    encoding_results[encoding] = {
                        'original': text,
                        'error': str(e),
                        'encoding_successful': False
                    }
            
            return encoding_results
        
        # Character code operations
        def character_code_operations():
            """Demonstrate character code conversions."""
            
            test_characters = ['A', 'z', '0', '9', '!', 'π', '🐍', '世']
            
            char_operations = {}
            
            for char in test_characters:
                try:
                    char_operations[char] = {
                        'character': char,
                        'ord_value': ord(char),
                        'hex_value': hex(ord(char)),
                        'chr_roundtrip': chr(ord(char)),
                        'roundtrip_successful': char == chr(ord(char))
                    }
                except Exception as e:
                    char_operations[char] = {
                        'character': char,
                        'error': str(e)
                    }
            
            # Generate character ranges
            ascii_lowercase = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
            ascii_uppercase = ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))
            digits = ''.join(chr(i) for i in range(ord('0'), ord('9') + 1))
            
            return {
                'individual_characters': char_operations,
                'character_ranges': {
                    'lowercase_letters': ascii_lowercase,
                    'uppercase_letters': ascii_uppercase,
                    'digits': digits
                }
            }
        
        encoding_ops = demonstrate_encoding_operations()
        char_codes = character_code_operations()
        
        return {
            'unicode_examples': unicode_examples,
            'encoding_operations': encoding_ops,
            'character_code_operations': char_codes
        }
    
    # String memory and performance characteristics
    def string_memory_performance():
        """Analyze string memory usage and performance characteristics."""
        
        import sys
        
        # Memory analysis of different string types
        def memory_analysis():
            """Analyze memory usage of different string constructions."""
            
            test_strings = {
                'empty': '',
                'short': 'Hi',
                'medium': 'Hello World' * 10,
                'long': 'Hello World' * 1000,
                'unicode': 'Hello 世界 🌍' * 100,
                'repeated_char': 'A' * 1000,
                'multiline': '\n'.join(['Line ' + str(i) for i in range(100)])
            }
            
            memory_results = {}
            
            for name, string in test_strings.items():
                memory_results[name] = {
                    'string_length': len(string),
                    'memory_size_bytes': sys.getsizeof(string),
                    'bytes_per_character': sys.getsizeof(string) / max(1, len(string)),
                    'string_preview': string[:50] + '...' if len(string) > 50 else string
                }
            
            return memory_results
        
        # String interning analysis
        def string_interning_analysis():
            """Demonstrate Python string interning behavior."""
            
            # Create identical strings different ways
            str1 = 'hello'
            str2 = 'hello'
            str3 = 'hel' + 'lo'
            str4 = ''.join(['h', 'e', 'l', 'l', 'o'])
            str5 = 'HELLO'.lower()
            
            # Check identity (same object in memory)
            interning_results = {
                'str1_str2_same_object': str1 is str2,
                'str1_str3_same_object': str1 is str3,
                'str1_str4_same_object': str1 is str4,
                'str1_str5_same_object': str1 is str5,
                'all_equal_value': str1 == str2 == str3 == str4 == str5,
                'memory_addresses': {
                    'str1': id(str1),
                    'str2': id(str2),
                    'str3': id(str3),
                    'str4': id(str4),
                    'str5': id(str5)
                }
            }
            
            # Test with longer strings
            long_str1 = 'this_is_a_longer_string_for_testing_interning'
            long_str2 = 'this_is_a_longer_string_for_testing_interning'
            long_str3 = 'this_is_a_longer_string' + '_for_testing_interning'
            
            interning_results['long_strings'] = {
                'long_str1_long_str2_same': long_str1 is long_str2,
                'long_str1_long_str3_same': long_str1 is long_str3,
                'long_str_addresses': {
                    'long_str1': id(long_str1),
                    'long_str2': id(long_str2),
                    'long_str3': id(long_str3)
                }
            }
            
            return interning_results
        
        memory_analysis_results = memory_analysis()
        interning_results = string_interning_analysis()
        
        return {
            'memory_analysis': memory_analysis_results,
            'string_interning': interning_results
        }
    
    # Execute all fundamental demonstrations
    basic_creation = basic_string_creation()
    literal_types = string_literal_types()
    encoding_unicode = string_encoding_unicode()
    memory_perf = string_memory_performance()
    
    return {
        'basic_string_creation': basic_creation,
        'string_literal_types': literal_types,
        'string_encoding_unicode': encoding_unicode,
        'string_memory_performance': memory_perf
    }

# =============================================================================
# 2. STRING PROPERTIES & CHARACTERISTICS - IMMUTABILITY MASTERY
# =============================================================================

"""
STRING PROPERTIES AND CHARACTERISTICS:
Master string immutability, properties, and behavioral characteristics
"""

def demonstrate_string_properties():
    """
    COMPREHENSIVE STRING PROPERTIES DEMONSTRATION
    Master string immutability and characteristic behaviors
    """
    
    # Immutability demonstration
    def immutability_demonstration():
        """Demonstrate string immutability and its implications."""
        
        # Basic immutability examples
        original_string = "Hello World"
        string_id = id(original_string)
        
        # Attempt modifications (these create new strings)
        modified_operations = {
            'upper': original_string.upper(),
            'lower': original_string.lower(),
            'replace': original_string.replace('World', 'Python'),
            'slice': original_string[0:5],
            'concatenation': original_string + ' Extra',
            'strip': ('  ' + original_string + '  ').strip()
        }
        
        # Check if original string changed
        immutability_proof = {
            'original_string': original_string,
            'original_id': string_id,
            'after_operations_string': original_string,
            'after_operations_id': id(original_string),
            'string_unchanged': original_string == "Hello World",
            'id_unchanged': string_id == id(original_string)
        }
        
        # Analyze new string objects
        operation_analysis = {}
        for operation, result in modified_operations.items():
            operation_analysis[operation] = {
                'result': result,
                'result_id': id(result),
                'is_new_object': id(result) != string_id,
                'equals_original': result == original_string
            }
        
        # Consequences of immutability
        def immutability_consequences():
            """Show practical consequences of immutability."""
            
            # Inefficient string building
            def inefficient_string_building():
                """Demonstrate inefficient string concatenation."""
                result = ""
                string_ids = [id(result)]
                
                for i in range(10):
                    result = result + str(i)  # Creates new string each time
                    string_ids.append(id(result))
                
                return {
                    'final_result': result,
                    'string_ids': string_ids,
                    'unique_objects_created': len(set(string_ids)),
                    'total_operations': len(string_ids) - 1
                }
            
            # Efficient string building
            def efficient_string_building():
                """Demonstrate efficient string building methods."""
                
                # Method 1: List join
                parts = []
                for i in range(10):
                    parts.append(str(i))
                result_join = ''.join(parts)
                
                # Method 2: List comprehension with join
                result_comprehension = ''.join(str(i) for i in range(10))
                
                # Method 3: f-string (for smaller cases)
                result_fstring = ''.join(f'{i}' for i in range(10))
                
                return {
                    'join_method_result': result_join,
                    'comprehension_result': result_comprehension,
                    'fstring_result': result_fstring,
                    'all_methods_equal': result_join == result_comprehension == result_fstring
                }
            
            inefficient = inefficient_string_building()
            efficient = efficient_string_building()
            
            return {
                'inefficient_building': inefficient,
                'efficient_building': efficient
            }
        
        consequences = immutability_consequences()
        
        return {
            'immutability_proof': immutability_proof,
            'operation_analysis': operation_analysis,
            'immutability_consequences': consequences
        }
    
    # String comparison behaviors
    def string_comparison_behaviors():
        """Demonstrate various string comparison behaviors."""
        
        # Basic comparisons
        comparison_examples = [
            ('hello', 'hello'),
            ('hello', 'Hello'),
            ('hello', 'world'),
            ('abc', 'abd'),
            ('123', '45'),
            ('', ''),
            (' ', ''),
            ('hello world', 'hello world ')
        ]
        
        comparison_results = {}
        for str1, str2 in comparison_examples:
            comparison_key = f"'{str1}' vs '{str2}'"
            comparison_results[comparison_key] = {
                'equality': str1 == str2,
                'inequality': str1 != str2,
                'less_than': str1 < str2,
                'less_equal': str1 <= str2,
                'greater_than': str1 > str2,
                'greater_equal': str1 >= str2,
                'lexicographic_order': sorted([str1, str2])
            }
        
        # Case-sensitive vs case-insensitive comparisons
        def case_comparison_analysis():
            """Analyze case-sensitive comparison behaviors."""
            
            test_pairs = [
                ('Hello', 'hello'),
                ('PYTHON', 'python'),
                ('MiXeD cAsE', 'mixed case')
            ]
            
            case_results = {}
            for str1, str2 in test_pairs:
                pair_key = f"'{str1}' vs '{str2}'"
                case_results[pair_key] = {
                    'case_sensitive_equal': str1 == str2,
                    'case_insensitive_equal': str1.lower() == str2.lower(),
                    'case_insensitive_equal_upper': str1.upper() == str2.upper(),
                    'casefold_equal': str1.casefold() == str2.casefold()  # More aggressive case folding
                }
            
            return case_results
        
        # Numeric string comparisons
        def numeric_string_comparisons():
            """Demonstrate numeric string comparison pitfalls."""
            
            numeric_strings = ['1', '2', '10', '20', '100']
            
            # Lexicographic vs numeric sorting
            lexicographic_sort = sorted(numeric_strings)
            numeric_sort = sorted(numeric_strings, key=int)
            
            # Comparison examples
            numeric_comparisons = {
                '1 < 2 (string)': '1' < '2',
                '10 < 2 (string)': '10' < '2',  # True due to lexicographic ordering!
                '100 < 20 (string)': '100' < '20',  # True due to lexicographic ordering!
                'int("10") < int("2")': int('10') < int('2')
            }
            
            return {
                'original_list': numeric_strings,
                'lexicographic_sort': lexicographic_sort,
                'numeric_sort': numeric_sort,
                'comparison_examples': numeric_comparisons
            }
        
        case_analysis = case_comparison_analysis()
        numeric_analysis = numeric_string_comparisons()
        
        return {
            'basic_comparisons': comparison_results,
            'case_comparison_analysis': case_analysis,
            'numeric_string_comparisons': numeric_analysis
        }
    
    # String hashing and identity
    def string_hashing_identity():
        """Explore string hashing and identity behaviors."""
        
        # Hash consistency
        test_strings = ['hello', 'world', '', 'Hello', 'hello world', '123', '🐍']
        
        hash_analysis = {}
        for string in test_strings:
            hash_value = hash(string)
            hash_analysis[string] = {
                'string': string,
                'hash': hash_value,
                'hash_hex': hex(hash_value),
                'id': id(string)
            }
        
        # Hash collision testing (artificial example)
        def hash_collision_exploration():
            """Explore potential hash behaviors (educational)."""
            
            # Create many similar strings to see hash distribution
            similar_strings = [f'test_{i}' for i in range(100)]
            hashes = [hash(s) for s in similar_strings]
            
            unique_hashes = set(hashes)
            
            return {
                'total_strings': len(similar_strings),
                'unique_hashes': len(unique_hashes),
                'collision_free': len(similar_strings) == len(unique_hashes),
                'hash_sample': dict(zip(similar_strings[:10], hashes[:10]))
            }
        
        # String identity vs equality
        def identity_vs_equality():
            """Compare identity (is) vs equality (==)."""
            
            # Create strings in different ways
            s1 = 'hello'
            s2 = 'hello'
            s3 = 'hel' + 'lo'
            s4 = ''.join(['h', 'e', 'l', 'l', 'o'])
            s5 = 'HELLO'.lower()
            
            strings = {'s1': s1, 's2': s2, 's3': s3, 's4': s4, 's5': s5}
            
            identity_matrix = {}
            equality_matrix = {}
            
            for name1, str1 in strings.items():
                identity_matrix[name1] = {}
                equality_matrix[name1] = {}
                
                for name2, str2 in strings.items():
                    identity_matrix[name1][name2] = str1 is str2
                    equality_matrix[name1][name2] = str1 == str2
            
            return {
                'string_values': strings,
                'identity_matrix': identity_matrix,
                'equality_matrix': equality_matrix,
                'string_ids': {name: id(string) for name, string in strings.items()}
            }
        
        collision_exploration = hash_collision_exploration()
        identity_equality = identity_vs_equality()
        
        return {
            'hash_analysis': hash_analysis,
            'hash_collision_exploration': collision_exploration,
            'identity_vs_equality': identity_equality
        }
    
    # Execute all property demonstrations
    immutability = immutability_demonstration()
    comparisons = string_comparison_behaviors()
    hashing_identity = string_hashing_identity()
    
    return {
        'immutability_demonstration': immutability,
        'string_comparison_behaviors': comparisons,
        'string_hashing_identity': hashing_identity
    }

# =============================================================================
# 3. STRING INDEXING & SLICING MASTERY - ADVANCED ACCESS TECHNIQUES
# =============================================================================

"""
STRING INDEXING AND SLICING MASTERY:
Master advanced string indexing and slicing techniques
"""

def demonstrate_string_indexing_slicing():
    """
    COMPREHENSIVE STRING INDEXING AND SLICING DEMONSTRATION
    Master all aspects of string indexing and slicing operations
    """
    
    # Basic indexing patterns
    def basic_indexing_patterns():
        """Demonstrate fundamental string indexing patterns."""
        
        test_string = "Python Programming"
        
        # Single character access
        indexing_examples = {
            'first_character': {
                'expression': 'test_string[0]',
                'result': test_string[0],
                'description': 'First character (leftmost)'
            },
            'last_character': {
                'expression': 'test_string[-1]',
                'result': test_string[-1],
                'description': 'Last character (rightmost)'
            },
            'second_character': {
                'expression': 'test_string[1]',
                'result': test_string[1],
                'description': 'Second character'
            },
            'second_to_last': {
                'expression': 'test_string[-2]',
                'result': test_string[-2],
                'description': 'Second to last character'
            },
            'middle_character': {
                'expression': f'test_string[{len(test_string)//2}]',
                'result': test_string[len(test_string)//2],
                'description': 'Middle character (approximate)'
            }
        }
        
        # Index validation and bounds checking
        def index_bounds_analysis():
            """Analyze index bounds and edge cases."""
            
            string_length = len(test_string)
            
            bounds_tests = []
            
            # Test valid indices
            for i in range(-string_length, string_length):
                try:
                    char = test_string[i]
                    positive_equivalent = i if i >= 0 else string_length + i
                    
                    bounds_tests.append({
                        'index': i,
                        'character': char,
                        'positive_equivalent': positive_equivalent,
                        'is_valid': True,
                        'error': None
                    })
                except IndexError as e:
                    bounds_tests.append({
                        'index': i,
                        'character': None,
                        'positive_equivalent': None,
                        'is_valid': False,
                        'error': str(e)
                    })
            
            # Test invalid indices
            invalid_indices = [string_length, -string_length - 1, string_length + 10, -100]
            
            for idx in invalid_indices:
                try:
                    char = test_string[idx]
                    bounds_tests.append({
                        'index': idx,
                        'character': char,
                        'is_valid': True,
                        'error': None
                    })
                except IndexError as e:
                    bounds_tests.append({
                        'index': idx,
                        'character': None,
                        'is_valid': False,
                        'error': str(e)
                    })
            
            return {
                'string_length': string_length,
                'valid_index_range': f'[{-string_length}, {string_length - 1}]',
                'bounds_test_results': bounds_tests
            }
        
        bounds_analysis = index_bounds_analysis()
        
        return {
            'test_string': test_string,
            'string_length': len(test_string),
            'indexing_examples': indexing_examples,
            'bounds_analysis': bounds_analysis
        }
    
    # Advanced slicing techniques
    def advanced_slicing_techniques():
        """Master advanced string slicing patterns."""
        
        test_text = "The quick brown fox jumps over the lazy dog"
        
        # Comprehensive slicing patterns
        slicing_patterns = {
            # Basic slicing
            'first_word': {
                'slice': test_text[:3],
                'expression': 'text[:3]',
                'description': 'First 3 characters'
            },
            'last_word': {
                'slice': test_text[-3:],
                'expression': 'text[-3:]',
                'description': 'Last 3 characters'
            },
            'middle_section': {
                'slice': test_text[10:20],
                'expression': 'text[10:20]',
                'description': 'Characters from index 10 to 19'
            },
            
            # Step slicing
            'every_second_char': {
                'slice': test_text[::2],
                'expression': 'text[::2]',
                'description': 'Every second character'
            },
            'every_third_char': {
                'slice': test_text[::3],
                'expression': 'text[::3]',
                'description': 'Every third character'
            },
            'reverse_string': {
                'slice': test_text[::-1],
                'expression': 'text[::-1]',
                'description': 'Entire string reversed'
            },
            'reverse_every_second': {
                'slice': test_text[::-2],
                'expression': 'text[::-2]',
                'description': 'Every second character in reverse'
            },
            
            # Complex slicing
            'middle_third': {
                'slice': test_text[len(test_text)//3:2*len(test_text)//3],
                'expression': 'text[len(text)//3:2*len(text)//3]',
                'description': 'Middle third of string'
            },
            'skip_first_last': {
                'slice': test_text[1:-1],
                'expression': 'text[1:-1]',
                'description': 'All except first and last character'
            },
            'odd_positions': {
                'slice': test_text[1::2],
                'expression': 'text[1::2]',
                'description': 'Characters at odd positions'
            }
        }
        
        # Word-level slicing
        def word_level_slicing():
            """Demonstrate word-level slicing techniques."""
            
            words = test_text.split()
            
            word_slicing = {
                'first_word': words[0],
                'last_word': words[-1],
                'first_three_words': ' '.join(words[:3]),
                'last_three_words': ' '.join(words[-3:]),
                'middle_words': ' '.join(words[2:-2]),
                'every_second_word': ' '.join(words[::2]),
                'words_in_reverse': ' '.join(words[::-1]),
                'alternate_words_reverse': ' '.join(words[::-2])
            }
            
            return {
                'original_text': test_text,
                'word_list': words,
                'word_count': len(words),
                'word_slicing_examples': word_slicing
            }
        
        # Dynamic slicing based on content
        def dynamic_slicing():
            """Demonstrate dynamic slicing based on string content."""
            
            sample_text = "Hello, World! This is a test string with punctuation."
            
            # Find and slice around specific characters
            def slice_around_character(text, char, context_length=5):
                """Find character and return slice with context."""
                results = []
                for i, c in enumerate(text):
                    if c == char:
                        start = max(0, i - context_length)
                        end = min(len(text), i + context_length + 1)
                        results.append({
                            'position': i,
                            'context_slice': text[start:end],
                            'slice_range': f'[{start}:{end}]'
                        })
                return results
            
            # Find and extract words
            def extract_words_by_position(text):
                """Extract words and their positions."""
                word_positions = []
                current_word_start = None
                
                for i, char in enumerate(text):
                    if char.isalpha():
                        if current_word_start is None:
                            current_word_start = i
                    else:
                        if current_word_start is not None:
                            word = text[current_word_start:i]
                            word_positions.append({
                                'word': word,
                                'start': current_word_start,
                                'end': i,
                                'slice_expression': f'text[{current_word_start}:{i}]'
                            })
                            current_word_start = None
                
                # Handle word at end of string
                if current_word_start is not None:
                    word = text[current_word_start:]
                    word_positions.append({
                        'word': word,
                        'start': current_word_start,
                        'end': len(text),
                        'slice_expression': f'text[{current_word_start}:]'
                    })
                
                return word_positions
            
            # Slice by punctuation
            comma_contexts = slice_around_character(sample_text, ',', 3)
            exclamation_contexts = slice_around_character(sample_text, '!', 4)
            word_extractions = extract_words_by_position(sample_text)
            
            return {
                'sample_text': sample_text,
                'comma_contexts': comma_contexts,
                'exclamation_contexts': exclamation_contexts,
                'word_extractions': word_extractions
            }
        
        word_slicing = word_level_slicing()
        dynamic = dynamic_slicing()
        
        return {
            'test_text': test_text,
            'basic_slicing_patterns': slicing_patterns,
            'word_level_slicing': word_slicing,
            'dynamic_slicing': dynamic
        }
    
    # String indexing for text processing
    def text_processing_indexing():
        """Demonstrate indexing techniques for text processing tasks."""
        
        # CSV-like text processing
        csv_text = "Name,Age,City,Salary\nJohn,30,NYC,50000\nJane,25,LA,60000"
        
        def parse_csv_with_indexing(text):
            """Parse CSV using string indexing techniques."""
            
            lines = text.split('\n')
            header = lines[0]
            data_lines = lines[1:]
            
            # Parse header
            header_fields = []
            current_field = ""
            for char in header:
                if char == ',':
                    header_fields.append(current_field)
                    current_field = ""
                else:
                    current_field += char
            header_fields.append(current_field)  # Last field
            
            # Parse data lines
            parsed_data = []
            for line in data_lines:
                fields = []
                current_field = ""
                for char in line:
                    if char == ',':
                        fields.append(current_field)
                        current_field = ""
                    else:
                        current_field += char
                fields.append(current_field)  # Last field
                
                # Create record
                record = {}
                for i, field_value in enumerate(fields):
                    if i < len(header_fields):
                        record[header_fields[i]] = field_value
                
                parsed_data.append(record)
            
            return {
                'header_fields': header_fields,
                'parsed_records': parsed_data,
                'record_count': len(parsed_data)
            }
        
        # URL parsing with indexing
        def parse_url_with_indexing(url):
            """Parse URL components using string indexing."""
            
            # Find protocol
            protocol_end = url.find('://')
            if protocol_end != -1:
                protocol = url[:protocol_end]
                remaining_url = url[protocol_end + 3:]
            else:
                protocol = None
                remaining_url = url
            
            # Find domain and path
            path_start = remaining_url.find('/')
            if path_start != -1:
                domain = remaining_url[:path_start]
                path = remaining_url[path_start:]
            else:
                domain = remaining_url
                path = '/'
            
            # Find query parameters
            query_start = path.find('?')
            if query_start != -1:
                actual_path = path[:query_start]
                query_string = path[query_start + 1:]
            else:
                actual_path = path
                query_string = None
            
            # Parse query parameters
            query_params = {}
            if query_string:
                param_pairs = query_string.split('&')
                for pair in param_pairs:
                    eq_pos = pair.find('=')
                    if eq_pos != -1:
                        key = pair[:eq_pos]
                        value = pair[eq_pos + 1:]
                        query_params[key] = value
            
            return {
                'original_url': url,
                'protocol': protocol,
                'domain': domain,
                'path': actual_path,
                'query_string': query_string,
                'query_parameters': query_params
            }
        
        # Email extraction with indexing
        def extract_emails_with_indexing(text):
            """Extract email addresses using string indexing."""
            
            emails = []
            i = 0
            
            while i < len(text):
                # Find @ symbol
                at_pos = text.find('@', i)
                if at_pos == -1:
                    break
                
                # Find start of email (work backwards)
                email_start = at_pos
                while email_start > 0:
                    char = text[email_start - 1]
                    if char.isalnum() or char in '._-':
                        email_start -= 1
                    else:
                        break
                
                # Find end of email (work forwards)
                email_end = at_pos + 1
                while email_end < len(text):
                    char = text[email_end]
                    if char.isalnum() or char in '.-':
                        email_end += 1
                    else:
                        break
                
                # Extract potential email
                potential_email = text[email_start:email_end]
                
                # Basic validation
                if '.' in potential_email[at_pos - email_start:] and len(potential_email) > 5:
                    emails.append({
                        'email': potential_email,
                        'start_position': email_start,
                        'end_position': email_end,
                        'context': text[max(0, email_start-10):min(len(text), email_end+10)]
                    })
                
                i = email_end
            
            return emails
        
        # Test examples
        csv_parsing = parse_csv_with_indexing(csv_text)
        
        test_urls = [
            "https://www.example.com/path/to/page?param=value&other=data",
            "http://subdomain.site.org/api/v1/users",
            "ftp://files.example.com/directory/"
        ]
        
        url_parsing = [parse_url_with_indexing(url) for url in test_urls]
        
        email_text = "Contact us at info@example.com or support@company.org for assistance."
        email_extraction = extract_emails_with_indexing(email_text)
        
        return {
            'csv_processing': {
                'original_text': csv_text,
                'parsing_result': csv_parsing
            },
            'url_parsing': {
                'test_urls': test_urls,
                'parsing_results': url_parsing
            },
            'email_extraction': {
                'source_text': email_text,
                'extracted_emails': email_extraction
            }
        }
    
    # Execute all indexing and slicing demonstrations
    basic_indexing = basic_indexing_patterns()
    advanced_slicing = advanced_slicing_techniques()
    text_processing = text_processing_indexing()
    
    return {
        'basic_indexing_patterns': basic_indexing,
        'advanced_slicing_techniques': advanced_slicing,
        'text_processing_indexing': text_processing
    }

# =============================================================================
# 4. STRING METHODS & OPERATIONS - COMPLETE METHOD MASTERY
# =============================================================================

def demonstrate_string_methods():
    """Master all string methods and operations with comprehensive examples."""
    
    sample_text = "  Hello, World! Welcome to Python Programming.  "
    
    # Case manipulation methods
    case_methods = {
        'lower': sample_text.lower(),
        'upper': sample_text.upper(),
        'title': sample_text.title(),
        'capitalize': sample_text.capitalize(),
        'swapcase': sample_text.swapcase(),
        'casefold': sample_text.casefold()
    }
    
    # Cleaning and trimming methods
    cleaning_methods = {
        'strip': sample_text.strip(),
        'lstrip': sample_text.lstrip(),
        'rstrip': sample_text.rstrip(),
        'strip_custom': sample_text.strip(' .'),
        'removeprefix': sample_text.removeprefix('  Hello'),
        'removesuffix': sample_text.removesuffix('.  ')
    }
    
    # Search and find methods
    search_text = "The quick brown fox jumps over the lazy dog"
    search_methods = {
        'find_fox': search_text.find('fox'),
        'rfind_the': search_text.rfind('the'),
        'index_quick': search_text.index('quick'),
        'count_the': search_text.count('the'),
        'startswith_the': search_text.startswith('The'),
        'endswith_dog': search_text.endswith('dog')
    }
    
    # Split and join methods
    split_join_methods = {
        'split_default': search_text.split(),
        'split_space': search_text.split(' '),
        'rsplit': search_text.rsplit(' ', 2),
        'splitlines': "Line 1\nLine 2\nLine 3".splitlines(),
        'partition': search_text.partition('fox'),
        'rpartition': search_text.rpartition('the'),
        'join_words': '-'.join(['Python', 'is', 'awesome'])
    }
    
    # Replacement methods
    replacement_methods = {
        'replace_simple': search_text.replace('fox', 'cat'),
        'replace_count': search_text.replace('the', 'THE', 1),
        'translate_table': search_text.translate(str.maketrans('fox', 'cat')),
        'expandtabs': "Hello\tWorld\tPython".expandtabs(4)
    }
    
    # Validation methods
    validation_text_samples = ['123', 'ABC', 'abc123', '   ', 'Hello World', '']
    validation_methods = {}
    
    for text in validation_text_samples:
        validation_methods[f"'{text}'"] = {
            'isalnum': text.isalnum(),
            'isalpha': text.isalpha(),
            'isascii': text.isascii(),
            'isdecimal': text.isdecimal(),
            'isdigit': text.isdigit(),
            'isidentifier': text.isidentifier(),
            'islower': text.islower(),
            'isnumeric': text.isnumeric(),
            'isprintable': text.isprintable(),
            'isspace': text.isspace(),
            'istitle': text.istitle(),
            'isupper': text.isupper()
        }
    
    # Formatting methods
    formatting_methods = {
        'center': 'Python'.center(20, '-'),
        'ljust': 'Python'.ljust(15, '.'),
        'rjust': 'Python'.rjust(15, '.'),
        'zfill': '42'.zfill(8),
        'format_basic': 'Hello, {}!'.format('World'),
        'format_positional': '{0} {1} {0}'.format('Hello', 'World'),
        'format_keyword': '{greeting} {name}!'.format(greeting='Hello', name='Python')
    }
    
    return {
        'sample_text': sample_text,
        'case_methods': case_methods,
        'cleaning_methods': cleaning_methods,
        'search_methods': search_methods,
        'split_join_methods': split_join_methods,
        'replacement_methods': replacement_methods,
        'validation_methods': validation_methods,
        'formatting_methods': formatting_methods
    }

# =============================================================================
# 5. STRING FORMATTING & INTERPOLATION - MODERN FORMATTING MASTERY
# =============================================================================

def demonstrate_string_formatting():
    """Master all string formatting techniques from basic to advanced."""
    
    # Sample data for formatting examples
    name = "Python"
    version = 3.11
    pi = 3.14159265359
    large_number = 1234567890
    date_parts = (2024, 1, 15)
    
    # f-string formatting (Python 3.6+)
    fstring_examples = {
        'basic': f"Hello, {name}!",
        'expression': f"{name} version is {version}",
        'calculation': f"2 + 2 = {2 + 2}",
        'method_call': f"Uppercase: {name.upper()}",
        'precision': f"Pi with 3 decimals: {pi:.3f}",
        'width_alignment': f"Right aligned: {name:>15}",
        'zero_padding': f"Zero padded: {42:05d}",
        'thousands_separator': f"Large number: {large_number:,}",
        'percentage': f"Percentage: {0.856:.1%}",
        'date_format': f"Date: {date_parts[0]}-{date_parts[1]:02d}-{date_parts[2]:02d}"
    }
    
    # str.format() method formatting
    format_examples = {
        'positional': "Hello, {}! Version {}.".format(name, version),
        'indexed': "{0} {1} {0}".format("Hello", "World"),
        'named': "{lang} version {ver}".format(lang=name, ver=version),
        'precision': "Pi: {:.4f}".format(pi),
        'alignment': "Left: {:<10} Right: {:>10} Center: {:^10}".format("Hi", "There", "Centered"),
        'fill_char': "{:*^20}".format("Title"),
        'number_format': "Binary: {:b}, Hex: {:x}, Octal: {:o}".format(42, 42, 42)
    }
    
    # % formatting (legacy but still used)
    percent_examples = {
        'basic': "Hello, %s!" % name,
        'multiple': "%s version %.1f" % (name, version),
        'named': "%(lang)s is version %(ver).2f" % {'lang': name, 'ver': version},
        'integer': "Number: %d" % 42,
        'float': "Pi: %.3f" % pi,
        'padding': "Padded: %05d" % 42
    }
    
    # Advanced formatting patterns
    def advanced_formatting_patterns():
        """Demonstrate advanced formatting techniques."""
        
        # Dynamic formatting
        data = [
            {'name': 'Alice', 'age': 30, 'salary': 50000},
            {'name': 'Bob', 'age': 25, 'salary': 45000},
            {'name': 'Charlie', 'age': 35, 'salary': 60000}
        ]
        
        # Table formatting
        table_header = f"{'Name':<10} {'Age':>5} {'Salary':>10}"
        table_rows = [f"{person['name']:<10} {person['age']:>5} {person['salary']:>10,}" for person in data]
        table_format = [table_header] + ['-' * len(table_header)] + table_rows
        
        # Custom formatting classes
        class CustomFormatter:
            def __init__(self, value):
                self.value = value
            
            def __format__(self, format_spec):
                if format_spec == 'reverse':
                    return str(self.value)[::-1]
                elif format_spec == 'upper':
                    return str(self.value).upper()
                elif format_spec.startswith('pad'):
                    width = int(format_spec[3:])
                    return str(self.value).center(width, '*')
                else:
                    return str(self.value)
        
        custom_obj = CustomFormatter("hello")
        custom_formatting = {
            'normal': f"{custom_obj}",
            'reverse': f"{custom_obj:reverse}",
            'upper': f"{custom_obj:upper}",
            'padded': f"{custom_obj:pad20}"
        }
        
        # Template strings
        from string import Template
        template = Template("$greeting, $name! Welcome to $language programming.")
        template_result = template.substitute(
            greeting="Hello",
            name="Developer", 
            language="Python"
        )
        
        template_safe = template.safe_substitute(
            greeting="Hi",
            name="Coder"
            # language is missing - will be left as $language
        )
        
        return {
            'table_formatting': table_format,
            'custom_formatting': custom_formatting,
            'template_basic': template_result,
            'template_safe': template_safe
        }
    
    advanced_patterns = advanced_formatting_patterns()
    
    return {
        'fstring_examples': fstring_examples,
        'format_examples': format_examples,
        'percent_examples': percent_examples,
        'advanced_patterns': advanced_patterns
    }

# =============================================================================
# 6. REAL-WORLD TEXT PROCESSING APPLICATIONS
# =============================================================================

def demonstrate_real_world_applications():
    """Demonstrate practical text processing applications."""
    
    # Email processing system
    def email_processing():
        """Process and validate email addresses."""
        emails = ["user@example.com", "invalid-email", "test.user+tag@domain.co.uk"]
        
        def validate_email(email):
            """Basic email validation."""
            if '@' not in email:
                return False
            local, domain = email.rsplit('@', 1)
            if '.' not in domain:
                return False
            return len(local) > 0 and len(domain) > 0
        
        results = []
        for email in emails:
            is_valid = validate_email(email)
            if is_valid:
                local, domain = email.rsplit('@', 1)
                results.append({
                    'email': email,
                    'valid': True,
                    'local_part': local,
                    'domain': domain
                })
            else:
                results.append({
                    'email': email, 
                    'valid': False,
                    'error': 'Invalid format'
                })
        
        return results
    
    # Log file analysis
    def log_analysis():
        """Analyze log file entries."""
        log_entries = [
            "2024-01-15 10:30:45 INFO User logged in successfully",
            "2024-01-15 10:31:12 ERROR Failed to connect to database",
            "2024-01-15 10:32:01 INFO User accessed dashboard"
        ]
        
        parsed_logs = []
        for entry in log_entries:
            parts = entry.split(' ', 3)  # Split into at most 4 parts
            if len(parts) >= 4:
                parsed_logs.append({
                    'date': parts[0],
                    'time': parts[1],
                    'level': parts[2],
                    'message': parts[3]
                })
        
        # Count by level
        level_counts = {}
        for log in parsed_logs:
            level = log['level']
            level_counts[level] = level_counts.get(level, 0) + 1
        
        return {
            'parsed_logs': parsed_logs,
            'level_counts': level_counts
        }
    
    # Text statistics
    def text_statistics():
        """Calculate comprehensive text statistics."""
        text = """Python is a high-level programming language. 
        Python emphasizes code readability and simplicity.
        Many developers choose Python for various applications."""
        
        # Basic stats
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        word_count = len(text.split())
        sentence_count = text.count('.')
        paragraph_count = len([p for p in text.split('\n') if p.strip()])
        
        # Word frequency
        words = text.lower().replace('.', '').replace(',', '').split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        most_common = max(word_freq.items(), key=lambda x: x[1])
        
        return {
            'text_length': char_count,
            'chars_no_spaces': char_count_no_spaces,
            'word_count': word_count,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count,
            'unique_words': len(word_freq),
            'most_common_word': most_common,
            'word_frequency': dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5])
        }
    
    return {
        'email_processing': email_processing(),
        'log_analysis': log_analysis(),
        'text_statistics': text_statistics()
    }

# =============================================================================
# DEMONSTRATION EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("PYTHON TEXT PROCESSING & STRING MANIPULATION - COMPLETE MASTERY GUIDE")
    print("=" * 80)
    
    try:
        print("\n1. STRING FUNDAMENTALS & CREATION")
        fundamentals = demonstrate_string_fundamentals()
        print("✓ String creation and fundamentals demonstrated")
        
        print("\n2. STRING PROPERTIES & CHARACTERISTICS")
        properties = demonstrate_string_properties()
        print("✓ String properties and immutability demonstrated")
        
        print("\n3. STRING INDEXING & SLICING MASTERY")
        indexing = demonstrate_string_indexing_slicing()
        print("✓ Advanced indexing and slicing techniques demonstrated")
        
        print("\n4. STRING METHODS & OPERATIONS")
        methods = demonstrate_string_methods()
        print("✓ Complete string methods reference demonstrated")
        
        print("\n5. STRING FORMATTING & INTERPOLATION")
        formatting = demonstrate_string_formatting()
        print("✓ Modern formatting techniques demonstrated")
        
        print("\n6. REAL-WORLD TEXT PROCESSING APPLICATIONS")
        applications = demonstrate_real_world_applications()
        print("✓ Practical text processing applications demonstrated")
        
        print("\n" + "=" * 80)
        print("COMPLETE TEXT PROCESSING MASTERY ACHIEVED!")
        print("✓ All major text processing concepts covered")
        print("✓ Professional-grade examples and applications")
        print("✓ Performance optimization techniques included")
        print("=" * 80)
        
    except Exception as e:
        print(f"Error: {e}")

# Original examples preserved below for reference
print("\nORIGINAL EXAMPLES - PRESERVED FOR REFERENCE:")
print("=" * 50)
            
print("""\
Hello World!
This is a multiline string.
It can span multiple lines.
It is useful for long text or documentation.
""")
# (Automatic initial line break)
# Hello World!
# This is a multiline string.
# It can span multiple lines.
# It is useful for long text or documentation.            

# ----------

""" Line breaks """
# Line breaks inside a Print() function, generate a new line in the output.
# Use "\n" as a line break character inside the Print() function.
#   The "\n" character is not printed, but it generates a line break in the output.

print("Hello \nWorld!") 
# Hello
# World!

""" Exception """
# "\n" is included as part of the Str content.
# Not included in the print() function as a line break.
#       "... \Name\..."
# In the print() function 
#       Use r or R before the "Str" to indicate that it is a raw string.
#           >>> print(r"...\Name\...")
#               "...\Name\...            

print(r"Hollow world... trying to use \n... as a non-line break character")
# Hollow world... trying to use \n... as a non-line break character

# ----------

""" Strings length """
# Use the len() function to obtain the length of a string.
#   The len() function returns the number of characters in the string.
#       Includes all characters, including spaces and punctuation.

p1 = "Python"
len(p1)
# 6

# ----------

""" Concatenated strings """

""" Glue together two or more strings using the "+" operator. """

p1 = "Py"
p2 = "thon"
p3 = " is a programming language"

print(p1 + p2 + p3)
# Python is a programming language

""" Repeat a string multiple times using the "*" operator. """

p1 = "Py"
p2 = "thon"
p3 = " is a programming language"

print(p1*2 + p2*3 + p3)
# PyPYthonthonthon is a programming language

""" Automatic concatenation of string literals """
# Two o more strings literals next to each other are automatically concatenated.
#       The interpreter automatically concatenates them.

print("Py" "thon")
#Python
          
# OR

text = ('Put several strings within parentheses '
'to have them joined together.')
print(text)
# 'Put several strings within parentheses to have them joined together.'

# ----------

"""Indexed strings"""
# Strings are indexed, meaning each character has a unique number, obtaining individual characters.
#   Works similar to an array and allows you to locate a character using a numerical index
#       The first character (counting right to left) is at index 0, the second at index 1, and so on.
#           The last character (counting right to left) is at index -1, the second to last at -2, and so on.

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

""" Slide index"""
# An indexed string can be sliced, allowing you to obtain a substring.
#   The slice is defined by two indexes, the first and the last.
#       The first index is included in the slice, while the last index is excluded.
#           The slice is defined by the syntax [first:last].
#               Following the  logical string recomposition rule: s[:i] + s[i:]
#                   The length of a slice is the difference of the indices
#                       word[1:3] length equals 2

text = 'Python' 

text[:2]   # Slice from the beginning of the string to index 2 (excluding index 2)
# 'Py'

text[2:]   # Slice from index 2 to the end of the string
# 'thon'

text[0:2]  # Slice from index 0 to index 2 (excluding index 2)
# 'Py'

text[2:5]  # Slice from index 2 to index 5 (excluding index 5)
# 'tho'

text[:]    # Slice the entire string
# 'Python'

text[::2]  # Slice the string with a step of 2
# 'Pto'

text[::-1] # Slice the string in reverse order
# 'nohtyP'

text[-2:]  # Slice the last two characters of the string
# 'on'

text[-2:-1] # Slice the last two characters of the string
# 'o'

""" Slice out of range can be handled without error. """

#   The slice will be empty if the first index is greater than the last index.
text[42:]  # Slice from index 42 to the end of index
# ''             # Empty string

text[:42]  # Slice from index 0 to index 42 (excluding index 42)
# 'Python'       # The entire string, included the character after the last number of the index

# ----------

""" Check if a string contains a substring using "in" """
# Use the "in" operator to check if a substring is present in a string. 

text = "Python is a programming language"
print("Python" in text)  
# True

""" Check if a string contains a substring using "if" and "in". """
# Use an "if" statement to check if a substring is present in a string.

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Yes, 'free' is present.

""" Check if a string does not contain a substring using "if", "not", "in" """
# Use an "if not" statement to check if a substring is not present in a string.

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
# No, 'expensive' is NOT present.

# ----------

""" PRACTICAL EXAMPLES: REAL-WORLD TEXT PROCESSING """

# 📧 Example 1: Email Validation and Processing
print("=== EMAIL PROCESSING SYSTEM ===")
email = "user.name@example.com"

# Extract username and domain
username = email.split('@')[0]
domain = email.split('@')[1]

print(f"Full email: {email}")
print(f"Username: {username}")
print(f"Domain: {domain}")

# Validate email format (basic check)
if '@' in email and '.' in domain:
    print("✅ Valid email format")
else:
    print("❌ Invalid email format")

# Clean up email (remove spaces, convert to lowercase)
messy_email = "  USER.NAME@EXAMPLE.COM  "
clean_email = messy_email.strip().lower()
print(f"Original: '{messy_email}'")
print(f"Cleaned: '{clean_email}'")

# ----------

# 📝 Example 2: Text Analysis and Word Count
print("\n=== TEXT ANALYSIS TOOL ===")
article = """Python is a high-level programming language. 
Python is known for its simplicity and readability. 
Many developers choose Python for web development, 
data analysis, and artificial intelligence projects."""

# Basic statistics
word_count = len(article.split())
char_count = len(article)
char_count_no_spaces = len(article.replace(' ', ''))
sentence_count = article.count('.')

print(f"📊 Article Statistics:")
print(f"Characters (with spaces): {char_count}")
print(f"Characters (no spaces): {char_count_no_spaces}")  
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")

# Find most common words
words = article.lower().replace(',', '').replace('.', '').split()
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Find word that appears most
most_common_word = max(word_frequency, key=word_frequency.get)
print(f"Most common word: '{most_common_word}' ({word_frequency[most_common_word]} times)")

# Search for specific terms
search_terms = ['python', 'development', 'language']
for term in search_terms:
    count = article.lower().count(term)
    print(f"'{term}' appears {count} time(s)")

# ----------

# 🏪 Example 3: Product Code Processing
print("\n=== PRODUCT INVENTORY SYSTEM ===")
product_codes = ["ELEC-001-BLK", "CLTH-025-RED", "BOOK-103-HRD", "ELEC-045-WHT"]

print("📦 Product Analysis:")
for code in product_codes:
    parts = code.split('-')
    category = parts[0]
    item_id = parts[1]
    attribute = parts[2]
    
    # Decode category
    if category == "ELEC":
        category_name = "Electronics"
    elif category == "CLTH":
        category_name = "Clothing"
    elif category == "BOOK":
        category_name = "Books"
    else:
        category_name = "Unknown"
    
    # Decode attribute
    attribute_map = {
        "BLK": "Black", "RED": "Red", "WHT": "White", 
        "HRD": "Hardcover", "SFT": "Softcover"
    }
    attribute_name = attribute_map.get(attribute, attribute)
    
    print(f"Code: {code}")
    print(f"  Category: {category_name}")
    print(f"  Item ID: {item_id}")
    print(f"  Attribute: {attribute_name}")
    print()

# ----------

# 🔐 Example 4: Password Validation
print("=== PASSWORD VALIDATION SYSTEM ===")

def validate_password(password):
    """Validate password strength"""
    issues = []
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        issues.append("Must be at least 8 characters long")
    
    # Uppercase check
    if any(c.isupper() for c in password):
        score += 1
    else:
        issues.append("Must contain at least one uppercase letter")
    
    # Lowercase check  
    if any(c.islower() for c in password):
        score += 1
    else:
        issues.append("Must contain at least one lowercase letter")
    
    # Number check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        issues.append("Must contain at least one number")
    
    # Special character check
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(c in special_chars for c in password):
        score += 1
    else:
        issues.append("Must contain at least one special character")
    
    return score, issues

# Test different passwords
test_passwords = ["weak", "StrongPass123", "MyP@ssw0rd!", "abc123"]

for pwd in test_passwords:
    score, issues = validate_password(pwd)
    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong"][score]
    
    print(f"Password: '{pwd}'")
    print(f"Strength: {strength} ({score}/5)")
    if issues:
        print("Issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ Password meets all requirements!")
    print()

# ----------

# 📱 Example 5: Phone Number Formatting
print("=== PHONE NUMBER FORMATTER ===")
phone_numbers = ["1234567890", "123-456-7890", "(123) 456-7890", "+1-123-456-7890"]

def format_phone(phone):
    """Format phone number to standard format"""
    # Remove all non-digit characters
    digits = ''.join(c for c in phone if c.isdigit())
    
    # Handle different lengths
    if len(digits) == 10:
        # Format as (XXX) XXX-XXXX
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        # Format as +1 (XXX) XXX-XXXX
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return "Invalid phone number"

print("📞 Phone Number Formatting:")
for phone in phone_numbers:
    formatted = format_phone(phone)
    print(f"Original: {phone:15} → Formatted: {formatted}")

# ----------

# 📄 Example 6: CSV Data Processing
print("\n=== CSV DATA PROCESSOR ===")
csv_data = """Name,Age,City,Salary
John Smith,30,New York,75000
Jane Doe,25,Los Angeles,65000
Bob Johnson,35,Chicago,80000
Alice Brown,28,Miami,70000"""

print("📊 Employee Data Analysis:")
lines = csv_data.strip().split('\n')
headers = lines[0].split(',')
print(f"Headers: {headers}")

employees = []
for line in lines[1:]:  # Skip header
    data = line.split(',')
    employee = {
        'name': data[0],
        'age': int(data[1]),
        'city': data[2],
        'salary': int(data[3])
    }
    employees.append(employee)

# Analysis
total_employees = len(employees)
total_salary = sum(emp['salary'] for emp in employees)
avg_salary = total_salary / total_employees
avg_age = sum(emp['age'] for emp in employees) / total_employees

print(f"Total employees: {total_employees}")
print(f"Average salary: ${avg_salary:,.2f}")
print(f"Average age: {avg_age:.1f} years")

# Find highest paid employee
highest_paid = max(employees, key=lambda x: x['salary'])
print(f"Highest paid: {highest_paid['name']} (${highest_paid['salary']:,})")

# Group by city
cities = {}
for emp in employees:
    city = emp['city']
    if city not in cities:
        cities[city] = []
    cities[city].append(emp['name'])

print("Employees by city:")
for city, names in cities.items():
    print(f"  {city}: {', '.join(names)}")

# ----------

# 🔍 Example 7: Log File Analysis
print("\n=== LOG FILE ANALYZER ===")
log_entries = [
    "2024-01-15 10:30:45 INFO User logged in successfully",
    "2024-01-15 10:31:12 ERROR Failed to connect to database",  
    "2024-01-15 10:32:01 INFO User accessed dashboard",
    "2024-01-15 10:35:22 WARNING High memory usage detected",
    "2024-01-15 10:36:45 ERROR Connection timeout",
    "2024-01-15 10:38:01 INFO User logged out"
]

print("🔍 Log Analysis Results:")

# Count log levels
log_levels = {}
errors = []
warnings = []

for entry in log_entries:
    parts = entry.split()
    timestamp = f"{parts[0]} {parts[1]}"
    level = parts[2]
    message = ' '.join(parts[3:])
    
    # Count levels
    log_levels[level] = log_levels.get(level, 0) + 1
    
    # Collect errors and warnings
    if level == "ERROR":
        errors.append(f"{timestamp}: {message}")
    elif level == "WARNING":
        warnings.append(f"{timestamp}: {message}")

print("Log level summary:")
for level, count in sorted(log_levels.items()):
    print(f"  {level}: {count}")

if errors:
    print(f"\n❌ {len(errors)} Error(s) found:")
    for error in errors:
        print(f"  {error}")

if warnings:  
    print(f"\n⚠️  {len(warnings)} Warning(s) found:")
    for warning in warnings:
        print(f"  {warning}")

# ----------

""" STRING METHODS CHEAT SHEET """
print("\n=== STRING METHODS REFERENCE ===")

sample_text = "  Hello, World! Welcome to Python Programming.  "
print(f"Original: '{sample_text}'")

print("\n🔧 Cleaning Methods:")
print(f"strip():     '{sample_text.strip()}'")
print(f"lower():     '{sample_text.lower()}'")
print(f"upper():     '{sample_text.upper()}'")
print(f"title():     '{sample_text.title()}'")
print(f"capitalize(): '{sample_text.capitalize()}'")

print("\n🔍 Search Methods:")
print(f"find('World'):    {sample_text.find('World')}")
print(f"count('o'):       {sample_text.count('o')}")
print(f"startswith('  '): {sample_text.startswith('  ')}")
print(f"endswith('.  '):  {sample_text.endswith('.  ')}")

print("\n✂️ Split/Join Methods:")
words = sample_text.strip().split()
print(f"split():     {words}")
print(f"join():      {'|'.join(words)}")

print("\n🔄 Replace Methods:")
print(f"replace('Hello', 'Hi'): '{sample_text.replace('Hello', 'Hi')}'")

print("\n✅ Check Methods:")
print(f"isdigit():   {'123'.isdigit()}")
print(f"isalpha():   {'ABC'.isalpha()}")  
print(f"isalnum():   {'ABC123'.isalnum()}")
print(f"isspace():   {'   '.isspace()}")

# ----------