#!/usr/bin/env python3
"""
Model Training Script for Indian House Price Prediction
This script creates sample data, trains the ML model, and saves it for deployment
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error
import pickle
import json
import os
import random

def create_indian_housing_data():
    """Create realistic Indian housing dataset"""
    print("🏗️ Creating Indian housing dataset...")

    np.random.seed(42)
    random.seed(42)
    n_samples = 15000

    # Indian locations
    indian_locations = {
        'maharashtra': ['mumbai', 'pune', 'nashik', 'nagpur', 'aurangabad'],
        'karnataka': ['bangalore', 'mysore', 'hubli', 'mangalore', 'belgaum'],
        'telangana': ['hyderabad', 'warangal', 'nizamabad', 'karimnagar'],
        'delhi': ['new delhi', 'gurgaon', 'noida', 'faridabad', 'ghaziabad'],
        'tamil_nadu': ['chennai', 'coimbatore', 'madurai', 'salem', 'tiruchirappalli'],
        'gujarat': ['ahmedabad', 'surat', 'vadodara', 'rajkot', 'bhavnagar'],
        'rajasthan': ['jaipur', 'jodhpur', 'udaipur', 'kota', 'ajmer'],
        'west_bengal': ['kolkata', 'howrah', 'durgapur', 'asansol', 'siliguri']
    }

    # Generate data
    states = []
    cities = []
    for state, city_list in indian_locations.items():
        state_samples = np.random.randint(1500, 2500)
        for _ in range(min(state_samples, n_samples - len(states))):
            states.append(state)
            cities.append(np.random.choice(city_list))
            if len(states) >= n_samples:
                break
        if len(states) >= n_samples:
            break

    # Pad if needed
    while len(states) < n_samples:
        state = np.random.choice(list(indian_locations.keys()))
        states.append(state)
        cities.append(np.random.choice(indian_locations[state]))

    states = states[:n_samples]
    cities = cities[:n_samples]

    # Create dataset
    data = {
        'State': states,
        'City': cities,
        'Property_Type': np.random.choice(['apartment', 'independent_house', 'villa', 'duplex'], 
                                        n_samples, p=[0.5, 0.25, 0.15, 0.1]),
        'BHK': np.random.choice([1, 2, 3, 4, 5, 6], n_samples, p=[0.15, 0.35, 0.30, 0.15, 0.04, 0.01]),
        'Size_in_SqFt': np.random.randint(400, 4000, n_samples),
        'Year_Built': np.random.randint(1990, 2024, n_samples),
        'Furnished_Status': np.random.choice(['unfurnished', 'semi_furnished', 'fully_furnished'], 
                                           n_samples, p=[0.4, 0.35, 0.25]),
        'Floor_No': np.random.randint(0, 30, n_samples),
        'Total_Floors': np.random.randint(1, 40, n_samples),
        'Nearby_Schools': np.random.randint(1, 15, n_samples),
        'Nearby_Hospitals': np.random.randint(1, 10, n_samples),
        'Public_Transport_Accessibility': np.random.choice(['poor', 'average', 'good', 'excellent'], 
                                                          n_samples, p=[0.2, 0.3, 0.35, 0.15]),
        'Parking_Space': np.random.choice(['no', 'yes'], n_samples, p=[0.3, 0.7]),
        'Security': np.random.choice(['no', 'basic', 'high'], n_samples, p=[0.3, 0.5, 0.2]),
        'Amenities_Score': np.random.randint(0, 10, n_samples),
        'Facing': np.random.choice(['north', 'south', 'east', 'west', 'north_east', 
                                  'north_west', 'south_east', 'south_west'], n_samples),
        'Owner_Type': np.random.choice(['owner', 'broker', 'builder'], n_samples, p=[0.6, 0.3, 0.1]),
        'Availability_Status': np.random.choice(['ready', 'under_construction'], n_samples, p=[0.7, 0.3])
    }

    # Fix floor logic
    for i in range(n_samples):
        if data['Floor_No'][i] >= data['Total_Floors'][i]:
            data['Floor_No'][i] = max(0, data['Total_Floors'][i] - 1)

    # Calculate age
    current_year = 2024
    data['Age_of_Property'] = [current_year - year for year in data['Year_Built']]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Calculate realistic prices
    def calculate_price(row):
        base_price = 2000000  # 20 lakhs base

        state_mult = {
            'maharashtra': 1.8, 'karnataka': 1.4, 'delhi': 2.2, 'telangana': 1.3,
            'tamil_nadu': 1.2, 'gujarat': 1.1, 'rajasthan': 0.9, 'west_bengal': 1.0
        }

        premium_cities = ['mumbai', 'bangalore', 'hyderabad', 'chennai', 'pune', 'gurgaon', 'noida']
        city_mult = 1.5 if row['City'] in premium_cities else 1.0

        prop_mult = {'apartment': 1.0, 'independent_house': 1.3, 'villa': 1.8, 'duplex': 1.4}

        price = base_price
        price *= state_mult.get(row['State'], 1.0)
        price *= city_mult
        price *= prop_mult.get(row['Property_Type'], 1.0)
        price *= (row['BHK'] * 0.3 + 0.7)
        price *= (row['Size_in_SqFt'] / 1000 * 0.8 + 0.2)
        price *= (1 - (row['Age_of_Property'] * 0.015))

        furn_mult = {'unfurnished': 1.0, 'semi_furnished': 1.1, 'fully_furnished': 1.25}
        price *= furn_mult.get(row['Furnished_Status'], 1.0)

        price *= (1 + row['Nearby_Schools'] * 0.02)
        price *= (1 + row['Nearby_Hospitals'] * 0.03)

        transport_mult = {'poor': 0.9, 'average': 1.0, 'good': 1.1, 'excellent': 1.2}
        price *= transport_mult.get(row['Public_Transport_Accessibility'], 1.0)

        price *= (1 + row['Amenities_Score'] * 0.05)
        price *= np.random.uniform(0.8, 1.2)

        return max(500000, price)

    print("💰 Calculating realistic prices...")
    prices = [calculate_price(row) for _, row in df.iterrows()]
    df['Price_INR'] = prices
    df['Price_Lakhs'] = df['Price_INR'] / 100000

    return df

def train_model(df):
    """Train the machine learning model"""
    print("🤖 Training machine learning model...")

    # Prepare features
    numerical_features = ['BHK', 'Size_in_SqFt', 'Year_Built', 'Floor_No', 'Total_Floors',
                         'Nearby_Schools', 'Nearby_Hospitals', 'Amenities_Score', 'Age_of_Property']

    categorical_features = ['State', 'City', 'Property_Type', 'Furnished_Status',
                          'Public_Transport_Accessibility', 'Parking_Space', 'Security',
                          'Facing', 'Owner_Type', 'Availability_Status']

    # Encode categorical variables
    encoders = {}
    df_encoded = df.copy()

    for feature in categorical_features:
        le = LabelEncoder()
        df_encoded[feature] = le.fit_transform(df_encoded[feature])
        encoders[feature] = le

    # Prepare X and y
    feature_columns = numerical_features + categorical_features
    X = df_encoded[feature_columns]
    y = df_encoded['Price_Lakhs']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"📊 Model Performance:")
    print(f"   R² Score: {r2:.4f} ({r2*100:.2f}%)")
    print(f"   MAE: {mae:.2f} Lakhs")

    return model, encoders, r2, mae, feature_columns

def main():
    """Main training function"""
    print("🏠 Indian House Price Predictor - Model Training")
    print("=" * 60)

    # Create directories
    os.makedirs('models', exist_ok=True)
    os.makedirs('data', exist_ok=True)

    # Create dataset
    df = create_indian_housing_data()

    # Save datasets
    df.to_csv('data/indian_housing_data.csv', index=False)
    print("💾 Dataset saved to data/indian_housing_data.csv")

    # Train model
    model, encoders, r2, mae, feature_columns = train_model(df)

    # Save model and encoders
    with open('models/indian_house_price_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open('models/feature_encoders.pkl', 'wb') as f:
        pickle.dump(encoders, f)

    print("💾 Model saved to models/indian_house_price_model.pkl")
    print("💾 Encoders saved to models/feature_encoders.pkl")

    # Save feature info
    feature_info = {
        'model_performance': {
            'r2_score': float(r2),
            'mae': float(mae),
            'accuracy_percentage': float(r2 * 100)
        },
        'feature_columns': feature_columns,
        'target_stats': {
            'min': float(df['Price_Lakhs'].min()),
            'max': float(df['Price_Lakhs'].max()),
            'mean': float(df['Price_Lakhs'].mean()),
            'std': float(df['Price_Lakhs'].std())
        }
    }

    with open('data/indian_feature_info.json', 'w') as f:
        json.dump(feature_info, f, indent=2)

    print("💾 Feature info saved to data/indian_feature_info.json")
    print("🎉 Training completed successfully!")

    # Sample predictions
    print("\n🎯 Sample Predictions:")
    sample_indices = np.random.choice(len(df), 3)
    for i, idx in enumerate(sample_indices):
        actual = df.iloc[idx]['Price_Lakhs']
        print(f"Sample {i+1}: ₹{actual:.1f} Lakhs")

if __name__ == '__main__':
    main()
