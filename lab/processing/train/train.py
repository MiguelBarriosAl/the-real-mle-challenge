import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from utils.utils import BASE_DIR


def train_random_forest(df: pd.DataFrame, config: dict):
    """
    Train Random Forest Model
    :param df: Dataframe containing the data to train the model on.
    :param config: Configuration dictionary containing the parameters for the model.
    :return: Trained model.
    """
    X = df[config['feature_cols']]
    y = df[config['target_col']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config['test_size'],
                                                        random_state=config['random_state_split'])
    rf = RandomForestTrainer(config['n_estimators'], config['random_state'], config['class_weight'],
                             config['n_jobs'])
    print(X_train, y_train)
    rf.fit(X_train, y_train)

    # Accuracy Score
    print(rf.accuracy_score(X_test, y_test))

    # Metrics
    rf.plot_feature_importances(X_train)
    rf.plot_confusion_matrix(X_test, y_test, config)

    # Save Model
    path = BASE_DIR / config['trained_file']
    rf.save(path)


class RandomForestTrainer:
    """
    Class to train a Random Forest model.
    """

    def __init__(self, n_estimators: int, random_state: int, class_weight: str, n_jobs: int):
        self.clf = None
        self.n_estimators = n_estimators
        self.random_state = random_state
        self.class_weight = class_weight
        self.n_jobs = n_jobs

    def fit(self, X, y):
        self.clf = RandomForestClassifier(
            n_estimators=self.n_estimators,
            random_state=self.random_state,
            class_weight=self.class_weight,
            n_jobs=self.n_jobs
        )
        self.clf.fit(X, y)

    def accuracy_score(self, X, y) -> float:
        y_pred = self.clf.predict(X)
        return accuracy_score(y, y_pred)

    def _feature_importances(self, X_train) -> (np.ndarray, np.ndarray):
        importances = self.clf.feature_importances_
        indices = np.argsort(importances)[::-1]
        features = X_train.columns[indices]
        importances = importances[indices]
        return features, importances

    def plot_feature_importances(self, X_train, figsize=(12, 7)):
        features, importances = self._feature_importances(X_train)
        fig, ax = plt.subplots(figsize=figsize)
        plt.barh(range(len(importances)), importances)
        plt.yticks(range(len(importances)), features, fontsize=12)
        ax.invert_yaxis()
        ax.set_xlabel("Feature importance", fontsize=12)
        plt.show()

    def plot_confusion_matrix(self, X_test, y_test, config_train: dict):
        classes = config_train['classes']
        labels = config_train['labels']
        y_pred = self.clf.predict(X_test)
        c = confusion_matrix(y_test, y_pred)
        c = c / c.sum(axis=1).reshape(len(classes), 1)
        # Plot confusion matrix
        sns.heatmap(c, annot=True, cmap='BuGn', square=True, fmt='.2f', annot_kws={'size': 10}, cbar=False)
        plt.xlabel('Predicted', fontsize=16)
        plt.ylabel('Real', fontsize=16)
        plt.xticks(ticks=np.arange(.5, len(classes)), labels=labels, rotation=0, fontsize=12)
        plt.yticks(ticks=np.arange(.5, len(classes)), labels=labels, rotation=0, fontsize=12)
        plt.title("Simple model", fontsize=18)
        plt.show()

    def save(self, path: str):
        with open(path, 'wb') as f:
            pickle.dump(self.clf, f)
