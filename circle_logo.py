with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add rounded-full to all logo image tags
old_class_string = 'src="logo.png" alt="ManTalks Logo" class="'
new_class_string = 'src="logo.png" alt="ManTalks Logo" class="rounded-full shadow-md aspect-square '

content = content.replace(old_class_string, new_class_string)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Logo made circular.")
