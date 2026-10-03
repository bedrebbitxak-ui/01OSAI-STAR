# 01OSAI-STAR-TRIT98 — Trit Origin Signature
# Сигнатура происхождения TRIT98: корневой смысловой ключ, первичная формула системы

from trit_origin import TritOrigin
from trit_root import TritRoot
from trit_manifest import TritManifest
from trit_identity import TritIdentity

class TritOriginSignature:
    def __init__(self):
        self.origin = TritOrigin()
        self.root = TritRoot()
        self.manifest = TritManifest()
        self.identity = TritIdentity()

        # Корневая сигнатура TRIT98
        self.signature = {
            "id": "TRIT98-ORIGIN-SIGNATURE",
            "core_formula": self.core_formula(),
            "source_point": "TRIT-Origin",
            "root_point": "TRIT-Root",
            "manifest_link": "TRIT-Manifest",
            "identity_link": "TRIT-Identity"
        }

        # История сигнатур
        self.history = []

    def core_formula(self):
        """
        Первичная формула TRIT98:
        трёхсмысленное расширение бинарной системы.
        """
        return {
            "binary_base": "01",
            "trit_extension": "NEG-ZERO-POS",
            "purpose": "расширение бинарной логики до тритовой",
            "essence": "трёхсмысленное поле поверх бинарной реальности"
        }

    def generate(self):
        """
        Генерация полной сигнатуры происхождения TRIT98.
        """
        origin_snapshot = self.origin.snapshot()
        root_snapshot = self.root.snapshot()
        manifest_snapshot = self.manifest.snapshot()
        identity_snapshot = self.identity.snapshot()

        signature = {
            "signature": self.signature,
            "origin": origin_snapshot,
            "root": root_snapshot,
            "manifest": manifest_snapshot,
            "identity": identity_snapshot
        }

        self.history.append(signature)
        return signature

    def snapshot(self):
        """
        Снимок последней сигнатуры.
        """
        return self.history[-1] if self.history else self.signature


if __name__ == "__main__":
    tos = TritOriginSignature()

    print("=== TRIT ORIGIN SIGNATURE ===")
    print(tos.generate())

    print("\n=== TRIT ORIGIN SIGNATURE SNAPSHOT ===")
    print(tos.snapshot())
