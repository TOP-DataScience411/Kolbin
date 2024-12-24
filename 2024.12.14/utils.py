from shutil import copy2
from sys import path
from pathlib import Path

def load_file(path_file: Path):
    name = path_file.name
    copy2(path_file, path[0])
    return path[0] + "\\" + name
