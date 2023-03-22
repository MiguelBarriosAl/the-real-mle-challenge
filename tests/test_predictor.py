import unittest

from api.app.configs import config_predict
from api.app.prediction_model.predictor import PricePredictor
from api.app.schemas.payloads import InputData
from utils.utils import BASE_DIR


class TestPricePredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = PricePredictor(BASE_DIR / config_predict["trained_file"])

        self.input_data = InputData(
            id=1,
            accommodates=2,
            bedrooms=1,
            bathrooms=1,
            neighbourhood='Copacabana',
            room_type='Entire home/apt',
            beds=1.0,
            tv=False,
            elevator=True,
            internet=True,
            latitude=-22.987856,
            longitude=-43.197141
        )

    def test_predict_valid_input(self):
        result = self.predictor.predict(self.input_data)
        self.assertIsInstance(result, str)

    def test_predict_valid_output(self):
        result = self.predictor.predict(self.input_data)
        allowed_values = set(['Low', 'Mid', 'High', 'Lux'])
        self.assertIn(result, allowed_values)


if __name__ == '__main__':
    unittest.main()
