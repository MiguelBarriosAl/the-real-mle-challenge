from pathlib import Path
import json


def load_config_file(file_path: Path) -> dict:
    """
    Loads a configuration file as a dictionary.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    with open(file_path, "r") as f:
        config_data = json.load(f)

    return config_data
