import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the JS so it only opens non-hash links in a new tab
bad_js = "link.setAttribute('target', '_blank');"
good_js = """if (link.getAttribute('href') && !link.getAttribute('href').startsWith('#')) {
    link.setAttribute('target', '_blank');
  }"""

content = content.replace(bad_js, good_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
