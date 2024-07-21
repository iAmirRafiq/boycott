import os
from PIL import Image

def compress_png_images(folder_path, quality=85):
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
                # Compress and save the image with the same filename
                img.save(file_path, optimize=True, quality=quality)
                print(f'Compressed "{filename}"')

# Example usage
folder_path = './'  # Replace with the path to your folder
compress_png_images(folder_path)
