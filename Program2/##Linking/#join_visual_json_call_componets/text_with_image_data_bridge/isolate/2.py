import os
import re
import json

def extract_number_from_filename(file_name):
    # Extract the numeric part from the file name
    match = re.search(r'\d+', file_name)
    return int(match.group()) if match else 0

def process_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Check if there are at least two lines in the file
        if len(lines) >= 2:
            text1 = lines[0].strip()
            text2 = lines[1].strip()
        elif len(lines) == 1:
            # If there is only one line, set it to "text1" and set "text2" to an empty string
            text1 = lines[0].strip()
            text2 = ""
        else:
            # Handle the case where there are no lines in the file
            print(f"Warning: No lines in {file_path}. Skipping this file.")
            return None, None
        
        return text1, text2

def generate_json(folder_path):
    animations = []
    
    # List the files and sort them based on the numeric part of the file name
    files = sorted(os.listdir(folder_path), key=extract_number_from_filename)
    
    for file_name in files:
        if file_name.endswith(".txt"):
            image_name = file_name.replace(".txt", "").split("_")[1]
            image_path = os.path.join(folder_path, "Visuals Production\\Assest\\Image\\Charectes", f"{image_name}.png")
            
            text1, text2 = process_text_file(os.path.join(folder_path, file_name))
            
            if text1 is not None and text2 is not None:
                animation_data = {
                    "image_path": image_path,
                    "text1": text1,
                    "text2": text2
                }
                animations.append(animation_data)
    
    json_data = {"animations": animations}
    return json_data

def save_json(json_data, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

def main():
    # Hardcoded folder path and output path
    folder_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\Data_framing\out2"
    output_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\text_with_image_data_bridge\out\file.json"

    json_data = generate_json(folder_path)
    save_json(json_data, output_path)

if __name__ == "__main__":
    main()
