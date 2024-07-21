import os
from PIL import Image

def resize_png_images(folder_path, width=350, height=270):
    # Ensure the provided folder path is valid
    if not os.path.isdir(folder_path):
        print(f"The folder path {folder_path} does not exist.")
        return

    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .png file
        if filename.endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            # Open the image file
            with Image.open(file_path) as img:
                # Resize the image
                resized_img = img.resize((width, height), Image.ANTIALIAS)
                # Save the resized image back to the same file path
                resized_img.save(file_path, optimize=True)
                print(f'Resized "{filename}" to {width}x{height} pixels')

# Example usage
folder_path = './'  # Replace with the path to your folder
resize_png_images(folder_path)
