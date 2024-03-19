import os

def read_numeric_value(file_path):
    with open(file_path, 'r') as file:
        return float(file.read().strip())

def write_calculated_values(output_file, data_values):
    with open(output_file, 'w') as file:
        for i, value in enumerate(data_values, start=1):
            file.write(f'data{i}: {value}\n')

def process_text_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            numeric_value = read_numeric_value(file_path)

            parts = filename.split('_')
            base_name = f"{parts[0]}_{parts[1]}"

            output_file = os.path.join(output_folder, f"{base_name}.txt")

            if not os.path.exists(output_file):
                data_values = [0.0, 0.5]
            else:
                with open(output_file, 'r') as existing_file:
                    existing_data = existing_file.readlines()
                    data_values = [float(line.split(': ')[1].strip()) for line in existing_data]

            data_values.append(data_values[-1] + numeric_value)

            write_calculated_values(output_file, data_values)

# Example usage:
input_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Timeline\Output"
output_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\data_level\out"

process_text_files(input_folder, output_folder)


