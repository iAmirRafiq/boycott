import os

def rename_files_in_folder(folder_path):
    # Ensure the provided folder path is valid
    if not os.path.isdir(folder_path):
        print(f"The folder path {folder_path} does not exist.")
        return

    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .png file
        if filename.endswith('.png'):
            # Check if there is a space in the filename
            if ' ' in filename:
                # Create the new filename by replacing spaces with underscores
                new_filename = filename.replace(' ', '_')
                # Construct the full file paths
                old_file_path = os.path.join(folder_path, filename)
                new_file_path = os.path.join(folder_path, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f'Renamed "{filename}" to "{new_filename}"')

# Example usage
folder_path = './'  # Replace with the path to your folder
rename_files_in_folder(folder_path)
