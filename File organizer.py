
import os
import shutil

folder_path= "test_folder"
for filename in os.listdir(folder_path):
    file_path=os.path.join(folder_path,filename)

    if os.path.isfile(file_path):
        file_name, file_ext=os.path.splitext(file_path)

        if file_ext==".png" or file_ext==".jpg" or file_ext==".jpeg":
            des_folder= "Images"

        elif file_ext==".pdf":
            des_folder= "Documents"

        if file_ext==".mp3":
            des_folder= "Audio"

        else:
            des_folder= "others"

        dest_path= os.path.join(folder_path,des_folder)

        if not os.path.exists(dest_path):
            os.mkdir(dest_path)

        shutil.move(file_path, os.path.join(dest_path,filename))

