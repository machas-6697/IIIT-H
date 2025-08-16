def check_and_remove_empty_lines(file_path):
    # Open the file with the correct encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    empty_lines = [index + 1 for index, line in enumerate(lines) if line.strip() == '']
    
    if empty_lines:
        print(f"Empty lines found at line numbers: {empty_lines}")
        
        # Filter out empty lines
        non_empty_lines = [line for line in lines if line.strip() != '']
        
        # Write back the non-empty lines to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(non_empty_lines)
        
        print("All empty lines removed.")
    else:
        print("No empty lines found.")

# Replace 'your_file.txt' with the path to your actual text file
check_and_remove_empty_lines('path/directory/t-en.txt')
