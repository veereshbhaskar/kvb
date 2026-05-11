import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the HTML
old_hero_content = """  <div class="hero-content">
    <img src="hero-image.png" alt="Veeresh" style="width: 180px; height: 180px; border-radius: 50%; object-fit: cover; margin-bottom: 2rem; border: 4px solid var(--accent); box-shadow: 0 0 30px rgba(0,255,204,0.3); animation: fadeUp 1s ease both;">
    <div class="hero-tag">🚀 MCA Candidate · Data + Web + Business</div>
    <h1 class="hero-title">
      <span class="name" id="typewriter-name" style="min-height: 1.2em; display: inline-block;"></span><span class="cursor" id="type-cursor" style="animation: blink 1s infinite; color: var(--accent);">|</span>
      <span class="role">MCA Innovator — blending Data, Web & Business<br>to build smarter solutions</span>
    </h1>
    <p class="hero-subtitle">Analytically driven developer with expertise in <em>SQL</em>, <em>Python</em>, <em>Machine Learning</em>, and <em>Business Development</em>. Currently pursuing MCA at KI University with a 8.78 CGPA.</p>
    <div class="hero-ctas">
      <a href="#projects" class="btn-primary">View Projects</a>
      <a href="#contact" class="btn-secondary">Hire Me</a>
      <a href="#ml-demo" class="btn-secondary">Try ML Demo</a>
    </div>
    <div class="hero-stats">
      <div class="stat"><span class="stat-num">8.78</span><span class="stat-label">CGPA / 10</span></div>
      <div class="stat"><span class="stat-num">30%</span><span class="stat-label">Query Reduction</span></div>
      <div class="stat"><span class="stat-num">3+</span><span class="stat-label">Departments Served</span></div>
      <div class="stat"><span class="stat-num">5+</span><span class="stat-label">Projects Built</span></div>
    </div>
  </div>"""

new_hero_content = """  <div class="hero-content" style="display: flex; align-items: center; justify-content: space-between; gap: 4rem; text-align: left; max-width: 1200px; width: 100%;">
    <style>
      @media(max-width: 900px) {
        .hero-content {
          flex-direction: column-reverse;
          text-align: center !important;
        }
        .hero-subtitle {
          margin: 0 auto 3.5rem !important;
        }
        .hero-ctas, .hero-stats {
          justify-content: center !important;
        }
        .hero-image-wrapper img {
          width: 250px !important;
          height: 250px !important;
        }
      }
    </style>
    <div class="hero-text" style="flex: 1;">
      <div class="hero-tag">🚀 MCA Candidate · Data + Web + Business</div>
      <h1 class="hero-title">
        <span class="name" id="typewriter-name" style="min-height: 1.2em; display: inline-block;"></span><span class="cursor" id="type-cursor" style="animation: blink 1s infinite; color: var(--accent);">|</span>
        <span class="role">MCA Innovator — blending Data, Web & Business<br>to build smarter solutions</span>
      </h1>
      <p class="hero-subtitle" style="margin-left: 0; margin-right: 0; max-width: 100%;">Analytically driven developer with expertise in <em>SQL</em>, <em>Python</em>, <em>Machine Learning</em>, and <em>Business Development</em>. Currently pursuing MCA at KI University with a 8.78 CGPA.</p>
      <div class="hero-ctas" style="justify-content: flex-start;">
        <a href="#projects" class="btn-primary">View Projects</a>
        <a href="#contact" class="btn-secondary">Hire Me</a>
        <a href="#ml-demo" class="btn-secondary">Try ML Demo</a>
      </div>
      <div class="hero-stats" style="justify-content: flex-start; margin-top: 3rem; padding-top: 3rem;">
        <div class="stat"><span class="stat-num">8.78</span><span class="stat-label">CGPA / 10</span></div>
        <div class="stat"><span class="stat-num">30%</span><span class="stat-label">Query Reduction</span></div>
        <div class="stat"><span class="stat-num">3+</span><span class="stat-label">Departments Served</span></div>
        <div class="stat"><span class="stat-num">5+</span><span class="stat-label">Projects Built</span></div>
      </div>
    </div>
    <div class="hero-image-wrapper" style="flex-shrink: 0;">
      <img src="hero-image.png" alt="Veeresh" style="width: 400px; height: 400px; border-radius: 50%; object-fit: cover; border: 4px solid var(--accent); box-shadow: 0 0 50px rgba(0,255,204,0.3); animation: fadeUp 1s ease both;">
    </div>
  </div>"""

# Remove leading spaces from the search string to be safe with indentation
old_hero_content = old_hero_content.strip()

if old_hero_content in content:
    content = content.replace(old_hero_content, new_hero_content.strip())
else:
    print("Could not find the exact HTML block to replace. Attempting regex.")
    pattern = r'<div class="hero-content">.*?</div>\s+</div>' # Rough match
    # A bit risky, so let's stick to simple replace and if it fails we check the file again
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
