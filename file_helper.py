import os


class FileHelper:

    @staticmethod
    def reed_file(file_path):
        with open(file_path, 'r') as f:
            return f.read()

    @staticmethod
    def write_file(file_path, text):
        mode = "a" if os.path.exists(file_path) else "w"
        with open(file_path, mode) as f:
            f.write(text)
