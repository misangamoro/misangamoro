import os

def delete_files_in_folders(source_folders):
    for source_folder in source_folders:
        try:
            for root, dirs, files in os.walk(source_folder, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"File deleted: {file_path}")
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    os.rmdir(dir_path)
                    print(f"Folder deleted: {dir_path}")
            print(f"All files and folders deleted inside: {source_folder}")
        except FileNotFoundError:
            print(f"Folder not found: {source_folder}")
        except PermissionError:
            print(f"Permission error: Unable to delete files in {source_folder}")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    # Define the source folders

    source_folders = [
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Input_reading\const',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\out',
        r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\music_data_handing_data_bridge\#out",
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#No._of_rep\out',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Temp_data\out',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Audio_clips',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Video_clips',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Music_clips',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\Curr',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\out',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\out',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\out',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\music_data_handing_data_bridge\#finalOut',
        r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Sound_define\out1'
    ]  # Replace with the paths to your folders

    # Delete files and folders in specified folders
    delete_files_in_folders(source_folders)

if __name__ == "__main__":
    main()
