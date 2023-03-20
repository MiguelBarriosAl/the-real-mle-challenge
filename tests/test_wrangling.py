import unittest
import pandas as pd
from lab.processing.data_wrangling.wrangling import Wrangling
from lab.processing.models.data_processing import DataRaw, DataProcessed


class TestWrangling(unittest.TestCase):
    def setUp(self):
        self.config = {
            "mapping_columns": {
                "neighbourhood": {"Bronx": 1, "Brooklyn": 2, "Manhattan": 3, "Queens": 4, "Staten Island": 5},
                "room_type": {"Entire home/apt": 1, "Private room": 2, "Shared room": 3}
            },
            "bins_price": [0, 100, 200, 300, 400, 500],
            "labels_price": [1, 2, 3, 4, 5],
            "min_price": 50
        }
        self.wrangling = Wrangling(self.config)

    def test_rename_column_bathrooms(self):
        test_data = {
            'id': [1, 2, 3],
            'neighbourhood_group_cleansed': ['Manhattan', 'Brooklyn', 'Queens'],
            'property_type': ['Apartment', 'House', 'Apartment'],
            'room_type': ['Entire home/apt', 'Private room', 'Shared room'],
            'latitude': [40.71, 40.68, 40.73],
            'longitude': [-74.01, -73.94, -73.87],
            'accommodates': [2, 4, 1],
            'bathrooms_text': ['1 bath', '2 baths', '1 shared bath'],
            'bedrooms': [1, 2, 1],
            'beds': [1, 3, 1],
            'amenities': ['TV, Wifi', 'Kitchen, Gym', 'Elevator'],
            'price': ['$100.00', '$200.00', '$50.00']
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.rename_column_bathrooms(test_df)
        expected_columns = [
            'id', 'neighbourhood_group_cleansed', 'property_type', 'room_type',
            'latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms',
            'beds', 'amenities', 'price'
        ]
        assert list(result.columns) == expected_columns

    def test_rename_column_neighbourhood(self):
        test_data = {
            'id': [1, 2, 3],
            'neighbourhood_group_cleansed': ['Manhattan', 'Brooklyn', 'Queens'],
            'property_type': ['Apartment', 'House', 'Apartment'],
            'room_type': ['Entire home/apt', 'Private room', 'Shared room'],
            'latitude': [40.71, 40.68, 40.73],
            'longitude': [-74.01, -73.94, -73.87],
            'accommodates': [2, 4, 1],
            'bathrooms': [1, 2, 1],
            'bedrooms': [1, 2, 1],
            'beds': [1, 3, 1],
            'amenities': ['TV, Wifi', 'Kitchen, Gym', 'Elevator'],
            'price': ['$100.00', '$200.00', '$50.00']
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.rename_column_neighbourhood(test_df)
        assert "neighbourhood" in result.columns
        assert "neighbourhood_group_cleansed" not in result.columns

    def test_categorize_neighbourhood(self):
        test_data = {
            'id': [1, 2, 3],
            'neighbourhood': ['Manhattan', 'Brooklyn', 'Queens'],
            'property_type': ['Apartment', 'House', 'Apartment'],
            'room_type': ['Entire home/apt', 'Private room', 'Shared room'],
            'latitude': [40.71, 40.68, 40.73],
            'longitude': [-74.01, -73.94, -73.87],
            'accommodates': [2, 4, 1],
            'bathrooms': [1, 2, 1],
            'bedrooms': [1, 2, 1],
            'beds': [1, 3, 1],
            'amenities': ['TV, Wifi', 'Kitchen, Gym', 'Elevator'],
            'price': ['$100.00', '$200.00', '$50.00']
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.categorize_neighbourhood(test_df)
        expected_neighbourhoods = [3, 2, 4]
        assert list(result['neighbourhood']) == expected_neighbourhoods

    def test_filter_price_by_minimum(self):
        test_data = {
            'id': [1, 2, 3],
            'neighbourhood': ['Manhattan', 'Brooklyn', 'Queens'],
            'property_type': ['Apartment', 'House', 'Apartment'],
            'room_type': ['Entire home/apt', 'Private room', 'Shared room'],
            'latitude': [40.71, 40.68, 40.73],
            'longitude': [-74.01, -73.94, -73.87],
            'accommodates': [2, 4, 1],
            'bathrooms': [1, 2, 1],
            'bedrooms': [1, 2, 1],
            'beds': [1, 3, 1],
            'amenities': ['TV, Wifi', 'Kitchen, Gym', 'Elevator'],
            'price': ['$100.00', '$200.00', '$50.00']
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.filter_price_by_minimum(test_df)
        assert result['price'].min() >= self.config['min_price']

    def test_dropna(self):
        test_data = {
            'id': [1, 2, 3],
            'neighbourhood': ['Manhattan', None, 'Queens'],
            'property_type': ['Apartment', 'House', 'Apartment'],
            'room_type': ['Entire home/apt', 'Private room', 'Shared room'],
            'latitude': [40.71, 40.68, 40.73],
            'longitude': [-74.01, -73.94, -73.87],
            'accommodates': [2, None, 1],
            'bathrooms': [1, 2, 1],
            'bedrooms': [1, None, 1],
            'beds': [1, 3, 1],
            'amenities': ['TV, Wifi', 'Kitchen, Gym', 'Elevator'],
            'price': ['$100.00', None, '$50.00']
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.dropna(test_df)
        assert len(result) == 2
        assert result.isnull().sum().sum() == 0

    def test_price_category(self):
        test_data = {
            'id': [1, 2, 3, 4],
            'neighbourhood': ['Brooklyn', 'Manhattan', 'Queens', 'Bronx'],
            'room_type': ['Entire home/apt', 'Private room', 'Entire home/apt', 'Shared room'],
            'bathrooms': [1, 2, 1, 0],
            'bedrooms': [1, 2, 1, 1],
            'beds': [1, 3, 2, 1],
            'amenities': ['TV, Wifi', 'Kitchen', 'TV, Kitchen, Gym', 'Wifi'],
            'price': [90, 220, 170, 40]
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.price_category(test_df)
        expected_categories = pd.cut(test_df[DataProcessed.PRICE], bins=self.config['bins_price'],
                                     labels=self.config['labels_price'])
        assert list(result[DataProcessed.CATEGORY]) == list(expected_categories)

    def test_preprocess_amenities_column(self):
        test_data = {
            'id': [1, 2],
            'neighbourhood_group_cleansed': ['Manhattan', 'Brooklyn'],
            'property_type': ['Apartment', 'House'],
            'room_type': ['Entire home/apt', 'Private room'],
            'latitude': [40.71, 40.68],
            'longitude': [-74.01, -73.94],
            'accommodates': [2, 4],
            'bathrooms': [1, 2],
            'bedrooms': [1, 2],
            'beds': [1, 3],
            'amenities': ['TV, Wifi', 'Kitchen, Gym'],
            'price': [100, 200]
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.preprocess_amenities_column(test_df)
        expected_columns = [
            'id', 'neighbourhood_group_cleansed', 'property_type', 'room_type',
            'latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms',
            'beds', 'price', 'TV', 'Internet', 'Air_conditioning', 'Kitchen',
            'Heating', 'Wifi', 'Elevator', 'Breakfast'
        ]
        assert list(result.columns) == expected_columns

    def test_categorize_room_type(self):
        test_data = {
            'id': [1, 2],
            'neighbourhood_group_cleansed': ['Manhattan', 'Brooklyn'],
            'property_type': ['Apartment', 'House'],
            'room_type': ['Entire home/apt', 'Private room'],
            'latitude': [40.71, 40.68],
            'longitude': [-74.01, -73.94],
            'accommodates': [2, 4],
            'bathrooms': [1, 2],
            'bedrooms': [1, 2],
            'beds': [1, 3],
            'amenities': ['TV, Wifi', 'Kitchen, Gym'],
            'price': [100, 200]
        }
        test_df = pd.DataFrame(test_data)
        result = self.wrangling.categorize_room_type(test_df)
        expected_values = [1, 2]
        assert result['room_type'].tolist() == expected_values
