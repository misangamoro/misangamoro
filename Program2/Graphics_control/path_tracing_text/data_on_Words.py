import os
import json
import re

def process_folder(input_folder, output_folder):
    data = {"text_duration": []}

    filenames = sorted(os.listdir(input_folder), key=lambda x: [int(i) if i.isdigit() else i for i in re.split('(\d+)', x)])

    for filename in filenames:
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                # Read the numerical value from the file
                numerical_value = int(file.read().strip())
                
                # Remove ".txt" from the filename
                entry_key = os.path.splitext(filename)[0]
                entry = {entry_key: numerical_value}
                data["text_duration"].append(entry)

    json_output_path = os.path.join(output_folder, "input.json")
    with open(json_output_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    input_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\number_of_aphabet_in_text_part1,2\no_of_words"
    output_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Graphics_control\path_tracing_text\data_on_words"
    
    process_folder(input_folder, output_folder)
    print("JSON file created successfully.")
