import json
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace colors in the JS config block
# We will just do a simple string replace for the key colors.
replacements = {
    '"background": "#fff8f5"': '"background": "#f8f9fa"',
    '"primary": "#06190d"': '"primary": "#091221"',
    '"secondary": "#476550"': '"secondary": "#cc6b4d"',
    '"primary-container": "#1b2e20"': '"primary-container": "#1a2a40"',
    '"on-primary-container": "#819684"': '"on-primary-container": "#8b9cbe"',
    '"secondary-container": "#c6e8cd"': '"secondary-container": "#fce0d4"',
    '"on-secondary-container": "#4b6954"': '"on-secondary-container": "#8a3a1d"',
    '"tertiary": "#260f00"': '"tertiary": "#cc6b4d"',
    '"on-tertiary-container": "#d17c35"': '"on-tertiary-container": "#cc6b4d"',
    '"surface": "#fff8f5"': '"surface": "#f8f9fa"',
    '"surface-bright": "#fff8f5"': '"surface-bright": "#ffffff"',
    '"surface-dim": "#e1d8d3"': '"surface-dim": "#e9ecef"',
    '"surface-container": "#f5ece7"': '"surface-container": "#e9ecef"',
    '"surface-container-low": "#fbf2ed"': '"surface-container-low": "#f1f3f5"',
    '"surface-container-high": "#efe6e1"': '"surface-container-high": "#dee2e6"',
    '"surface-variant": "#eae1dc"': '"surface-variant": "#dee2e6"',
    '"on-surface": "#1f1b18"': '"on-surface": "#091221"',
    '"on-background": "#1f1b18"': '"on-background": "#091221"',
    '"primary-fixed": "#d1e8d3"': '"primary-fixed": "#d0dcf5"',
    '"on-primary-fixed": "#0c1f12"': '"on-primary-fixed": "#091221"',
    '"secondary-fixed": "#c9ebd0"': '"secondary-fixed": "#fcdbc9"',
    '"on-secondary-fixed": "#032110"': '"on-secondary-fixed": "#8a3a1d"',
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Also update the razorpay theme color
content = content.replace('"theme": { "color": "#7D9D85" }', '"theme": { "color": "#cc6b4d" }')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Colors updated successfully")
