with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Navbar Logo
old_nav = """<div class="font-headline-md text-headline-md font-semibold text-primary">
                ManTalks
            </div>"""
new_nav = """<a href="#" class="flex items-center">
                <img src="logo.png" alt="ManTalks Logo" class="h-14 w-auto object-contain mix-blend-multiply">
            </a>"""
content = content.replace(old_nav, new_nav)

# Replace Footer Logo
old_foot = """<div class="font-headline-md text-headline-md text-primary dark:text-on-primary-fixed">
            ManTalks
        </div>"""
new_foot = """<div class="flex items-center">
            <img src="logo.png" alt="ManTalks Logo" class="h-10 w-auto object-contain mix-blend-multiply">
        </div>"""
content = content.replace(old_foot, new_foot)

# Replace Modal Logo
old_modal = """<h1 class="font-headline-lg-mobile text-headline-lg-mobile text-primary tracking-tighter mb-2">ManTalks</h1>"""
new_modal = """<div class="mb-4">
    <img src="logo.png" alt="ManTalks Logo" class="h-12 w-auto object-contain mix-blend-multiply">
</div>"""
content = content.replace(old_modal, new_modal)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Logos inserted.")
