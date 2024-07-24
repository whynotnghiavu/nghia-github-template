# sudo apt-get install python3-tk
import os
import tkinter as tk
from tkinter import filedialog
from modules.new_repo import NewRepo


def on_button_click(event=None):
    try:
        Downloads_Nghia_Git = os.path.expanduser("~/Downloads/Nghia/Git")

        root_folder = filedialog.askdirectory(initialdir=Downloads_Nghia_Git, title="nghia-github-template")
        if root_folder:
            print(f"Selected folder: {root_folder}")

            new = NewRepo(root_folder)
            new.start()

            exit()
    except Exception as e:
        print(f"Error: {e}")


# Tự động hỏi thư mục
on_button_click()
