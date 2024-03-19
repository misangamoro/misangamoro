import os

def read_numeric_value(file_path):
    with open(file_path, 'r') as file:
        return float(file.read().strip())

def write_calculated_values(output_file, data_values):
    with open(output_file, 'w') as file:
        for i, value in enumerate(data_values, start=1):
            file.write(f'data{i}: {value}\n')

def process_text_files(input_folder, output_folder):
    # Get all text files in the input folder
    text_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".txt")]
    
    # Sort files based on their names
    text_files.sort()

    # Initialize data3_value and data4_value to 0.0
    data3_value = 0.0
    data4_value = 0.0

    for filename in text_files:
        file_path = os.path.join(input_folder, filename)
        numeric_value = read_numeric_value(file_path)

        parts = filename.split('_')
        base_name = f"{parts[0]}_{parts[1]}"

        output_file = os.path.join(output_folder, f"{base_name}.txt")

        if not os.path.exists(output_file):
            data_values = [0.5, 0.5, data3_value, data4_value]  # Initialize with constant values for data1, data2, data3, and data4
        else:
            with open(output_file, 'r') as existing_file:
                existing_data = existing_file.readlines()
                data_values = [float(line.split(': ')[1].strip()) for line in existing_data]

        # Update values for data3 and data4
        if "part1" in filename:
            data3_value = numeric_value
        elif "part2" in filename:
            data4_value = numeric_value

        # Update data_values with the new numeric_value
        data_values[:2] = [0.5, 0.5]  # data1 and data2 remain constant
        data_values[2] = data3_value
        data_values[3] = data4_value

        write_calculated_values(output_file, data_values[:4])  # Write only data1 to data4

# Example usage:
input_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Timeline\Output"
output_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\data_level\out"

process_text_files(input_folder, output_folder)
