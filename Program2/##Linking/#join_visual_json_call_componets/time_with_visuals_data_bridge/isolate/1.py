import os
import json

def create_json(folder_path):
    animations = []

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Group files by their prefixes
    grouped_files = {}
    for file in files:
        # Split the file name into parts using underscores
        parts = file.split('_')

        # Check if the file name has at least three parts
        if len(parts) >= 3:
            prefix = f"{parts[0]}_{parts[1]}"
            if prefix not in grouped_files:
                grouped_files[prefix] = []
            grouped_files[prefix].append(file)

    # Iterate over grouped files
    for prefix, files in grouped_files.items():
        delay_text_duration = 0
        text_display_duration = 0

        # Sort files to make sure part1 comes before part2
        sorted_files = sorted(files)

        for file in sorted_files:
            file_path = os.path.join(folder_path, file)
            value = read_value(file_path)

            if "part1" in file:
                delay_text_duration = value
            elif "part2" in file:
                text_display_duration += value

        animation = {
            "delay_text_duration": delay_text_duration,
            "text_display_duration": text_display_duration
        }
        animations.append(animation)

    # Create the final JSON structure
    json_data = {"animations": animations}

    # Replace the output file path with your desired location
    output_file_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\time_with_visuals_data_bridge\out\output.json"

    # Write the JSON to a file
    with open(output_file_path, "w") as json_file:
        json.dump(json_data, json_file, indent=2)

def read_value(file_path):
    # Read the numerical value from the file
    with open(file_path, "r") as file:
        value = int(file.read().strip())
    return value

# Replace 'your_folder_path' with the actual path to your folder containing the text files
folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Timeline\Output'
create_json(folder_path)
