import streamlit as st
import pickle
import numpy as np
import joblib

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# --------------------------------------------------
# Load Model
# --------------------------------------------------
with open("housing_price_model.pkl", "rb") as file:
    model = joblib.load("housing_price_model.pkl")

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.main-title {
    font-size: 44px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #b0b0b0;
    margin-bottom: 30px;
}

.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
}

.result-box {
    margin-top: 30px;
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(135deg, #11998e, #38ef7d);
    color: black;
    font-size: 28px;
    font-weight: 700;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.markdown('<h1 class="main-title">🏠 House Price Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-powered real estate price estimation</p>', unsafe_allow_html=True)

# --------------------------------------------------
# Input Card
# --------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

area = st.slider("📐 Area (Sqft)", 500, 5000, 2000, step=50)
bedrooms = st.slider("🛏 Bedrooms", 1, 6, 2)
bathrooms = st.slider("🚿 Bathrooms", 1, 5, 2)
age = st.slider("🏚 Age of House (Years)", 0, 50, 10)
distance = st.slider("📍 Distance from City (KM)", 1, 50, 12)

predict_btn = st.button("🔮 Predict Price")

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if predict_btn:
    features = np.array([[area, bedrooms, bathrooms, age, distance]])
    prediction = model.predict(features)[0]

    st.markdown(
        f'<div class="result-box">💰 Estimated Price: ₹ {prediction:,.2f} Lakhs</div>',
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    "<p style='text-align:center; color:#777; margin-top:40px;'>"
    "Built with ❤️ using Streamlit & Machine Learning</p>",
    unsafe_allow_html=True
)

