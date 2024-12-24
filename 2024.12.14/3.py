import utils
from sys import path
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

def ask_for_file():
    while True:
        path_file = Path(input("Введите путь к файлу: "))
        if path_file.exists():
            module_path = utils.load_file(path_file)
            name = Path(module_path).name
            spec = spec_from_file_location(name.split(".")[0], module_path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        print("\n! по указанному пути отсутствует необходимый файл !\n")



# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}