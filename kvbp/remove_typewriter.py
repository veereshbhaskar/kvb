import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove cursor and populate name
html_to_replace = '<span class="name" id="typewriter-name" style="min-height: 1.2em; display: inline-block;"></span><span class="cursor" id="type-cursor" style="animation: blink 1s infinite; color: var(--accent);">|</span>'
html_normal = '<span class="name">Veeresh Bhaskar<br>Karatam</span>'
content = content.replace(html_to_replace, html_normal)

# 2. Remove JS typeWriter
script_start = "// LOOPING TYPEWRITER EFFECT"
script_end = "setTimeout(typeWriter, 50);\n    }\n  }"

if script_start in content:
    content = re.sub(r'// LOOPING TYPEWRITER EFFECT.*?setTimeout\(typeWriter, 50\);\n    }\n  }', '', content, flags=re.DOTALL)

# 3. Remove the setTimeout call in the loader
content = content.replace("setTimeout(typeWriter, 500); // start typing shortly after loader hides", "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
