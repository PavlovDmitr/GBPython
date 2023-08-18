from os import chdir, listdir, mkdir, getcwd, remove as rm
from pathlib import Path

def remove(name: str = '', extension_del: str = ''):

    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        extension = file.name[-4:]
        print(file.name, extension, end='. ')
        if len(extension_del) > 0 and extension == extension_del:
            print(file, " - удален.")
            rm(file)
            