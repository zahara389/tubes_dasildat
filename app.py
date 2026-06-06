import streamlit as st

# Set halaman utama agar melebar dan responsif
st.set_page_config(
    page_title="Sleep Quality Analytics",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk tampilan Dashboard Modern & Minimalis (Bukan gaya AI kaku)
st.markdown("""
    <style>
        /* Mengubah font utama aplikasi */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        /* Style untuk Banner Utama */
        .main-banner {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            padding: 40px;
            border-radius: 16px;
            color: white;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }
        .main-banner h1 {
            color: #f8fafc !important;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        .main-banner p {
            color: #94a3b8;
            font-size: 1.1rem;
        }
        /* Style untuk Card Anggota Kelompok */
        .team-card {
            background-color: #ffffff;
            padding: 24px;
            border-radius: 12px;
            border-left: 5px solid #38bdf8;
            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
            margin-bottom: 15px;
        }
        .team-title {
            font-weight: 600;
            color: #1e293b;
            font-size: 1.2rem;
            margin-bottom: 5px;
        }
        .team-role {
            color: #64748b;
            font-size: 0.95rem;
        }
    </style>
""", unsafe_allow_html=True)

# Banner Utama
st.markdown("""
    <div class="main-banner">
        <h1>Sleep Quality Prediction Dashboard</h1>
        <p>Platform analitik berbasis Machine Learning untuk mendeteksi gangguan dan kualitas tidur secara akurat.</p>
    </div>
""", unsafe_allow_html=True)

# Layout Dua Kolom untuk Konten Utama
col_info, col_team = st.columns([1.3, 1])

with col_info:
    st.subheader("📋 Latar Belakang Proyek")
    st.markdown("""
    Kualitas tidur merupakan salah satu pilar utama kesehatan fisik dan mental manusia. 
    Melalui proyek analitik data ini, kami mengeksplorasi faktor-faktor dominan yang memengaruhi 
    pola tidur seseorang—seperti tingkat stres, aktivitas fisik, usia, dan durasi tidur.
    
    Aplikasi ini mengintegrasikan **4 algoritma klasifikasi utama** yang dilatih menggunakan data riil, 
    guna membandingkan performa terbaik demi menghasilkan model prediksi dengan tingkat reliabilitas tertinggi.
    """)
    
    st.info("💡 **Petunjuk Penggunaan:** Silakan gunakan menu navigasi di sebelah kiri untuk melihat detail performa tiap model (Halaman 1-4) atau melakukan pengujian data baru (Halaman 5).")

with col_team:
    st.subheader("👥 Tim Pengembang Sistem")
    
    # Daftar Anggota Kelompok (Sesuaikan dengan nama teman sekelompokmu ya)
    st.markdown("""
        <div class="team-card">
            <div class="team-title">Zahara</div>
            <div class="team-role">Data Scientist & Developer K-NN</div>
        </div>
        <div class="team-card">
            <div class="team-title">Anisa</div>
            <div class="team-role">Data Scientist & Developer Decision Tree</div>
        </div>
        <div class="team-card">
            <div class="team-title">Athaya</div>
            <div class="team-role">Data Scientist & Developer Neural Network</div>
        </div>
        <div class="team-card">
            <div class="team-title">Aqila</div>
            <div class="team-role">Data Scientist & Developer SVM</div>
        </div>
    """, unsafe_allow_html=True)