#!/usr/bin/python3
# import os
import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# List all files and directories in the current directory
files_and_directories = os.listdir(current_directory)
print("Files and directories in the current directory:")
for item in files_and_directories:
    print(item)

# Create a new directory
new_directory = os.path.join(current_directory, "new_directory")
os.mkdir(new_directory)
print(f"Created new directory: {new_directory}")

# Change the current working directory to the new directory
os.chdir(new_directory)
print(f"Changed working directory to: {os.getcwd()}")

# More examples of os.path.join()
# Join multiple path components. this is the recommended way to construct paths for cross-platform compatibility, avoiding manual string concatenation.
data_dir = os.path.join(current_directory, "data", "processed")
print(f"Joined path: {data_dir}")

# Create a file path using os.path.join
config_file = os.path.join(current_directory, "config", "settings.json")
print(f"Config file path: {config_file}")

# Using os.path.join with a filename
log_file = os.path.join(current_directory, "logs", "app.log")
print(f"Log file path: {log_file}")

# Examples of os.path.isfile() and os.path.isdir()
print("\n--- Checking paths with os.path.isfile() and os.path.isdir() ---")

# Create a test file in the new directory
test_file_path = os.path.join(os.getcwd(), "test_file.txt")
with open(test_file_path, "w") as f:
    f.write("This is a test file")

# Check if paths exist and if they are files or directories
paths_to_check = [
    test_file_path,              # Should be a file
    new_directory,               # Should be a directory
    os.path.join(current_directory, "non_existent_file.txt"),  # Should not exist
    __file__,                    # Current script file
    os.path.dirname(__file__)    # Directory containing the script
]

for path in paths_to_check:
    print(f"\nChecking path: {path}")
    if os.path.exists(path):
        print(f"  Path exists: {os.path.exists(path)}")
        print(f"  Is file: {os.path.isfile(path)}")
        print(f"  Is directory: {os.path.isdir(path)}")
    else:
        print(f"  Path does not exist")

# Clean up the test file
os.remove(test_file_path)
print(f"\nRemoved test file: {test_file_path}")

# Move back to the original directory
os.chdir(current_directory)

# Remove the new directory
os.rmdir(new_directory)
print(f"Removed directory: {new_directory}")

# Tester module with additional os.path functions
def test_additional_os_path_functions():
    """Test additional os.path functions not already covered in the main script"""
    
    print("\n--- Additional os.path Functions Tester ---")
    
    # Create a temp file for testing
    test_file = "path_test_file.txt"
    with open(test_file, "w") as f:
        f.write("Test content")
    
    # Get the absolute path
    abs_path = os.path.abspath(test_file)
    print(f"1. os.path.abspath(): {abs_path}")
    
    # Get path components
    dirname = os.path.dirname(abs_path)
    basename = os.path.basename(abs_path)
    print(f"2. os.path.dirname(): {dirname}")
    print(f"3. os.path.basename(): {basename}")
    
    # Split extension
    root, ext = os.path.splitext(test_file)
    print(f"4. os.path.splitext(): root='{root}', extension='{ext}'")
    
    # Get file size and modification time
    size = os.path.getsize(test_file)
    mtime = os.path.getmtime(test_file)
    print(f"5. os.path.getsize(): {size} bytes")
    print(f"6. os.path.getmtime(): {mtime} (seconds since epoch)")
    
    # Normalize paths
    messy_path = os.path.join(".", "folder", "..", "folder", ".", test_file)
    norm_path = os.path.normpath(messy_path)
    print(f"7. os.path.normpath(): '{messy_path}' → '{norm_path}'")
    
    # Clean up
    os.remove(test_file)
    print(f"Removed test file: {test_file}")


# Only run the tester if this script is executed directly
if __name__ == "__main__":
    test_additional_os_path_functions()

