""" 2.0.0_Python_QUICK_REFERENCE.py """

# =============================================================================
# PYTHON INTERPRETER - COMPREHENSIVE QUICK REFERENCE GUIDE
# =============================================================================
# Version: 2.0.0 | Educational Excellence Target: 9.5/10
# Purpose: Complete cheat sheet for Python Interpreter concepts and usage
# Target: Review sessions, exam prep, coding reference, and professional use
# =============================================================================

"""
QUICK NAVIGATION INDEX:
├── 1. INTERPRETER BASICS
├── 2. INTERACTIVE MODE
├── 3. PROMPT TYPES
├── 4. EXECUTION MODES
├── 5. COMMAND LINE USAGE
├── 6. PRACTICAL EXAMPLES
├── 7. TROUBLESHOOTING
├── 8. PERFORMANCE TIPS
├── 9. COMMON PATTERNS
└── 10. PROFESSIONAL PRACTICES
"""

# =============================================================================
# 1. INTERPRETER BASICS - CORE CONCEPTS
# =============================================================================

"""
WHAT IS THE PYTHON INTERPRETER?
• Program that reads and executes Python code line by line
• Converts Python source code into bytecode, then executes it
• Available in interactive mode (REPL) and script execution mode
• Built-in error handling and debugging capabilities

KEY CHARACTERISTICS:
✓ Dynamic typing - types determined at runtime
✓ Interactive execution - immediate feedback
✓ Cross-platform compatibility
✓ Extensible with C/C++ modules
✓ Garbage collection for memory management
"""

# INTERPRETER COMPONENTS
interpreter_components = {
    "lexer": "Tokenizes source code into tokens",
    "parser": "Builds Abstract Syntax Tree (AST)",
    "compiler": "Converts AST to bytecode",
    "interpreter_loop": "Executes bytecode instructions",
    "memory_manager": "Handles object allocation/deallocation"
}

# =============================================================================
# 2. INTERACTIVE MODE (REPL) - READ-EVAL-PRINT LOOP
# =============================================================================

"""
REPL WORKFLOW:
1. READ: Accept user input
2. EVAL: Evaluate the expression/statement
3. PRINT: Display the result
4. LOOP: Return to step 1

ACTIVATION METHODS:
• Command line: python, python3, py
• IDEs: Built-in interactive consoles
• Jupyter notebooks: Cell-based execution
• Online interpreters: repl.it, Python.org shell
"""

# Interactive Mode Examples
interactive_examples = {
    "basic_calculation": ">>> 2 + 2\n4",
    "variable_assignment": ">>> x = 10\n>>> x\n10",
    "function_definition": ">>> def greet(name):\n...     return f'Hello, {name}!'\n...\n>>> greet('World')\n'Hello, World!'",
    "import_module": ">>> import math\n>>> math.pi\n3.141592653589793"
}

# =============================================================================
# 3. PROMPT TYPES - VISUAL INDICATORS
# =============================================================================

"""
PRIMARY PROMPT (>>>):
• Indicates ready for new statement
• Appears at start of interactive session
• Used for top-level expressions/statements
• Standard input prompt for complete statements

SECONDARY PROMPT (...):
• Continuation of multi-line statements
• Appears when statement is incomplete
• Used for indented blocks (if, for, while, def, class)
• Indicates interpreter waiting for completion
"""

# Prompt Examples with Detailed Explanations
prompt_examples = {
    "primary_simple": {
        "code": ">>> print('Hello, World!')",
        "output": "Hello, World!",
        "explanation": "Single line statement execution"
    },
    
    "secondary_function": {
        "code": """>>> def calculate_area(radius):
...     import math
...     return math.pi * radius ** 2
...
>>> calculate_area(5)""",
        "output": "78.53981633974483",
        "explanation": "Multi-line function definition with secondary prompts"
    },
    
    "secondary_conditional": {
        "code": """>>> x = 10
>>> if x > 5:
...     print("x is greater than 5")
...     print(f"x value is: {x}")
... else:
...     print("x is 5 or less")
...""",
        "output": "x is greater than 5\nx value is: 10",
        "explanation": "Conditional block with multiple secondary prompts"
    },
    
    "secondary_loop": {
        "code": """>>> for i in range(3):
...     print(f"Iteration: {i}")
...     if i == 1:
...         print("  Middle iteration")
...""",
        "output": "Iteration: 0\nIteration: 1\n  Middle iteration\nIteration: 2",
        "explanation": "Loop with nested conditional and secondary prompts"
    }
}

# =============================================================================
# 4. EXECUTION MODES - DIFFERENT WAYS TO RUN PYTHON
# =============================================================================

