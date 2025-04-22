# Python Examples

This directory contains examples of Python programming concepts. Files have been organized by topic to make learning easier.

## Running Python Code

Python is an interpreted language.

- Open the Python interpreter:  
  `$ python3`

- Run a Python file:  
  `$ python3 filename.py`

- Execute a Python file directly (if it has the shebang line and executable permission):  
  `$ ./filename.py`

  Note: This requires the file to have a shebang line (`#!/usr/bin/python3`) and executable permission (`chmod +x filename.py`).

## Directory Contents

### Core Concepts
- **basic_data_types.py** - Variables, strings, and basic type operations
- **data_structures.py** - Lists, tuples, dictionaries, and sets
- **flow_control.py** - Conditional statements and control flow
- **functions.py** - Function definitions and usage examples
- **functions_tester.py** - Examples of using the functions defined in functions.py
- **logical_operators.py** - Boolean logic and operators

### Advanced Concepts
- **classes.py** - Object-oriented programming with classes and inheritance
- **functional_programming.py** - Functional programming paradigms
- **module_examples.py** - Examples of common Python modules (os, sys, re)
- **subprocess_examples.py** - Examples of running external commands using the subprocess module
- **working_with_files.py** - File operations (reading, writing, etc.)
- **working_with_url.py** - Working with URL requests
- **regex.py** - Regular expression examples

### Mathematics and Time
- **math_operations.py** - Mathematical operations and math module examples
- **time_operations.py** - Date, time, and calendar operations

### Testing
- **test_examples.py** - Examples of testing in Python
- **test_file.py** - Additional testing examples

## Development Environment

### Virtual Environments
Python has tools to set up isolated environments with specific Python versions/packages:

```bash
sudo apt-get install python3-virtualenv
python3 -m venv my_env
source my_env/bin/activate
# When finished
deactivate
```

### Package Management with pip
Pip is Python's package manager:

```bash
sudo apt-get install python3-pip
pip3 search <package-name>
pip3 install <package-name>
```

### Requirements File
To install dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```