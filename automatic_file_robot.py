import os, shutil


def file_robot(file_path):
    file_list = os.listdir(file_path)
    categories = {
        ".jpg": "Images", ".png": "Images", ".jpeg": "Images",
        ".pdf": "PDFs",
        ".txt": "Text", ".docx": "Text",
        ".mp3": "Audio", ".mp4": "Video",
    }

    for file in file_list:
        full_path = os.path.join(file_path, file)
        if os.path.isfile(full_path):
            extension = os.path.splitext(file)[1]
            category = categories.get(extension, "Others")
            category_folder = os.path.join(file_path, category)
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(category_folder, file))

file_loc = input(r"Enter the folder location:")

file_robot(file_loc)
