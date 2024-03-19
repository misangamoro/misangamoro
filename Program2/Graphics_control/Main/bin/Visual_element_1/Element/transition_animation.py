from PIL import Image
import numpy as np

def generate_background_frames(background_reader, width, height, max_frames=500):
    frames = []
    try:
        for _ in range(max_frames) if max_frames else iter(int, 1):
            background_frame = Image.fromarray(background_reader.get_next_data()).resize((width, height))
            frames.append(np.array(background_frame.convert("RGBA")))
    except StopIteration:
        pass
    return frames

def generate_transition_frames(img, width, height, fps, duration, background_reader, max_background_frames=500):
    img_height, img_width, _ = img.shape
    transition_frames = int(fps * duration)

    frames = []

    # Generate a fixed number of background frames lazily
    background_frames = generate_background_frames(background_reader, width, height, max_frames=max_background_frames)

    # Generate transition frames
    for i in range(transition_frames):
        scale = 1 - i / transition_frames
        new_width = max(1, int(img_width * scale))
        new_height = max(1, int(img_height * scale))

        scaled_img = Image.fromarray(img).resize((new_width, new_height))
        frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        x_position = int((width - new_width) * scale)
        y_position = int((height - new_height) * scale)
        frame.paste(scaled_img, (x_position, y_position), scaled_img)

        # Combine with the background frame from the list
        if background_frames:
            combined_frame = Image.alpha_composite(Image.fromarray(background_frames.pop(0)), frame)
            frames.append(np.array(combined_frame))

    return frames