"""
EXECUTION MODES COMPARISON:
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ Mode            │ Use Case        │ Pros            │ Cons            │
├─────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ Interactive     │ Testing/Learning│ Immediate       │ No persistence  │
│ Script Mode     │ Production Code │ Reusable        │ No interaction  │
│ Module Import   │ Code Reuse      │ Organized       │ Memory overhead │
│ Jupyter/IPython │ Data Science    │ Rich output     │ Tool dependency │
│ Debugger Mode   │ Troubleshooting │ Step-by-step    │ Slower execution│
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
"""

execution_modes = {
    "interactive": {
        "command": "python",
        "description": "REPL for immediate code execution",
        "best_for": ["Learning", "Testing", "Quick calculations", "Prototyping"]
    },
    
    "script": {
        "command": "python script.py",
        "description": "Execute Python file from command line",
        "best_for": ["Production code", "Automation", "Batch processing"]
    },
    
    "module": {
        "command": "python -m module_name",
        "description": "Run module as script",
        "best_for": ["Running packages", "Tool execution", "Standard library modules"]
    },
    
    "one_liner": {
        "command": "python -c 'print(\"Hello\")'",
        "description": "Execute single command",
        "best_for": ["Shell scripting", "Quick tasks", "System administration"]
    }
}

# =============================================================================
# 5. COMMAND LINE USAGE - PRACTICAL REFERENCE
# =============================================================================

"""
ESSENTIAL COMMAND LINE OPTIONS:
-c cmd     : Execute command string
-m module  : Run module as script
-i         : Interactive mode after script
-u         : Unbuffered stdout/stderr
-v         : Verbose import tracking
-W arg     : Warning control
-O         : Optimize bytecode
-B         : Don't write .pyc files
-q         : Quiet startup (no version info)
-h         : Help message
--version  : Python version information
"""

# Command Line Examples
cli_examples = {
    "version_check": {
        "command": "python --version",
        "output": "Python 3.11.0",
        "purpose": "Verify Python installation and version"
    },
    
    "direct_execution": {
        "command": "python -c \"import sys; print(sys.version)\"",
        "output": "3.11.0 | packaged by conda-forge",
        "purpose": "Execute Python code directly from command line"
    },
    
    "module_execution": {
        "command": "python -m pip list",
        "output": "Package list display",
        "purpose": "Run Python module as script"
    },
    
    "interactive_after_script": {
        "command": "python -i script.py",
        "output": "Script execution + interactive shell",
        "purpose": "Debug script then continue interactively"
    }
}

# =============================================================================
# 6. PRACTICAL EXAMPLES - REAL-WORLD USAGE
# =============================================================================

"""
INTERACTIVE CALCULATOR
Building a practical calculator using interpreter features
"""

def interactive_calculator_demo():
    """
    Demonstration of Python interpreter as powerful calculator
    Shows mathematical operations, function usage, and variable storage
    """
    
    # Basic arithmetic operations
    examples = [
        ">>> 2 + 3 * 4",           # Order of operations
        ">>> (2 + 3) * 4",         # Parentheses precedence
        ">>> 17 / 3",              # Float division
        ">>> 17 // 3",             # Integer division
        ">>> 17 % 3",              # Modulo operation
        ">>> 2 ** 10",             # Exponentiation
        
        # Advanced mathematical functions
        ">>> import math",
        ">>> math.sqrt(144)",       # Square root
        ">>> math.sin(math.pi/2)",  # Trigonometric function
        ">>> math.log(100, 10)",    # Logarithm with base
        
        # Working with variables
        ">>> radius = 5",
        ">>> area = math.pi * radius**2",
        ">>> print(f'Circle area: {area:.2f}')",
        
        # Complex calculations
        ">>> numbers = [1, 2, 3, 4, 5]",
        ">>> sum(numbers)",
        ">>> sum(x**2 for x in numbers)",  # Sum of squares
        
        # String operations
        ">>> name = 'Python'",
        ">>> f'{name} has {len(name)} characters'",
        ">>> name.upper().center(20, '=')",
        
        # Data structure operations
        ">>> data = {'a': 1, 'b': 2, 'c': 3}",
        ">>> list(data.keys())",
        ">>> [v*2 for v in data.values()]"
    ]
    
    return examples

"""
DEBUGGING AND EXPLORATION
Using interpreter for code investigation and debugging
"""

