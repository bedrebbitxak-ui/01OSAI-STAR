import time
from memory_01 import Memory01
from safety import Safety
from shell_01 import Shell01
from module_loader import ModuleLoader

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    log("01OSAI: initializing system")

    memory = Memory01()
    safety = Safety()
    shell = Shell01(memory)
    loader = ModuleLoader()

    log("01OSAI: loading modules")
    loader.load_modules()

    log("01OSAI: system ready")
    log("01OSAI: interactive shell started")

    shell.run()

if __name__ == "__main__":
    main()
