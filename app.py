

import streamlit as st
import numpy as np
import joblib
model = joblib.load("housing_price_model.pkl")
st.title("House Price Prediction (Lakhs)")
st.write("Enter the inputs and hit predict to get a estimated price for your house!")

#2

area_sqft = st.number_input("Area (Sqft)", min_value=200.0,max_value=10000.0, value=1200.0, step=50.0)
bedrooms = st.number_input("Bedrooms", min_value=1,max_value=10, value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1,max_value=10, value=1, step=1)
age_years = st.number_input("Age of House(Years)", min_value=0.0,max_value=100.0, value=10.0, step=1.0)
distance_city_km = st.number_input("Distance from City (KM)", min_value=0.1,max_value=600.0, value=12.0, step=0.5)


#predict

if st.button("Predict Price"):
  X=np.array([[area_sqft,bedrooms,bathrooms,age_years,distance_city_km]])
  pred=model.predict(X)[0]
  st.success(f"Estimated Price: {pred:.2f} lakhs")
