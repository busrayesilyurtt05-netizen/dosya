import mysql.connector
import requests
import time

# --- AYARLAR ---
FIREBASE_URL = "https://akilli-menu-sistemi-default-rtdb.firebaseio.com/siparisler.json"

def baglan_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cemilay_kafe"
        )
        return conn
    except Exception as e:
        print(f"❌ MySQL Bağlantı Hatası: {e}")
        return None

print("--- Robot Başlatıldı ---")
print("Sistem çalışıyor... Firebase'den veri bekleniyor...")

while True:
    try:
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200:
            veriler = response.json()

            if veriler is not None:
                db = baglan_mysql()
                if db:
                    cursor = db.cursor()
                    ogeler = veriler.items() if isinstance(veriler, dict) else enumerate(veriler)

                    for key, s in ogeler:
                        if s is not None and isinstance(s, dict):
                            # --- GÖRSELDEKİ İSİMLERE GÖRE GÜNCELLEDİK ---
                            # HTML kodunda 'siparisler', 'saat' ve 'toplam' olarak gönderiyorsun
                            yemek_detay = str(s.get('siparisler', 'Bilinmiyor'))
                            saat = str(s.get('saat', '00:00'))
                            fiyat = str(s.get('toplam', '0'))
                            masa = str(s.get('masa', 'Bilinmiyor'))

                            # Terminalde daha detaylı görelim diye masa nosunu da ekledim
                            print(f"📦 Yeni Sipariş! Masa: {masa} | Ürünler: {yemek_detay}")

                            sql = "INSERT INTO siparisler (yemek, saat, fiyat) VALUES (%s, %s, %s)"
                            val = (f"{masa} Nolu Masa: {yemek_detay}", saat, fiyat)
                            
                            cursor.execute(sql, val)
                            db.commit()
                            print(f"✅ MySQL'e Kaydedildi.")

                    cursor.close()
                    db.close()
                    requests.delete(FIREBASE_URL)
                    print("🧹 Firebase temizlendi, yeni siparişler bekleniyor...")
        
    except Exception as e:
        print(f"⚠️ Hata: {e}")
    
    time.sleep(5)