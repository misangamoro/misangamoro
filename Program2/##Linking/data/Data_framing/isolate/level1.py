import re
import os

# Function to create text files for each conversation based on the first line
def create_text_files(file_path, output_folder):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_conversation_lines = []

    for line in lines:
        if line.strip():  # Skip empty lines
            current_conversation_lines.append(line.strip())
        elif current_conversation_lines:
            first_line = current_conversation_lines[0]
            sanitized_name = re.sub(r'\W+', '', first_line)[:10]  # Limit to the first 10 characters and remove non-alphanumeric characters
            file_name = os.path.join(output_folder, f"{sanitized_name}.txt")
            with open(file_name, 'w') as output_file:
                output_file.write('\n'.join(current_conversation_lines))
            current_conversation_lines = []

    if current_conversation_lines:
        first_line = current_conversation_lines[0]
        sanitized_name = re.sub(r'\W+', '', first_line)[:10]  # Limit to the first 10 characters and remove non-alphanumeric characters
        file_name = os.path.join(output_folder, f"{sanitized_name}.txt")
        with open(file_name, 'w') as output_file:
            output_file.write('\n'.join(current_conversation_lines))



# Replace 'your_file_path.txt' with the actual path to your text file
# Replace 'your_output_folder' with the desired output folder location
create_text_files(r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\input.txt', r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\Data_framing\out')
