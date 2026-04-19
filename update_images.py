import os
from bs4 import BeautifulSoup

def normalize_text(text):
    # Türkçe karakterleri ASCII'ye çevir
    trans = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return text.translate(trans).lower().replace(" ", "")

# HTML dosyasını oku
with open('cemilay-sistem.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Resimler klasöründeki dosyaları listele
resimler_dir = 'resimler'
resimler = os.listdir(resimler_dir)
resimler_set = set(resimler)
print("Available images:", sorted(resimler_set))

# Tüm urun-kart'ları bul
urun_kartlar = soup.find_all('div', class_='urun-kart')

for kart in urun_kartlar:
    # urun-ad'ı bul
    urun_ad_div = kart.find('div', class_='urun-ad')
    if urun_ad_div:
        urun_adi = urun_ad_div.get_text().strip()
        # Normalize et
        resim_adi = normalize_text(urun_adi)
        resim_dosyasi = resim_adi + '.jpg'
        print(f"Processing {urun_adi} -> {resim_dosyasi}")
        
        if resim_dosyasi in resimler_set:
            # urun-emoji img'yi bul
            urun_emoji = kart.find('img', class_='urun-emoji')
            if urun_emoji:
                # background-image ekle
                style = urun_emoji.get('style', '')
                bg_url = f"./resimler/{resim_dosyasi}"
                if style:
                    style += f"; background-image: url('{bg_url}');"
                else:
                    style = f"background-image: url('{bg_url}');"
                urun_emoji['style'] = style
                print(f"Updated {urun_adi} with {resim_dosyasi}")
            else:
                print(f"No urun-emoji for {urun_adi}")
        else:
            print(f"No image for {urun_adi} -> {resim_dosyasi}")

# Değişiklikleri kaydet
with open('cemilay-sistem.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("İşlem tamamlandı.")