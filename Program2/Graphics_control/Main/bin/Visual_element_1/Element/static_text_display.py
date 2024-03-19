from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np

def generate_static_text_frames(img, width, height, fps, duration, background_reader, text1, text2):
    img_height, img_width, _ = img.shape
    text_frames = int(fps * duration)

    frames = []
    for i in range(text_frames):
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        x_position = int((width - img_width) / 2)
        y_position = int((height - img_height) / 2)
        frame.paste(Image.fromarray(img), (x_position, y_position), Image.fromarray(img))

        draw = ImageDraw.Draw(frame)
        font_size = 75
        font_color = (0, 0, 0, 255)
        font_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Font\Tealand.ttf"
        font = ImageFont.truetype(font_path, font_size)

        x_text1, y_text1 = 675, 300
        x_text2, y_text2 = 675, 400 

        text_position1 = (x_text1, y_text1)
        draw.text(text_position1, text1, font=font, fill=font_color)

        text_position2 = (x_text2, y_text2)
        draw.text(text_position2, text2, font=font, fill=font_color)

        background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))
        combined_frame = Image.alpha_composite(background_frame.convert("RGBA"), frame)

        frames.append(np.array(combined_frame.convert("RGBA")))

    return frames
