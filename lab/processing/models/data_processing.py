class DataRaw:
    ID = 'id'
    NEIGHBOURHOOD_GROUP = 'neighbourhood_group_cleansed'
    PROPERTY_TYPE = 'property_type'
    ROOM_TYPE = 'room_type'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    ACCOMMODATES = 'accommodates'
    BATHROOMS_TEXT = "bathrooms_text"
    BATHROOMS = 'bathrooms'
    BEDROOMS = 'bedrooms'
    BEDS = 'beds'
    AMENITIES = 'amenities'
    PRICE = 'price'
    SUBSET = ['id', 'neighbourhood_group_cleansed', 'property_type', 'room_type', 'latitude', 'longitude',
              'accommodates', 'bathrooms', 'bedrooms', 'beds', 'amenities', 'price']


class DataProcessed:
    ID = 'id'
    NEIGHBOURHOOD = 'neighbourhood'
    PROPERTY_TYPE = 'property_type'
    ROOM_TYPE = 'room_type'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    ACCOMMODATES = 'accommodates'
    BATHROOMS = 'bathrooms'
    BEDROOMS = 'bedrooms'
    BEDS = 'beds'
    PRICE = 'price'
    CATEGORY = 'category'
    TV = 'TV'
    INTERNET = 'Internet'
    AIR = 'Air_conditioning'
    KITCHEN = 'Kitchen'
    HEATING = 'Heating'
    WIFI = 'Wifi'
    ELEVATOR = 'Elevator'
    BREAKFAST = 'Breakfast'
