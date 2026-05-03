import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_price_prediction.pkl", 'rb'))

# Page configuration
st.set_page_config(page_title="House Price Prediction")

# Title
st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict the price")

# Input fields
area = st.number_input("Enter Area (in sq.ft)", min_value=100)

bedrooms = st.number_input("Enter Number of Bedrooms", min_value=1)

bathrooms = st.number_input("Enter Number of Bathrooms", min_value=1)

stories = st.number_input("Enter Number of Floors", min_value=1)

parking = st.number_input("Enter Parking Spaces", min_value=0)

# Predict button
if st.button("Predict Price"):

    # Input array
    input_data = np.array([[area, bedrooms, bathrooms, stories, parking]])

    # Prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
