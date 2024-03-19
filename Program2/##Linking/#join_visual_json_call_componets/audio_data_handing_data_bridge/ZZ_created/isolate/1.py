import os

def process_input(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:
        lines = infile.readlines()

    open_values = []
    text_values = []
    close_values = []

    for line in lines:
        if line.startswith('open:'):
            # Remove the trailing comma and convert to float
            value = line.split(':')[1].strip().rstrip(',')
            open_values.append(float(value))
        elif line.startswith('text:'):
            try:
                # Remove the trailing comma and convert to float
                values = line.split(':')[1].strip().rstrip(',').split(',')
                text_values.extend(map(float, values))
            except ValueError:
                print(f"Error converting to float in line: {line}")
        elif line.startswith('close:'):
            # Remove the trailing comma and convert to float
            value = line.split(':')[1].strip().rstrip(',')
            close_values.append(float(value))

    total_value = sum(open_values + text_values + close_values)

    output_dir = os.path.dirname(output_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file_path, 'w') as outfile:
        outfile.write(f'open: {", ".join(map(str, open_values))},\n')
        outfile.write(f'text: {", ".join(map(str, text_values))},\n')
        outfile.write(f'close: {", ".join(map(str, close_values))},\n')
        outfile.write(f'total: {total_value}\n')

    return open_values, text_values, close_values, total_value


# Example usage:
input_file_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\z_created\out\output.txt'  # Replace with the actual input file path
output_file_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\ZZ_created\out\output.txt'  # Replace with the desired output file path

open_values, text_values, close_values, total_value = process_input(input_file_path, output_file_path)

print("Open values:", open_values)
print("Text values:", text_values)
print("Close values:", close_values)
print("Total value:", total_value)
