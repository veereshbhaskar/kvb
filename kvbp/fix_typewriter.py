import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_script = """// TYPEWRITER EFFECT
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
  }"""

new_script = """// LOOPING TYPEWRITER EFFECT
  const typeText = "Veeresh Bhaskar Karatam";
  let typeIndex = 0;
  let isDeleting = false;
  function typeWriter() {
    const el = document.getElementById("typewriter-name");
    if (!el) return;
    
    if (!isDeleting && typeIndex <= typeText.length) {
      el.innerHTML = typeText.substring(0, typeIndex);
      typeIndex++;
      if (typeIndex > typeText.length) {
        isDeleting = true;
        setTimeout(typeWriter, 2000); // pause at end
        return;
      }
      setTimeout(typeWriter, 100);
    } else if (isDeleting && typeIndex >= 0) {
      el.innerHTML = typeText.substring(0, typeIndex);
      typeIndex--;
      if (typeIndex < 0) {
        isDeleting = false;
        typeIndex = 0;
        setTimeout(typeWriter, 500); // pause before restart
        return;
      }
      setTimeout(typeWriter, 50);
    }
  }"""

content = content.replace(old_script, new_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
