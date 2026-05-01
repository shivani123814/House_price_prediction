import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("ML Model Deployment")

st.write("Enter feature values:")

feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")
feature4 = st.number_input("Feature 4")
feature5 = st.number_input("Feature 5")
feature6 = st.number_input("Feature 6")
feature7 = st.number_input("Feature 7")
feature8 = st.number_input("Feature 8")
feature9 = st.number_input("Feature 9")
feature10 = st.number_input("Feature 10")

if st.button("Predict"):
    features = np.array([[feature1, feature2, feature3,
                          feature4, feature5, feature6,
                          feature7, feature8, feature9,
                          feature10]])

    prediction = model.predict(features)

    st.success(f"Prediction: {prediction[0]}")