import re

def fix(p):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
        
    # add ./ to URLs
    c = c.replace("url('resimler/", "url('./resimler/")
    
    # fix the CSS of urun-emoji
    old_css = r""".urun-emoji {
      width: 96px;
      min-height: 100px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 44px;
      flex-shrink: 0
    }"""
    
    new_css = """.urun-emoji {
      width: 100px;
      height: 100px;
      display: block;
      background-size: cover;
      background-position: center;
      flex-shrink: 0;
      border-radius: 12px 0 0 12px;
    }"""
    
    # replace css
    c = re.sub(r'\.urun-emoji\s*\{[^\}]+\}', new_css, c)
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Fixed {p}")

fix(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\cemilay-sistem.html')
