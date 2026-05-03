import streamlit as st
import pickle
import numpy as np

# Load model
with open("house_price_prediction.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🏠 House Price Prediction System")

# Input
area = st.number_input(
    "Enter Area (sq.ft)",
    min_value=100,
    step=10
)

# Predict Button
if st.button("Predict Price"):

    # Prepare input
    input_data = np.array([[area]])

    # Prediction
    prediction = model.predict(input_data)

    # Convert prediction into float
    predicted_price = float(prediction[0])

    # Display Result
    st.success(f"Estimated House Price: ₹ {predicted_price}")
