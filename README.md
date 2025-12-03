
# 🚜 SmartFarm: Crop Yield Prediction Project

##  Proje Hakkında
Bu proje, FAO verilerini kullanarak tarımsal verimi tahmin eden uçtan uca bir Makine Öğrenmesi çözümüdür. Çiftçilerin ekecekleri ürün, bölge ve hava durumu koşullarına göre ne kadar ürün alacaklarını (hg/ha) tahmin eder.

##  Sonuçlar
* **Baseline Model (Decision Tree):** R2 Score: 0.94
* **Final Model (XGBoost):** R2 Score: 0.96
* **En Önemli Faktörler:** Ürün Tipi (Item) ve Bölge (Continent), pestisit kullanımından daha etkilidir.

##  Kurulum
1. Repoyu klonlayın.
2. `pip install -r requirements.txt`
3. Uygulamayı başlatın: `streamlit run src/app.py`

##  Repo Yapısı
* `notebooks/`: EDA ve Model eğitimi adımları.
* `src/`: Streamlit uygulama kodları.
* `models/`: Eğitilmiş XGBoost modeli.

* ---
## 📝 Proje Raporu ve Soru-Cevap

Bootcamp final projesi gereksinimleri kapsamında sorulan soruların cevapları aşağıdadır:

### 1. Problem Tanımı
Tarımsal üretimde verim belirsizliği, çiftçilerin gelir kaybına ve kaynak israfına (su, gübre) yol açmaktadır. Bu proje, FAO verilerini kullanarak belirli iklim, gübre ve ürün koşullarında hektar başına düşen verimi (hg/ha) tahmin eden bir regresyon modelidir. Amaç, çiftçilere veri odaklı ekim kararları aldırmaktır.

### 2. Baseline Süreci ve Skoru
İlk aşamada veri seti temizlendikten sonra karmaşık olmayan bir **Decision Tree Regressor** kuruldu.
* **Model:** Decision Tree (Default parametreler)
* **Özellikler:** One-Hot Encoded `Item` ve `Continent` + Ham sayısal veriler.
* **Baseline Skoru:** MAE: ~7200, **R2 Score: 0.9495**

### 3. Feature Engineering Denemeleri
Veri setindeki 10 feature kuralını sağlamak ve model başarısını artırmak için şunlar yapıldı:
* **Continent:** Ülke (`Area`) sütunu kardinalitesi yüksek olduğu için kıtalara indirgendi.
* **Rain_Temp_Ratio:** Yağış ve sıcaklık arasındaki dengeyi yakalamak için matematiksel bir oran türetildi.
* **Temp_Category:** Sıcaklık değerleri bitki gelişimine göre (Cool, Mild, Hot) kategorize edildi.
Sonuç olarak model, coğrafi ve iklimsel ilişkileri daha iyi öğrendi.

### 4. Validasyon Şeması
Veri seti 28.000+ satırdan oluştuğu için **Hold-out Validation (%80 Train - %20 Test)** yöntemi seçildi. Veri hacmi yeterli olduğundan Cross-Validation'ın maliyetine girilmedi. `random_state=42` sabitlenerek sonuçların tekrarlanabilir olması sağlandı.

### 5. Final Pipeline ve Model Seçimi
Final model olarak **XGBoost Regressor** seçildi.
* **Neden XGBoost?** Tabular verilerde, özellikle doğrusal olmayan ilişkilerde (Tarım verisi gibi) en yüksek performansı verdiği ve overfitting'e karşı dirençli olduğu için.
* **Skor:** **R2 Score: 0.9586**. Baseline modele göre yaklaşık %1'lik bir iyileşme sağlandı ve hata payı (MAE) düştü.

### 6. Business Gereksinimleri ve Yorumu
Modelin `feature_importance` analizi sonucunda, verimi en çok etkileyen faktörün **"Ürün Tipi" (Item)** ve **"Coğrafi Konum" (Continent)** olduğu görüldü. Pestisit kullanımı daha alt sıralarda kaldı.
* **İş İçgörüsü:** Çiftçiler verimi artırmak için gübreyi artırmaktan ziyade, toprağa ve bölgeye en uygun ürünü seçmeye odaklanmalıdır. Model bu kararı desteklemektedir.

### 7. Canlıya Alma (Deployment) ve İzleme
Model, **Streamlit** kullanılarak son kullanıcı arayüzüne dönüştürüldü.
Canlı ortamda (Production) izlenmesi gereken metrikler:
* **Model Drift:** Gerçek dünya iklim verileri değiştikçe modelin tahmin başarısı düşüyor mu?
* **Data Drift:** Kullanıcıların girdiği verilerin dağılımı (örn: aşırı sıcaklık girişleri) eğitim verisinden sapıyor mu?
Bu metrikler aylık olarak kontrol edilip model yeniden eğitilmelidir (Retraining).