def debugging_examples():
    """
    Interactive debugging and exploration techniques
    """
    
    exploration_commands = {
        "object_inspection": [
            ">>> type(42)",                    # Check object type
            ">>> isinstance(42, int)",         # Type checking
            ">>> dir(42)",                     # Available methods
            ">>> help(int)",                   # Documentation
            ">>> int.__doc__",                 # Docstring access
        ],
        
        "variable_exploration": [
            ">>> locals()",                    # Local namespace
            ">>> globals()",                   # Global namespace
            ">>> vars()",                      # Variable dictionary
            ">>> id(variable_name)",           # Object identity
        ],
        
        "module_investigation": [
            ">>> import sys",
            ">>> sys.path",                    # Module search path
            ">>> sys.modules.keys()",          # Loaded modules
            ">>> import os; os.__file__",      # Module file location
        ],
        
        "error_handling": [
            ">>> try:",
            "...     1/0",
            "... except ZeroDivisionError as e:",
            "...     print(f'Error: {e}')",
            "...     print(f'Type: {type(e)}')"
        ]
    }
    
    return exploration_commands

# =============================================================================
# 7. TROUBLESHOOTING - COMMON ISSUES AND SOLUTIONS
# =============================================================================

"""
COMMON INTERPRETER ISSUES AND SOLUTIONS
"""

troubleshooting_guide = {
    "secondary_prompt_stuck": {
        "problem": "Stuck in secondary prompt (...), can't get back to >>>",
        "symptoms": ["Continuous ... prompts", "Commands not executing"],
        "solutions": [
            "Press Ctrl+C to interrupt",
            "Add missing closing brackets/parentheses",
            "Complete the incomplete statement",
            "Add empty line to end multi-line blocks"
        ],
        "prevention": "Always close brackets and complete statements"
    },
    
    "import_errors": {
        "problem": "Module not found or import errors",
        "symptoms": ["ModuleNotFoundError", "ImportError"],
        "solutions": [
            "Check module installation: pip list",
            "Verify Python path: sys.path",
            "Install missing modules: pip install module_name",
            "Check virtual environment activation"
        ],
        "prevention": "Use virtual environments and requirements.txt"
    },
    
    "encoding_issues": {
        "problem": "Unicode or encoding errors",
        "symptoms": ["UnicodeDecodeError", "SyntaxError with special characters"],
        "solutions": [
            "Add # -*- coding: utf-8 -*- to file header",
            "Use python -u for unbuffered output",
            "Set environment variable PYTHONIOENCODING=utf-8"
        ],
        "prevention": "Always use UTF-8 encoding for Python files"
    },
    
    "performance_issues": {
        "problem": "Slow interpreter response or high memory usage",
        "symptoms": ["Delayed responses", "Memory warnings"],
        "solutions": [
            "Clear variables: del variable_name",
            "Restart interpreter session",
            "Use garbage collection: import gc; gc.collect()",
            "Profile code: python -m cProfile script.py"
        ],
        "prevention": "Clean up large objects and use generators"
    }
}

# =============================================================================
# 8. PERFORMANCE TIPS - OPTIMIZATION STRATEGIES
# =============================================================================

"""
INTERPRETER PERFORMANCE OPTIMIZATION
"""

performance_tips = {
    "startup_optimization": {
        "description": "Reduce interpreter startup time",
        "techniques": [
            "Use python -O for optimized bytecode",
            "Set PYTHONDONTWRITEBYTECODE=1 to skip .pyc files",
            "Minimize imports in frequently run scripts",
            "Use python -q for quiet startup"
        ]
    },
    
    "memory_management": {
        "description": "Efficient memory usage in interactive mode",
        "techniques": [
            "Delete large objects: del large_list",
            "Use generators instead of lists when possible",
            "Clear variables between tests: globals().clear()",
            "Monitor memory: import psutil; psutil.Process().memory_info()"
        ]
    },
    
    "interactive_efficiency": {
        "description": "Faster interactive development",
        "techniques": [
            "Use IPython for enhanced interactive experience",
            "Enable tab completion and history",
            "Use %timeit magic command for performance testing",
            "Leverage %run magic command for script execution"
        ]
    }
}

# =============================================================================
# 9. COMMON PATTERNS - BEST PRACTICES
# =============================================================================

"""
PROFESSIONAL INTERPRETER USAGE PATTERNS
"""

# Pattern 1: Safe Interactive Testing
def safe_testing_pattern():
    """
    Pattern for safely testing code in interactive mode
    """
    pattern = """
    # Always test in isolated namespace
    >>> def test_function():
    ...     # Your test code here
    ...     try:
    ...         # Risky operation
    ...         result = potentially_dangerous_operation()
    ...         return result
    ...     except Exception as e:
    ...         print(f"Error caught: {e}")
    ...         return None
    ...
    >>> test_function()
    """
    return pattern

