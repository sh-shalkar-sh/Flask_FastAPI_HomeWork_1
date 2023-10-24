import os
import logging
from collections import namedtuple

FileSystemItem = namedtuple("FileSystemItem", ["name_no_ext", "extension", "is_directory", "parent_directory"])

def configure_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(message)s", encoding="utf-8")

def log_directory_contents(directory_path):
    contents = get_directory_contents(directory_path)
    for item in contents:
        log_message = f"Имя файла без расширения: {item.name_no_ext}\n" + \
                      f"Расширение файла: {item.extension}\n" if not item.is_directory else "Это директория\n" + \
                      f"Флаг каталога: {item.is_directory}\n" + \
                      f"Название родительского каталога: {item.parent_directory}\n" + "=" * 50
        logging.info(log_message)

def get_directory_contents(directory_path):
    contents = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)

        if is_directory:
            name_no_ext, extension = item, None
        else:
            name_no_ext, extension = os.path.splitext(item)

        parent_directory = os.path.basename(directory_path)
        item_info = FileSystemItem(name_no_ext=name_no_ext, extension=extension, is_directory=is_directory, parent_directory=parent_directory)
        contents.append(item_info)
    return contents

if __name__ == "__main__":
    log_file = "directory_contents.log"
    configure_logging(log_file)
    directory_path = "C:\\Users\\shake\\PycharmProjects\\pogruzhenie_15_attestfcya"

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        log_directory_contents(directory_path)
    else:
        logging.error(f"Директория {directory_path} не существует.")