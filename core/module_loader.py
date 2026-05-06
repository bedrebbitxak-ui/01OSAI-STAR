import os
import importlib
from modules.base import BaseModule
from .utils import log

class ModuleLoader:
    def __init__(self, modules_path="modules"):
        self.modules_path = modules_path
        self.modules = {}

    def load_modules(self):
        log("MODULE_LOADER: scanning modules/")

        for filename in os.listdir(self.modules_path):
            if not filename.endswith(".py"):
                continue
            if filename == "base.py":
                continue

            module_name = filename[:-3]  # text.py → text
            full_path = f"{self.modules_path}.{module_name}"

            try:
                log(f"MODULE_LOADER: loading {module_name}")
                module = importlib.import_module(full_path)

                # ищем класс, наследующий BaseModule
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type) and issubclass(obj, BaseModule) and obj is not BaseModule:
                        instance = obj()
                        self.modules[instance.name] = instance
                        break

            except Exception as e:
                log(f"MODULE_LOADER ERROR: {e}")

        return self.modules
