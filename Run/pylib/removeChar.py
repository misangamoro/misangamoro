import os

def empty_file(file_path):
    try:
        with open(file_path, 'w') as f:
            f.truncate(0)
            print(f"Emptied file: {file_path}")
    except OSError as e:
        print(f"Error: {e}")

def delete_subfiles(directory):
    try:
        # Iterate over all items (files and directories) in the specified directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            # Check if the item is a file
            if os.path.isfile(item_path):
                # If it's the specified file, empty it
                if item == "name.txt":
                    empty_file(item_path)
    except OSError as e:
        print(f"Error: {e}")

# Directory to delete subfiles from
directory_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\run\nowChar"

# Call the function to delete subfiles
delete_subfiles(directory_path)
