import os.path
import typing
from os import listdir, environ
from dotenv import load_dotenv
import chardet


class File:
    def __init__(self, file_name: str, folder_path: str):
        self.file_name = file_name
        self.folder_path = folder_path
        self.file_path = self.folder_path + "/" + self.file_name
        if self.__file_not_exists():
            raise FileExistsError("File not found!")
        self.content = self.__read_file()
        self.encoding = self.__get_encoding()

    def print_file_summary(self):
        self.stdout_encoding()
        self.stdout_content()

    def stdout_content(self):
        print(f"Строка из файла: {self.content.decode(self.encoding)}")

    def stdout_encoding(self):
        print(f"Кодировка - {self.encoding}")

    def __get_encoding(self) -> str:
        return chardet.detect(self.content)["encoding"]

    def __read_file(self) -> bytes:
        return open(file=self.file_path, mode="rb").read()

    def __file_not_exists(self) -> bool:
        if os.path.exists(self.file_path):
            return False
        return True


def load_env_variables():
    load_dotenv(".env")
    return environ["FILES_FOLDER_PATH"]


def main():
    files_folder_path = load_env_variables()
    file_names = listdir(files_folder_path)
    for number, file_name in enumerate(file_names):
        file = File(file_name=file_name, folder_path=files_folder_path)
        print(f"№{number + 1}")
        file.print_file_summary()


if __name__ == "__main__":
    main()