# Pattern 2: Development Workflow
def development_workflow():
    """
    Efficient development workflow using interpreter
    """
    workflow = {
        "step_1": "Start with interactive mode for experimentation",
        "step_2": "Test small code fragments",
        "step_3": "Gradually build larger functions",
        "step_4": "Copy working code to script file",
        "step_5": "Test script with python -i script.py",
        "step_6": "Refactor and optimize in script mode"
    }
    return workflow

# Pattern 3: Data Exploration
def data_exploration_pattern():
    """
    Pattern for data science and analysis
    """
    pattern = """
    >>> import pandas as pd
    >>> import numpy as np
    
    # Load and examine data
    >>> data = pd.read_csv('data.csv')
    >>> data.head()
    >>> data.info()
    >>> data.describe()
    
    # Interactive exploration
    >>> data.columns
    >>> data['column_name'].value_counts()
    >>> data.plot()  # Quick visualization
    
    # Iterative analysis
    >>> for column in data.columns:
    ...     print(f"{column}: {data[column].dtype}")
    """
    return pattern

# =============================================================================
# 10. PROFESSIONAL PRACTICES - INDUSTRY STANDARDS
# =============================================================================

"""
INDUSTRY BEST PRACTICES FOR PYTHON INTERPRETER USAGE
"""

professional_practices = {
    "development_environment": {
        "description": "Setting up professional development environment",
        "practices": [
            "Use virtual environments (venv, conda)",
            "Install IPython or Jupyter for enhanced REPL",
            "Configure proper IDE integration",
            "Set up version control integration",
            "Use linting tools (pylint, flake8)",
            "Configure debugging tools (pdb, debugger)"
        ]
    },
    
    "code_quality": {
        "description": "Maintaining code quality in interactive development",
        "practices": [
            "Follow PEP 8 style guidelines",
            "Write docstrings for functions",
            "Use type hints where appropriate",
            "Test code thoroughly before moving to production",
            "Document interactive sessions for reproducibility"
        ]
    },
    
    "security_considerations": {
        "description": "Security best practices",
        "practices": [
            "Never execute untrusted code in interpreter",
            "Be careful with eval() and exec() functions",
            "Validate input data thoroughly",
            "Use virtual environments to isolate dependencies",
            "Keep Python and packages updated"
        ]
    },
    
    "collaboration": {
        "description": "Team development practices",
        "practices": [
            "Share Jupyter notebooks for data science work",
            "Use version control for interactive notebooks",
            "Document interpreter sessions for knowledge sharing",
            "Establish team coding standards",
            "Use code review processes"
        ]
    }
}

# =============================================================================
# QUICK REFERENCE CHEAT SHEET
# =============================================================================

"""
PYTHON INTERPRETER CHEAT SHEET - MEMORIZE THESE!

PROMPT SYMBOLS:
>>> : Primary prompt (ready for new statement)
... : Secondary prompt (continuation)

ESSENTIAL COMMANDS:
exit()     : Exit interpreter
quit()     : Exit interpreter  
help()     : Interactive help
help(obj)  : Help for specific object
dir(obj)   : List object attributes
type(obj)  : Show object type
len(obj)   : Object length
str(obj)   : String representation
repr(obj)  : Official string representation

SPECIAL VARIABLES:
_          : Last expression result
__name__   : Module name
__file__   : Current file path
__doc__    : Documentation string

DEBUGGING:
import pdb; pdb.set_trace()  : Set breakpoint
python -m pdb script.py      : Run with debugger
python -i script.py          : Interactive after script

PERFORMANCE:
python -O script.py          : Optimized execution
python -m cProfile script.py : Profile performance
import timeit; timeit.timeit() : Time execution

QUICK MATH:
import math                  : Mathematical functions
import random               : Random numbers
import statistics           : Statistical functions
import decimal              : Precise decimal arithmetic
"""

# =============================================================================
# CROSS-REFERENCES TO OTHER FILES
# =============================================================================

cross_references = {
    "prerequisite_files": [
        "1.0.0_Python_HOW_TO_LUNCH.py - Basic Python setup and installation"
    ],
    
    "related_concepts": [
        "3.0.0_Python_QUICK_REFERENCE.py - General Python syntax reference",
        "4.0.0_Python_BUILT_IN_FUNCTION.py - Built-in functions reference"
    ],
    
    "advanced_topics": [
        "Virtual environments and package management",
        "IDE integration and debugging tools",
        "Performance profiling and optimization"
    ]
}

if __name__ == "__main__":
    print("Python Interpreter Quick Reference Guide")
    print("========================================")
    print("This comprehensive guide covers all aspects of Python interpreter usage.")
    print("Use this file for quick reference, exam preparation, and professional development.")
    print("\nFor interactive learning, copy and paste examples into Python interpreter.")
    print("For advanced usage, refer to cross-referenced files and documentation.")