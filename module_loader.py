import importlib
import os
from core.utils import log

MODULES_PATH = "modules"

class ModuleLoader:
    def __init__(self):
        self.modules = {}

    def load_all(self):
        """
        Загружает все модули из папки modules/
        """
        log("MODULE_LOADER: scanning modules/")
        for file in os.listdir(MODULES_PATH):
            if file.endswith(".py"):
                name = file[:-3]
                self.load(name)

    def load(self, name: str):
        """
        Загружает один модуль по имени.
        """
        try:
            log(f"MODULE_LOADER: loading {name}")
            module = importlib.import_module(f"{MODULES_PATH}.{name}")
            self.modules[name] = module
            return module
        except Exception as e:
            log(f"MODULE_LOADER ERROR: {name} — {e}")
            return None

    def get(self, name: str):
        """
        Возвращает модуль, если он загружен.
        """
        return self.modules.get(name)
