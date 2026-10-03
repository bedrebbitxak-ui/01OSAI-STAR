# 01OSAI-STAR-TRIT98 — Trit Sync
# Синхронизация тритовой архитектуры с бинарной системой 01OSAI-STAR

from trit_system import TritSystem
from trit_bridge import TritBridge

class TritSync:
    def __init__(self):
        self.system = TritSystem()
        self.bridge = TritBridge()

        # Последняя бинарная карта
        self.last_binary = None

        # Последний трит-снимок
        self.last_trit = None

    def sync_to_binary(self):
        """
        Синхронизация TRIT98 → бинарная система.
        Экспорт тритовой карты в бинарную.
        """
        binary_map = self.system.trit_export_binary()
        self.last_binary = binary_map
        return {
            "status": "synced_to_binary",
            "binary_map": binary_map
        }

    def sync_to_trit(self, binary_map):
        """
        Синхронизация бинарной системы → TRIT98.
        Импорт бинарной карты в тритовую систему.
        """
        self.system.trit_import_binary(binary_map)
        self.last_trit = self.system.trit_snapshot()
        return {
            "status": "synced_to_trit",
            "trit_snapshot": self.last_trit
        }

    def full_sync(self):
        """
        Полная двусторонняя синхронизация:
        1) TRIT → бинарная
        2) бинарная → TRIT
        """
        binary_map = self.system.trit_export_binary()
        self.system.trit_import_binary(binary_map)

        self.last_binary = binary_map
        self.last_trit = self.system.trit_snapshot()

        return {
            "status": "full_sync_complete",
            "binary_map": binary_map,
            "trit_snapshot": self.last_trit
        }

    def snapshot(self):
        """
        Снимок состояния синхронизации.
        """
        return {
            "last_binary": self.last_binary,
            "last_trit": self.last_trit
        }


if __name__ == "__main__":
    sync = TritSync()

    print("=== FULL SYNC ===")
    print(sync.full_sync())
