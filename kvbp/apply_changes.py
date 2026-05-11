import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add hero image
hero_tag_pattern = r'<div class="hero-content">\s*<div class="hero-tag">'
hero_image_html = '''<div class="hero-content">
    <img src="hero-image.png" alt="Veeresh" style="width: 180px; height: 180px; border-radius: 50%; object-fit: cover; margin-bottom: 2rem; border: 4px solid var(--accent); box-shadow: 0 0 30px rgba(0,255,204,0.3); animation: fadeUp 1s ease both;">
    <div class="hero-tag">'''
content = re.sub(hero_tag_pattern, hero_image_html, content)

# 2. Add typing effect target to the name
name_pattern = r'<span class="name">Veeresh Bhaskar<br>Karatam</span>'
name_html = '<span class="name" id="typewriter-name" style="min-height: 1.2em; display: inline-block;"></span><span class="cursor" id="type-cursor" style="animation: blink 1s infinite; color: var(--accent);">|</span>'
content = content.replace(name_pattern, name_html)

# Add cursor blink animation to CSS
css_to_add = '''@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }\n</style>'''
content = content.replace('</style>', css_to_add)

# 3. Add JavaScript for typing effect and target="_blank"
js_pattern = r'// LOADER\nwindow\.addEventListener\(\'load\',\(\)=>\{setTimeout\(\(\)=>\{document\.getElementById\(\'loader\'\)\.classList\.add\(\'hide\'\)\},2000\)\}\)'
js_code = '''// LOADER & TYPING EFFECT & LINKS
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('loader').classList.add('hide');
    setTimeout(typeWriter, 500); // start typing shortly after loader hides
  }, 2000);
});

// TYPEWRITER EFFECT
const typeText = "Veeresh Bhaskar Karatam";
let typeIndex = 0;
function typeWriter() {
  const el = document.getElementById("typewriter-name");
  if (el && typeIndex < typeText.length) {
    el.innerHTML += typeText.charAt(typeIndex);
    typeIndex++;
    setTimeout(typeWriter, 100);
  } else {
    // optional: remove cursor after typing
    // document.getElementById("type-cursor").style.display = 'none';
  }
}

// MAKE ALL LINKS OPEN IN NEW TAB
document.querySelectorAll('a').forEach(link => {
  link.setAttribute('target', '_blank');
});'''

content = re.sub(js_pattern, js_code, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
