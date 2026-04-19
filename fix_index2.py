import re

def fix_index(p):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
        
    # add ./ to URLs
    c = c.replace("url('resimler/", "url('./resimler/")
    
    # fix the CSS of urun-emoji-kutu
    new_css = """.urun-emoji-kutu { 
      width: 110px; 
      height: 110px; 
      display: block; 
      background-size: cover; 
      background-position: center; 
      flex-shrink: 0; 
      border-radius: 18px 0 0 18px; 
    }"""
    
    c = re.sub(r'\.urun-emoji-kutu\s*\{[^\}]+\}', new_css, c)
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Fixed {p}")

fix_index(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\index.html')
