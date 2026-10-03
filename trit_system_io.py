# 01OSAI-STAR-TRIT98 — Trit System IO
# Ввод-вывод TRIT98: базовый интерфейс обмена данными

class TritSystemIO:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def read(self, data):
        self.inputs.append(data)
        return data

    def write(self, data):
        self.outputs.append(data)
        return data

    def snapshot(self):
        return {
            "inputs_count": len(self.inputs),
            "outputs_count": len(self.outputs),
            "last_input": self.inputs[-1] if self.inputs else None,
            "last_output": self.outputs[-1] if self.outputs else None
        }


if __name__ == "__main__":
    tsio = TritSystemIO()
    tsio.read({"msg": "hello"})
    tsio.write({"msg": "world"})
    print("=== TRIT SYSTEM IO SNAPSHOT ===")
    print(tsio.snapshot())
