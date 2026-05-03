import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_prediction.pkl")

# Page title
st.title("🏠 House Price Prediction System")

st.write("Enter area to predict house price")

# User input
area = st.number_input(
    "Enter Area (sq.ft)",
    min_value=100,
    step=10
)

# Prediction button
if st.button("Predict Price"):

    # Convert input to 2D array
    input_data = np.array([[area]])

    # Predict
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Estimated House Price: ₹ {prediction[0]}")
