with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(" mix-blend-multiply", "")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Mix blend mode removed.")
