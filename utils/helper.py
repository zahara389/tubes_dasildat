import streamlit as st
import pandas as pd

def tampilkan_panduan_skala():
    """Fungsi untuk menampilkan penjelasan skala 1-10 yang diminta asprak"""
    st.markdown("""
    <div style="background-color: #111; border-left: 5px solid #deff9a; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h4 style="color: #deff9a; margin-top: 0;">ℹ️ PANDUAN SKALA PENILAIAN (1 - 10)</h4>
        <p style="color: #daffde; font-size: 14px; margin-bottom: 10px;">
            Agar tidak bingung saat mengisi data, berikut adalah penjelasan indikator skala yang digunakan dalam sistem SleepSpace AI berdasarkan deskwork penelitian:
        </p>
        <table style="width:100%; border-collapse: collapse; font-size: 13px; color: #f5f5f5;">
            <tr style="border-bottom: 1px solid #333;">
                <th style="text-align: left; padding: 8px; color: #deff9a; width: 20%;">Kategori</th>
                <th style="text-align: left; padding: 8px; color: #deff9a; width: 40%;">🧠 Tingkat Stres Harian</th>
                <th style="text-align: left; padding: 8px; color: #deff9a; width: 40%;">🔋 Tingkat Kelelahan Mental</th>
            </tr>
            <tr style="border-bottom: 1px solid #222;">
                <td style="padding: 8px; color: #4ade80; font-weight: bold;">1 - 3 (Rendah)</td>
                <td style="padding: 8px;">Kondisi santai, rileks, pikiran tenang, dan beban pikiran minimal (misal: hari libur/tanpa deadline).</td>
                <td style="padding: 8px;">Energi penuh, otak segar, fokus sangat tajam, mudah berpikir jernih dan konsentrasi.</td>
            </tr>
            <tr style="border-bottom: 1px solid #222;">
                <td style="padding: 8px; color: #facc15; font-weight: bold;">4 - 7 (Sedang)</td>
                <td style="padding: 8px;">Stres harian wajar akibat rutinitas padat atau tugas kuliah, namun pikiran masih bisa mengontrol situasi.</td>
                <td style="padding: 8px;">Mulai lelah, fokus sedikit menurun, mata terasa berat, butuh istirahat sejenak untuk kembali paham.</td>
            </tr>
            <tr>
                <td style="padding: 8px; color: #f87171; font-weight: bold;">8 - 10 (Tinggi)</td>
                <td style="padding: 8px;">Kondisi cemas parah, panik, atau burnout yang menguras emosi dan mengganggu kenyamanan fisik.</td>
                <td style="padding: 8px;">Kelelahan total (exhaustion), otak terasa 'blank' atau membeku, tidak bisa diajak berpikir berat lagi.</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

def ambil_data_evaluasi():
    """Fungsi untuk menyediakan data tabel perbandingan model untuk halaman evaluasi"""
    data = {
        'Nama Model': [
            'Random Forest (Anisa) 👑', 
            'Neural Network (Ataya)', 
            'SVM (Aqila)', 
            'K-NN (Zahara)'
        ],
        'Akurasi Global': ['87%', '85%', '83%', '82%'],
        'Precision (Kelas 1)': ['42%', '41%', '38%', '35%'],
        'Recall (Kelas 1)': ['74%', '70%', '93%', '65%'],
        'F1-Score (Kelas 1)': [0.54, 0.53, 0.52, 0.48],
        'Keterangan': [
            'Model Terbaik (Digunakan di Web)', 
            'Model Deep Learning (Sesuai Praktikum)', 
            'Paling Sensitif Menjaring Gejala Sakit', 
            'Model Baseline Berbasis Jarak'
        ]
    }
    return pd.DataFrame(data)