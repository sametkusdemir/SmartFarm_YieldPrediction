# 🚜 SmartFarm: End-to-End Crop Yield Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

##  Proje Özeti
**SmartFarm**, tarımsal verimliliği artırmak ve çiftçilerin karar alma süreçlerini desteklemek amacıyla geliştirilmiş bir Makine Öğrenmesi (ML) projesidir. FAO (Birleşmiş Milletler Gıda ve Tarım Örgütü) veri setlerini kullanarak; iklim koşulları, gübre kullanımı ve ekilen ürün türüne göre hektar başına düşen verimi (**hg/ha**) tahmin eder.

Proje; veri analizi, özellik mühendisliği, model optimizasyonu ve canlıya alma (deployment) adımlarını kapsayan uçtan uca bir pipeline sunar.

###  Canlı Demo
Uygulamayı aşağıdaki linkten deneyebilirsiniz:
 **https://huggingface.co/spaces/sametkusdemir/SmartFarm-App**

---

## Veri Seti ve Özellikler
Bu projede kullanılan veri seti, gerçek dünya tarım verilerini içerir ve ~28.000 satırdan oluşur.
* **Kaynak:** Kaggle - FAO Crop Yield Prediction
* **Veri Hacmi:** 28,000+ Satır, 10+ Özellik (Feature Engineering sonrası).

**Girdi Değişkenleri (Features):**
* `Item`: Ekilen ürün (Mısır, Patates, Pirinç vb.)
* `Continent`: Ülkenin bulunduğu kıta (Coğrafi konum etkisi için türetildi).
* `average_rain_fall_mm_per_year`: Yıllık ortalama yağış miktarı.
* `pesticide_tonnes`: Kullanılan pestisit miktarı.
* `avg_temp`: Ortalama sıcaklık.
* `Rain_Temp_Ratio`: Nemlilik ve kuraklık dengesini ölçen türetilmiş değişken.

---

##  Proje Mimarisi

Proje şu adımlardan oluşmaktadır:

1.  **EDA (Keşifçi Veri Analizi):** Veri dağılımı, eksik değerler ve aykırı değer (outlier) analizi.
2.  **Preprocessing:** Veri temizliği, One-Hot Encoding ve `StandardScaler`.
3.  **Feature Engineering:** Coğrafi gruplandırma (`Continent`) ve iklimsel oranlar (`Rain_Temp_Ratio`) türetilmesi.
4.  **Modelleme:**
    * *Baseline:* Decision Tree Regressor
    * *Final:* XGBoost Regressor (Hyperparameter Optimization)
5.  **Deployment:** Streamlit arayüzü ile Hugging Face Spaces üzerinde yayınlama.

---

##  Model Performansı

Baseline model ile optimize edilmiş Final model arasındaki performans farkı aşağıdadır:

| Model | MAE (Ortalama Hata) | R² Score (Doğruluk) | Açıklama |
|-------|---------------------|---------------------|----------|
| **Decision Tree (Baseline)** | ~7206 | **0.9495** | Temel model, hızlı kurulum. |
| **XGBoost (Final)** | ~6500 | **0.9586** | Optimize edilmiş, daha kararlı. |

> **Sonuç:** XGBoost modeli, karmaşık ve doğrusal olmayan ilişkileri daha iyi yakalayarak başarı oranını artırmıştır.

---

## Proje Raporu (Bootcamp Gereksinimleri)
1. Problem Tanımı: Tarımsal üretimde verim belirsizliği, kaynak israfına yol açmaktadır. Bu proje, iklim ve toprak verilerine dayanarak verim tahmini yapan bir regresyon problemidir.

2. Validasyon Şeması: Veri seti yeterince büyük olduğu için (%80 Train - %20 Test) Hold-out Validation yöntemi kullanılmıştır. random_state=42 ile sonuçların tekrarlanabilirliği sağlanmıştır.

3. Feature Engineering: Model başarısını artırmak için ülkeler kıtalara (Continent) indirgenmiş, sıcaklık ve yağış arasındaki ilişkiyi kuran Rain_Temp_Ratio özelliği türetilmiştir.

4. Business İçgörüsü (Feature Importance): Model analizine göre, verimi en çok etkileyen faktörler Ürün Tipi (Item) ve Konum (Continent)'dur. Pestisit kullanımının etkisi, doğru ürün ve bölge seçiminden sonra gelmektedir.

5. İzleme (Monitoring): Canlı ortamda modelin başarısı, "Data Drift" (Girdi verilerinin dağılımının değişmesi) metrikleri ile aylık periyotlarla izlenmelidir.

## İletişim
  Geliştirici: Samet Kuşdemir  
  LinkedIn: linkedin.com/in/sametkusdemir

##  Repo Yapısı

```text
SmartFarm_YieldPrediction/
├── data/                  # Ham ve işlenmiş veriler
├── notebooks/             # Jupyter Notebook çalışmaları
│   ├── 1_EDA.ipynb        # Veri analizi ve temizlik
│   ├── 2_Baseline.ipynb   # Temel model eğitimi
│   └── 3_Final_Model.ipynb# XGBoost ve Feature Importance
├── src/                   # Kaynak kodlar
│   ├── app.py             # Streamlit arayüz kodu
│   ├── inference.py       # Tahminleme mantığı (Backend)
│   └── config.py          # Proje ayarları
├── models/                # Eğitilmiş model (.json) ve pickle dosyaları
├── requirements.txt       # Kütüphane bağımlılıkları
└── README.md              # Proje dokümantasyonu
