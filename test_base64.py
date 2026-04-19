import base64

def inject():
    with open(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\resimler\demlemecay.jpg', 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    html_path = r'c:\Users\Servet\OneDrive\Masaüstü\dosya\cemilay-sistem.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        c = f.read()
    # Replace just demlemecay.jpg with base64
    c = c.replace('src="resimler/demlemecay.jpg"', f'src="data:image/jpeg;base64,{b64}"')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Base64 injected for demlemecay.jpg')

inject()
