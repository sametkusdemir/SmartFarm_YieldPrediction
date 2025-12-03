import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib

# --- 1. Model ve Sütun Bilgilerini Yükle ---
# Not: Dosyaların app.py ile aynı klasörde olması gerekir
model = xgb.XGBRegressor()
model.load_model('xgb_agriculture_model.json')
model_columns = joblib.load('model_columns.pkl')

# --- 2. Sayfa Başlığı ve Açıklama ---
st.set_page_config(page_title="Akıllı Tarım Verim Tahmini", layout="centered")
st.title("🚜 Akıllı Tarım: Mahsul Verim Tahminleyicisi")
st.write("""
Bu uygulama, Yapay Zeka (XGBoost) kullanarak tarlanızdan alacağınız tahmini verimi hesaplar.
Lütfen aşağıdaki parametreleri giriniz.
""")

# --- 3. Kullanıcı Girdileri (Sidebar) ---
st.sidebar.header("Tarla Bilgileri")

# Kullanıcıdan alınacak veriler
# Bu listeler One-Hot Encoding mantığına göre backend'de işlenecek
item_list = ['Maize', 'Potatoes', 'Rice, paddy', 'Sorghum', 'Soybeans', 'Wheat', 'Cassava', 'Sweet potatoes', 'Yams']
continent_list = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']

selected_item = st.sidebar.selectbox("Ekeceğiniz Ürün:", item_list)
selected_continent = st.sidebar.selectbox("Bölge (Kıta):", continent_list)

rain = st.sidebar.slider("Yıllık Ortalama Yağış (mm):", min_value=100, max_value=3000, value=1200)
temp = st.sidebar.slider("Ortalama Sıcaklık (°C):", min_value=5, max_value=40, value=20)
pesticide = st.sidebar.number_input("Pestisit Kullanımı (Ton):", min_value=0.0, value=10.0)

# --- 4. Arka Plan İşlemleri (Preprocessing) ---
# Kullanıcı girdilerini modelin anlayacağı formata çevirmemiz lazım

# Bir sözlük (dictionary) oluşturuyoruz
input_data = {
    'average_rain_fall_mm_per_year': rain,
    'pesticide_tonnes': pesticide,
    'avg_temp': temp,
    # Feature Engineering ile türettiğimiz alanları burada da hesaplamalıyız!
    'Rain_Temp_Ratio': rain / temp if temp != 0 else 0
}

# Veriyi DataFrame'e çevir
df_input = pd.DataFrame([input_data])

# One-Hot Encoding işlemi (Kullanıcı seçimini sütunlara çevirme)
# Önce tüm sütunları 0 olarak oluştur
for col in model_columns:
    if col not in df_input.columns:
        df_input[col] = 0

# Seçilen Ürün ve Kıta için ilgili sütunu 1 yap
# Örn: Kullanıcı 'Maize' seçtiyse 'Item_Maize' sütunu 1 olmalı.
item_col = f"Item_{selected_item}"
continent_col = f"Continent_{selected_continent}"

if item_col in df_input.columns:
    df_input[item_col] = 1

if continent_col in df_input.columns:
    df_input[continent_col] = 1

# Sütun sırasını modelin eğitimiyle birebir aynı yap (Çok Önemli!)
df_input = df_input[model_columns]

# --- 5. Tahmin Butonu ve Sonuç ---
if st.button("Verimi Hesapla"):
    prediction = model.predict(df_input)
    verim = prediction[0]
    
    st.success(f"🌱 Tahmini Verim: {verim:.2f} hg/ha")
    
    # İş içgörüsü mesajı
    if verim > 70000:
        st.balloons()
        st.info("Harika! Bu koşullarda yüksek verim bekleniyor.")
    elif verim < 20000:
        st.warning("Dikkat: Bu koşullarda verim düşük olabilir. Gübrelemeyi veya ürün seçimini gözden geçirin.")

# --- 6. Alt Bilgi ---
st.markdown("---")
st.caption("Bootcamp Final Projesi | Veri Kaynağı: FAO")