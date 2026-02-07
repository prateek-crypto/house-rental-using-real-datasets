# API Documentation

## Overview
The Indian House Price Predictor API provides endpoints for predicting house prices in India using machine learning.

## Base URL
```
http://localhost:5000/api
```

## Endpoints

### 1. Predict House Price
```http
POST /api/predict
Content-Type: application/json
```

**Request Body:**
```json
{
    "State": "maharashtra",
    "City": "mumbai",
    "Property_Type": "apartment",
    "BHK": 3,
    "Size_in_SqFt": 1200,
    "Year_Built": 2018,
    "Floor_No": 15,
    "Total_Floors": 25,
    "Furnished_Status": "fully_furnished",
    "Nearby_Schools": 8,
    "Nearby_Hospitals": 5,
    "Public_Transport_Accessibility": "excellent",
    "Parking_Space": "yes",
    "Security": "high",
    "Amenities_Score": 9,
    "Facing": "south",
    "Owner_Type": "owner",
    "Availability_Status": "ready",
    "Age_of_Property": 6
}
```

**Response:**
```json
{
    "status": "success",
    "prediction": {
        "price_lakhs": 245.67,
        "price_inr": 24567000,
        "formatted_price": "₹245.67 Lakhs",
        "formatted_price_inr": "₹24,567,000",
        "confidence": 85.2
    },
    "model_info": {
        "algorithm": "Gradient Boosting Regressor",
        "accuracy": "80.97%"
    }
}
```

### 2. Get Available Locations
```http
GET /api/locations
```

### 3. Get Sample Data
```http
GET /api/samples
```

### 4. Health Check
```http
GET /api/health
```

## Error Responses
All error responses follow this format:
```json
{
    "status": "error",
    "message": "Error description"
}
```

## Status Codes
- `200 OK`: Success
- `400 Bad Request`: Invalid input
- `500 Internal Server Error`: Server error
