from pydub import AudioSegment
import os

def main():
    input_music_file = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\inputmusic.txt"
    output_base_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\out"

    # Read inputmusic.txt
    with open(input_music_file, 'r') as f:
        for line in f:
            # Extract the name of the text file (which represents the folder name)
            folder_name, music_path = line.strip().split(': ')
            folder_name = folder_name.strip('"')
            # Create output folder
            output_folder = os.path.join(output_base_folder, folder_name)
            os.makedirs(output_folder, exist_ok=True)

            # Read Serilda.txt
            serilda_file = os.path.join(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\music_data_handing_data_bridge\#finalOut", f"{folder_name}.txt")
            with open(serilda_file, 'r') as serilda_f:
                serilda_data = serilda_f.readline().strip().split(': ')[1]
                cut_times = [float(x.strip()) for x in serilda_data.split(',') if x.strip()]

            # Apply cuts and export
            audio = AudioSegment.from_mp3(music_path.strip('"'))
            for i, cut_time in enumerate(cut_times):
                if i == 0:
                    start_time = 0
                else:
                    start_time = sum(cut_times[:i])
                end_time = sum(cut_times[:i + 1])
                output_file = os.path.join(output_folder, f"out{i + 1}.mp3")
                cut_audio = audio[start_time * 1000:end_time * 1000]

                # Apply fade in/out effect if necessary
                if i == 0:
                    fade_in_duration =  1000 # 0.5 seconds
                    fade_out_duration = 1000  # 0.5 seconds
                    fade_in_audio = cut_audio[:fade_in_duration].fade_in(fade_in_duration)
                    fade_out_audio = cut_audio[-fade_out_duration:].fade_out(fade_out_duration)
                    cut_audio = fade_in_audio + cut_audio[fade_in_duration:-fade_out_duration] + fade_out_audio

                cut_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    main()
