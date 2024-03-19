from PIL import Image
import os

def convert_black_to_transparent(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        image = Image.open(input_path)

        # Convert black pixels to transparent
        image = image.convert("RGBA")
        data = image.getdata()

        new_data = []
        for item in data:
            # If the pixel is black (0, 0, 0), make it transparent (0, 0, 0, 0)
            if item[:3] == (0, 0, 0):
                new_data.append((0, 0, 0, 0))
            else:
                new_data.append(item)

        image.putdata(new_data)

        # Save the result in the output folder as a PNG image
        image.save(output_path, "PNG")

if __name__ == "__main__":
    # Specify your input and output folders
    input_folder = r"C:\Users\Sumit\Desktop\Online\Enhance\OUT"
    output_folder = r"C:\Users\Sumit\Desktop\Online\Enhance\#finallize"

    convert_black_to_transparent(input_folder, output_folder)
    print("Conversion complete.")

