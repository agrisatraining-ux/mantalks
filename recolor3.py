with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Teal with Royal Blue
replacements = {
    '"primary": "#144e66"': '"primary": "#1c3bd1"',
    '"primary-container": "#0c3b4d"': '"primary-container": "#11237a"',
    '"on-primary-container": "#9ad1e6"': '"on-primary-container": "#a3bbf0"',
    '"on-surface": "#144e66"': '"on-surface": "#1c3bd1"',
    '"on-background": "#144e66"': '"on-background": "#1c3bd1"',
    '"on-primary-fixed": "#144e66"': '"on-primary-fixed": "#1c3bd1"',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Colors updated to Blue/Green.")
