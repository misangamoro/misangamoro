from PIL import Image, ImageDraw, ImageFont
import numpy as np
import imageio

def write_output_video(frames, output_path, fps):
    writer = imageio.get_writer(output_path, fps=fps, macro_block_size=1)

    for frame in frames:
        writer.append_data(frame)

    writer.close()

# ... (previous code)

def generate_frames(img_path, params_list, background_reader):
    frames = []
    total_frames = 0

    for params in params_list:
        img_frames, total_frames_current = generate_all_frames(img_path, params, background_reader)
        frames.extend(img_frames)
        total_frames += total_frames_current

    return frames, total_frames

# ... (previous code)


    for animation_params in params['animations']:
        img_frames, total_frames_current = generate_all_frames(img, animation_params, background_reader)
        frames.extend(img_frames)
        total_frames += total_frames_current

    return frames, total_frames

def generate_all_frames(img_path, params, background_reader):
    img = imageio.v2.imread(img_path)
    animation_params = params['animation_params']

    # Resize animation
    resize_frames = generate_resize_frames(img, animation_params, background_reader)
    
    # Text display animation
    text_frames = generate_text_frames(img, animation_params, background_reader)

    # Transition animation
    transition_frames = generate_transition_frames(img, animation_params, background_reader, start_frame=len(resize_frames) + len(text_frames))

    # Combine all frames
    all_frames = resize_frames + text_frames + transition_frames

    return all_frames, len(all_frames)

def generate_resize_frames(img, params, background_reader):
    img_height, img_width, _ = img.shape
    fps = params['fps']
    duration = params['resize_duration']
    width, height = params['width'], params['height']

    frames = []

    # Generate resize frames
    for i in range(int(fps * duration)):
        scale = i / (fps * duration)
        new_width = max(1, int(img_width * scale))
        new_height = max(1, int(img_height * scale))

        scaled_img = Image.fromarray(img).resize((new_width, new_height))
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        x_position = int((width - new_width) * scale)
        y_position = int((height - new_height) * scale)
        frame.paste(scaled_img, (x_position, y_position), scaled_img)

        # Combine with the background frame
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)
        frames.append(np.array(combined_frame))

    return frames

def generate_text_frames(img, params, background_reader):
    img_height, img_width, _ = img.shape
    fps = params['fps']
    duration = params['text_display_duration_static']
    width, height = params['width'], params['height']

    frames = []

    # Generate text frames
    for i in range(int(fps * duration)):
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

        # Use the specific coordinates for the text position
        x_text, y_text = 675, 300
        text_position = (x_text, y_text)
        draw.text(text_position, params['text'], font=font, fill=font_color)

        # Combine with the background frame
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)
        frames.append(np.array(combined_frame))

    return frames

def generate_transition_frames(img, params, background_reader, start_frame=0):
    img_height, img_width, _ = img.shape
    fps = params['fps']
    duration = params['transition_duration']
    width, height = params['width'], params['height']

    frames = []

    # Start reading the background video from the specified frame
    for _ in range(start_frame):
        try:
            background_reader.get_next_data()
        except StopIteration:
            # If we reach the end of the video, break the loop
            break

    # Generate transition frames
    for i in range(int(fps * duration)):
        scale = 1 - i / (fps * duration)
        new_width = max(1, int(img_width * scale))
        new_height = max(1, int(img_height * scale))

        scaled_img = Image.fromarray(img).resize((new_width, new_height))
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        x_position = int((width - new_width) * scale)
        y_position = int((height - new_height) * scale)
        frame.paste(scaled_img, (x_position, y_position), scaled_img)

        # Combine with the background frame
        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)
        frames.append(np.array(combined_frame))

    return frames
