import streamlit as st
import config
from inference import YieldPredictor

# --- Sayfa Ayarları ---
st.set_page_config(page_title=config.PAGE_TITLE, page_icon=config.PAGE_ICON, layout="centered")

# --- Modeli Yükle (Cache kullanarak hızlandırıyoruz) ---
@st.cache_resource
def get_predictor():
    return YieldPredictor()

predictor = get_predictor()

# --- Arayüz Başlıkları ---
st.title(config.PAGE_TITLE)
st.markdown("""
Bu proje, **Makine Öğrenmesi (XGBoost)** kullanarak tarımsal verim tahmini yapar.
Veri kaynağı: **FAO**.
""")

# --- Sidebar (Kullanıcı Girdileri) ---
st.sidebar.header(" Tarla Bilgileri")

selected_item = st.sidebar.selectbox("Ürün Seçiniz:", config.ITEMS)
selected_continent = st.sidebar.selectbox("Bölge (Kıta):", config.CONTINENTS)

rain = st.sidebar.slider("Yıllık Yağış (mm):", 100, 3000, 1200)
temp = st.sidebar.slider("Ortalama Sıcaklık (°C):", 5, 40, 20)
pesticide = st.sidebar.number_input("Pestisit (Ton):", min_value=0.0, value=10.0)

# --- Tahmin İşlemi ---
if st.button("Verimi Hesapla 🚀", use_container_width=True):
    # Veriyi hazırla
    input_data = {
        'Item': selected_item,
        'Continent': selected_continent,
        'average_rain_fall_mm_per_year': rain,
        'avg_temp': temp,
        'pesticide_tonnes': pesticide
    }
    
    try:
        # Inference dosyasındaki fonksiyonu çağırıyoruz
        result = predictor.predict(input_data)
        
        # Sonucu Göster
        st.success(f"Tahmini Verim: **{result:.2f} hg/ha**")
        
        # Görsel Geri Bildirim
        if result > 60000:
            st.balloons()
            st.info(" Mükemmel verim bekleniyor!")
        elif result < 20000:
            st.warning(" Düşük verim riski. Gübreleme planını gözden geçirin.")
            
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Bootcamp Final Projesi | v1.0.0")
