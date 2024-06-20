import re
import sys
import os

def check_syntax(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    errors = []
    for line_number, line in enumerate(lines, 1):
        stack = []
        in_quotes = False
        for char in line.strip():
            if char == '"':
                in_quotes = not in_quotes
            elif char == '{':
                stack.append(char)
            elif char == '}':
                if not stack or stack[-1] != '{':
                    errors.append(f"Error: ❌ Unmatched closing brace in {file_path} on line {line_number}")
                    break
                stack.pop()
            elif char == '[':
                stack.append(char)
            elif char == ']':
                if not stack or stack[-1] != '[':
                    errors.append(f"Error: ❌ Unmatched closing bracket in {file_path} on line {line_number}")
                    break
                stack.pop()
        
        if stack:
            unmatched = stack[-1]
            if unmatched == '{':
                errors.append(f"Error: ❌ Unmatched opening brace in {file_path} on line {line_number}")
            elif unmatched == '[':
                errors.append(f"Error: ❌ Unmatched opening bracket in {file_path} on line {line_number}")
        
        if in_quotes:
            errors.append(f"Error: ❌ Unmatched quote in {file_path} on line {line_number}")

    return errors

def check_directory(directory):
    all_errors = []
    valid_files_count = 0
    invalid_files_count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                errors = check_syntax(file_path)
                if errors:
                    all_errors.extend(errors)
                    invalid_files_count += 1
                else:
                    valid_files_count += 1
    
    return all_errors, valid_files_count, invalid_files_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resource_validator.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    errors, valid_files_count, invalid_files_count = check_directory(directory_path)
    
    if errors:
        for error in errors:
            print(error)
        print(f"\nError: ❌ {invalid_files_count} files have syntax errors.")
    else:
        print("✅ No syntax errors found.")
    
    print(f"✅ {valid_files_count} files are valid.")
    sys.exit(1 if errors else 0)
