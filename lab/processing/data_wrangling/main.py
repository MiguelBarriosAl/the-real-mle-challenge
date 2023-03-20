import pandas as pd
from lab.processing.configs.config_loader import load_config_file
from logs import Logs
from pathlib import Path

log = Logs()
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


def main():
    log.info("Initializing data processing")
    # Load Preprocess Config
    path_config = BASE_DIR / "lab/processing/configs/data_preprocess.json"
    config = load_config_file(path_config)
    # Read csv
    path_data = BASE_DIR / config["raw_file"]
    df_raw = pd.read_csv(path_data)
    # Processing File Csv
    # Save File Csv


if __name__ == "__main__":
    main()
