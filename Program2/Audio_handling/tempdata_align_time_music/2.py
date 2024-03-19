def extract_alternate_lines(input_file, output_file):
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        lines = f_input.readlines()
        for i in range(0, len(lines), 2):
            f_output.write(lines[i])

input_file = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\out\data.txt"
output_file = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\out\out.txt"  # Output file name

extract_alternate_lines(input_file, output_file)

print(f"Alternate lines extracted from '{input_file}' and saved to '{output_file}'.")
