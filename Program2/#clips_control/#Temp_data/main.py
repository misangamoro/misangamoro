import os

def create_output_files(input_file, output_folder):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    output_lines = [line.strip() for line in lines if line.strip()]

    if not output_lines or len(output_lines) % 2 != 0:
        return

    output_files = [f"{output_folder}/{i // 2 + 1}.txt" for i in range(len(output_lines))]

    for i, output_file in enumerate(output_files):
        with open(output_file, 'a') as file:
            file.write(output_lines[i] + '\n')


if __name__ == "__main__":
    input_file = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\input.txt"  # Replace with your input file name
    output_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Temp_data\out"   # Replace with your desired output folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    create_output_files(input_file, output_folder)
