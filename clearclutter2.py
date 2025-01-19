import os

# Directory to monitor
target_dir = r'D:\instaserver'
list_dir = os.listdir(target_dir)
os.chdir(target_dir)

# Initialize max indices for .jpg and .mp4
max_jpg_index = 55
max_mp4_index = 129

# Lists to hold the files that need renaming
heic_files = []
mp4_non_numeric_files = []

# One pass to gather information
for file in list_dir:
    # Check for already renamed .jpg files
    if file.endswith('.jpg'):
        try:
            # Extract numeric index
            file_index = int(file.split('.')[0])
            if file_index > max_jpg_index:
                max_jpg_index = file_index
        except ValueError:
            # Skip files that aren't numeric
            heic_files.append(file)

    # Check for already renamed .mp4 files
    elif file.endswith('.mp4'):
        try:
            file_index = int(file.split('.')[0])
            if file_index > max_mp4_index:
                max_mp4_index = file_index
        except ValueError:
            # Collect non-numeric .mp4 files
            mp4_non_numeric_files.append(file)

    # Collect all .heic files
    elif file.endswith('.heic') or file.endswith(".webp"):
        heic_files.append(file)

# Rename .heic files to the next available .jpg index
for file in heic_files:
    max_jpg_index += 1
    new_file_name = f"{max_jpg_index}.jpg"
    os.rename(file, new_file_name)

# Rename non-numeric .mp4 files to the next available .mp4 index
for file in mp4_non_numeric_files:
    max_mp4_index += 1
    new_file_name = f"{max_mp4_index}.mp4"
    os.rename(file, new_file_name)
