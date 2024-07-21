import os

def list_png_files(folder_path):
    """
    List all PNG files in the given folder.
 
    Parameters:
        folder_path (str): The path to the folder.

    Returns:
        list: A list of PNG filenames.
    """
    png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
    return png_files

# Example usage:
folder_path = './'  # Replace with the path to your folder
png_files = list_png_files(folder_path)

print(png_files)
