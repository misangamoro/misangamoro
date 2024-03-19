def modify_file(input_file):
    output_lines = []

    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Modify the lines and add numbering
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        output_lines.append(f"{line}={i}\n")

    # Write the modified content back to the file
    with open(input_file, 'w') as file:
        file.writelines(output_lines)

# Example usage:
file_location = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\out\out.txt"  # Replace with your file location
modify_file(file_location)

