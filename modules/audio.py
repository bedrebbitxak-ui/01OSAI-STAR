from modules.base import BaseModule
import subprocess
from core.utils import log


class AudioModule(BaseModule):
    name = "audio"
    commands = ["play", "info", "convert"]

    def run(self, command: str, args: str):
        command = command.lower()

        # -------------------------
        # PLAY (как было)
        # -------------------------
        if command == "play":
            return f"[audio.play] playing sound: {args}"

        # -------------------------
        # INFO
        # -------------------------
        if command == "info":
            return self.info()

        # -------------------------
        # CONVERT (НОВЫЙ)
        # -------------------------
        if command == "convert":
            """
            Формат:
                module audio convert input.wma output.ogg
            """
            parts = args.split(" ", 1)
            if len(parts) < 2:
                return "Usage: module audio convert <input> <output>"

            input_file, output_file = parts[0], parts[1]

            cmd = [
                "ffmpeg",
                "-y",
                "-i", input_file,
                output_file
            ]

            log(f"[audio.convert] ffmpeg → {cmd}")

            try:
                subprocess.run(
                    cmd,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                return f"[audio.convert] OK → {output_file}"
            except Exception as e:
                return f"[audio.convert] ERROR: {e}"

        # -------------------------
        # UNKNOWN
        # -------------------------
        return f"Unknown command '{command}' for module '{self.name}'"

    def info(self):
        return f"AudioModule: commands = {', '.join(self.commands)}"
