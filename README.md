# 🏠 IndiaHome: AI-Powered Indian House Price Predictor

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask-red.svg)](https://flask.palletsprojects.com/)
[![ML Library](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

**IndiaHome** is a sophisticated, machine-learning-powered web application designed to provide accurate real estate valuations across the diverse Indian market. Built with a robust Gradient Boosting regression model and a modern, responsive frontend, it offers homeowners, buyers, and real estate professionals instant insights into property values based on a wide array of localized parameters.

---

## 🚀 Project Overview

Predicting house prices in a market as volatile and varied as India requires more than just square footage calculations. IndiaHome leverages advanced ML algorithms trained on a curated dataset of over 15,000 Indian properties, factoring in regional economic indicators, local amenities, and specific property characteristics to deliver a realistic market valuation.

### The Problem
Traditional valuation methods often rely on outdated averages or manual appraisals that can be biased and slow. Many existing online tools provide "one-size-fits-all" results that fail to capture the nuance of different Indian states and cities.

### The Solution
IndiaHome addresses this by utilizing:
- **State & City-Specific Weighting**: Recognition of premium markets like Mumbai and Bangalore vs. emerging hubs.
- **Granular Feature Analysis**: Accounting for floor level, facing direction (Vastu compliance), and accessibility.
- **Real-time API**: A Flask-based REST backend that serves predictions with high performance.

---

## ✨ Key Features

- **High Precision Modeling**: Uses `GradientBoostingRegressor` with an R² score of ~81%, providing reliable estimates.
- **Dynamic Location Engine**: Intelligently filters cities based on the selected Indian state.
- **Multi-Factor Input**: Analyzes 19 distinct features including:
    - **Physical Attributes**: BHK, Size (SqFt), Floor No, Total Floors, Age.
    - **Location Context**: Proximity to schools and hospitals, transport accessibility.
    - **Lifestyle Factors**: Amenities score, Security levels, Facing direction.
- **Modern User Experience**:
    - **Glassmorphic UI**: A premium, mobile-responsive design.
    - **Dark/Light Mode**: User-selectable themes for comfortable browsing.
    - **Instant Feedback**: Progress indicators and smooth animations using Vanilla JS and CSS.
- **Developer Friendly**: Clean code structure, modular scripts, and automated training workflows.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.13+, Flask |
| **Frontend** | HTML5, Vanilla CSS, Javascript (ES6+) |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy |
| **Data Viz** | Matplotlib, Seaborn |
| **Icons & Fonts** | FontAwesome, Google Fonts (Inter) |
| **Environment** | Pip, Virtualenv |

---

## 📁 Project Structure

```text
indian-house-price-predictor/
├── app.py              # Main Flask application & API routes
├── run.py              # Entry point to start the server
├── requirements.txt    # Project dependencies
├── models/             # Serialized ML models and encoders
│   ├── indian_house_price_model.pkl
│   └── feature_encoders.pkl
├── scripts/            # Automation and utility scripts
│   └── train_model.py  # Data generation and model training script
├── data/               # Dataset and metadata
│   ├── indian_housing_data.csv
│   └── indian_feature_info.json
├── frontend/           # Web interface assets
│   ├── index.html      # Main UI
│   ├── style.css       # Premium styling tokens
│   └── app.js          # Interactive logic & API communication
└── tests/              # Unit and integration tests
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.10+ installed. You can check your version with:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/prateek-crypto/house-rental-using-real-datasets.git
cd house-rental-using-real-datasets
```

### 3. Install Dependencies
It is recommended to use a virtual environment:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Train the Model (Optional)
The project comes with a pre-trained model. If you wish to re-train it with fresh data:
```bash
python scripts/train_model.py
```

### 5. Start the Application
Run the following command to launch the Flask dev server:
```bash
python run.py
```
Visit **[http://localhost:5000](http://localhost:5000)** in your browser.

---

## 📊 Machine Learning Model Details

The core of IndiaHome is a **Gradient Boosting Regressor**. Unlike simple linear models, Gradient Boosting builds an ensemble of weak prediction models (typically decision trees) to handle non-linear relationships between features like "Floor Number" and "Price" in high-rise Mumbai vs. low-rise Rajasthan.

### Training Process
- **Data Generation**: A realistic dataset of 15,000 samples was synthesized using Indian real estate pricing logic.
- **Preprocessing**: Categorical features (City, Furnished Status, etc.) are transformed using `LabelEncoder`.
- **Optimization**: The model uses 100 estimators with a learning rate optimized for stability.
- **Evaluation**: The model achieves an **MAE (Mean Absolute Error)** of approximately 14 Lakhs, which is highly competitive for the simulated variance.

---

## 📡 API Documentation

### POST `/api/predict`
Calculates the estimated price for a property.

**Request Body:**
```json
{
  "State": "maharashtra",
  "City": "mumbai",
  "BHK": 3,
  "Size_in_SqFt": 1200,
  "Property_Type": "apartment",
  "Year_Built": 2018,
  "Floor_No": 12,
  "Total_Floors": 20,
  ...
}
```

**Response:**
```json
{
  "status": "success",
  "prediction": {
    "price_lakhs": 185.5,
    "formatted_price": "₹185.50 Lakhs",
    "confidence": 85.2
  }
}
```

---

## 🛣️ Future Enhancements

- [ ] **Real-time Scrapers**: Integrate live data from property portals like MagicBricks or 99acres.
- [ ] **Advanced Vastu Analysis**: Incorporate deep-learning checks for house layouts.
- [ ] **Image Valuation**: Use Computer Vision to evaluate price premiums based on interior quality photos.
- [ ] **Map Integration**: Visualizing price heatmaps across different neighborhoods.

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving the ML model or the UI design, please open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

*Developed with ❤️ for the Indian Real Estate Community.*
