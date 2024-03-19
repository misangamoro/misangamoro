# from pydub import AudioSegment

# def export_audio_with_embedded_sound(total_duration, silence_duration, embedded_sound_path, export_path):
#     # Create silent audio for the specified duration
#     silent_audio = AudioSegment.silent(duration=silence_duration * 1000)

#     # Load the embedded sound
#     embedded_sound = AudioSegment.from_file(embedded_sound_path)

#     # Concatenate silent audio and embedded sound at the 5th second
#     final_audio = silent_audio[:5000] + embedded_sound + silent_audio[5000:]

#     # Export the final audio
#     final_audio.export(export_path, format="mp3")

# if __name__ == "__main__":
#     # Set the total duration and silence duration
#     total_duration = 20  # in seconds
#     silence_duration = total_duration - 5  # silence duration before the 5th second

#     # Provide the path to the audio file you want to embed
#     embedded_sound_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\text.mp3"

#     # Specify the export path for the final audio
#     export_path = r"C:\Extension\exported_audio.mp3"

#     # Export the audio with the embedded sound
#     export_audio_with_embedded_sound(total_duration, silence_duration, embedded_sound_path, export_path)

#     print("Audio exported successfully.")










from pydub import AudioSegment

def export_audio_with_specific_timing(timings, embedded_sounds, export_path):
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

    # Export the final audio
    final_audio.export(export_path, format="mp3")

if __name__ == "__main__":
    # Provide the paths to the audio files you want to embed
    embedded_sounds = {
        "text": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\text.mp3"),
        "close": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\OC\close.mp3"),
        "open": AudioSegment.from_file(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Audio\OC\open.mp3"),
    }

    # Specify the export path for the final audio
    export_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\Audio_handling\Out\exported_audio.mp3"

    # Read timings from the text file
    timings = {}
    with open(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\##Linking\#join_visual_json_call_componets\audio_data_handing_data_bridge\#out\output.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                key, values = parts
                timings[key.lower()] = [float(value) for value in values.split(",")]

    # Export audio with specific timing
    export_audio_with_specific_timing(timings, embedded_sounds, export_path)

    print("Audio exported successfully.")
