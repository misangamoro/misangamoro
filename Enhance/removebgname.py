import os

def rename_images(folder_path):
    try:
        # List all files in the given folder
        files = os.listdir(folder_path)

        # Iterate through each file in the folder
        for file_name in files:
            # Check if the file is a PNG image
            if file_name.lower().endswith('.png') and '-removebg-preview-0000' in file_name:
                # Generate the new file name by removing the specified substring
                new_name = file_name.replace('-removebg-preview-0000', '')
                
                # Construct the full paths for the old and new file names
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(folder_path, new_name)

                # Rename the file
                os.rename(old_path, new_path)
                
                print(f'Renamed: {file_name} -> {new_name}')

        print('Renaming completed.')
    
    except Exception as e:
        print(f'Error: {e}')

# Example usage: Replace 'path_to_your_folder' with the actual path to your image folder
folder_path = r'C:\Users\Sumit\Desktop\Online\Enhance\OUT'
rename_images(folder_path)
