import re

html_file = r'c:\Users\Servet\OneDrive\Masaüstü\dosya\index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

image_map = {
    "Demleme Çay": "demlemecay.jpg",
    "Türk Kahvesi": "turkkahvesi.jpg",
    "Filtre Kahve": "filtrekahve.jpg",
    "Bitki Çayı": "bitkicayi.jpg",
    "Sıcak Çikolata": "sicakcikolata.jpg",
    "Limonata": "limonata.jpg",
    "Iced Mocha": "icedmocha.jpg",
    "Portakal Suyu": "portakalsuyu.jpg",
    "Soğuk Çay": "sogukcay.jpg",
    "Milkshake": "milkshakee.jpg",
    "Karışık Pizza": "karisikpizza.jpg",
    "Hamburger": "hamburger.jpg",
    "Mantı": "manti.jpg",
    "Lahmacun": "lahmacun.jpg",
    "Izgara Köfte": "izgarakofte.jpg",
    "Tavuk Izgara": "tavukizgara.jpg",
    "Mevsim Salatası": "mevsimsalatasi (2).jpg",
    "Çoban Salatası": "cobansalatasi.jpg",
    "Sezar Salata": "sezarsalatasi.jpg",
    "Akdeniz Salatası": "akdenizsalatasi.jpg",
    "Cheesecake": "cheescake.jpg",
    "Baklava": "baklava.jpg",
    "Sufle": "sugle.jpg",
    "Kazandibi": "kazandibi.jpg",
    "Tiramisu": "tiramisu.jpg",
    "Mini Pankek": "minipankek.jpg",
    "Mini Pizza": "minipizza.jpg",
    "Nugget \\+ Patates": "nugget+patates.jpg", # regex escape just in case
    "Nugget \+ Patates": "nugget+patates.jpg", # alternative
    "Mini Sandviç": "minisandivic.jpg",
    "Dondurma": "dondurma.jpg",
    "Waffle": "waffle.jpg",
    "Meyve Suyu": "meyvesuyu.jpg",
    "Ayran": "ayran.jpg",
    "Sütlü Kakao": "sutlukakao.jpg"
}

def replace_emoji(match):
    full_match = match.group(0)
    product_name = match.group(1)
    
    # Handle the plus sign gracefully
    lookup_name = product_name
    if lookup_name == "Nugget + Patates":
        img_name = "nugget+patates.jpg"
    else:
        img_name = image_map.get(lookup_name)
        
    if img_name:
        return f'<div class="urun-emoji-kutu" style="background:url(\'resimler/{img_name}\') center/cover;"></div><div class="urun-bilgi"><h4>{product_name}</h4>'
    return full_match

# Regex to match the div with emoji, up to the h4 tag containing the product name
pattern = re.compile(r'<div class="urun-emoji-kutu" style="background:[^>]+>.*?</div><div class="urun-bilgi"><h4>([^<]+)</h4>')
new_content = pattern.sub(replace_emoji, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced images.")
