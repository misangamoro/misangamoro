import os
import json

def count_alphabets_and_spaces(text):
    return sum(c.isalpha() or c.isspace() for c in text)

def process_folder(input_folder, output_folder):
    data = {"text_duration": []}

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                text_content = file.read()
                alphabet_count = count_alphabets_and_spaces(text_content)
                # Remove ".txt" from the filename
                entry_key = os.path.splitext(filename)[0]
                entry = {entry_key: alphabet_count}
                data["text_duration"].append(entry)

    json_output_path = os.path.join(output_folder, "input.json")
    with open(json_output_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    # Manually set input and output folders
    input_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\#finallizing_data_for_timeline\out"
    output_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Graphics_control\path_tracing_text\data_on_words"
    
    process_folder(input_folder, output_folder)
    print("JSON file created successfully.")
