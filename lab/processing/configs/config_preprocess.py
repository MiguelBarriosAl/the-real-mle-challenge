import numpy as np

config_preprocess = {
    "name": "preprocess",
    "raw_file": "data/raw/listings.csv",
    "preprocess_file": "data/processed/processed_listings.csv",
    "min_price": 10,
    "bins_price": [
        10,
        90,
        180,
        400,
        np.inf
    ],
    "labels_price": [
        0,
        1,
        2,
        3
    ],
    "mapping_columns": {
        "room_type": {
            "Shared room": 1,
            "Private room": 2,
            "Entire home/apt": 3,
            "Hotel room": 4
        },
        "neighbourhood": {
            "Bronx": 1,
            "Queens": 2,
            "Staten Island": 3,
            "Brooklyn": 4,
            "Manhattan": 5
        }
    }
}
