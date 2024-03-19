import os

def get_next_file_number(number_file_folder):
    # Get the current file number from the last run
    number_file_path = os.path.join(number_file_folder, 'current_file_number.txt')
    
    if os.path.exists(number_file_path):
        with open(number_file_path, 'r') as number_file:
            current_file_number = int(number_file.read().strip())
    else:
        current_file_number = 1

    # Update the current file number for the next run
    with open(number_file_path, 'w') as number_file:
        next_file_number = (current_file_number % 3) + 1
        number_file.write(str(next_file_number))

    return current_file_number

def update_output_file(input_folder, output_folder, current_file_number):
    # Read the content of the current file and write it to output.txt
    input_file_path = os.path.join(input_folder, f'{current_file_number}.txt')
    output_file_path = os.path.join(output_folder, 'input.txt')

    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

    with open(output_file_path, 'w') as output_file:
        output_file.write(content)

    print(f"Output file 'output.txt' has been updated with data from '{current_file_number}.txt'.")

# Example usage
input_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Temp_data\out'
output_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Input_reading\out'
number_file_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Input_reading\const'

current_file_number = get_next_file_number(number_file_folder_path)
update_output_file(input_folder_path, output_folder_path, current_file_number)
