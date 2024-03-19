def modify_text_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                # Add ":happy" at the end of each line
                modified_line = line.strip() + ":happy\n"
                file.write(modified_line)

        print("Text file modified successfully!")
    except FileNotFoundError:
        print("File not found. Please provide a valid filename.")

# Example usage:
filename = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\inputsoundmodify.txt"   # Provide the path to your text file here
modify_text_file(filename)
