with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Navbar Logo
old_nav = """<a href="#" class="flex items-center">
                <img src="logo.png" alt="ManTalks Logo" class="h-14 w-auto object-contain">
            </a>"""
new_nav = """<a href="#" class="flex items-center gap-3">
                <img src="logo.png" alt="ManTalks Logo" class="h-14 w-auto object-contain">
                <span class="font-headline-md text-headline-md font-semibold text-primary">ManTalks</span>
            </a>"""
content = content.replace(old_nav, new_nav)

# Replace Footer Logo
old_foot = """<div class="flex items-center">
            <img src="logo.png" alt="ManTalks Logo" class="h-10 w-auto object-contain">
        </div>"""
new_foot = """<div class="flex items-center gap-2">
            <img src="logo.png" alt="ManTalks Logo" class="h-10 w-auto object-contain">
            <span class="font-headline-md text-headline-md font-semibold text-primary dark:text-on-primary-fixed">ManTalks</span>
        </div>"""
content = content.replace(old_foot, new_foot)

# Replace Modal Logo
old_modal = """<div class="mb-4">
    <img src="logo.png" alt="ManTalks Logo" class="h-12 w-auto object-contain">
</div>"""
new_modal = """<div class="flex items-center gap-3 mb-6">
    <img src="logo.png" alt="ManTalks Logo" class="h-12 w-auto object-contain">
    <h1 class="font-headline-lg-mobile text-headline-lg-mobile text-primary tracking-tighter">ManTalks</h1>
</div>"""
content = content.replace(old_modal, new_modal)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Text added next to logos.")
