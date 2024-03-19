import os

def extract_values(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        values = [line.split(': ')[1].strip() for line in content.split('\n') if ':' in line]
        return values

def combine_and_write(output_file, folder_path):
    file_paths = [os.path.join(folder_path, f) for f in sorted(os.listdir(folder_path), key=lambda x: int(x.split('_')[0])) if f.endswith('.txt')]
    
    with open(output_file, 'w') as output:
        for file_path in file_paths:
            values = extract_values(file_path)
            output.write('\n'.join(values) + '\n')

if __name__ == "__main__":
    folder_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\data_level\out"  # Change this to the actual folder path
    output_file = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\openned_data\out\combined_values.txt"

    combine_and_write(output_file, folder_path)

    print(f"Values from files in {folder_path} are combined and written to {output_file}.")
