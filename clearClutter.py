import os

target_dir=r'D:\FuckingDownloads\instaserver'
list_dir=os.listdir(target_dir)
os.chdir(target_dir)
# print(list_dir)

for file in list_dir:
    if file.endswith('.heic'):
        i=0
        while True:
            if not os.path.exists(f"{i}.jpg"):
                os.rename(file,f"{i}.jpg")
                break
            i=i+1
    
    if file.endswith('.mp4'):
        i=0
        while True:
            if not os.path.exists(f"{i}.mp4"):
                os.rename(file,f"{i}.mp4")
                break
            i=i+1
    