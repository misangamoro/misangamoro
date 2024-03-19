import os

def count_and_create_text_file(input_folder, output_folder):
    # Ensure input and output folders exist
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    if not os.path.exists(output_folder):
        print(f"Error: Output folder '{output_folder}' does not exist.")
        return

    # Count text files in the input folder
    text_file_count = sum(1 for file in os.listdir(input_folder) if file.endswith('.txt'))

    # Create a text file in the output folder with the count as its content
    output_file_path = os.path.join(output_folder, 'count.txt')
    with open(output_file_path, 'w') as output_file:
        output_file.write(str(text_file_count))

    print(f"Number of text files in '{input_folder}': {text_file_count}")
    print(f"Count has been saved to '{output_file_path}'.")

# Example usage
input_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Temp_data\out'
output_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#No._of_rep\out'

count_and_create_text_file(input_folder_path, output_folder_path)
