import pickle

from api.app.configs import config_predict
from api.app.schemas.payloads import InputData


class PricePredictor:
    def __init__(self, model_path: str):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, input_data: InputData) -> str:
        input_array = self._preprocess_input(input_data)
        price_category = self.model.predict(input_array)[0]
        price_category_map = config_predict["feature_cols"]["price_category"]
        price_category_value = price_category_map.get(price_category, 0)
        return price_category_value

    def _preprocess_input(self, input_data: InputData):
        neighbourhood_map = config_predict["feature_cols"]["neighbourhood"]
        neighbourhood_value = neighbourhood_map.get(input_data.neighbourhood, 0)
        room_type_map = config_predict["feature_cols"]["room_type"]
        room_type_binary = room_type_map.get(input_data.neighbourhood, 0)
        input_array = [
            input_data.accommodates,
            input_data.bedrooms,
            input_data.bathrooms,
            neighbourhood_value,
            room_type_binary
        ]
        return [input_array]
