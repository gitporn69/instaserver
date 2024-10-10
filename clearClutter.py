import os
import re

# Directory to monitor
target_dir = r'D:\FuckingDownloads\instaserver'
list_dir = os.listdir(target_dir)
os.chdir(target_dir)

# Initialize max indices for .jpg and .mp4
max_jpg_index = -1
max_mp4_index = 17

# Regular expression to check if the file name is in the format 'i.ext'
numeric_pattern = re.compile(r'^\d+\.(jpg|mp4)$')

# Find the highest current index for .jpg and .mp4 files
for file in list_dir:
    if numeric_pattern.match(file):
        try:
            # Extract the numeric part from the filename
            file_index = int(file.split('.')[0])
            if file.endswith('.jpg') and file_index > max_jpg_index:
                max_jpg_index = file_index
            if file.endswith('.mp4') and file_index > max_mp4_index:
                max_mp4_index = file_index
        except ValueError:
            pass

# Process files that are not named in the numeric format
for file in list_dir:
    # If file is a .heic and is not in numeric format
    if file.endswith('.heic') and not numeric_pattern.match(file):
        max_jpg_index += 1
        new_file_name = f"{max_jpg_index}.jpg"
        os.rename(file, new_file_name)

    # If file is a .mp4 and is not in numeric format
    if file.endswith('.mp4') and not numeric_pattern.match(file):
        max_mp4_index += 1
        new_file_name = f"{max_mp4_index}.mp4"
        os.rename(file, new_file_name)
