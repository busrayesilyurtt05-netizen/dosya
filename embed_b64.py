import base64
import re
import os

def embed_images(filepath):
    print("Processing", filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find all src="resimler/XYZ.jpg"
    pattern = re.compile(r'src="resimler/([^"]+)"')
    
    def replacer(match):
        filename = match.group(1)
        img_path = os.path.join(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\resimler', filename)
        if os.path.exists(img_path):
            with open(img_path, 'rb') as img_f:
                b64_data = base64.b64encode(img_f.read()).decode('utf-8')
            return f'src="data:image/jpeg;base64,{b64_data}"'
        else:
            print("WARNING: Image not found:", img_path)
            return match.group(0)
            
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully embedded images in", filepath)
    else:
        print("No changes needed or no matches found in", filepath)

embed_images(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\cemilay-sistem.html')
embed_images(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\index.html')
