import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_style = """<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#030305;--bg2:#08080c;--bg3:#0f0f15;
  --surface:rgba(20,20,30,0.4);--surface2:rgba(30,30,45,0.6);
  --accent:#00ffcc;--accent2:#b052ff;--accent3:#ff3366;
  --text:#ffffff;--text2:#a3a3bd;--text3:#666680;
  --border:rgba(255,255,255,0.08);--border2:rgba(255,255,255,0.15);
  --card-glow:rgba(0,255,204,0.15);
  --font-head:'Syne',sans-serif;--font-body:'DM Mono',monospace;--font-serif:'Instrument Serif',serif;
}
[data-theme="light"]{
  --bg:#f4f4f9;--bg2:#ffffff;--bg3:#ebebef;
  --surface:rgba(255,255,255,0.6);--surface2:rgba(240,240,245,0.8);
  --accent:#00b386;--accent2:#8233ff;--accent3:#ff3366;
  --text:#11111a;--text2:#555566;--text3:#888899;
  --border:rgba(0,0,0,0.08);--border2:rgba(0,0,0,0.15);
  --card-glow:rgba(0,179,134,0.1);
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--font-body);line-height:1.7;overflow-x:hidden;position:relative}

/* GLOBAL BACKGROUND MESH */
body::before {
  content: '';
  position: fixed;
  inset: -50%;
  background: 
    radial-gradient(circle at 20% 30%, rgba(0, 255, 204, 0.05) 0%, transparent 40%),
    radial-gradient(circle at 80% 70%, rgba(176, 82, 255, 0.05) 0%, transparent 40%),
    radial-gradient(circle at 50% 50%, rgba(255, 51, 102, 0.03) 0%, transparent 50%);
  z-index: -1;
  animation: bgMesh 20s ease-in-out infinite alternate;
  pointer-events: none;
}
@keyframes bgMesh {
  0% { transform: rotate(0deg) scale(1); }
  100% { transform: rotate(10deg) scale(1.1); }
}

/* LOADER */
#loader{position:fixed;inset:0;background:var(--bg);z-index:9999;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1.5rem;transition:opacity .8s cubic-bezier(0.4, 0, 0.2, 1)}
#loader.hide{opacity:0;pointer-events:none}
.loader-text{font-family:var(--font-head);font-size:1.5rem;color:transparent;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;letter-spacing:.3em;font-weight:800;animation:pulse 2s infinite}
.loader-bar{width:240px;height:3px;background:var(--border);border-radius:3px;overflow:hidden;position:relative}
.loader-fill{position:absolute;left:0;top:0;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));animation:fill 1.8s cubic-bezier(0.65, 0, 0.35, 1) forwards}
@keyframes fill{from{width:0}to{width:100%}}
@keyframes pulse{0%,100%{opacity:.8}50%{opacity:1;transform:scale(1.02)}}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:1rem 2.5rem;display:flex;align-items:center;justify-content:space-between;background:rgba(3,3,5,0.7);border-bottom:1px solid var(--border);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);transition:all .4s}
.nav-logo{font-family:var(--font-head);font-weight:800;font-size:1.4rem;color:var(--accent);letter-spacing:-.02em;text-shadow: 0 0 10px rgba(0,255,204,0.3)}
.nav-logo span{color:var(--text);font-weight:400;text-shadow:none}
.nav-links{display:flex;gap:2.5rem;list-style:none}
.nav-links a{color:var(--text2);text-decoration:none;font-size:.85rem;letter-spacing:.15em;text-transform:uppercase;transition:.3s ease;font-family:var(--font-head);font-weight:700;position:relative}
.nav-links a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--accent);transition:.3s ease;border-radius:2px}
.nav-links a:hover{color:var(--text)}
.nav-links a:hover::after{width:100%;box-shadow:0 0 8px var(--accent)}
.nav-actions{display:flex;gap:1.5rem;align-items:center}
.btn-theme{background:var(--surface);border:1px solid var(--border);color:var(--text);padding:.5rem .9rem;border-radius:8px;cursor:pointer;font-size:.9rem;transition:.3s ease;display:flex;align-items:center;justify-content:center}
.btn-theme:hover{border-color:var(--accent);color:var(--accent);box-shadow:0 0 15px rgba(0,255,204,0.2);transform:translateY(-1px)}
.hamburger{display:none;background:none;border:none;cursor:pointer;color:var(--text);font-size:1.5rem}

/* HERO */
#hero{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:8rem 2rem 4rem;position:relative;overflow:hidden}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(var(--border) 1px,transparent 1px),linear-gradient(90deg,var(--border) 1px,transparent 1px);background-size:80px 80px;opacity:.2;transform:perspective(500px) rotateX(60deg) translateY(-100px) translateZ(-200px);animation:gridMove 20s linear infinite}
@keyframes gridMove{from{background-position:0 0}to{background-position:0 80px}}
.hero-glow{position:absolute;top:10%;left:50%;transform:translateX(-50%);width:800px;height:800px;background:radial-gradient(ellipse,rgba(0,255,204,.15) 0%,transparent 60%);pointer-events:none;filter:blur(40px)}
.hero-content{text-align:center;position:relative;z-index:1;max-width:1000px}
.hero-tag{display:inline-flex;align-items:center;gap:0.5rem;background:var(--surface2);border:1px solid var(--border);color:var(--accent);font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;padding:.5rem 1.2rem;border-radius:999px;margin-bottom:2.5rem;animation:fadeUp 1s cubic-bezier(0.2, 0.8, 0.2, 1) both;backdrop-filter:blur(10px);box-shadow:0 4px 20px rgba(0,0,0,0.2)}
.hero-title{font-family:var(--font-head);font-size:clamp(3rem,9vw,7.5rem);font-weight:800;line-height:1.05;letter-spacing:-.04em;margin-bottom:2rem;animation:fadeUp 1s .2s cubic-bezier(0.2, 0.8, 0.2, 1) both}
.hero-title .name{background:linear-gradient(135deg,var(--text) 0%,var(--text2) 100%);-webkit-background-clip:text;background-clip:text;color:transparent;display:block;padding-bottom:.2em}
.hero-title .role{color:var(--text);display:block;font-size:.4em;font-weight:400;font-family:var(--font-serif);font-style:italic;letter-spacing:.03em;margin-top:1rem;opacity:0.9}
.hero-subtitle{color:var(--text2);font-size:1.1rem;max-width:650px;margin:0 auto 3.5rem;animation:fadeUp 1s .4s cubic-bezier(0.2, 0.8, 0.2, 1) both;line-height:1.9}
.hero-subtitle em{color:var(--accent);font-style:normal;font-weight:500;text-shadow:0 0 10px rgba(0,255,204,0.3)}
.hero-ctas{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;animation:fadeUp 1s .6s cubic-bezier(0.2, 0.8, 0.2, 1) both}
.btn-primary{background:linear-gradient(135deg,var(--accent),#00ccaa);color:#000;padding:.9rem 2.5rem;border-radius:12px;font-family:var(--font-head);font-weight:800;font-size:.95rem;text-decoration:none;transition:all .3s ease;border:none;cursor:pointer;letter-spacing:.05em;box-shadow:0 10px 30px rgba(0,255,204,.2)}
.btn-primary:hover{transform:translateY(-3px) scale(1.02);box-shadow:0 15px 40px rgba(0,255,204,.4)}
.btn-secondary{background:var(--surface);color:var(--text);padding:.9rem 2.5rem;border-radius:12px;font-family:var(--font-head);font-weight:700;font-size:.95rem;text-decoration:none;transition:all .3s ease;border:1px solid var(--border);cursor:pointer;backdrop-filter:blur(10px)}
.btn-secondary:hover{border-color:var(--accent2);color:var(--accent2);transform:translateY(-3px);background:rgba(176,82,255,0.05);box-shadow:0 10px 30px rgba(176,82,255,.15)}
.hero-stats{display:flex;gap:4rem;justify-content:center;margin-top:5rem;padding-top:4rem;border-top:1px solid var(--border);animation:fadeUp 1s .8s cubic-bezier(0.2, 0.8, 0.2, 1) both;background:linear-gradient(90deg,transparent,var(--border),transparent);background-size:100% 1px;background-repeat:no-repeat}
.stat{text-align:center;position:relative}
.stat::after{content:'';position:absolute;right:-2rem;top:50%;transform:translateY(-50%);width:1px;height:30px;background:var(--border)}
.stat:last-child::after{display:none}
.stat-num{font-family:var(--font-head);font-size:2.5rem;font-weight:800;color:transparent;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;display:block;line-height:1.2}
.stat-label{font-size:.8rem;color:var(--text3);text-transform:uppercase;letter-spacing:.15em;font-weight:600}
.scroll-indicator{position:absolute;bottom:2.5rem;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:.75rem;color:var(--text3);font-size:.75rem;animation:bounce 2s infinite cubic-bezier(0.4, 0, 0.2, 1);letter-spacing:.2em;text-transform:uppercase}
@keyframes bounce{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(-10px)}}

/* SECTIONS */
section{padding:8rem 2rem;position:relative}
.container{max-width:1200px;margin:0 auto}
.section-label{display:inline-block;font-size:.8rem;letter-spacing:.3em;text-transform:uppercase;color:var(--accent);margin-bottom:1rem;font-family:var(--font-head);font-weight:700;background:rgba(0,255,204,0.1);padding:0.4rem 1rem;border-radius:999px;border:1px solid rgba(0,255,204,0.2)}
.section-title{font-family:var(--font-head);font-size:clamp(2.5rem,6vw,4rem);font-weight:800;line-height:1.1;letter-spacing:-.03em;margin-bottom:1.5rem;color:var(--text)}
.section-subtitle{color:var(--text2);font-size:1.05rem;max-width:650px;margin-bottom:5rem;line-height:1.8}

/* ABOUT */
#about{background:linear-gradient(180deg,transparent,var(--bg2),transparent)}
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}
.about-visual{position:relative}
.about-card{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:24px;padding:2.5rem;position:relative;overflow:hidden;transform:perspective(1000px) rotateY(5deg);transition:transform 0.5s ease;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.1)}
.about-card:hover{transform:perspective(1000px) rotateY(0deg) translateY(-10px);box-shadow:0 20px 40px rgba(0,0,0,0.3), 0 0 30px var(--card-glow)}
.about-card::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at top right,var(--card-glow),transparent 70%);pointer-events:none}
.avatar{width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-family:var(--font-head);font-weight:800;font-size:2rem;color:#000;margin-bottom:2rem;box-shadow:0 10px 25px rgba(0,255,204,0.3);border:4px solid var(--surface2)}
.about-name{font-family:var(--font-head);font-size:1.6rem;font-weight:800;margin-bottom:.5rem;color:var(--text)}
.about-role{color:var(--accent);font-size:.95rem;margin-bottom:2rem;font-weight:600;letter-spacing:.05em}
.about-detail{display:flex;align-items:center;gap:1rem;margin-bottom:1rem;font-size:.9rem;color:var(--text2)}
.about-detail i{color:var(--accent);width:20px;font-size:1.1rem;text-shadow:0 0 10px rgba(0,255,204,0.4)}
.about-cgpa{display:inline-block;background:linear-gradient(135deg,rgba(0,255,204,0.1),transparent);border:1px solid var(--accent);border-radius:12px;padding:.75rem 1.25rem;font-family:var(--font-head);font-weight:800;color:var(--accent);font-size:1.3rem;margin-top:1.5rem;box-shadow:0 0 20px rgba(0,255,204,0.1)}
.about-text p{color:var(--text2);margin-bottom:1.5rem;font-size:1.05rem;line-height:1.9}
.about-text strong{color:var(--text);font-weight:600}

/* SKILLS */
#skills{background:var(--bg)}
.skills-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:2rem;margin-bottom:4rem}
.skill-category{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:20px;padding:2rem;transition:all .4s cubic-bezier(0.175, 0.885, 0.32, 1.275);position:relative;overflow:hidden;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.1)}
.skill-category::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,var(--card-glow),transparent);opacity:0;transition:.4s ease}
.skill-category:hover{border-color:var(--accent);transform:translateY(-10px) scale(1.02);box-shadow:0 20px 40px rgba(0,255,204,0.1)}
.skill-category:hover::before{opacity:1}
.skill-cat-label{font-family:var(--font-head);font-weight:800;font-size:.9rem;text-transform:uppercase;letter-spacing:.15em;color:var(--accent);margin-bottom:1.5rem;display:flex;align-items:center;gap:.75rem}
.skill-item{display:flex;align-items:center;gap:1rem;margin-bottom:1rem;font-size:.95rem;color:var(--text2);font-weight:500;transition:.2s ease}
.skill-item:hover{color:var(--text);transform:translateX(5px)}
.skill-dot{width:8px;height:8px;border-radius:50%;background:var(--accent);flex-shrink:0;box-shadow:0 0 10px var(--accent)}
.chart-wrap{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:24px;padding:3rem;position:relative;overflow:hidden;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.1)}
.chart-title{font-family:var(--font-head);font-weight:800;margin-bottom:2rem;font-size:1.3rem;color:var(--text)}

/* EXPERIENCE */
#experience{background:linear-gradient(180deg,transparent,var(--bg2),transparent)}
.timeline{position:relative;padding-left:2.5rem}
.timeline::before{content:'';position:absolute;left:0;top:0;bottom:0;width:2px;background:linear-gradient(to bottom,transparent,var(--accent),var(--accent2),transparent)}
.timeline-item{position:relative;margin-bottom:4rem;padding-left:2.5rem;transition:.3s ease}
.timeline-item:hover{transform:translateX(10px)}
.timeline-dot{position:absolute;left:-3rem;top:.25rem;width:16px;height:16px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 6px var(--bg2),0 0 20px var(--accent);transition:.3s ease}
.timeline-item:hover .timeline-dot{transform:scale(1.3)}
.timeline-date{font-size:.85rem;color:var(--accent);font-family:var(--font-head);font-weight:700;letter-spacing:.15em;text-transform:uppercase;margin-bottom:.75rem;display:inline-block;background:rgba(0,255,204,0.1);padding:.3rem .8rem;border-radius:6px}
.timeline-title{font-family:var(--font-head);font-size:1.4rem;font-weight:800;margin-bottom:.5rem;color:var(--text)}
.timeline-company{color:var(--text2);font-size:.95rem;margin-bottom:1.5rem;font-weight:500}
.timeline-company span{color:var(--accent2);font-weight:600}
.timeline-bullets{list-style:none;display:flex;flex-direction:column;gap:1rem}
.timeline-bullets li{color:var(--text2);font-size:.95rem;padding-left:2rem;position:relative;line-height:1.8}
.timeline-bullets li::before{content:'▹';position:absolute;left:0;top:-2px;color:var(--accent);font-size:1.2rem;font-weight:bold}

/* PROJECTS */
#projects{background:var(--bg)}
.projects-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:2.5rem}
.project-card{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:20px;padding:2.5rem;transition:all .4s cubic-bezier(0.175, 0.885, 0.32, 1.275);cursor:pointer;position:relative;overflow:hidden;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.1);display:flex;flex-direction:column}
.project-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:4px;background:linear-gradient(90deg,var(--accent),var(--accent2));transform:scaleX(0);transform-origin:left;transition:transform .4s ease}
.project-card:hover{border-color:var(--border2);transform:translateY(-12px);box-shadow:0 25px 50px rgba(0,0,0,.4), 0 0 20px rgba(0,255,204,0.1)}
.project-card:hover::before{transform:scaleX(1)}
.project-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:1.5rem}
.project-icon{width:56px;height:56px;border-radius:14px;background:linear-gradient(135deg,var(--surface2),var(--surface));border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:1.6rem;flex-shrink:0;box-shadow:inset 0 2px 10px rgba(255,255,255,0.05)}
.project-badge{font-size:.7rem;font-family:var(--font-head);font-weight:800;text-transform:uppercase;letter-spacing:.15em;padding:.4rem 1rem;border-radius:999px;border:1px solid}
.badge-academic{color:var(--accent);border-color:rgba(0,255,204,0.3);background:rgba(0,255,204,0.05)}
.badge-personal{color:var(--accent2);border-color:rgba(176,82,255,0.3);background:rgba(176,82,255,0.05)}
.project-name{font-family:var(--font-head);font-size:1.3rem;font-weight:800;margin-bottom:.75rem;color:var(--text);transition:.3s ease}
.project-card:hover .project-name{color:var(--accent)}
.project-desc{color:var(--text2);font-size:.95rem;margin-bottom:2rem;line-height:1.7;flex-grow:1}
.project-tags{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:auto}
.tag{font-size:.75rem;font-family:var(--font-head);background:rgba(255,255,255,0.03);border:1px solid var(--border);padding:.35rem .8rem;border-radius:6px;color:var(--text2);font-weight:600;transition:.3s ease}
.project-card:hover .tag{background:rgba(255,255,255,0.08);color:var(--text)}

/* ML DEMO */
#ml-demo{background:linear-gradient(180deg,transparent,var(--bg2),transparent)}
.demo-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:3rem;align-items:start}
.demo-panel{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:24px;padding:3rem;position:relative;overflow:hidden;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.1)}
.demo-panel::after{content:'';position:absolute;inset:0;background:radial-gradient(circle at bottom right,rgba(176,82,255,0.08),transparent 60%);pointer-events:none}
.demo-title{font-family:var(--font-head);font-weight:800;font-size:1.2rem;margin-bottom:2rem;color:transparent;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;display:inline-block}
.demo-input{width:100%;background:rgba(0,0,0,0.3);border:1px solid var(--border2);color:var(--text);padding:1rem 1.5rem;border-radius:12px;font-family:var(--font-body);font-size:.95rem;outline:none;transition:all .3s ease;box-shadow:inset 0 2px 10px rgba(0,0,0,0.2)}
.demo-input:focus{border-color:var(--accent);box-shadow:0 0 15px rgba(0,255,204,0.2), inset 0 2px 10px rgba(0,0,0,0.2);background:rgba(0,0,0,0.5)}
.demo-btn{margin-top:1rem;background:linear-gradient(135deg,var(--accent),#00ccaa);color:#000;border:none;padding:1rem 2rem;border-radius:12px;font-family:var(--font-head);font-weight:800;cursor:pointer;width:100%;font-size:.95rem;transition:all .3s ease;text-transform:uppercase;letter-spacing:.1em;box-shadow:0 8px 20px rgba(0,255,204,0.2)}
.demo-btn:hover{transform:translateY(-2px);box-shadow:0 12px 25px rgba(0,255,204,0.3)}
.demo-result{margin-top:2rem;padding:1.5rem;border-radius:12px;font-size:1rem;font-family:var(--font-head);text-align:center;font-weight:800;display:none;animation:fadeIn .5s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.result-safe{background:rgba(0,255,204,.1);border:1px solid var(--accent);color:var(--accent);box-shadow:0 0 20px rgba(0,255,204,0.1)}
.result-danger{background:rgba(255,51,102,.1);border:1px solid var(--accent3);color:var(--accent3);box-shadow:0 0 20px rgba(255,51,102,0.1)}
.result-neutral{background:rgba(176,82,255,.1);border:1px solid var(--accent2);color:var(--accent2);box-shadow:0 0 20px rgba(176,82,255,0.1)}
.features-list{display:flex;flex-direction:column;gap:1rem}
.feature-item{display:flex;align-items:center;gap:1.2rem;padding:1rem 1.2rem;background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:12px;transition:.3s ease}
.feature-item:hover{background:rgba(255,255,255,0.05);transform:translateX(5px);border-color:var(--border2)}
.feature-icon{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0;box-shadow:0 4px 10px rgba(0,0,0,0.2)}
.feature-txt{font-size:.85rem;color:var(--text2);line-height:1.4}
.feature-txt strong{color:var(--text);display:block;font-size:.95rem;margin-bottom:.2rem;font-weight:700}

/* CONTACT */
#contact{background:var(--bg)}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem}
.contact-form{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:24px;padding:3rem;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.1)}
.form-group{margin-bottom:1.5rem}
.form-label{display:block;font-size:.85rem;font-family:var(--font-head);font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:var(--text2);margin-bottom:.75rem}
.form-control{width:100%;background:rgba(0,0,0,0.3);border:1px solid var(--border2);color:var(--text);padding:1rem 1.2rem;border-radius:12px;font-family:var(--font-body);font-size:.95rem;outline:none;transition:all .3s ease;resize:vertical}
.form-control:focus{border-color:var(--accent);box-shadow:0 0 15px rgba(0,255,204,0.15);background:rgba(0,0,0,0.5)}
textarea.form-control{min-height:150px}
.form-submit{background:linear-gradient(135deg,var(--accent),#00ccaa);color:#000;border:none;padding:1.1rem 2rem;border-radius:12px;font-family:var(--font-head);font-weight:800;cursor:pointer;width:100%;font-size:1rem;transition:all .3s ease;text-transform:uppercase;letter-spacing:.1em;box-shadow:0 8px 20px rgba(0,255,204,0.2)}
.form-submit:hover{transform:translateY(-3px);box-shadow:0 15px 30px rgba(0,255,204,.3)}
.form-success{display:none;text-align:center;padding:3rem 2rem;color:var(--accent);background:rgba(0,255,204,0.05);border-radius:16px;border:1px dashed var(--accent)}
.contact-info{display:flex;flex-direction:column;gap:1.5rem}
.contact-detail{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:16px;padding:1.5rem;display:flex;align-items:center;gap:1.5rem;transition:all .3s ease;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.1)}
.contact-detail:hover{border-color:var(--accent);transform:translateX(10px);background:rgba(255,255,255,0.05);box-shadow:0 10px 25px rgba(0,0,0,0.2)}
.contact-icon{width:56px;height:56px;background:linear-gradient(135deg,var(--surface2),var(--surface));border:1px solid var(--border);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--accent);font-size:1.3rem;flex-shrink:0;box-shadow:inset 0 2px 10px rgba(255,255,255,0.05)}
.contact-detail-text{font-size:.9rem;color:var(--text2);line-height:1.5}
.contact-detail-text strong{color:var(--text);display:block;font-family:var(--font-head);font-weight:800;font-size:1.1rem;margin-bottom:.2rem}

/* RESUME */
#resume{background:linear-gradient(180deg,transparent,var(--bg2),transparent)}
.resume-preview{background:var(--surface);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:24px;padding:4rem;max-width:800px;margin:0 auto;position:relative;box-shadow:0 20px 60px rgba(0,0,0,0.3), 0 0 40px rgba(0,255,204,0.05);border:1px solid var(--border)}
.resume-header{display:flex;align-items:center;gap:2.5rem;margin-bottom:3rem;padding-bottom:2.5rem;border-bottom:1px solid var(--border)}
.resume-avatar{width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-family:var(--font-head);font-weight:800;font-size:1.5rem;color:#000;box-shadow:0 8px 20px rgba(0,255,204,0.3);border:3px solid var(--surface)}
.resume-name{font-family:var(--font-head);font-size:1.8rem;font-weight:800;margin-bottom:.4rem;color:var(--text)}
.resume-role{color:var(--accent);font-size:.95rem;font-weight:600;letter-spacing:.05em}
.resume-section{margin-bottom:2.5rem}
.resume-section-title{font-family:var(--font-head);font-size:.85rem;text-transform:uppercase;letter-spacing:.25em;color:var(--accent);margin-bottom:1.2rem;padding-bottom:.5rem;border-bottom:1px solid var(--border);font-weight:800}
.resume-item{margin-bottom:1rem;padding-left:1rem;border-left:2px solid var(--border);transition:.3s ease}
.resume-item:hover{border-left-color:var(--accent);background:rgba(255,255,255,0.02)}
.resume-item-title{font-family:var(--font-head);font-weight:700;font-size:1rem;color:var(--text);margin-bottom:.2rem}
.resume-item-sub{color:var(--text2);font-size:.85rem;font-weight:500}
.download-btn{display:flex;align-items:center;gap:1rem;background:linear-gradient(135deg,var(--accent),#00ccaa);color:#000;padding:1.1rem 2.5rem;border-radius:12px;text-decoration:none;font-family:var(--font-head);font-weight:800;font-size:1rem;transition:all .3s ease;margin:3rem auto 0;max-width:fit-content;border:none;cursor:pointer;text-transform:uppercase;letter-spacing:.1em;box-shadow:0 10px 30px rgba(0,255,204,.2)}
.download-btn:hover{transform:translateY(-3px);box-shadow:0 15px 40px rgba(0,255,204,.4)}

/* ADMIN SECTION */
#admin{background:var(--bg);border-top:1px solid var(--border)}
.admin-toggle{text-align:center;margin-bottom:3rem}
.admin-unlock{background:var(--surface);border:1px solid var(--border);color:var(--text2);padding:.8rem 2rem;border-radius:12px;cursor:pointer;font-family:var(--font-body);font-size:.9rem;transition:all .3s ease;font-weight:600}
.admin-unlock:hover{border-color:var(--accent3);color:var(--accent3);background:rgba(255,51,102,0.05);box-shadow:0 0 20px rgba(255,51,102,0.1)}
.admin-panel{display:none;background:var(--surface);border:1px solid var(--border2);border-radius:24px;padding:3rem;max-width:800px;margin:0 auto;backdrop-filter:blur(16px);box-shadow:0 20px 50px rgba(0,0,0,0.3)}
.admin-panel.active{display:block;animation:fadeIn .5s ease}
.admin-title{font-family:var(--font-head);font-weight:800;font-size:1.3rem;margin-bottom:2rem;display:flex;align-items:center;gap:1rem;color:var(--text)}
.admin-badge{font-size:.75rem;background:rgba(255,51,102,.15);border:1px solid var(--accent3);color:var(--accent3);padding:.3rem .8rem;border-radius:6px;font-weight:700;letter-spacing:.1em}
.project-entries{display:flex;flex-direction:column;gap:1rem;margin-bottom:2.5rem}
.project-entry{background:rgba(0,0,0,0.2);border:1px solid var(--border);border-radius:12px;padding:1.2rem 1.5rem;display:flex;align-items:center;justify-content:space-between;transition:.3s ease}
.project-entry:hover{background:rgba(255,255,255,0.03);border-color:var(--border2)}
.entry-name{font-family:var(--font-head);font-weight:700;font-size:1rem;color:var(--text);margin-bottom:.2rem}
.entry-actions{display:flex;gap:.75rem}
.btn-edit,.btn-delete{background:var(--surface);border:1px solid var(--border);padding:.4rem 1rem;border-radius:8px;cursor:pointer;font-size:.8rem;font-family:var(--font-head);font-weight:700;transition:all .3s ease}
.btn-edit{color:var(--accent2)}
.btn-edit:hover{border-color:var(--accent2);background:rgba(176,82,255,0.1)}
.btn-delete{color:var(--accent3)}
.btn-delete:hover{border-color:var(--accent3);background:rgba(255,51,102,0.1)}
.add-project-form{background:rgba(0,0,0,0.2);border:1px solid var(--border);border-radius:16px;padding:2rem}
.add-form-title{font-family:var(--font-head);font-size:1rem;font-weight:800;color:var(--accent);margin-bottom:1.5rem;text-transform:uppercase;letter-spacing:.1em}
.add-btn{background:var(--surface2);border:1px solid var(--border);color:var(--text);padding:.8rem 1.5rem;border-radius:10px;font-family:var(--font-head);font-weight:700;cursor:pointer;font-size:.9rem;transition:all .3s ease;margin-top:1rem}
.add-btn:hover{border-color:var(--accent);color:var(--accent);background:rgba(0,255,204,0.05);box-shadow:0 0 15px rgba(0,255,204,0.1)}
.toast{position:fixed;bottom:2.5rem;right:2.5rem;background:var(--surface);border:1px solid var(--accent);color:var(--text);padding:1.2rem 2rem;border-radius:12px;font-family:var(--font-head);font-size:.95rem;font-weight:600;z-index:1000;transform:translateY(100px);opacity:0;transition:all .4s cubic-bezier(0.175, 0.885, 0.32, 1.275);display:flex;align-items:center;gap:1rem;backdrop-filter:blur(16px);box-shadow:0 10px 30px rgba(0,0,0,0.3)}
.toast.show{transform:translateY(0);opacity:1}
.toast i{color:var(--accent);font-size:1.2rem}

/* FOOTER */
footer{background:var(--bg);border-top:1px solid var(--border);padding:4rem 2rem;text-align:center;position:relative;overflow:hidden}
footer::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:300px;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent)}
.footer-logo{font-family:var(--font-head);font-size:2rem;font-weight:800;color:var(--accent);margin-bottom:1.5rem;text-shadow:0 0 15px rgba(0,255,204,0.3)}
.footer-links{display:flex;gap:2.5rem;justify-content:center;margin-bottom:2.5rem;flex-wrap:wrap}
.footer-links a{color:var(--text2);text-decoration:none;font-size:.9rem;transition:.3s ease;font-family:var(--font-head);font-weight:600;text-transform:uppercase;letter-spacing:.1em}
.footer-links a:hover{color:var(--accent)}
.footer-social{display:flex;gap:1.5rem;justify-content:center;margin-bottom:2.5rem}
.social-btn{width:48px;height:48px;border-radius:12px;background:var(--surface);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;color:var(--text2);text-decoration:none;transition:all .3s ease;font-size:1.1rem}
.social-btn:hover{border-color:var(--accent);color:var(--accent);transform:translateY(-5px);box-shadow:0 10px 20px rgba(0,255,204,0.15)}
.footer-copy{color:var(--text3);font-size:.85rem;font-weight:500}

@keyframes fadeUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
.reveal{opacity:0;transform:translateY(40px);transition:all .8s cubic-bezier(0.175, 0.885, 0.32, 1.275)}
.reveal.visible{opacity:1;transform:none}

/* MOBILE */
@media(max-width:768px){
.nav-links{display:none;position:fixed;inset:0;top:70px;background:rgba(10,10,15,0.95);backdrop-filter:blur(20px);flex-direction:column;align-items:center;justify-content:center;gap:2.5rem;z-index:99;border-top:1px solid var(--border)}
.nav-links.open{display:flex;animation:fadeIn .3s ease}
.hamburger{display:block}
.about-grid,.demo-grid,.contact-grid{grid-template-columns:1fr}
.hero-stats{gap:2rem;flex-wrap:wrap}
.stat::after{display:none}
section{padding:5rem 1.25rem}
.hero-title{font-size:clamp(2.5rem,10vw,4rem)}
.project-card{padding:1.5rem}
}
</style>"""

content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
