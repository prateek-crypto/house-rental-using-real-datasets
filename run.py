#!/usr/bin/env python3
"""
Application Runner for Indian House Price Predictor
"""

import os
import sys
from app import app

def main():
    print("🏠 Indian House Price Predictor")
    print("🚀 Starting Flask application...")

    # Check if model files exist
    if not os.path.exists('models/indian_house_price_model.pkl'):
        print("⚠️  Model files not found!")
        print("Please run: python scripts/train_model.py")
        return

    try:
        app.run(
            debug='--debug' in sys.argv,
            host='0.0.0.0',
            port=5000
        )
    except KeyboardInterrupt:
        print("\n👋 Application stopped")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
