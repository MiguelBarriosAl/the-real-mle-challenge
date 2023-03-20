import pandas as pd

from lab.processing.configs.data_preprocess import config_preprocess
from lab.processing.data_wrangling.wrangling import processing
from logs import Logs
from pathlib import Path

log = Logs()
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


def main():
    log.info("Initializing data processing")
    # Read csv
    path_data = BASE_DIR / config_preprocess["raw_file"]
    df_raw = pd.read_csv(path_data)
    # Processing File Csv
    data_processed = processing(df_raw, config_preprocess)
    # Save File Csv


if __name__ == "__main__":
    main()
