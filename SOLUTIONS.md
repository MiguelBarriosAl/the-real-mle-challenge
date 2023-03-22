# Airbnb Price Prediction
Description
Airbnb Price Prediction is a project that aims to predict the price of Airbnb listings based on various factors such as location, amenities, and reviews. The project involves processing Airbnb data and training classification models to predict the price range of a listing.

# Folder Structure

    ├───api
    │   ├───app
    │   │   ├───prediction_model
    │   │   ├───schemas
    │   │  
    │   └───main.py
    ├───lab
    │   ├───analysis
    │   ├───processing
    │   ├───configs
    │   ├───data_wrangling
    │   ├───models
    │   └───train
    │   
    ├───requirements.txt
    ├───tests
    └───utils
    
* api: Contains the main application code, including the prediction model and schemas for data validation.
* lab: Contains Jupyter notebooks and scripts for data analysis, processing, and model training.
* tests: Contains test files for the project.
* utils: Contains utility scripts and modules for the project.

## Data Processing
The **lab/processing/data_wrangling** directory contains the main.py and wrangling.py files, which are responsible for 
processing the data in the dataframe and storing it in the data/processed directory.


## Model Training
The **lab/processing/train** directory contains the train.py file, which reads in the processed dataframe and trains the 
classification model. The trained model is then saved in the data/processed directory for use by the main application.

# API Usage
To use this API, you can build a Docker image using the included Dockerfile. First, navigate to the root directory 
of the project and run the following command to build the Docker image:

    docker build -t airbnb-predictor .


This will create a Docker image called airbnb-predictor that contains the application code and its dependencies.

Once you've built the Docker image, you can start the application by running the following command:

    docker run -p 8000:8000 airbnb-predictor

This will start the application on port 8000.
## Services
### /healthcheck
You can then make requests to the API using the following endpoint:

    curl -X 'GET' \
      'http://127.0.0.1:8000/' \
      -H 'accept: application/json'

Response Body:

    {
      "HealthCheck": "Ok",
      "Version": "0.0.1"
    }

### /predict
You can then make requests to the API using the following endpoint:

    curl -X 'POST' \
      'http://127.0.0.1:8000/predict' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
        "id": 1001,
        "accommodates": 4,
        "room_type": "Entire home/apt",
        "beds": 4,
        "bedrooms": 4,
        "bathrooms": 2,
        "neighbourhood": "Manhattan",
        "tv": 1,
        "elevator": 1,
        "internet": 0,
        "latitude": 40.71383,
        "longitude": -73.9658
    }'

Response Body:

    {
      "id": 1001,
      "price_range": "high"
    }

# Testing
To run the tests, you can use the following command:

    python -m unittest discover tests
