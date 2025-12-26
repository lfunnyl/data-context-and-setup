import pandas as pd
from pathlib import Path

class Olist:
    def get_data(self):
        """
        Bu metod, csv dizinindeki tüm verileri okur ve temizlenmiş 
        anahtarlarla bir sözlük (dict) olarak döndürür.
        """
        # 1. CSV yolunu tanımla
        csv_path = Path("~/.workintech/olist/data/csv").expanduser()
        
        # 2. Klasördeki tüm dosyaları listele
        file_paths = list(csv_path.iterdir())
        
        data = {}
        
        for path in file_paths:
            # Sadece .csv dosyalarını işle
            if path.suffix == '.csv':
                # Anahtar ismini temizle: olist_sellers_dataset.csv -> sellers
                key = path.name.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
                
                # DataFrame'i yükle ve sözlüğe ekle
                data[key] = pd.read_csv(path)
        
        # EN ÖNEMLİ KISIM: Sözlüğü döndür
        return data

    def ping(self):
        return "pong"