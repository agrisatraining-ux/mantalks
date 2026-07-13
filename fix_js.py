with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

if '<script src="script.js"></script>' not in content:
    content = content.replace('</body>', '    <script src="script.js"></script>\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Make JS robust to missing elements
js_content = js_content.replace("navbar.classList", "navbar?.classList")
js_content = js_content.replace("mobileMenu.classList", "mobileMenu?.classList")
js_content = js_content.replace("hamburger.classList", "hamburger?.classList")
js_content = js_content.replace("hamburger.addEventListener", "if(hamburger) hamburger.addEventListener")

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Linked script.js and added null checks.")
