import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("house_price_prediction.pkl", "rb") as file:
    model = pickle.load(file)

# Page Configuration
st.set_page_config(page_title="House Price Prediction App")

# Title
st.title("🏠 House Price Prediction System")

st.write("Enter the area of the house to predict the estimated price")

# User Input
area = st.number_input(
    "Enter Area (in sq.ft)",
    min_value=100,
    step=10
)

# Prediction Button
if st.button("Predict Price"):

    # Convert input into 2D array
    input_data = np.array([[area]])

    # Prediction
    prediction = model.predict(input_data)

    # Show Result
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
