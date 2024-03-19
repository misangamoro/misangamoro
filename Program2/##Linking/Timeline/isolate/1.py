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
    file_number = int(''.join(filter(str.isdigit, base_name)))
    time_taken_rounded = math.ceil(time_taken)
    
    output_file_name = f'{file_number}.txt'
    output_file_path = os.path.join(output_folder, output_file_name)

    with open(output_file_path, 'w') as output_file:
        output_file.write(f'{time_taken_rounded}')

if __name__ == "__main__":
    input_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\data\#finallizing_data_for_timeline\out'
    output_folder = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\Timeline\Output'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in sorted(os.listdir(input_folder)):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_folder, file_name)
            speak_text_from_file(file_path, output_folder, speed_factor=1.5, volume_level=0.02)
