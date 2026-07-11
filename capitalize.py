with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace ManTalks with MANTALKS in the span next to the logo
old_text = '<span class="font-headline-md text-headline-md font-semibold text-primary">ManTalks</span>'
new_text = '<span class="font-headline-md text-headline-md font-semibold text-primary uppercase">MANTALKS</span>'
content = content.replace(old_text, new_text)

old_foot = '<span class="font-headline-md text-headline-md font-semibold text-primary dark:text-on-primary-fixed">ManTalks</span>'
new_foot = '<span class="font-headline-md text-headline-md font-semibold text-primary dark:text-on-primary-fixed uppercase">MANTALKS</span>'
content = content.replace(old_foot, new_foot)

old_modal = '<h1 class="font-headline-lg-mobile text-headline-lg-mobile text-primary tracking-tighter">ManTalks</h1>'
new_modal = '<h1 class="font-headline-lg-mobile text-headline-lg-mobile text-primary tracking-tighter uppercase">MANTALKS</h1>'
content = content.replace(old_modal, new_modal)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Text capitalized.")
