import streamlit as st
import requests

st.title("House Price Predictor")

longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age")
total_rooms = st.number_input("Total Rooms")
total_bedrooms = st.number_input("Total Bedrooms")
population = st.number_input("Population")
households = st.number_input("Households")
median_income = st.number_input("Median Income")

if st.button("Predict Price"):
    data = {
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    result = response.json()

    st.success(f"Predicted Price: ${result['predicted_price']:.2f}")
