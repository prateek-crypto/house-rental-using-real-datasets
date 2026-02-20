// Indian House Price Prediction App JavaScript

class IndianHousePricePredictor {
    constructor() {
        this.locations = {
            "maharashtra": ["mumbai", "pune", "nashik", "nagpur", "aurangabad"],
            "karnataka": ["bangalore", "mysore", "hubli", "mangalore", "belgaum"], 
            "telangana": ["hyderabad", "warangal", "nizamabad", "karimnagar"],
            "delhi": ["new delhi", "gurgaon", "noida", "faridabad", "ghaziabad"],
            "tamil_nadu": ["chennai", "coimbatore", "madurai", "salem", "tiruchirappalli"],
            "gujarat": ["ahmedabad", "surat", "vadodara", "rajkot", "bhavnagar"],
            "rajasthan": ["jaipur", "jodhpur", "udaipur", "kota", "ajmer"],
            "west_bengal": ["kolkata", "howrah", "durgapur", "asansol", "siliguri"]
        };

        this.sampleData = {
            mumbai: {
                State: "maharashtra",
                City: "mumbai",        
                Property_Type: "apartment",
                BHK: 3,
                Size_in_SqFt: 1200,
                Year_Built: 2018,
                Floor_No: 15,
                Total_Floors: 25,
                Furnished_Status: "fully_furnished",
                Nearby_Schools: 8,
                Nearby_Hospitals: 5,
                Public_Transport_Accessibility: "excellent",
                Parking_Space: "yes",
                Security: "high",
                Amenities_Score: 9,
                Facing: "south",
                Owner_Type: "owner",
                Availability_Status: "ready"
            },
            bangalore: {
                State: "karnataka",
                City: "bangalore",
                Property_Type: "villa",
                BHK: 4,
                Size_in_SqFt: 2800,
                Year_Built: 2015,
                Floor_No: 0,
                Total_Floors: 2,
                Furnished_Status: "semi_furnished",
                Nearby_Schools: 12,
                Nearby_Hospitals: 7,
                Public_Transport_Accessibility: "good",
                Parking_Space: "yes",
                Security: "high",
                Amenities_Score: 8,
                Facing: "east",
                Owner_Type: "owner",
                Availability_Status: "ready"
            }
        };

        this.init();
    }

    init() {
        this.bindEvents();
        this.updateCityOptions();
        this.updateAgeOfProperty();
    }

    bindEvents() {
        // State change event
        document.getElementById('State').addEventListener('change', () => {
            this.updateCityOptions();
        });

        // Year built change event  
        document.getElementById('Year_Built').addEventListener('change', () => {
            this.updateAgeOfProperty();
        });

        // Sample data buttons
        document.getElementById('sampleMumbai').addEventListener('click', () => {
            this.fillSampleData('mumbai');
        });

        document.getElementById('sampleBangalore').addEventListener('click', () => {
            this.fillSampleData('bangalore');
        });

        // Form submission
        document.getElementById('predictionForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.handlePrediction();
        });

        // Reset form
        document.getElementById('resetForm').addEventListener('click', () => {
            this.resetForm();
        });

