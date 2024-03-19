from pydub import AudioSegment
import os

def generate_export_path(base_path, extension):
    index = 1
    while True:
        export_path = os.path.join(base_path, f"out{index}.{extension}")
        if not os.path.exists(export_path):
            return export_path
        index += 1

def export_audio_with_specific_timing(timings, embedded_sounds, export_folder):
    # Handle the case where 'total' may not be present
    total_duration = sum(timings.get("total", [0]))

    # Create an empty audio segment for the total duration
    final_audio = AudioSegment.silent(duration=int(total_duration * 1000))

    # Iterate through timings and embed sounds
    for key, start_times in timings.items():
        if key.lower() in embedded_sounds:
            embedded_sound = embedded_sounds[key.lower()]
            for start_time in start_times:
                start_time_ms = int(start_time * 1000)
                final_audio = final_audio.overlay(embedded_sound, position=start_time_ms)

    # Generate the export path with an incremented index if needed
    export_path = generate_export_path(export_folder, "mp3")

    # Export the final audio
    final_audio.export(export_path, format="mp3")
    print(f"Audio exported successfully to {export_path}")

if __name__ == "__main__":
    # Provide the paths to the audio files you want to embed
    embedded_sounds = {
        "happy": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\happy.mp3"),
        "sad": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\sad.mp3"),
        "realization": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\realization.mp3"),
        "fear": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\fear.mp3"),
        "ahhh": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\ahhh.mp3"),
        "anger": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\anger.mp3"),
        "byby": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\byby.mp3"),
        "happyaa": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\happyaa.mp3"),
        "nani": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\nani.mp3"),
        "sadxx": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\snd\sadxx.mp3"),
        "close": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\OC\close.mp3"),
        "open": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\OC\open.mp3"),
    }

    # Specify the export folder for the final audio
    export_folder = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Audio_clips"

    # Read timings from the text file
    timings = {}
    with open(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\#out\output.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                key, values = parts
                if values:  # Check if values is not an empty string
                    timings[key.lower()] = [float(value) for value in values.split(",")]

    # Export audio with specific timing
    export_audio_with_specific_timing(timings, embedded_sounds, export_folder)
