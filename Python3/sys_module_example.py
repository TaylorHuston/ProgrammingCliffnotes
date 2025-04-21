#!/usr/bin/python3
# Examples of working with the sys module
import sys

def print_section(title):
    """Print a section title with decorative formatting"""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")

# System information
print_section("System Information")
print(f"Python version: {sys.version}")
print(f"Python version info: {sys.version_info}")
print(f"Python executable: {sys.executable}")
print(f"Platform: {sys.platform}")

# Command-line arguments
print_section("Command-line Arguments")
print(f"Script name: {sys.argv[0]}")
print(f"All arguments: {sys.argv}")
print("Arguments list:")
for i, arg in enumerate(sys.argv):
    print(f"  Argument {i}: {arg}")

# System path
print_section("System Path")
print("sys.path contains the search paths for modules:")
for i, path in enumerate(sys.path):
    print(f"  {i}: {path}")

# Standard I/O streams
print_section("Standard I/O Streams")
print("sys.stdin: Input stream (for reading input)")
print("sys.stdout: Output stream (for printing output)")
print("sys.stderr: Error stream (for error messages)")

# Writing to stdout and stderr
sys.stdout.write("This is written directly to stdout\n")
sys.stderr.write("This is written directly to stderr\n")

# Module management
print_section("Module Management")
print(f"Loaded modules: {len(sys.modules)} modules loaded")
print("Some key modules loaded:")
important_modules = ['os', 'sys', 'datetime', 'math', 'random']
for module in important_modules:
    if module in sys.modules:
        print(f"  {module} is loaded")
    else:
        print(f"  {module} is not loaded")

# Exit the program with a status code
def exit_example():
    print_section("Exit Example")
    print("The sys.exit() function allows you to exit the program with a status code")
    print("sys.exit(0) means successful termination")
    print("sys.exit(1) or other non-zero values indicate errors")
    print("Uncommenting the next line would terminate the program:")
    # sys.exit(0)

exit_example()

# Memory usage and management
print_section("Memory Usage")
print(f"Reference counts for 5: {sys.getrefcount(5)}")
x = 5
print(f"Reference counts for 5 after assignment: {sys.getrefcount(5)}")

# Get the size of an object in bytes
print(f"Size of an integer (5): {sys.getsizeof(5)} bytes")
print(f"Size of a string ('hello'): {sys.getsizeof('hello')} bytes")
print(f"Size of a list ([1,2,3]): {sys.getsizeof([1,2,3])} bytes")
print(f"Size of a dict({{1:2}}): {sys.getsizeof({1:2})} bytes")

# Interactive mode check
print_section("Interactive Mode")
if sys.flags.interactive:
    print("Running in interactive mode")
else:
    print("Running in script mode")

# Example of handling a deprecated feature
def using_deprecated_feature():
    if sys.version_info >= (3, 8):
        import warnings
        warnings.warn("This feature is deprecated", DeprecationWarning, stacklevel=2)

using_deprecated_feature()

# Recursion limit
print_section("Recursion Limit")
print(f"Current recursion limit: {sys.getrecursionlimit()}")
print("The recursion limit protects against infinite recursion crashes")
print("You can modify it (with caution) using sys.setrecursionlimit()")

print_section("Usage Example")
print("To run this script with command-line arguments:")
print(f"  python {sys.argv[0]} arg1 arg2 arg3")
print("Example output would then include these arguments in sys.argv")