import os

# Read the input file and parse the data
data = {}
with open(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\out\out.txt", "r") as file:
    for line in file:
        name, number = line.strip().split("=")
        if name not in data:
            data[name] = []
        data[name].append(int(number))

# Create a folder if it doesn't exist
folder_name = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\Curr"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Write data to individual files
for name, numbers in data.items():
    with open(os.path.join(folder_name, f"{name}.txt"), "w") as output_file:
        output_file.write(",".join(map(str, numbers)))
