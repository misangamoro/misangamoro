import os
import time
import pyttsx3
import math

def speak_text_from_file(file_path, output_folder, speed_factor=2, volume_level=0.02):
    with open(file_path, 'r') as file:
        text_content = file.read()

    engine = pyttsx3.init()

    # Set properties including speed and volume
    engine.setProperty('rate', 150 * speed_factor)
    engine.setProperty('volume', volume_level)

    start_time = time.time()

    engine.say(text_content)
    engine.runAndWait()

    end_time = time.time()
    time_taken = end_time - start_time

    base_name = os.path.basename(file_path)
    # Use the original file name for the output file
    output_file_name = base_name
    output_file_path = os.path.join(output_folder, output_file_name)

    with open(output_file_path, 'w') as output_file:
        # Write the rounded time taken to the output file
        output_file.write(f'{math.ceil(time_taken)}')

if __name__ == "__main__":
    input_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\#finallizing_data\out'
    output_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Timeline\Output'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in sorted(os.listdir(input_folder)):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_folder, file_name)
            speak_text_from_file(file_path, output_folder, speed_factor=1.5, volume_level=0.02)
