import sys
import re

with open('c:\\Users\\Servet\\OneDrive\\Masaüstü\\dosya\\cemilay-sistem.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace .urun-emoji CSS
old_css = '.urun-emoji{min-width:96px;height:100px;width:96px;min-height:100px;display:flex;align-items:center;justify-content:center;font-size:44px;flex-shrink:0}'
new_css = '.urun-emoji{display:block !important;width:100px !important;height:100px !important;background-size:cover;background-position:center;flex-shrink:0}'
c = c.replace(old_css, new_css)

# Replace background image styles
c = re.sub(r'style="background:url\(''resimler/(.*?)''\) center/cover"', r'style="background-image: url(''./resimler/\1''); background-size: cover; background-position: center;"', c)

with open('c:\\Users\\Servet\\OneDrive\\Masaüstü\\dosya\\cemilay-sistem.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('SUCCESS')
