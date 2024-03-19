import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_animation(image_path, text1, text2, delay_text_duration, writer, background_reader, resize_duration=0.5, text_display_duration=5, transition_duration=0.5, fps=60, height=1080, width=1920):
    # Read the PNG image with an alpha channel
    img = imageio.v2.imread(image_path)

    # Get image dimensions
    img_height, img_width, _ = img.shape

    # Calculate the number of frames for the resizing animation
    resize_frames = int(fps * resize_duration)

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

    # Generate additional frames for the static period with text on top of the input image
    delay_frames = int(fps * delay_text_duration)  

    for i in range(int(fps * text_display_duration)):
        # Create a blank frame with an alpha channel
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # Calculate the position for the top-left corner motion
        x_position = int((width - img_width) / 2)
        y_position = int((height - img_height) / 2)

        # Paste the input image onto the frame at the calculated position
        frame.paste(Image.fromarray(img), (x_position, y_position), Image.fromarray(img))

        # Use ImageDraw to draw the text on the frame
        draw = ImageDraw.Draw(frame)
        font_size = 75
        font_color = (0, 0, 0, 255)  # Black color
        font_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Font\Tealand.ttf"
        font = ImageFont.truetype(font_path, font_size)

        # Use the specific coordinates for the first text position
        x_text1, y_text1 = 675, 300

        # Use the specific coordinates for the second text position
        x_text2, y_text2 = 675, 400

        # Adjust the position of the first text
        text_position1 = (x_text1, y_text1)
        draw.text(text_position1, text1, font=font, fill=font_color)

        # Display the second text after the specified delay
        if i >= delay_frames:
            text_position2 = (x_text2, y_text2)
            draw.text(text_position2, text2, font=font, fill=font_color)

        # Read a frame from the background video
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))

        # Combine the foreground and background frames
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)

        # Print statement for debugging
        print(f"Static Text Frame {i}/{text_display_duration * fps}")

        # Convert the combined frame to a numpy array and write it to the video
        writer.append_data(np.array(combined_frame.convert("RGBA")))

    # Calculate the number of frames for the transition animation
    transition_frames = int(fps * transition_duration)

    # Generate video frames for the transition animation
    for i in range(transition_frames):
        # Calculate the scaling factor for the image during the transition
        scale = 1 - i / transition_frames

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
        print(f"Transition Frame {i}/{transition_frames} - Writing at position ({x_position}, {y_position}), Scale: {scale}")

        # Convert the combined frame to a numpy array and write it to the video
        writer.append_data(np.array(combined_frame.convert("RGBA")))

def main():
    # Set up video writer
    output_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output\output_combined.mp4"
    writer = imageio.get_writer(output_video_path, fps=60, macro_block_size=1)

    # Set up background video reader
    background_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Video\BP.mp4"
    background_reader = imageio.get_reader(background_video_path)

    # Animation 1
    image_path_1 = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\Charectes\hunter.png"
    text_1_1 = "Hello Animation 1"
    text_2_1 = "Hello2 Animation 1"
    delay_text_duration_1 = 2

    create_animation(image_path_1, text_1_1, text_2_1, delay_text_duration_1, writer, background_reader, resize_duration=0.5)

    # Animation 2
    image_path_2 = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\Charectes\man.png"
    text_1_2 = "Hello Animation 2"
    text_2_2 = "Hello2 Animation 2"
    delay_text_duration_2 = 3

    create_animation(image_path_2, text_1_2, text_2_2, delay_text_duration_2, writer, background_reader, resize_duration=0.5)

    # Release the video writer and background reader
    writer.close()
    background_reader.close()

    print("Video creation completed.")

if __name__ == "__main__":
    main()
