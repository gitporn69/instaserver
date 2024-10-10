import os
file_exts=['.jpg','.mp4']

file_list=os.listdir(os.getcwd())
os.chdir(os.getcwd())
for ext in file_exts:
    for file in file_list:
        if file.endswith(ext):
            os.remove(file)
