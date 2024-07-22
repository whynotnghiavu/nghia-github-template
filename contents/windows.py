from modules.new_repo import NewRepo


if __name__ == "__main__":

    print(f"Chương trình nghia-github-template")

    root_folder = input(f"Nhập vị trí repo mới: ")

    new = NewRepo(root_folder)
    new.start()
