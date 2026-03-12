import os
import shutil

path = input("Enter folder path to organize: ")

files = os.listdir(path)

for file in files:

    filename, extension = os.path.splitext(file)

    extension = extension.lower()

    if extension in [".jpeg", ".jpeg",".png", ".gif"]:
        folder = "Images"

    elif extension in [".mp4",".mkv",".mov"]:
        folder = "Videos"

    elif extension in [".pdf",".docx",".txt"]:
        folder = "Documents"
    
    elif extension in [".mp3",".wav"]:
        folder = "Music"

    else:
        folder = "others"

    folder_path = os.path.join(path,folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move (os.path.join(path,file), os.path.join(folder_path,file))

    print("Files organized successfully!")

    
    
