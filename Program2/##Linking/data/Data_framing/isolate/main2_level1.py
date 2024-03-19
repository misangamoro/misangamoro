import os

def create_text_files(input_folder, output_folder):
    # Get a list of all text files in the input folder
    text_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    # Sort the files numerically based on their names
    text_files = sorted(text_files, key=lambda x: int(x.split('_')[0]))

    for file_name in text_files:
        file_path = os.path.join(input_folder, file_name)

        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Extract text on the left side of the colon
        title = content.split(':')[0].strip()

        # Replace illegal characters in the title
        title = title.replace('\n', '_')
        title = "".join(c for c in title if c.isalnum() or c in (' ', '_'))

        # Generate the new file name
        new_file_name = f"{file_name.split('_')[0]}_{title}.txt"

        # Generate the new file path
        new_file_path = os.path.join(output_folder, new_file_name)

        # Write the content to the new file
        with open(new_file_path, 'w') as new_file:
            new_file.write(content)

if __name__ == "__main__":
    input_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\Data_framing\out"
    output_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\Data_framing\out2"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    create_text_files(input_folder, output_folder)
    print("Text files created successfully.")
