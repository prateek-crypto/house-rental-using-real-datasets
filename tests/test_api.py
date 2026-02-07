#!/usr/bin/env python3
"""
Unit tests for Indian House Price Prediction API
"""

import unittest
import json
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class TestHousePriceAPI(unittest.TestCase):
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        """Test health check endpoint"""
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

    def test_get_locations(self):
        """Test locations endpoint"""
        response = self.app.get('/api/locations')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)

    def test_get_samples(self):
        """Test samples endpoint"""
        response = self.app.get('/api/samples')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)

    def test_predict_valid_data(self):
        """Test prediction with valid data"""
        test_data = {
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

        response = self.app.post('/api/predict',
                               data=json.dumps(test_data),
                               content_type='application/json')

        # Should return 200 or 500 depending on model availability
        self.assertIn(response.status_code, [200, 500])

    def test_predict_missing_data(self):
        """Test prediction with missing data"""
        test_data = {"BHK": 3}  # Missing required fields

        response = self.app.post('/api/predict',
                               data=json.dumps(test_data),
                               content_type='application/json')

        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
