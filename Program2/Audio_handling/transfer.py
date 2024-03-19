# import os
# import shutil

# def move_mp3_files(source_folder1, source_folder2, destination_folder):
#     # Ensure the destination folder exists
#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)

#     # Iterate over the files in the first source folder
#     for filename in os.listdir(source_folder1):
#         if filename.endswith(".mp3"):
#             source_path = os.path.join(source_folder1, filename)
#             destination_path = os.path.join(destination_folder, filename)
#             shutil.move(source_path, destination_path)
#             print(f"Moved {filename} from {source_folder1} to {destination_folder}")

#     # Iterate over the files in the second source folder
#     for filename in os.listdir(source_folder2):
#         if filename.endswith(".mp3"):
#             source_path = os.path.join(source_folder2, filename)
#             destination_path = os.path.join(destination_folder, filename)
#             shutil.move(source_path, destination_path)
#             print(f"Moved {filename} from {source_folder2} to {destination_folder}")

# # Example usage
# if __name__ == "__main__":
#     source_folder1 = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\out\Serilda'
#     source_folder2 = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\out\Vespera'
#     destination_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Music_clips'

#     move_mp3_files(source_folder1, source_folder2, destination_folder)


import os
import shutil

def move_mp3_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over all subfolders inside the source folder
    for root, _, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith(".mp3"):
                source_path = os.path.join(root, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} from {root} to {destination_folder}")

# Example usage
if __name__ == "__main__":
    source_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\out'
    destination_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Music_clips'

    move_mp3_files(source_folder, destination_folder)
