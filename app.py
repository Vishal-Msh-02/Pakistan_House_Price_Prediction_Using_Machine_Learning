import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and feature list
model, feature_names = joblib.load("xgboost_house_price_model.pkl")

st.set_page_config(page_title="Pakistan House Price Predictor", layout="centered")
st.title("🏡 Pakistan House Price Prediction App")
st.markdown("Fill in the details below to get an estimated house price:")

# ========= User Inputs =========
property_type = st.selectbox("Property Type", ['Flat', 'House', 'Penthouse'])
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
baths = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
total_area = st.number_input("Total Area (in sq ft)", min_value=100, max_value=50000, value=2000)
city_options = [col.replace("city_", "") for col in feature_names if col.startswith("city_")]
city = st.selectbox("City", sorted(city_options))

# ========= One-Hot Encoding =========

# Start with numerical features
input_data = {
    'bedrooms': bedrooms,
    'baths': baths,
    'Total_Area': (total_area - 3000) / 2000,  # adjust if different scaling used
}

# Encode property type
for pt in ['Flat', 'House', 'Penthouse']:
    input_data[f'property_type_{pt}'] = 1 if property_type == pt else 0

# Encode purpose (you only have 'For Sale')
input_data['purpose_For Sale'] = 1

# Encode city
for c in city_options:
    input_data[f'city_{c}'] = 1 if c == city else 0

# Fill any missing dummy variables (to match training columns)
for col in feature_names:
    if col not in input_data:
        input_data[col] = 0

# Convert to DataFrame in correct column order
input_df = pd.DataFrame([input_data])[feature_names]

# ========= Predict and Show Result =========
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated House Price: Rs. {int(prediction):,}")
