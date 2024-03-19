import os
import json

def create_json(folder_path):
    animations = {}

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
                grouped_files[prefix] = {"part1": None, "part2": None}
            if "part1" in file:
                grouped_files[prefix]["part1"] = file
            elif "part2" in file:
                grouped_files[prefix]["part2"] = file

    # Iterate over grouped files
    for prefix, files in grouped_files.items():
        part1_path = os.path.join(folder_path, files["part1"])
        part2_path = os.path.join(folder_path, files["part2"])

        delay_text_duration = read_value(part1_path)
        text_display_duration = delay_text_duration + read_value(part2_path)

        animation = {
            "delay_text_duration": delay_text_duration,
            "text_display_duration": text_display_duration
        }
        animations[prefix] = animation

    # Create the final JSON structure
    json_data = {"animations": list(animations.values())}

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
