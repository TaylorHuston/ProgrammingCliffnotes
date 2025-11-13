#!/usr/bin/python3

"""
This module demonstrates various uses of the Python subprocess module.
The subprocess module allows you to spawn new processes, connect to their
input/output/error pipes, and obtain their return codes.
"""

import subprocess
import sys
import os
from datetime import datetime

print("Python Subprocess Module Examples\n" + "="*30)

# Example 1: Basic command execution with run()
print("\n1. Basic Command Execution")
print("--------------------------")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(f"Command: ls -l")
print(f"Return code: {result.returncode}")
print(f"Command output (first 3 lines):")
output_lines = result.stdout.splitlines()
for line in output_lines[:3]:
    print(f"  {line}")
print(f"Total lines in output: {len(output_lines)}")

# Example 2: Error handling
print("\n2. Handling Command Errors")
print("-------------------------")
try:
    # Try to run a command that doesn't exist
    result = subprocess.run(["thiscommanddoesnotexist"],
                            capture_output=True, text=True)
    print(f"Return code: {result.returncode}")
except FileNotFoundError as e:
    print(f"Error occurred: {e}")

# Example 3: Shell=True for shell features (use with caution - security implications)
print("\n3. Using shell=True (with caution)")
print("--------------------------------")
result = subprocess.run("echo $HOME | wc -c", shell=True,
                        capture_output=True, text=True)
print(f"Command: echo $HOME | wc -c")
print(
    f"Output: {result.stdout.strip()} (characters in home path including newline)")

# Example 4: Passing environment variables
print("\n4. Using Environment Variables")
print("-----------------------------")
my_env = os.environ.copy()
my_env["CUSTOM_VAR"] = "Hello from subprocess"
result = subprocess.run(["echo", "$CUSTOM_VAR"],
                        env=my_env, capture_output=True, text=True)
print(f"Using env dict directly: {result.stdout}")

# This will work because shell=True enables shell expansion
result = subprocess.run("echo $CUSTOM_VAR", shell=True,
                        env=my_env, capture_output=True, text=True)
print(f"With shell=True: {result.stdout}")

# Example 5: Input and output redirection
print("\n5. Input/Output Redirection")
print("--------------------------")
# Provide input to a command
result = subprocess.run(
    ["wc", "-w"], input="Count these words", text=True, capture_output=True)
print(f"Word count: {result.stdout.strip()}")

# Example 6: Running background processes
print("\n6. Background Processes")
print("---------------------")
print("Starting a background process (sleep 1)...")
process = subprocess.Popen(["sleep", "1"])
print(f"Process ID: {process.pid}")
print("Continuing with other work while process runs...")
# Do other work here
print("Waiting for process to complete...")
return_code = process.wait()
print(f"Process completed with return code: {return_code}")

# Example 7: Capturing real-time output
print("\n7. Capturing Real-time Output")
print("---------------------------")
process = subprocess.Popen(
    ["for", "i", "in", "1", "2", "3", "4", "5", ";", "do",
        "echo", "Line $i", ";", "sleep", "0.2", ";", "done"],
    stdout=subprocess.PIPE,
    text=True,
    shell=True
)

print("Reading output in real-time:")
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(f"  {output.strip()}")

# Example 8: Using CompletedProcess features
print("\n8. Working with CompletedProcess")
print("-----------------------------")
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(f"args: {result.args}")
print(f"returncode: {result.returncode}")
print(f"stdout length: {len(result.stdout)} characters")
print(f"stderr length: {len(result.stderr)} characters")

# Example 9: Running multiple commands
print("\n9. Running Multiple Commands")
print("--------------------------")
commands = [
    ["echo", "Hello World"],
    ["date"],
    ["pwd"]
]

for cmd in commands:
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Command '{' '.join(cmd)}' output: {result.stdout.strip()}")

# Example 10: Combining with other Python features
print("\n10. Advanced Usage - Timing Commands")
print("---------------------------------")


def time_command(cmd):
    """Run a command and time its execution."""
    start = datetime.now()
    result = subprocess.run(cmd, capture_output=True, text=True)
    end = datetime.now()
    return {
        'command': ' '.join(cmd),
        'output': result.stdout.strip(),
        'time': (end - start).total_seconds()
    }


results = [
    time_command(["sleep", "0.1"]),
    time_command(["echo", "Fast command"]),
    time_command(["sleep", "0.2"])
]

# Sort results by execution time
sorted_results = sorted(results, key=lambda x: x['time'])

print("Commands sorted by execution time:")
for idx, r in enumerate(sorted_results, 1):
    print(f"{idx}. {r['command']} - {r['time']:.4f}s - Output: {r['output']}")

print("\nEnd of subprocess examples")
