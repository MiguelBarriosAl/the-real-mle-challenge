import pandas as pd

from lab.processing.configs.config_preprocess import config_preprocess
from lab.processing.data_wrangling.wrangling import processing
from utils.logs import Logs
from utils.utils import BASE_DIR

log = Logs()


def main():
    log.info("Initializing data processing")
    # Read csv
    path_data = BASE_DIR / config_preprocess["raw_file"]
    df_raw = pd.read_csv(path_data)
    # Processing File Csv
    data_processed = processing(df_raw, config_preprocess)
    # Save File Csv
    data_processed.to_csv(BASE_DIR / config_preprocess['preprocess_file'])


if __name__ == "__main__":
    main()
