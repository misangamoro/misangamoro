import imageio
from PIL import Image, ImageDraw
import numpy as np

def generate_resizing_frames(img, width, height, fps, duration, background_reader):
    img_height, img_width, _ = img.shape
    resize_frames = int(fps * duration)

    frames = []
    for i in range(resize_frames):
        scale = i / resize_frames
        new_width = max(1, int(img_width * scale))
        new_height = max(1, int(img_height * scale))

        scaled_img = Image.fromarray(img).resize((new_width, new_height))
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        x_position = int((width - new_width) * scale)
        y_position = int((height - new_height) * scale)
        frame.paste(scaled_img, (x_position, y_position), scaled_img)

        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)

        frames.append(np.array(combined_frame.convert("RGBA")))

    return frames
