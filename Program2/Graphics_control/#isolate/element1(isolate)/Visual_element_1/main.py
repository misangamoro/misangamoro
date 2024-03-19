import imageio
import time

from resizing_animation import generate_resizing_frames
from static_text_display import generate_static_text_frames
from transition_animation import generate_transition_frames

def create_video(image_path, output_video_path, background_video_path, resize_duration, text_display_duration_static, transition_duration1, fps, height, width):
    img = imageio.v2.imread(image_path)
    background_reader = imageio.get_reader(background_video_path)
    writer = imageio.get_writer(output_video_path, fps=fps, macro_block_size=1)

    resizing_frames = generate_resizing_frames(img, width, height, fps, resize_duration, background_reader)
    text1 = "hello"
    text2 = "hello2"
    static_text_frames = generate_static_text_frames(img, width, height, fps, text_display_duration_static, background_reader, text1, text2)
    transition_frames1 = generate_transition_frames(img, width, height, fps, transition_duration1, background_reader)

    total_frames = len(resizing_frames) + len(static_text_frames) + len(transition_frames1)
    current_frame = 0

    print("Creating video:")
    for frames in [resizing_frames, static_text_frames, transition_frames1]:
        for frame in frames:
            writer.append_data(frame)
            current_frame += 1
            print(f"\rProgress: {current_frame}/{total_frames} frames", end="", flush=True)
            time.sleep(0.01)  # Simulate processing time

    writer.close()
    background_reader.close()

    print("\nVideo writing completed.")

if __name__ == "__main__":
    input_image_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\Charectes\hunter.png"
    output_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output\output.mp4"
    background_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Video\BP.mp4"

    resize_duration = 0.5
    text_display_duration_static = 5
    transition_duration1 = 0.5
    video_fps = 60
    video_width, video_height = 1920, 1080

    create_video(input_image_path, output_video_path, background_video_path, resize_duration, text_display_duration_static, transition_duration1, video_fps, video_height, video_width)
