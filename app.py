import streamlit as st
from model import load_model, predict_risk
from utils import get_weather
from image_model import predict_image
from PIL import Image

# Load model
model = load_model()

st.set_page_config(page_title="Crop Disease Predictor", layout="centered")

st.title("🌾 Crop Disease Prediction System")

# Sidebar
st.sidebar.header("Input Parameters")

city = st.sidebar.text_input("Enter Location", "Delhi")
crop = st.sidebar.selectbox("Select Crop", ["Rice", "Wheat", "Corn"])

# Get weather
if st.sidebar.button("Get Weather & Predict"):
    try:
        temp, humidity, rainfall = get_weather(city)

        st.subheader("🌦️ Weather Data")
        st.write(f"Temperature: {temp}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Rainfall: {rainfall} mm")

        risk = predict_risk(model, temp, humidity, rainfall)

        st.subheader("⚠️ Disease Risk Prediction")

        if risk < 0.3:
            st.success(f"Low Risk ({round(risk,2)})")
        elif risk < 0.7:
            st.warning(f"Medium Risk ({round(risk,2)})")
        else:
            st.error(f"High Risk ({round(risk,2)})")

            st.subheader("💊 Recommendation")
            st.write("Apply preventive fungicide within 2–3 days")

    except:
        st.error("Invalid location or API issue")

# Image upload
st.subheader("📸 Upload Leaf Image")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    result = predict_image(image)

    st.subheader("🧪 Image Analysis Result")
    st.write(result)
