
# 🚜 SmartFarm: Crop Yield Prediction Project

## 🎯 Proje Hakkında
Bu proje, FAO verilerini kullanarak tarımsal verimi tahmin eden uçtan uca bir Makine Öğrenmesi çözümüdür. Çiftçilerin ekecekleri ürün, bölge ve hava durumu koşullarına göre ne kadar ürün alacaklarını (hg/ha) tahmin eder.

## 📊 Sonuçlar
* **Baseline Model (Decision Tree):** R2 Score: 0.94
* **Final Model (XGBoost):** R2 Score: 0.96
* **En Önemli Faktörler:** Ürün Tipi (Item) ve Bölge (Continent), pestisit kullanımından daha etkilidir.

## 🚀 Kurulum
1. Repoyu klonlayın.
2. `pip install -r requirements.txt`
3. Uygulamayı başlatın: `streamlit run src/app.py`

## 📂 Repo Yapısı
* `notebooks/`: EDA ve Model eğitimi adımları.
* `src/`: Streamlit uygulama kodları.
* `models/`: Eğitilmiş XGBoost modeli.
