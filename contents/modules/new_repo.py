import os
from modules.create_file import CreateFile
from modules.create_folder import CreateFolder


class NewRepo:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def start(self):
        contents = ""
        print(f"Thư mục gốc: {self.root_folder}")

        CreateFile(f"{self.root_folder}/README.md")

        CreateFile(f"{self.root_folder}/.gitignore")

        code_workspace = "../nghia-github-template.code-workspace"
        with open(code_workspace, "r", encoding="utf-8") as file:
            contents = file.read()
        CreateFile(f"{self.root_folder}/{os.path.basename(self.root_folder)}.code-workspace", contents)

        CreateFolder(f"{self.root_folder}/contents")
        CreateFolder(f"{self.root_folder}/contents/code")
        CreateFolder(f"{self.root_folder}/contents/modules")
        CreateFolder(f"{self.root_folder}/contents/input")
        CreateFolder(f"{self.root_folder}/contents/output")
        CreateFolder(f"{self.root_folder}/contents/documents")
        CreateFolder(f"{self.root_folder}/contents/data")
        CreateFolder(f"{self.root_folder}/contents/video")

        all_gitignore = "../all.gitignore"
        with open(all_gitignore, "r", encoding="utf-8") as file:
            contents = file.read()
        CreateFile(f"{self.root_folder}/contents/.gitignore", contents)

        CreateFile(f"{self.root_folder}/contents/{os.path.basename(self.root_folder)}.py")
