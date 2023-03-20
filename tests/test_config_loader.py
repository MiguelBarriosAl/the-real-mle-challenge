import unittest
import json
from pathlib import Path
from lab.processing.configs.config_loader import load_config_file


class TestConfigLoader(unittest.TestCase):
    def test_load_config_file(self):
        config_file = "test_config.json"
        config_data = {
            "raw_file": "data/raw/listings.csv",
            "preprocess_file": "data/processed/new_processed_listings.csv",
            "min_price": 10,
            "bins_price": [10, 90, 180, 400, None],
            "labels_price": [0, 1, 2, 3],
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
        with open(config_file, "w") as f:
            json.dump(config_data, f)

        # Test if file is loaded correctly
        result = load_config_file(Path(config_file))
        self.assertEqual(result, config_data)

        # Test if file does not exist
        with self.assertRaises(FileNotFoundError):
            load_config_file(Path("nonexistent_config_file.json"))

        # Clean up test file
        Path(config_file).unlink()


if __name__ == '__main__':
    unittest.main()
