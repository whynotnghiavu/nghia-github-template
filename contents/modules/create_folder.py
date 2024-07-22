import os


def CreateFolder(folder):
    print(f"🚀 Tạo folder: {folder}")

    if not os.path.exists(folder):
        os.mkdir(folder)
