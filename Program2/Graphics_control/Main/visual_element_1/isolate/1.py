import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_video(image_path, output_video_path, background_video_path, rest_duration=5, text_display_duration=5, transition_duration=0.5, fps=60, height=1080, width=1920):
    # Read the PNG image with an alpha channel
    img = imageio.v2.imread(image_path)

    # Get image dimensions
    img_height, img_width, _ = img.shape

    # Read the background video
    background_reader = imageio.get_reader(background_video_path)

    # Set up video writer
    writer = imageio.get_writer(output_video_path, fps=fps, macro_block_size=1)

    # Calculate the number of frames for the resizing animation
    resize_frames = int(fps * rest_duration)

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

# ...

# ...

 # ...

# ...

    # Generate additional frames for the static period with "hello" and "hello2" text on top of the input image
    delayduration = 2
    text_frames = int(fps * text_display_duration)
    delay_frames = int(fps * delayduration)  

    for i in range(text_frames):
        # Create a blank frame with an alpha channel
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # Calculate the position for the top-left corner motion
        x_position = int((width - img_width) / 2)
        y_position = int((height - img_height) / 2)

        # Paste the input image onto the frame at the calculated position
        frame.paste(Image.fromarray(img), (x_position, y_position), Image.fromarray(img))

        # Use ImageDraw to draw the text "hello" on the frame
        draw = ImageDraw.Draw(frame)
        font_size = 75
        font_color = (0, 0, 0, 255)  # Black color
        font_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Font\Tealand.ttf"
        font = ImageFont.truetype(font_path, font_size)

        # Use the specific coordinates for the first text position
        x_text1, y_text1 = 675, 300

        # Use the specific coordinates for the second text position (hello2)
        x_text2, y_text2 = 675, 400

        # Adjust the position of the first text
        text_position1 = (x_text1, y_text1)
        draw.text(text_position1, "hello", font=font, fill=font_color)

        # Display "hello2" after 1 second
        if i >= delay_frames:
            # Adjust the position of the second text (hello2)
            text_position2 = (x_text2, y_text2)
            draw.text(text_position2, "hello2", font=font, fill=font_color)

        # Read a frame from the background video
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))

        # Combine the foreground and background frames
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)

        # Print statement for debugging
        print(f"Static Text Frame {i}/{text_frames}")

        # Convert the combined frame to a numpy array and write it to the video
        writer.append_data(np.array(combined_frame.convert("RGBA")))

    # ...





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
    input_image_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\Charectes\hunter.png"
    output_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output\output.mp4"
    background_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Video\BP.mp4"

    # Set the duration of the resizing animation in seconds
    resize_duration = 0.5

    # Set the duration of the static period with "hello" text on top of the input image in seconds
    text_display_duration_static = 5

    # Set the duration of the first transition animation in seconds
    transition_duration1 = 0.5

    # Set the frames per second (fps) for the video
    video_fps = 60

    # Set the resolution of the video (width x height)
    video_width, video_height = 1920, 1080

    # Create the video
    create_video(input_image_path, output_video_path, background_video_path, resize_duration, text_display_duration_static, transition_duration1, video_fps, video_height, video_width)
