import pandas as pd
import xgboost as xgb
import joblib
import config  # Az önce oluşturduğumuz config dosyasını çağırıyoruz

class YieldPredictor:
    def __init__(self):
        self.model = None
        self.model_columns = None
        self._load_artifacts()

    def _load_artifacts(self):
        """Modeli ve sütun listesini yükler."""
        try:
            self.model = xgb.XGBRegressor()
            self.model.load_model(config.MODEL_PATH)
            self.model_columns = joblib.load(config.COLUMNS_PATH)
            print(" Model ve artifact'ler başarıyla yüklendi.")
        except Exception as e:
            print(f" Model yüklenirken hata oluştu: {e}")
            raise e

    def preprocess_input(self, data: dict) -> pd.DataFrame:
        """Kullanıcı verisini modelin anlayacağı formata (One-Hot) çevirir."""
        
        # 1. Ham veriyi DataFrame'e çevir
        df = pd.DataFrame([data])
        
        # 2. Feature Engineering (Notebook'taki mantığın aynısı)
        # Rain_Temp_Ratio hesapla
        rain = data.get('average_rain_fall_mm_per_year', 0)
        temp = data.get('avg_temp', 0)
        df['Rain_Temp_Ratio'] = rain / temp if temp != 0 else 0

        # 3. One-Hot Encoding Hazırlığı
        # Modelin beklediği tüm sütunları 0 olarak oluştur
        for col in self.model_columns:
            if col not in df.columns:
                df[col] = 0

        # 4. Seçilen Kategorileri İşaretle (1 yap)
        # Örn: Item_Maize = 1
        item = data.get('Item')
        continent = data.get('Continent')
        
        if f"Item_{item}" in df.columns:
            df[f"Item_{item}"] = 1
        
        if f"Continent_{continent}" in df.columns:
            df[f"Continent_{continent}"] = 1
            
        # 5. Sütun Sıralamasını Garantiye Al
        return df[self.model_columns]

    def predict(self, data: dict) -> float:
        """Son tahmini döndürür."""
        processed_df = self.preprocess_input(data)
        prediction = self.model.predict(processed_df)
        return float(prediction[0])
