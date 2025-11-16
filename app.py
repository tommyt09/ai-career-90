# app.py - Titanic Survival Predictor
import streamlit as st
import joblib
import numpy as np

# Load model
@st.cache_resource
def load_model():
    return joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Predictor")
st.write("Built by @Tommytaylor09 | Day 2 of 90 to AI job")

# Input form
col1, col2 = st.columns(2)
with col1:
    pclass = st.selectbox("Ticket Class", [1, 2, 3], help="1 = Rich, 3 = Poor")
    sex = st.selectbox("Sex", ["Male", "Female"])
with col2:
    age = st.slider("Age", 1, 80, 30)
    fare = st.slider("Fare (£)", 0, 500, 32)

# Predict
if st.button("Predict Survival"):
    try:
        model = load_model()
        sex_num = 1 if sex == "Female" else 0
        input_data = np.array([[pclass, sex_num, age, fare]])
        pred = model.predict_proba(input_data)[0][1]
        survival = pred * 100
        st.metric("Survival Chance", f"{survival:.1f}%")
        if survival > 50:
            st.success("🟢 Likely to survive!")
        else:
            st.warning("🔴 High risk...")
    except:
        st.error("Upload `titanic_model.pkl` to repo root to activate AI")
