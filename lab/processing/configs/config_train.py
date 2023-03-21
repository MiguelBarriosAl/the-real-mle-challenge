from lab.processing.models.data_processing import DataProcessed

config_train = {
    "name": "train_model",
    "preprocess_file": "data/processed/processed_listings.csv",
    "trained_file": "models/trained_model_rf_classifier.pkl",
    "test_size": 0.15,
    "random_state_split": 1,
    "feature_cols": [
        DataProcessed.NEIGHBOURHOOD,
        DataProcessed.ROOM_TYPE,
        DataProcessed.ACCOMMODATES,
        DataProcessed.BATHROOMS,
        DataProcessed.BEDROOMS
    ],
    "target_col": DataProcessed.CATEGORY,
    "model": "RFClassifier",
    "n_estimators": 500,
    "random_state": 0,
    "class_weight": "balanced",
    "n_jobs": 4,
    "classes": [0, 1, 2, 3],
    "labels": ['low', 'mid', 'high', 'lux'],
    "metrics": ['precision', 'recall', 'support']
}
