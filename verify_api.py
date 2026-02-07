import requests
import json

url = "http://localhost:5000/api/predict"

# Sample 1: Mumbai
data1 = {
    "State": "maharashtra", "City": "mumbai", "Property_Type": "apartment",
    "BHK": 3, "Size_in_SqFt": 1200, "Year_Built": 2018, "Floor_No": 15,
    "Total_Floors": 25, "Nearby_Schools": 8, "Nearby_Hospitals": 5,
    "Amenities_Score": 9, "Age_of_Property": 6, "Furnished_Status": "fully_furnished",
    "Public_Transport_Accessibility": "excellent", "Parking_Space": "yes",
    "Security": "high", "Facing": "south", "Owner_Type": "owner", "Availability_Status": "ready"
}

# Sample 2: Bangalore
data2 = {
    "State": "karnataka", "City": "bangalore", "Property_Type": "villa",
    "BHK": 4, "Size_in_SqFt": 2800, "Year_Built": 2015, "Floor_No": 0,
    "Total_Floors": 2, "Nearby_Schools": 12, "Nearby_Hospitals": 7,
    "Amenities_Score": 8, "Age_of_Property": 9, "Furnished_Status": "semi_furnished",
    "Public_Transport_Accessibility": "good", "Parking_Space": "yes",
    "Security": "high", "Facing": "east", "Owner_Type": "owner", "Availability_Status": "ready"
}

try:
    print("Testing Mumbai Apartment...")
    res1 = requests.post(url, json=data1)
    print(f"Status: {res1.status_code}")
    print(f"Result: {res1.json()['prediction']['formatted_price']}")
    
    print("\nTesting Bangalore Villa...")
    res2 = requests.post(url, json=data2)
    print(f"Status: {res2.status_code}")
    print(f"Result: {res2.json()['prediction']['formatted_price']}")
    
    p1 = res1.json()['prediction']['price_lakhs']
    p2 = res2.json()['prediction']['price_lakhs']
    
    if p1 != p2:
        print("\n✅ Verification SUCCESS: Prices are different!")
    else:
        print("\n❌ Verification FAILED: Prices are identical!")
except Exception as e:
    print(f"Error during verification: {e}")
