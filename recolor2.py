with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace colors in the JS config block
replacements = {
    '"background": "#f8f9fa"': '"background": "#f4faec"',
    '"primary": "#091221"': '"primary": "#144e66"',
    '"secondary": "#cc6b4d"': '"secondary": "#1b8b32"',
    '"primary-container": "#1a2a40"': '"primary-container": "#0c3b4d"',
    '"on-primary-container": "#8b9cbe"': '"on-primary-container": "#9ad1e6"',
    '"secondary-container": "#fce0d4"': '"secondary-container": "#d6f5c4"',
    '"on-secondary-container": "#8a3a1d"': '"on-secondary-container": "#116323"',
    '"tertiary": "#cc6b4d"': '"tertiary": "#1b8b32"',
    '"on-tertiary-container": "#cc6b4d"': '"on-tertiary-container": "#1b8b32"',
    '"surface": "#f8f9fa"': '"surface": "#f4faec"',
    '"surface-dim": "#e9ecef"': '"surface-dim": "#e4edd8"',
    '"surface-container": "#e9ecef"': '"surface-container": "#e4edd8"',
    '"surface-container-low": "#f1f3f5"': '"surface-container-low": "#ebf5e1"',
    '"surface-container-high": "#dee2e6"': '"surface-container-high": "#d6e6c8"',
    '"surface-variant": "#dee2e6"': '"surface-variant": "#d6e6c8"',
    '"on-surface": "#091221"': '"on-surface": "#144e66"',
    '"on-background": "#091221"': '"on-background": "#144e66"',
    '"primary-fixed": "#d0dcf5"': '"primary-fixed": "#c7eefc"',
    '"on-primary-fixed": "#091221"': '"on-primary-fixed": "#144e66"',
    '"secondary-fixed": "#fcdbc9"': '"secondary-fixed": "#d3f7be"',
    '"on-secondary-fixed": "#8a3a1d"': '"on-secondary-fixed": "#116323"',
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Also update the razorpay theme color
content = content.replace('"theme": { "color": "#cc6b4d" }', '"theme": { "color": "#1b8b32" }')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Colors updated to Green/Teal successfully")
