import os

def search_file(starting_directory, target_file):
    for root, dirs, files in os.walk(starting_directory):
        if target_file in files:
            return os.path.join(root, target_file)

# Replace 'your_directory_path' with the actual path of the directory you want to search
directory_path = 'your_directory_path'

# Replace 'your_target_file' with the name of the file you are looking for
target_file_name = 'your_target_file'

# Search for the target file
result = search_file(directory_path, target_file_name)

if result:
    print(f"Found the file: {result}")
else:
    print(f"The file '{target_file_name}' was not found in the specified directory and its subdirectories.")
