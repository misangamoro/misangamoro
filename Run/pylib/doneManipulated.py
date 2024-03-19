import os
import glob

def create_text_file(folder_path):
    # Check if the directory exists
    if not os.path.exists(folder_path):
        print(f"Directory '{folder_path}' does not exist.")
        return
    
    # Search for .mp4 files in the subfolders
    mp4_files = glob.glob(os.path.join(folder_path, "**/*.mp4"), recursive=True)
    
    # Check if any .mp4 files were found
    if mp4_files:
        for mp4_file in mp4_files:
            # Get the directory of the mp4 file
            directory = os.path.dirname(mp4_file)
            
            # Create a text file in the same directory
            text_file_path = os.path.join(directory, "done.txt")
            with open(text_file_path, "w") as text_file:
                text_file.write("yes")
                print(f"Text file created at '{text_file_path}'")
    else:
        print("No .mp4 files found.")

# Directory path
directory_path = r"C:\Users\Sumit\Desktop\Online\Storys\lib"

# Call the function to create text files
create_text_file(directory_path)
