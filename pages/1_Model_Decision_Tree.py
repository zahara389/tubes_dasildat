import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="Decision Tree Deep-Dive",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Styling Kelas Atas (Clean, Profesional, No AI-ish look)
st.markdown("""
    <style>
        .main-header {
            background: linear-gradient(135deg, #1e3a8a 0%, #0d9488 100%);
            padding: 30px;
            border-radius: 12px;
            color: white;
            margin-bottom: 25px;
        }
        .main-header h1 { color: #ffffff !important; margin: 0; font-size: 2.2rem; font-weight: 700; }
        .main-header p { color: #ccfbf1; margin: 5px 0 0 0; font-size: 1rem; }
        
        .section-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .kpi-val { font-size: 2.2rem; font-weight: 700; color: #0f172a; line-height: 1; }
        .kpi-lbl { font-size: 0.85rem; color: #64748b; font-weight: 600; text-transform: uppercase; margin-top: 8px; }
        
        .status-badge {
            background-color: #f0fdf4;
            color: #166534;
            padding: 12px 18px;
            border-radius: 8px;
            border-left: 4px solid #22c55e;
            font-weight: 500;
            font-size: 0.95rem;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Header Banner Atas
st.markdown("""
    <div class="main-header">
        <h1>🌳 Algoritma Inteligensia: Decision Tree</h1>
        <p>Analisis mendalam optimasi model terbaik kelompok dalam klasifikasi pola dan kualitas tidur.</p>
    </div>
""", unsafe_allow_html=True)

# 4. KPI Scoreboard Section (Menggunakan struktur columns modern)
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📊 Evaluasi Kuantitatif Akhir (Data Uji Murni)</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div style="text-align: center; padding: 15px; background: #fafafa; border-radius: 8px; border-bottom: 4px solid #10b981;"><div class="kpi-val">85.87%</div><div class="kpi-lbl">Akurasi Global</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div style="text-align: center; padding: 15px; background: #fafafa; border-radius: 8px; border-bottom: 4px solid #3b82f6;"><div class="kpi-val">91.52%</div><div class="kpi-lbl">Presisi Kelas</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div style="text-align: center; padding: 15px; background: #fafafa; border-radius: 8px; border-bottom: 4px solid #f59e0b;"><div class="kpi-val">85.87%</div><div class="kpi-lbl">Sensitivitas / Recall</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div style="text-align: center; padding: 15px; background: #f0fdf4; border-radius: 8px; border-bottom: 4px solid #8b5cf6;"><div class="kpi-val" style="color: #15803d;">0.8777</div><div class="kpi-lbl" style="color: #166534;">F1-Score Harmonik</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. Layout Dua Kolom Utama (Visual Chart vs Analisis Teknis)
col_graph, col_text = st.columns([1.1, 0.9])

with col_graph:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📈 Grafik Komparasi: Mengapa Model Ini Menang?</div>', unsafe_allow_html=True)
    
    # Bikin data chart interaktif biar ga monoton polosan teks
    chart_data = pd.DataFrame({
        'Model Algoritma': ['K-NN (Zahara)', 'SVM (Aqila)', 'Neural Network (Athaya)', 'Decision Tree (Anisa)'],
        'F1-Score Kelompok': [0.4565, 0.5281, 0.5313, 0.8777]
    })
    
    # Nampilin grafik batang interaktif bawaan streamlit yang rapi
    st.bar_chart(data=chart_data, x='Model Algoritma', y='F1-Score Kelompok', color='#0d9488')
    
    st.markdown("""
    <p style="font-size: 0.85rem; color: #64748b; text-align: center; margin-top: 10px;">
        *Grafik di atas memetakan performa F1-Score dari seluruh eksperimen model kelompok. Decision Tree memimpin signifikant.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_text:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💡 Justifikasi & Keunggulan Model</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Model Decision Tree yang dirancang oleh Anisa berhasil mengatasi kendala ketimpangan kelas 
    berkat struktur seleksi fiturnya yang adaptif. Berbeda dengan model berbasis jarak atau hyperplane, 
    pohon keputusan mampu membagi partisi data secara lokal dengan akurat.
    """)
    
    st.markdown("""
    <div class="status-badge">
        🏆 <b>Rekomendasi Sistem:</b> Model ini resmi memiliki reliabilitas tertinggi dan 
        telah dikunci ke dalam file biner <b>model.pkl</b> sebagai mesin prediksi utama aplikasi kita.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Komponen Expander biar UI interaktif dan ga kepanjangan scroll kebawah
    with st.expander("🛠️ Detail Arsitektur & Hyperparameter Tuning"):
        st.markdown("""
        * **Kriteria Pembagian (Splitter):** Menggunakan optimasi Gini Impurity & Entropy.
        * **Validasi Silang (Cross-Validation):** Menggunakan skema K-Fold sebanyak 10 kali putaran fitting.
        * **Data Resampling:** Dilatih menggunakan data hasil sintesis SMOTE untuk menyeimbangkan kelas target kualitas tidur.
        """)