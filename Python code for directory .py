#Write a code to look for all files in a directory in Python 

import os

def list_files(directory):
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

# Replace 'your_directory_path' with the actual path of the directory you want to check
directory_path = 'your_directory_path'

# List all files in the specified directory
files_in_directory = list_files(directory_path)

# Print the list of files
for file in files_in_directory:
    print(file)
