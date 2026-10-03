# 01OSAI-STAR-TRIT98 — Trit System Core
# Центральное ядро TRIT98: объединение корня, идентичности и манифеста

from trit_root import TritRoot
from trit_identity import TritIdentity
from trit_manifest import TritManifest

class TritSystemCore:
    def __init__(self):
        self.root = TritRoot()
        self.identity = TritIdentity()
        self.manifest = TritManifest()

        self.history = []

    def pulse(self):
        """
        Центральный пульс TRIT98:
        обновляет корень, идентичность и манифест.
        """
        root_snap = self.root.pulse()
        identity_snap = self.identity.update()
        manifest_snap = self.manifest.generate()

        core_snapshot = {
            "root": root_snap,
            "identity": identity_snap,
            "manifest": manifest_snap
        }

        self.history.append(core_snapshot)
        return core_snapshot

    def snapshot(self):
        return {
            "last": self.history[-1] if self.history else None,
            "history_length": len(self.history)
        }


if __name__ == "__main__":
    tsc = TritSystemCore()
    print("=== TRIT SYSTEM CORE PULSE ===")
    print(tsc.pulse())
