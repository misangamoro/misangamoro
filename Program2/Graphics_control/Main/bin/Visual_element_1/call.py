from Element import *

# Specify the path to the output video and the background video
output_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output\output.mp4"
background_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Video\BP.mp4"

# Set the frames per second (fps) for the video
video_fps = 60

# Set the resolution of the video (width x height)
video_width, video_height = 1920, 1080

# First Animation
animation_params1 = {
    'fps': video_fps,
    'width': video_width,
    'height': video_height,
    'resize_duration': 0.5,
    'text_display_duration_static': 1,
    'transition_duration': 0.5,
    'text': "hello1"
}

animation_frames1, total_frames1 = generate_frames(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\Charectes\hunter.png", [animation_params1], imageio.get_reader(background_video_path))
write_output_video(animation_frames1, output_video_path, video_fps)

# Second Animation
animation_params2 = {
    'fps': video_fps,
    'width': video_width,
    'height': video_height,
    'resize_duration': 0.5,
    'text_display_duration_static': 1,
    'transition_duration': 0.5,
    'text': "hello2"
}

# Calculate the starting frame for the second animation based on the total duration of the first animation
start_frame2 = int(total_frames1)

animation_frames2, _ = generate_frames(r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\Charectes\man.png", [animation_params2], imageio.get_reader(background_video_path), start_frame=start_frame2)

# Append the frames from the second animation to the output video frames
animation_frames1.extend(animation_frames2)

# Write the combined output video
write_output_video(animation_frames1, output_video_path, video_fps)
