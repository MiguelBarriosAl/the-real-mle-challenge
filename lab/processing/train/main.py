import pandas as pd

from lab.processing.configs.config_train import config_train
from lab.processing.train.train import train_random_forest
from utils.logs import Logs
from utils.utils import BASE_DIR

log = Logs()


def main():
    log.info("Initializing data Training Model")
    # Load Model
    path_data = BASE_DIR / config_train["preprocess_file"]
    df = pd.read_csv(path_data)
    # Training Model
    train_random_forest(df, config_train)


if __name__ == "__main__":
    main()