        // Theme toggle
        document.getElementById('themeToggle').addEventListener('click', () => {
            this.toggleTheme();
        });
    }

    updateCityOptions() {
        const stateSelect = document.getElementById('State');
        const citySelect = document.getElementById('City');
        const selectedState = stateSelect.value;

        // Clear city options
        citySelect.innerHTML = '<option value="">Select City</option>';

        if (selectedState && this.locations[selectedState]) {
            this.locations[selectedState].forEach(city => {
                const option = document.createElement('option');
                option.value = city;
                option.textContent = city.charAt(0).toUpperCase() + city.slice(1).replace('_', ' ');
                citySelect.appendChild(option);
            });
        }
    }

    updateAgeOfProperty() {
        const yearBuilt = document.getElementById('Year_Built').value;
        const currentYear = new Date().getFullYear();
        const age = yearBuilt ? currentYear - parseInt(yearBuilt) : 5;
        document.getElementById('Age_of_Property').value = Math.max(0, age);
    }

    fillSampleData(sampleType) {
        const data = this.sampleData[sampleType];
        if (!data) return;

        Object.keys(data).forEach(key => {
            const element = document.getElementById(key);
            if (element) {
                element.value = data[key];
                // Trigger change event for dependent fields
                if (key === 'State') {
                    this.updateCityOptions();
                    setTimeout(() => {
                        document.getElementById('City').value = data.City;
                    }, 100);
                }
                if (key === 'Year_Built') {
                    this.updateAgeOfProperty();
                }
            }
        });

        // Scroll to form
        document.getElementById('predictionForm').scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });

        // Show success message
        this.showNotification('Sample data loaded successfully!', 'success');
    }

    async handlePrediction() {
        const form = document.getElementById('predictionForm');
        const submitButton = form.querySelector('.predict-btn');
        const resultsCard = document.getElementById('resultsCard');

        // Show loading state
        document.body.classList.add('loading');
        submitButton.innerHTML = '<i class="fas fa-spinner"></i> Predicting...';

        try {
            // Collect form data
            const formData = new FormData(form);
            const data = {};

            // Get all form fields
            const fields = [
                'State', 'City', 'Property_Type', 'BHK', 'Size_in_SqFt', 'Year_Built',
                'Floor_No', 'Total_Floors', 'Furnished_Status', 'Facing', 'Nearby_Schools',
                'Nearby_Hospitals', 'Public_Transport_Accessibility', 'Amenities_Score',
                'Parking_Space', 'Security', 'Owner_Type', 'Availability_Status', 'Age_of_Property'
            ];

            fields.forEach(field => {
                const element = document.getElementById(field);
                if (element) {
                    data[field] = element.value;
                }
            });

            // Convert numeric fields
            const numericFields = ['BHK', 'Size_in_SqFt', 'Year_Built', 'Floor_No', 'Total_Floors', 
                                 'Nearby_Schools', 'Nearby_Hospitals', 'Amenities_Score', 'Age_of_Property'];
            numericFields.forEach(field => {
                if (data[field]) {
                    data[field] = parseFloat(data[field]);
                }
            });

            console.log('Sending prediction data:', data);

            // Make API call
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            console.log('Prediction result:', result);

            if (result.status === 'success') {
                this.displayResults(result);
            } else {
                this.showNotification(result.message || 'Prediction failed', 'error');
            }

        } catch (error) {
            console.error('Prediction error:', error);
            this.showNotification('Network error. Please try again.', 'error');
        } finally {
            // Hide loading state
            document.body.classList.remove('loading');
            submitButton.innerHTML = '<i class="fas fa-calculator"></i> Predict House Price';
        }
    }

    displayResults(result) {
        const resultsCard = document.getElementById('resultsCard');
        const prediction = result.prediction;

        // Update result elements
        document.getElementById('predictedPrice').textContent = prediction.formatted_price;
        document.getElementById('predictedPriceINR').textContent = prediction.formatted_price_inr;
        document.getElementById('confidence').textContent = `${prediction.confidence}% Confidence`;

        // Show results card
        resultsCard.style.display = 'block';
        resultsCard.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });

        this.showNotification('Price prediction completed successfully!', 'success');
    }

    resetForm() {
        document.getElementById('predictionForm').reset();
        document.getElementById('resultsCard').style.display = 'none';
        this.updateCityOptions();
        this.showNotification('Form reset successfully!', 'info');
    }

    toggleTheme() {
        document.body.classList.toggle('dark-theme');
        const themeIcon = document.querySelector('#themeToggle i');
        if (document.body.classList.contains('dark-theme')) {
            themeIcon.classList.replace('fa-moon', 'fa-sun');
        } else {
            themeIcon.classList.replace('fa-sun', 'fa-moon');
        }
    }

    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;

        // Add styles
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#3b82f6'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            z-index: 1000;
            animation: slideIn 0.3s ease-out;
            max-width: 300px;
            word-wrap: break-word;
        `;

        // Add animation styles
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(100%); opacity: 0; }
            }
        `;
        document.head.appendChild(style);

        // Add to page
        document.body.appendChild(notification);

        // Auto remove after 3 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-out';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }, 3000);
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new IndianHousePricePredictor();
    console.log('🏠 Indian House Price Predictor initialized!');
});

// Additional utility functions
window.formatIndianCurrency = (amount) => {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 2
    }).format(amount);
};

window.formatLakhs = (amount) => {
    const lakhs = amount / 100000;
    return `₹${lakhs.toFixed(2)} Lakhs`;
};

// Service worker registration (for PWA support)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then((registration) => {
                console.log('SW registered: ', registration);
            })
            .catch((registrationError) => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
