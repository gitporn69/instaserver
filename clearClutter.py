import os

target_dir=r'D:\FuckingDownloads\instaserver'
list_dir=os.listdir(target_dir)
os.chdir(target_dir)
# print(list_dir)

for file in list_dir:
    if file.endswith('.heic'):
        i=0
        while True:
            if not os.path.exists(f"{i}.heic"):
                os.rename(file,f"{i}.heic")
                break
            i=i+1
    