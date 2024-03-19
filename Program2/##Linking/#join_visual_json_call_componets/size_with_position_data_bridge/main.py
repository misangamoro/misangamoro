import json

# Replace 'your_input_file.json' and 'your_output_file.json' with the actual file paths
input_file_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Graphics_control\path_tracing_text\out\output.json'
output_file_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\size_with_position_data_bridge\out\file.json'

# Read the JSON file
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Organize the data as specified
organized_animations = []
for i in range(0, len(data['animations']), 2):
    animation = {
        'font_size1': data['animations'][i]['font_size1'],
        'font_size2': data['animations'][i + 1]['font_size2'],
        'text1_position': data['animations'][i]['text1_position'],
        'text2_position': data['animations'][i + 1]['text2_position']
    }
    organized_animations.append(animation)

# Create a new dictionary with the organized data
organized_data = {'animations': organized_animations}

# Export the modified data to a new JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(organized_data, output_file, indent=2)

print(f"File '{output_file_path}' has been created with organized data.")
