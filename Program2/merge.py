# from moviepy.editor import VideoFileClip, AudioFileClip
# import os

# def merge_video_and_audio(video_folder, audio_folder, export_folder):
#     # Ensure output folder exists
#     if not os.path.exists(export_folder):
#         os.makedirs(export_folder)

#     # Get the list of video files in the video folder
#     video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

#     # Iterate over video files and merge with corresponding audio
#     for video_file in video_files:
#         video_path = os.path.join(video_folder, video_file)
#         audio_file = video_file.replace('.mp4', '.mp3')
#         audio_path = os.path.join(audio_folder, audio_file)

#         # Check if the corresponding audio file exists
#         if os.path.exists(audio_path):
#             # Load video and audio clips
#             video_clip = VideoFileClip(video_path)
#             audio_clip = AudioFileClip(audio_path)

#             # Set the audio of the video clip to the loaded audio clip
#             video_clip = video_clip.set_audio(audio_clip)

#             # Export the merged video to the export folder
#             export_path = os.path.join(export_folder, video_file)
#             video_clip.write_videofile(export_path, codec="libx264", audio_codec="aac")

#             print(f"Merged {video_file} with {audio_file} and exported to {export_path}")


# if __name__ == "__main__":
#     # Specify the paths to the video, audio, and export folders
#     video_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Video_clips'
#     audio_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Audio_clips'
#     export_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output'

#     # Merge video and audio files
#     merge_video_and_audio(video_folder_path, audio_folder_path, export_folder_path)

from moviepy.editor import VideoFileClip, CompositeAudioClip, AudioFileClip
import os

def merge_video_and_audio(video_folder, audio_folder1, audio_folder2, export_folder):
    # Ensure output folder exists
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    # Get the list of video files in the video folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

    # Iterate over video files and merge with corresponding audio
    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        audio_file1 = video_file.replace('.mp4', '.mp3')
        audio_file2 = 'outc' + audio_file1.split('out')[1]
        audio_path1 = os.path.join(audio_folder1, audio_file1)
        audio_path2 = os.path.join(audio_folder2, audio_file2)

        # Check if the corresponding audio files exist
        if os.path.exists(audio_path1) and os.path.exists(audio_path2):
            # Load audio clips
            audio_clip1 = AudioFileClip(audio_path1)
            audio_clip2 = AudioFileClip(audio_path2)

            # Mix audio clips together
            mixed_audio = CompositeAudioClip([audio_clip1, audio_clip2])

            # Load video clip
            video_clip = VideoFileClip(video_path)

            # Set the audio of the video clip to the mixed audio clip
            video_clip = video_clip.set_audio(mixed_audio)

            # Export the merged video to the export folder
            export_path = os.path.join(export_folder, video_file)
            video_clip.write_videofile(export_path, codec="libx264", audio_codec="aac")

            print(f"Merged {video_file} with {audio_file1} and {audio_file2} and exported to {export_path}")


if __name__ == "__main__":
    # Specify the paths to the video, audio, and export folders
    video_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Video_clips'
    audio_folder_path1 = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Audio_clips'
    audio_folder_path2 = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\#clips_control\Music_clips'
    export_folder_path = r'C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output'

    # Merge video and audio files
    merge_video_and_audio(video_folder_path, audio_folder_path1, audio_folder_path2, export_folder_path)
