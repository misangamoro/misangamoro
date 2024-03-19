import os
import shutil

def move_files(source_folders, destination_folder):
    for source_folder in source_folders:
        try:
            files = os.listdir(source_folder)
            for file in files:
                source_path = os.path.join(source_folder, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(source_path, destination_path)
                print(f"File moved: {file}")
        except FileNotFoundError:
            print(f"Source folder not found: {source_folder}")
        except PermissionError:
            print(f"Permission error: Unable to move files from {source_folder}")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    # Define the source folders and destination folder

    Output = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program\#Bin'
    
    source_folders = [r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\#Input_reading\out",
                      r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\Data_framing\out',
                      r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\Data_framing\out2',
                      r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\#finallizing_data\out',
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Timeline\Output",
                      r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\number_of_aphabet_in_text_part1,2\no_of_words',
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\data_level\out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\openned_data\out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\p_individual_sum\out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\z_created\out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\#out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\size_with_position_data_bridge\out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\text_with_image_data_bridge\out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\time_with_visuals_data_bridge\out",
                      r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\##visual_call_by_json\brighed",
                      ]  # Replace with the paths to your source folders
    destination_folder = Output  # Replace with the path to your destination folder

    # Move files from source folders to the destination folder
    move_files(source_folders, destination_folder)

if __name__ == "__main__":
    main()  