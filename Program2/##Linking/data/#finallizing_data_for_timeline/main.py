import os

def split_and_export_text(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each text file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            with open(input_path, 'r') as file:
                content = file.read().strip()

            # Split the content based on the newline character
            lines = content.split('\n')

            # Create two separate text files
            if len(lines) == 2:
                output_path_1 = os.path.join(output_folder, f"{filename.split('.')[0]}_part1.txt")
                output_path_2 = os.path.join(output_folder, f"{filename.split('.')[0]}_part2.txt")

                with open(output_path_1, 'w') as file_1:
                    file_1.write(lines[0])

                with open(output_path_2, 'w') as file_2:
                    file_2.write(lines[1])

                print(f"Files created for {filename}: {output_path_1} and {output_path_2}")
            else:
                print(f"Skipping {filename} as it doesn't have exactly two parts.")

# Example usage
input_folder_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\Data_framing\out2"
output_folder_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\#finallizing_data\out"

split_and_export_text(input_folder_path, output_folder_path)
