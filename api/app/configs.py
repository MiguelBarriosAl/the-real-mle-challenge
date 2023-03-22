config_predict = {
    "name": "predict",
    "version": "0.0.1",
    "trained_file": "models/trained_model_rf_classifier.pkl",
    "feature_cols": {
        "neighbourhood": {
            "Bronx": 1,
            "Queens": 2,
            "Staten Island": 3,
            "Brooklyn": 4,
            "Manhattan": 5,
        },
        "room_type": {
            "Shared room": 1,
            "Private room": 2,
            "Entire home/apt": 3,
            "Hotel room": 4,
        },
        "price_category": {0: "Low", 1: "Mid", 2: "High", 3: "Lux"},
    }
}