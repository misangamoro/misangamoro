import os

def remove_duplicate_names(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)
            
            with open(input_file_path, 'r') as input_file:
                data = input_file.read().strip().split(',')

            modified_data = []
            seen_names = set()

            for entry in data:
                if ':' in entry:
                    name, value = entry.split(':')
                    name = name.strip()
                    value = value.strip()
                    if name not in seen_names:
                        modified_data.append(entry)
                        seen_names.add(name)
                    else:
                        modified_data[-1] += f", {value}"
                else:
                    modified_data[-1] += f", {entry}"

            modified_content = ','.join(modified_data)

            with open(output_file_path, 'w') as output_file:
                output_file.write(modified_content)

            print(f"Modified content of {file_name} has been saved to {output_file_path}.")

if __name__ == "__main__":
    input_folder_location = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\music_data_handing_data_bridge\#out"
    output_folder_location = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\music_data_handing_data_bridge\#finalOut"

    remove_duplicate_names(input_folder_location, output_folder_location)
