def find_and_copy_line(input_file_path, output_file_path, target_word):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            if target_word in line:
                output_file.write(line)

# Replace 'your_input_file.txt' with the actual input file path
input_file_path = 'your_input_file.txt'

# Replace 'your_output_file.txt' with the desired output file path
output_file_path = 'your_output_file.txt'

# Replace 'your_target_word' with the specific word you want to find
target_word = 'your_target_word'

# Find and copy lines containing the target word
find_and_copy_line(input_file_path, output_file_path, target_word)

print(f"Lines containing '{target_word}' have been copied to '{output_file_path}'.")
