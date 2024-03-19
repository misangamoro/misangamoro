import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_repeating_animation(image_paths, text_list, background_video_path, output_video_path, rest_duration=5, text_display_duration=5, transition_duration=0.5, fps=60, height=1080, width=1920):
    background_reader = imageio.get_reader(background_video_path)
    writer = imageio.get_writer(output_video_path, fps=fps, macro_block_size=1)

    for i, (image_path, text) in enumerate(zip(image_paths, text_list)):
        img = imageio.v2.imread(image_path)
        img_height, img_width, _ = img.shape

        resize_frames = int(fps * rest_duration)
        text_frames = int(fps * text_display_duration)
        transition_frames = int(fps * transition_duration)

        for frame_num in range(resize_frames + text_frames + transition_frames):
            # Calculate scaling factor for resizing and transition
            if frame_num < resize_frames:
                scale = frame_num / resize_frames
            elif frame_num < resize_frames + text_frames:
                scale = 1
            else:
                scale = 1 - (frame_num - resize_frames - text_frames) / transition_frames

            # Resize the image based on the scaling factor
            new_width = max(1, int(img_width * scale))
            new_height = max(1, int(img_height * scale))
            scaled_img = Image.fromarray(img).resize((new_width, new_height))

            # Create a blank frame with an alpha channel
            frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))

            # Calculate the position for centering the image
            x_position = int((width - new_width) / 2)
            y_position = int((height - new_height) / 2)

            # Paste the scaled image onto the frame at the calculated position
            frame.paste(scaled_img, (x_position, y_position), scaled_img)

            # Use ImageDraw to draw the text on the frame
            draw = ImageDraw.Draw(frame)
            font_size = 75
            font_color = (0, 0, 0, 255)  # Black color
            font_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Font\Tealand.ttf"
            font = ImageFont.truetype(font_path, font_size)

            # Use specific coordinates for text position
            x_text, y_text = 675, 300

            # Draw the text on the frame
            text_position = (x_text, y_text)
            draw.text(text_position, text, font=font, fill=font_color)

            # Read a frame from the background video
            background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))

            # Combine the foreground and background frames
            combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)

            # Convert the combined frame to a numpy array and write it to the video
            writer.append_data(np.array(combined_frame.convert("RGBA")))

    # Release the video writer and background reader
    writer.close()
    background_reader.close()

    print("Video writing completed.")

if __name__ == "__main__":
    image_paths = [r"C:\path\to\image1.png", r"C:\path\to\image2.png"]
    text_list = ["Text for Image 1", "Text for Image 2"]

    background_video_path = r"C:\path\to\background_video.mp4"
    output_video_path = r"C:\path\to\output\output.mp4"

    resize_duration = 0.5
    text_display_duration_static = 2
    transition_duration1 = 0.5
    video_fps = 60
    video_width, video_height = 1920, 1080

    create_repeating_animation(image_paths, text_list, background_video_path, output_video_path, resize_duration, text_display_duration_static, transition_duration1, video_fps, video_height, video_width)



# background video is good
# give the vriable locations
