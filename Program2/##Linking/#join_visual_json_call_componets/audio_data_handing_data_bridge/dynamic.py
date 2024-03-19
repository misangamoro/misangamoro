def main():
    # Read the numerical value from count.txt
    with open(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Input_reading\const\current_file_number.txt", "r") as count_file:
        numerical_value = int(count_file.read().strip())-1

    # Read the data from datasound.txt
    with open(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\inputsoundmodify.txt", "r") as datasound_file:
        data_lines = datasound_file.readlines()

    # Extract the line number based on the numerical value
    line_number = (numerical_value - 1) % len(data_lines)

    # Extract the data from the specified line
    data = data_lines[line_number].strip().split(':')

    # Read and modify the third text file
    with open(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\#out\output.txt", "r") as third_file:
        lines = third_file.readlines()

    # Modify the appropriate lines in the third text file
    for i, line in enumerate(lines):
        if "text:" in line:
            lines[i] = f"{data[0]}:{line.split(':')[1]}"
        elif "text2:" in line:
            lines[i] = f"{data[1]}:{line.split(':')[1]}"

    # Write the modified content back to the third text file
    with open(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\#out\output.txt", "w") as third_file:
        third_file.writelines(lines)

if __name__ == "__main__":
    main()
