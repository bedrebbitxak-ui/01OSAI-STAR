import os
import importlib
from core.utils import log


class ModuleLoader:
    def __init__(self):
        self.modules_path = "modules"

    def load_modules(self):
        """
        Загружает все модули из папки modules/.
        Возвращает словарь:
        {
            "text": <module instance>,
            "image": <module instance>,
            ...
        }
        """
        loaded = {}

        if not os.path.isdir(self.modules_path):
            log(f"MODULE_LOADER: directory '{self.modules_path}' not found")
            return loaded

        log("MODULE_LOADER: scanning modules/")

        for filename in os.listdir(self.modules_path):
            if not filename.endswith(".py"):
                continue

            if filename == "base.py":
                continue  # базовый класс не загружаем как модуль

            module_name = filename[:-3]  # text.py → text
            full_path = f"{self.modules_path}.{module_name}"

            try:
                log(f"MODULE_LOADER: loading {module_name}")
                mod = importlib.import_module(full_path)

                # класс должен называться <Name>Module
                class_name = module_name.capitalize() + "Module"

                if hasattr(mod, class_name):
                    cls = getattr(mod, class_name)
                    loaded[module_name] = cls()
                else:
                    log(f"MODULE_LOADER: class {class_name} not found in {filename}")

            except Exception as e:
                log(f"MODULE_LOADER: error loading {module_name}: {e}")

        return loaded
