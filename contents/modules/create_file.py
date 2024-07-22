def CreateFile(file, contents=""):
    print(f"🚀 Tạo file: {file}")
    with open(f"{file}", "w", encoding="utf-8") as file:
        file.write(contents)
