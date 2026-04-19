import re

def img_to_tag(p, cls_name):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # Find <div class="urun-emoji" style="background-image: url('./resimler/XYZ.jpg'); ..."> </div>
    # Using a flexible regex that handles newlines and optional ./
    pattern = re.compile(r'<div\s+class="' + cls_name + r'"\s*style="background-image:\s*url\(\'(?:\./)?resimler/([^\']+)\'\)[^>]*>\s*</div>', re.IGNORECASE | re.DOTALL)
    
    def repl(m):
        filename = m.group(1)
        return f'<img class="{cls_name}" src="resimler/{filename}" alt="">'
        
    new_c = pattern.sub(repl, c)
    
    # Also fix the CSS
    css_pattern = re.compile(r'\.' + cls_name + r'\s*\{[^\}]+\}')
    if cls_name == "urun-emoji":
        new_css = """.urun-emoji {
      width: 100px;
      height: 100px;
      display: block;
      object-fit: cover;
      flex-shrink: 0;
      border-radius: 12px 0 0 12px;
    }"""
    else:
        new_css = """.urun-emoji-kutu {
      width: 110px;
      height: 110px;
      display: block;
      object-fit: cover;
      flex-shrink: 0;
      border-radius: 18px 0 0 18px;
    }"""
    
    new_c = css_pattern.sub(new_css, new_c)

    if c != new_c:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Fixed {p}")
    else:
        print(f"No changes made to {p}")

img_to_tag(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\cemilay-sistem.html', 'urun-emoji')
img_to_tag(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\index.html', 'urun-emoji-kutu')
