# Define the input and output file paths
input_file = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\input.txt"
output_file = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\out\data.txt"


# Function to process each line of the input text
def process_line(line):
    # Split the line at the colon (":")
    parts = line.split(':')
    if len(parts) >= 1:
        # Get the name before the colon
        name = parts[0]
        # Remove any text after "z"
        name = name.split('z')[0]
        return name.strip()  # Remove leading/trailing spaces

# Read input file and process each line
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Process each line and extract names
names = [process_line(line) for line in lines if process_line(line)]

# Write the processed names to output file
with open(output_file, 'w') as outfile:
    for name in names:
        outfile.write(name + "\n")
