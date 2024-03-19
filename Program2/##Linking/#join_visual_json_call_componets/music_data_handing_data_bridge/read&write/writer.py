import os

def process_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Dictionary to store sums for each file
    sums = {}

    # Loop through files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            # Extract the desired portion of the filename
            if 'z' in filename and '_' in filename:
                new_filename = filename.split('_')[-1].split('z')[0] + '.txt'
            elif 'z' in filename:
                new_filename = filename.split('z')[0] + '.txt'
            elif '_' in filename:
                new_filename = filename.split('_')[-1]
            else:
                new_filename = filename

            # Define the input and output file paths
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, new_filename)

            # Calculate the sum of data values
            total = 0
            with open(input_path, 'r') as file:
                for line in file:
                    if line.startswith('data'):
                        value = float(line.split(': ')[1])
                        total += value
            # Add the constant
            total += 0.5

            # Update the sums dictionary
            sums.setdefault(new_filename, []).append(total)

    # Update existing output files with new sums
    for filename, total_list in sums.items():
        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'a') as file:
            for total in total_list:
                file.write(f'{filename.split(".")[0]}: {total},')

# Define input and output folder paths
input_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\data_level\out'
output_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\music_data_handing_data_bridge\#out'

# Call the function to process files
process_files(input_folder, output_folder)
