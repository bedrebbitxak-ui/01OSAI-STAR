from core.utils import log
from memory_01 import Memory01
from safety import Safety
from shell_01 import Shell01
from core.module_loader import ModuleLoader


def main():
    log("01OSAI: initializing system")

    # память и безопасность
    memory = Memory01()
    safety = Safety()
    log("MEMORY: loaded")
    log("SAFETY: initialized")

    # загрузка модулей
    loader = ModuleLoader()
    log("01OSAI: loading modules")
    modules = loader.load_modules()

    # запуск shell
    shell = Shell01(memory, modules)
    log("01OSAI: system ready")
    log("01OSAI: interactive shell started")

    shell.run()


if __name__ == "__main__":
    main()
