import streamlit as st
import pandas as pd
import joblib
import os

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Prediksi Kualitas Tidur",
    layout="wide"
)

st.markdown("""
<div style="background: linear-gradient(135deg, #1e3a8a 0%, #0d9488 100%);
            padding:20px;
            border-radius:10px;
            margin-bottom:20px;">
    <h2 style="color:white; text-align:center; margin:0;">
        🩺 Ruang Pemeriksaan Kualitas Tidur
    </h2>
</div>
""", unsafe_allow_html=True)

# =====================================
# LOAD MODEL
# =====================================
@st.cache_resource
def load_pipeline():
    model_path = "models/model_final.pkl"

    if not os.path.exists(model_path):
        return None

    return joblib.load(model_path)

pipeline = load_pipeline()

if pipeline is None:
    st.error("❌ File model_final.pkl tidak ditemukan di folder models")
    st.stop()

# =====================================
# FORM INPUT
# =====================================
with st.form("form_pasien"):

    st.subheader("📝 Masukkan Data Pasien")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Usia",
            min_value=15,
            max_value=80,
            value=25
        )

        gender = st.selectbox(
            "Jenis Kelamin",
            ["Female", "Male", "Other"]
        )

        occupation = st.selectbox(
            "Pekerjaan",
            [
                "Designer",
                "Doctor",
                "Freelancer",
                "Manager",
                "Researcher",
                "Software Engineer",
                "Student",
                "Teacher"
            ]
        )

        sleep_duration_hours = st.number_input(
            "Durasi Tidur (Jam)",
            min_value=1.0,
            max_value=15.0,
            value=7.0
        )

        phone_usage = st.number_input(
            "Penggunaan HP Sebelum Tidur (Menit)",
            min_value=0,
            max_value=300,
            value=30
        )

        daily_screen = st.number_input(
            "Screen Time Harian (Jam)",
            min_value=0.0,
            max_value=24.0,
            value=5.0
        )

    with col2:
        stress_level = st.slider(
            "Level Stres",
            min_value=1.0,
            max_value=10.0,
            value=5.0
        )

        mental_fatigue = st.slider(
            "Kelelahan Mental",
            min_value=1.0,
            max_value=10.0,
            value=3.0
        )

        physical_activity = st.number_input(
            "Aktivitas Fisik (Menit)",
            min_value=0,
            max_value=300,
            value=45
        )

        caffeine = st.number_input(
            "Konsumsi Kafein (Gelas)",
            min_value=0,
            max_value=10,
            value=1
        )

        notifications = st.number_input(
            "Jumlah Notifikasi per Hari",
            min_value=0,
            max_value=500,
            value=50
        )

    submit_button = st.form_submit_button(
        "🔍 Jalankan Analisis"
    )

# =====================================
# PREDIKSI
# =====================================
if submit_button:

    data_input = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "occupation": [occupation],
        "daily_screen_time_hours": [daily_screen],
        "phone_usage_before_sleep_minutes": [phone_usage],
        "sleep_duration_hours": [sleep_duration_hours],
        "stress_level": [stress_level],
        "caffeine_intake_cups": [caffeine],
        "physical_activity_minutes": [physical_activity],
        "notifications_received_per_day": [notifications],
        "mental_fatigue_score": [mental_fatigue]
    })

    try:

        hasil = pipeline.predict(data_input)

        st.markdown("---")

        st.subheader("📋 Hasil Analisis")

        if hasil[0] == 1:
            st.error(
                "🚨 Kualitas Tidur Diprediksi BURUK (Poor Sleep)"
            )
        else:
            st.success(
                "✅ Kualitas Tidur Diprediksi NORMAL / BAIK"
            )

        with st.expander("Lihat Data Input"):
            st.dataframe(data_input)

    except Exception as e:
        st.error(f"❌ Error saat prediksi: {str(e)}")