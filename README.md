# 🏠 IndiaHome: AI-Powered Indian House Price Predictor

IndiaHome is a state-of-the-art machine learning application designed to estimate property values across the diverse Indian real estate market.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-red)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌐 Live Demo
**Try the AI Predictor now:** [https://house-rental-using-real-datasets.onrender.com](https://house-rental-using-real-datasets.onrender.com)

---

## 🌟 Key Features
- **Accurate Predictions**: Uses Gradient Boosting Regression to capture non-linear market trends.
- **Dynamic City Loading**: Automatically updates city lists based on the selected Indian state.
- **Comprehensive Analysis**: Considers features like BHK, Size, Furnishing, Vastu (Facing), Amenities, and Proximity to services.
- **Global Deployment Ready**: Ready to be hosted globally via ngrok or cloud services.
- **Modern UI**: Clean, responsive, glassmorphic design for all devices.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-Learn (Gradient Boosting Regressor)
- **Data Handling**: Pandas, NumPy
- **Frontend**: HTML5, Vanilla CSS, JavaScript (ES6)

## 📁 Project Structure
- `app.py`: Main API and route handler.
- `run.py`: Production-ready server launcher.
- `scripts/train_model.py`: Automates data generation and model training.
- `models/`: Contains the serialized ML model and encoders.
- `frontend/`: All web assets including styles and interactive logic.

## 🚀 Quick Start
1. **Clone the project**
   ```bash
   git clone https://github.com/prateek-crypto/house-rental-using-real-datasets.git
   cd indian-house-price-predictor
   ```
2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**
   ```bash
   python run.py
   ```
4. **Access the App**
   Visit `http://localhost:5000` or use your Public IP for global access.

## 📊 Model Training
To retrain the model with fresh synthetic data:
```bash
python scripts/train_model.py
```
*Current model accuracy (R² Score) is approximately 81%.*

## 🛡️ License
Distributed under the MIT License. See `LICENSE.md` for more information.

---
*Created with ❤️ for the Indian Real Estate Community.*
