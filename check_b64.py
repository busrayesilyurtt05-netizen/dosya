import re
import base64

with open(r'c:\Users\Servet\OneDrive\Masaüstü\dosya\cemilay-sistem.html', 'r', encoding='utf-8') as f:
    c = f.read()
m = re.search(r'src=\"(data:image/jpeg;base64,.*?)\"', c)
if m:
    b64 = m.group(1).split(',')[1]
    try:
        dec = base64.b64decode(b64)
        print('Valid base64, length:', len(dec))
    except Exception as e:
        print('Error:', e)
else:
    print('No base64 image found.')
