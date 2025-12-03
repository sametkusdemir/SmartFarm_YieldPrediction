import os

# Dosya Yolları (Project Root'tan çalıştırılacağı varsayılmıştır)
MODEL_PATH = 'models/xgb_agriculture_model.json'
COLUMNS_PATH = 'models/model_columns.pkl'

# Arayüz ve Model için Sabit Listeler
ITEMS = [
    'Maize', 'Potatoes', 'Rice, paddy', 'Sorghum', 
    'Soybeans', 'Wheat', 'Cassava', 'Sweet potatoes', 'Yams'
]

CONTINENTS = [
    'Africa', 'Asia', 'Europe', 
    'North America', 'Oceania', 'South America'
]

# Sayfa Ayarları
PAGE_TITLE = "Akıllı Tarım: Mahsul Verim Tahminleyicisi"
PAGE_ICON = "🚜"
