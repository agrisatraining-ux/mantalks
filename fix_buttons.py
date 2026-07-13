import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add onclick to the 'Time to Open Up' and 'Join the Circle Now' buttons
onclick_str = r' onclick="document.getElementById(\'booking-modal\').classList.remove(\'hidden\')"'

# Regex to find these specific buttons and add onclick
content = re.sub(
    r'(<button class="[^"]*?")(>[\s\n]*Time to Open Up[\s\n]*</button>)',
    r'\1' + onclick_str + r'\2',
    content
)

content = re.sub(
    r'(<button class="[^"]*?")(>[\s\n]*Join the Circle Now[\s\n]*</button>)',
    r'\1' + onclick_str + r'\2',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Added onclick handlers to booking buttons.")
