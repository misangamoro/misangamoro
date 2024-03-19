import imageio
from PIL import Image
import numpy as np

def create_video(image_path, output_video_path, background_video_path, duration_sec=5, fps=60, height=1080, width=1920):
    # Read the PNG image with an alpha channel
    img = imageio.v2.imread(image_path)


    # Get image dimensions
    img_height, img_width, _ = img.shape

    # Read the background video
    background_reader = imageio.get_reader(background_video_path)
    background_fps = background_reader.get_meta_data()['fps']

    # Set up video writer
    writer = imageio.get_writer(output_video_path, fps=fps, macro_block_size=1)

    # Calculate the number of frames
    num_frames = int(fps * duration_sec)

    # Generate video frames
    for i in range(num_frames):
        # Calculate the vertical position of the image
        y_position = int((i / num_frames) * (height - img_height))

        # Create a blank frame with an alpha channel
        frame = np.zeros((height, width, 4), dtype=np.uint8)

        # Paste the image onto the frame at the calculated position
        frame[y_position:y_position + img_height, 0:img_width, :] = img

        # Read a frame from the background video
        background_frame = background_reader.get_next_data()

        # Resize the background frame to match the output video resolution
        background_frame = Image.fromarray(background_frame).resize((width, height))

        # Combine the foreground and background frames
        combined_frame = np.where(frame[:, :, 3:4] > 0, frame[:, :, :3], np.array(background_frame))

        # Print statement for debugging
        print(f"Frame {i}/{num_frames} - Writing at position {y_position}")

        # Write the combined frame to the video
        writer.append_data(combined_frame)

    # Release the video writer and background reader
    writer.close()
    background_reader.close()

    print("Video writing completed.")

if __name__ == "__main__":
    # Specify the path to the input image (PNG), the output video, and the background video
    input_image_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Image\loc.png"
    output_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Program2\output\output.mp4"
    background_video_path = r"C:\Users\Sumit\Desktop\Online\Visuals Production\Assest\Video\BP.mp4"

    # Set the duration of the video in seconds
    video_duration = 5

    # Set the frames per second (fps) for the video
    video_fps = 60

    # Set the resolution of the video (width x height)
    video_width, video_height = 1920, 1080

    # Create the video
    create_video(input_image_path, output_video_path, background_video_path, video_duration, video_fps, video_height, video_width)
