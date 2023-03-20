import numpy as np
import pandas as pd

from lab.processing.models.data_processing import DataRaw, DataProcessed


def num_bathroom_from_text(text: str) -> float:
    """
    Parses the number of bathrooms from a string.
    param text: A string that contains the number of bathrooms.
    :return: The number of bathrooms as a float. Returns NaN if the string does not contain a valid number.
    """
    try:
        if isinstance(text, str):
            bath_num = text.split(" ")[0]
            return float(bath_num)
        else:
            return np.NaN
    except ValueError:
        return np.NaN


class Wrangling:
    """
    Wrangling class for data processing.

    This class provides methods for processing data stored in Pandas DataFrames.
    The class is initialized with a configuration dictionary that contains
    various settings for the data processing steps.
    """

    def __init__(self, config: dict):
        self.config = config

    def rename_column_bathrooms(self, dataframe: pd.DataFrame):
        dataframe[DataRaw.BATHROOMS] = dataframe[DataRaw.BATHROOMS_TEXT].apply(
            num_bathroom_from_text
        )
        return dataframe[DataRaw.SUBSET]

    def dataframe_subset(self, dataframe: pd.DataFrame):
        df_raw = dataframe.copy()
        return df_raw[DataRaw.SUBSET]

    def rename_column_neighbourhood(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe.rename(columns={DataRaw.NEIGHBOURHOOD_GROUP: DataProcessed.NEIGHBOURHOOD}, inplace=True)
        return dataframe

    def categorize_neighbourhood(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        neighbourhood_map = self.config["mapping_columns"]["neighbourhood"]
        dataframe[DataProcessed.NEIGHBOURHOOD] = dataframe[DataProcessed.NEIGHBOURHOOD].map(neighbourhood_map)
        return dataframe

    def filter_price_by_minimum(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe['price'] = dataframe['price'].str.extract(r"(\d+).")
        dataframe['price'] = dataframe['price'].astype(int)
        df_filtered = dataframe[dataframe['price'] >= self.config['min_price']]
        return df_filtered

    def dropna(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return dataframe.dropna()

    def price_category(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe[DataProcessed.CATEGORY] = pd.cut(dataframe[DataProcessed.PRICE], bins=self.config['bins_price'],
                                                   labels=self.config['labels_price'])
        return dataframe

    def preprocess_amenities_column(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        AMENITIES_COLUMNS = [
            DataProcessed.TV,
            DataProcessed.INTERNET,
            DataProcessed.AIR,
            DataProcessed.KITCHEN,
            DataProcessed.HEATING,
            DataProcessed.WIFI,
            DataProcessed.ELEVATOR,
            DataProcessed.BREAKFAST,
        ]
        for col in AMENITIES_COLUMNS:
            dataframe[col] = dataframe['amenities'].str.contains(col).astype(int)
        dataframe.drop('amenities', axis=1, inplace=True)
        return dataframe

    def categorize_room_type(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        mapping = self.config["mapping_columns"]["room_type"]
        dataframe[DataProcessed.ROOM_TYPE] = dataframe[DataProcessed.ROOM_TYPE].map(mapping)
        return dataframe


def processing(dataframe: pd.DataFrame, config: dict) -> pd.DataFrame:
    """
    Preprocesses a given DataFrame according to the provided configuration dictionary.

    :param dataframe: A pandas DataFrame containing the raw data to be preprocessed.
    :param config: A dictionary containing configuration parameters for data preprocessing.
    :return: A pandas DataFrame containing the preprocessed data.
    """
    wrangling = Wrangling(config)
    df = wrangling.rename_column_bathrooms(dataframe)
    df = wrangling.dataframe_subset(df)
    df = wrangling.rename_column_neighbourhood(df)
    df = wrangling.filter_price_by_minimum(df)
    df = wrangling.dropna(df)
    df = wrangling.price_category(df)
    df = wrangling.preprocess_amenities_column(df)
    df = wrangling.categorize_neighbourhood(df)
    return wrangling.categorize_room_type(df)
