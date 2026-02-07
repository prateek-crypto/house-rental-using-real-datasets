"""
Configuration settings for Indian House Price Predictor
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Model configuration
MODEL_CONFIG = {
    'model_path': BASE_DIR / 'models' / 'indian_house_price_model.pkl',
    'encoders_path': BASE_DIR / 'models' / 'feature_encoders.pkl',
    'feature_info_path': BASE_DIR / 'data' / 'indian_feature_info.json'
}

# Data configuration  
DATA_CONFIG = {
    'dataset_path': BASE_DIR / 'data' / 'indian_housing_data.csv',
    'raw_dataset_path': BASE_DIR / 'data' / 'indian_housing_data_raw.csv'
}

# Flask configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'

# Model parameters
MODEL_PARAMS = {
    'test_size': 0.2,
    'random_state': 42,
    'n_estimators': 100
}

# Feature configuration
FEATURE_GROUPS = {
    'numerical': [
        'BHK', 'Size_in_SqFt', 'Year_Built', 'Floor_No', 'Total_Floors',
        'Nearby_Schools', 'Nearby_Hospitals', 'Amenities_Score', 'Age_of_Property'
    ],
    'categorical': [
        'State', 'City', 'Property_Type', 'Furnished_Status',
        'Public_Transport_Accessibility', 'Parking_Space', 'Security',
        'Facing', 'Owner_Type', 'Availability_Status'
    ]
}

# API configuration
API_CONFIG = {
    'version': '1.0.0',
    'title': 'Indian House Price Prediction API',
    'description': 'ML-powered API for predicting house prices in India'
}
