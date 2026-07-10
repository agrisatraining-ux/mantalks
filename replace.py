# Replace text
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("A safe space for men to share, listen &amp; connect.", "An open space for men to share, listen &amp; connect.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Text replaced successfully")
