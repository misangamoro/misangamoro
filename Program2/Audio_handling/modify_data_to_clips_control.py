import os

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.readline().strip().split(',')
        return [int(num) for num in numbers]

def rename_files(folder_path, numbers):
    files = os.listdir(folder_path)
    files.sort()
    for i, file in enumerate(files, 1):
        old_name = os.path.join(folder_path, file)
        new_name = os.path.join(folder_path, f'outc{numbers[i-1]}.mp3')
        os.rename(old_name, new_name)
        print(f'Renamed {old_name} to {new_name}')

def main():
    text_files_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\tempdata_align_time_music\FinalOut\Curr"
    music_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\out"

    for text_file in os.listdir(text_files_folder):
        if text_file.endswith('.txt'):
            numbers = read_numbers_from_file(os.path.join(text_files_folder, text_file))
            music_subfolder = os.path.join(music_folder, os.path.splitext(text_file)[0])
            rename_files(music_subfolder, numbers)

if __name__ == "__main__":
    main()
