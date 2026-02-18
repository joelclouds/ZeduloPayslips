import json
import os
from pathlib import Path
from .config import APP_CONFIG_FILEPATH, APP_CONFIG


class ConfigManager:
    def __init__(self):
        self.path = Path(APP_CONFIG_FILEPATH)
        self._ensure_exists()

    def _ensure_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w") as f:
                json.dump(APP_CONFIG, f, indent=4)

    def load(self) -> dict:
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, updates: dict):
        config = self.load()
        config.update(updates)

        with open(self.path, "w") as f:
            json.dump(config, f, indent=4)
