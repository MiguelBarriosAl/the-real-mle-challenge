from lab.processing.models.data_processing import DataProcessed

config_train = {
    "name": "train_model",
    "preprocess_file": "data/processed/processed_listings.csv",
    "trained_file": "path",
    "test_size": 0.15,
    "random_state_split": 1,
    "feature_names": [
        DataProcessed['neighbourhood'],
        DataProcessed['room_type'],
        DataProcessed['accommodates'],
        DataProcessed['bathrooms'],
        DataProcessed['bedrooms']
    ],
    "label": DataProcessed["category"],
    "model": "RandomForestClassifier",
    "n_estimators": 500,
    "random_state_model": 0,
    "class_weight": "balanced",
    "n_jobs": 4,
}
