import os

def modify_first_file(folder_path):
    # Get a sorted list of files in alphanumeric order
    files = sorted(os.listdir(folder_path), key=lambda x: (int(x.split('_')[0]), x))

    for filename in files:
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Check if the file has the expected format
            if len(lines) >= 4 and lines[0].startswith("data1:") and lines[1].startswith("data2:"):
                # Modify the first line (data1)
                lines[0] = "data1: 0.0\n"

                # Write the modified lines back to the file
                with open(file_path, 'w') as file:
                    file.writelines(lines)

                print(f"Modification successful for {filename}")
                break
            else:
                print(f"File {filename} does not have the expected format.")


# Example usage:
folder_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\data_level\out"
modify_first_file(folder_path)
