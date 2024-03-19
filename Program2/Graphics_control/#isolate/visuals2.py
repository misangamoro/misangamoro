import imageio
from PIL import Image
import numpy as np
import time

def create_video(image_path, output_video_path, background_video_path, duration_sec=5, wait_sec=5, transition_duration=0.5, fps=60, height=1080, width=1920):
    # Read the PNG image with an alpha channel
    img = imageio.v2.imread(image_path)

    # Get image dimensions
    img_height, img_width, _ = img.shape

    # Read the background video
    background_reader = imageio.get_reader(background_video_path)

    # Set up video writer
    writer = imageio.get_writer(output_video_path, fps=fps, macro_block_size=1)

    # Calculate the number of frames for the resizing animation
    resize_frames = int(fps * duration_sec)

    # Generate video frames for the resizing animation
    for i in range(resize_frames):
        # Calculate the scaling factor for the image
        scale = i / resize_frames

        # Calculate the new dimensions after scaling
        new_width = max(1, int(img_width * scale))
        new_height = max(1, int(img_height * scale))

        # Resize the image based on the scaling factor
        scaled_img = Image.fromarray(img).resize((new_width, new_height))

        # Create a blank frame with an alpha channel
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # Calculate the position for the top-left corner motion
        x_position = int((width - new_width) * scale)
        y_position = int((height - new_height) * scale)

        # Paste the scaled image onto the frame at the calculated position
        frame.paste(scaled_img, (x_position, y_position), scaled_img)

        # Read a frame from the background video
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))

        # Combine the foreground and background frames
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)

        # Print statement for debugging
        print(f"Frame {i}/{resize_frames} - Writing at position ({x_position}, {y_position}), Scale: {scale}")

        # Convert the combined frame to a numpy array and write it to the video
        writer.append_data(np.array(combined_frame.convert("RGBA")))

    # Generate additional frames for the static period
    static_frames = int(fps * wait_sec)
    for i in range(static_frames):
        # Create a blank frame with an alpha channel
        frame = np.zeros((height, width, 4), dtype=np.uint8)

        # Resize the image based on the final scaling factor (1.0)
        scaled_img = Image.fromarray(img).resize((img_width, img_height))

        # Paste the scaled image onto the frame at the center position
        x_position = (width - img_width) // 2
        y_position = (height - img_height) // 2
        frame[y_position:y_position + img_height, x_position:x_position + img_width, :] = np.array(scaled_img)

        # Read a frame from the background video
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))

        # Combine the foreground and background frames
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), Image.fromarray(frame).convert("RGBA"))

        # Print statement for debugging
        print(f"Static Frame {i}/{static_frames}")

        # Convert the combined frame to a numpy array and write it to the video
        writer.append_data(np.array(combined_frame.convert("RGBA")))

    # Calculate the number of frames for the first transition animation
    transition_frames1 = int(fps * transition_duration)

    # Generate video frames for the first transition animation
    for i in range(transition_frames1):
        # Calculate the scaling factor for the image during the transition
        scale = 1 - i / transition_frames1

        # Calculate the new dimensions after scaling
        new_width = max(1, int(img_width * scale))
        new_height = max(1, int(img_height * scale))

        # Resize the image based on the scaling factor
        scaled_img = Image.fromarray(img).resize((new_width, new_height))

        # Create a blank frame with an alpha channel
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # Calculate the position for the top-right corner motion
        x_position = int((width - new_width) * scale)
        y_position = int((height - new_height) * scale)

        # Paste the scaled image onto the frame at the calculated position
        frame.paste(scaled_img, (x_position, y_position), scaled_img)

        # Read a frame from the background video
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))

        # Combine the foreground and background frames
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)

        # Print statement for debugging
        print(f"Transition Frame 1 {i}/{transition_frames1} - Writing at position ({x_position}, {y_position}), Scale: {scale}")

        # Convert the combined frame to a numpy array and write it to the video
        writer.append_data(np.array(combined_frame.convert("RGBA")))

    # Release the video writer and background reader
    writer.close()
    background_reader.close()

    print("Video writing completed.")

if __name__ == "__main__":
    # Specify the path to the input image (PNG), the output video, and the background video
    input_image_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\Charectes\char1.png"
    output_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output\output.mp4"
    background_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Video\BP.mp4"

    # Set the duration of the resizing animation in seconds
    resize_duration = 0.5

    # Set the wait duration in seconds
    wait_duration = 5

    # Set the duration of the first transition animation in seconds
    transition_duration1 = 0.5

    # Set the frames per second (fps) for the video
    video_fps = 60

    # Set the resolution of the video (width x height)
    video_width, video_height = 1920, 1080

    # Create the video
    create_video(input_image_path, output_video_path, background_video_path, resize_duration, wait_duration, transition_duration1, video_fps, video_height, video_width)
