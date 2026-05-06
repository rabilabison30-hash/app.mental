import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

st.title("Prediksi Kesehatan Mental 🧠")

# Input user
age = st.number_input("Umur", 10, 100)
work_stress = st.slider("Work Stress Level", 1, 10)
sleep = st.slider("Jam Tidur", 1, 12)
social = st.slider("Social Support", 1, 10)

st.subheader("Work Stress Level")
work_stress = st.slider("Work Stress Level", 1, 10)
st.caption("1 = Sangat rendah (tidak stres), 10 = Sangat tinggi (stres berat di pekerjaan)")

st.subheader("Jam Tidur")
sleep = st.slider("Jam Tidur", 1, 12)
st.caption("Jumlah jam tidur per malam. Idealnya 7–8 jam.")

st.subheader("Social Support")
social = st.slider("Social Support", 1, 10)
st.caption("Seberapa banyak dukungan sosial yang kamu rasakan (teman, keluarga, dll)")

if st.button("Prediksi"):
    data = np.array([[age, work_stress, sleep, social]])

    data_scaled = scaler.transform(data)
    data_pca = pca.transform(data_scaled)

    pred = model.predict(data_pca)

    if pred[0] == 1:
        st.error("Berpotensi memiliki masalah kesehatan mental")
    else:
        st.success("Kondisi mental cenderung baik")
        
