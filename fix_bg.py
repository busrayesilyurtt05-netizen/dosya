import re
import sys

def fix_html(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find background:url(...) center/cover
        pattern = re.compile(r'style="background:url\(\'([^\']+)\'\) center/cover;?"')
        
        def repl(m):
            url = m.group(1)
            return f'style="background-image: url(\'{url}\'); background-size: cover; background-position: center; background-repeat: no-repeat;"'

        new_content = pattern.sub(repl, content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filepath}')
        else:
            print(f'No changes needed for {filepath}')
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

fix_html('c:\\Users\\Servet\\OneDrive\\Masaüstü\\dosya\\index.html')
fix_html('c:\\Users\\Servet\\OneDrive\\Masaüstü\\dosya\\cemilay-sistem.html')
