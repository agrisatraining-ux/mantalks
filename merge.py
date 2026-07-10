import os
import re

# Read the old JS logic to keep
old_html = open("index.html", "r", encoding="utf-8").read()
# Extract the script tag at the bottom
script_match = re.search(r'<script>\s*// Intersection Observer.*?</script>', old_html, re.DOTALL)
if script_match:
    js_logic = script_match.group(0)
else:
    js_logic = ""

# Read the new design HTML
new_design = open("new_design.html", "r", encoding="utf-8").read()

# Split new design into head and body parts
head_part = new_design.split('</head>')[0]
body_part = new_design.split('</head>')[1]

# We need to add Razorpay script to head
head_part += '    <script src="https://checkout.razorpay.com/v1/checkout.js"></script>\n</head>'

# Read the modal design
modal_design = open("modal_design.html", "r", encoding="utf-8").read()
# Extract the form side of the modal. Stitch generated the form side for modal_design.html
# We'll just look for the form itself and wrap it.
form_side_match = re.search(r'<form.*?>(.*?)</form>', modal_design, re.DOTALL)
form_side = form_side_match.group(1) if form_side_match else ""

# Create a popup modal version of the form side
popup_modal = f"""
<!-- Booking Modal (Hidden by Default) -->
<div class="fixed inset-0 z-[100] hidden bg-surface-container-lowest/80 backdrop-blur-md flex items-center justify-center p-4 transition-all duration-300" id="booking-modal">
<div class="bg-surface-container max-w-2xl w-full p-8 md:p-12 rounded-2xl shadow-2xl relative max-h-[90vh] overflow-y-auto border border-outline-variant/20">
<button class="absolute top-4 right-4 text-on-surface-variant hover:text-on-surface transition-colors duration-200" onclick="document.getElementById('booking-modal').classList.add('hidden')">
<span class="material-symbols-outlined text-[24px]">close</span>
</button>
<h1 class="font-headline-lg-mobile text-headline-lg-mobile text-primary tracking-tighter mb-2">ManTalks</h1>
<h2 class="font-body-lg text-body-lg text-secondary mb-8">Session Request</h2>

<form class="space-y-8" id="joinForm" novalidate>
<!-- Personal Info -->
<div class="space-y-6">
<div class="relative group">
<label class="block font-label-md text-label-md text-on-surface-variant mb-2" for="display-name">Full Name (or Alias)</label>
<input id="display-name" name="displayName" class="w-full bg-surface-container-low border border-outline-variant/30 rounded-lg focus:border-secondary focus:ring-0 px-4 py-3 font-body-md text-body-md text-on-surface transition-colors" placeholder="John Doe" type="text" required/>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<div class="relative group">
<label class="block font-label-md text-label-md text-on-surface-variant mb-2" for="email">Email</label>
<input id="email" name="email" class="w-full bg-surface-container-low border border-outline-variant/30 rounded-lg focus:border-secondary focus:ring-0 px-4 py-3 font-body-md text-body-md text-on-surface transition-colors" placeholder="you@example.com" type="email" required/>
</div>
<div class="relative group">
<label class="block font-label-md text-label-md text-on-surface-variant mb-2" for="phone">Phone Number</label>
<input id="phone" name="phone" class="w-full bg-surface-container-low border border-outline-variant/30 rounded-lg focus:border-secondary focus:ring-0 px-4 py-3 font-body-md text-body-md text-on-surface transition-colors" placeholder="+91 98765 43210" type="tel" required/>
</div>
</div>
</div>
<!-- Divider -->
<div class="w-full h-[1px] bg-outline-variant/20 my-8"></div>
<!-- Preferences -->
<div class="space-y-8">
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<div>
<label class="block font-label-md text-label-md text-on-surface-variant mb-2" for="session-type">Session Type</label>
<select id="session-type" name="sessionType" class="w-full bg-surface-container-low border border-outline-variant/30 rounded-lg focus:border-secondary focus:ring-0 px-4 py-3 font-body-md text-body-md text-on-surface cursor-pointer" required>
<option value="" disabled selected>Select</option>
<option value="vent">I want to vent</option>
<option value="advice">I'd like peer advice</option>
<option value="listen">I just want to connect</option>
</select>
</div>
<div>
<label class="block font-label-md text-label-md text-on-surface-variant mb-2" for="language">Language</label>
<select id="language" name="language" class="w-full bg-surface-container-low border border-outline-variant/30 rounded-lg focus:border-secondary focus:ring-0 px-4 py-3 font-body-md text-body-md text-on-surface cursor-pointer" required>
<option value="" disabled selected>Select</option>
<option value="english">English</option>
<option value="tamil">Tamil</option>
</select>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<div>
<label class="block font-label-md text-label-md text-on-surface-variant mb-2" for="date">Preferred Date</label>
<input id="date" name="date" class="w-full bg-surface-container-low border border-outline-variant/30 rounded-lg focus:border-secondary focus:ring-0 px-4 py-3 font-body-md text-body-md text-on-surface" type="date" required/>
</div>
<div>
<label class="block font-label-md text-label-md text-on-surface-variant mb-2" for="time-pref">Time Slot</label>
<select id="time-pref" name="timePref" class="w-full bg-surface-container-low border border-outline-variant/30 rounded-lg focus:border-secondary focus:ring-0 px-4 py-3 font-body-md text-body-md text-on-surface cursor-pointer" required>
<option value="" disabled selected>Select time</option>
<option value="morning">Morning (6am – 10am)</option>
<option value="noon">Afternoon (12pm – 3pm)</option>
<option value="evening">Evening (6pm – 9pm)</option>
<option value="night">Night (9pm – 11pm)</option>
</select>
</div>
</div>
</div>
<!-- Consent & Submit -->
<div class="pt-6 space-y-8">
<label class="flex items-start gap-4 cursor-pointer group">
<div class="relative flex items-start pt-1">
<input id="consent" name="consent" class="peer sr-only" required type="checkbox"/>
<div class="w-5 h-5 border-2 border-outline-variant rounded bg-transparent peer-checked:bg-secondary peer-checked:border-secondary transition-colors flex items-center justify-center">
<span class="material-symbols-outlined text-[16px] text-white opacity-0 peer-checked:opacity-100">check</span>
</div>
</div>
<span class="font-label-sm text-label-sm text-on-surface-variant leading-relaxed block pt-1">
                            I understand this is a peer-led listening space and not a medical/therapeutic service. I agree to the guidelines.
                        </span>
</label>
<button id="submit-btn" class="w-full bg-secondary text-white font-label-md text-label-md py-4 px-8 rounded-xl hover:shadow-[0_4px_20px_rgba(188,108,37,0.3)] hover:-translate-y-1 transition-all duration-300 flex items-center justify-center gap-2" type="submit">
                        <span class="btn-text">Confirm Booking (₹399)</span>
                        <span class="btn-loading" style="display:none">Processing...</span>
                        <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
</button>
<div id="formSuccess" style="display:none;" class="mt-4 p-4 bg-secondary/10 rounded-lg text-secondary text-center text-label-md">
    SUCCESS. WE'LL CONTACT YOU SHORTLY.
</div>
</div>
</form>
</div>
</div>
"""

# Replace any href="#join" with modal popup trigger
body_part = re.sub(r'href="#join"', 'onclick="document.getElementById(\'booking-modal\').classList.remove(\'hidden\'); return false;" href="#"', body_part)

# Inject modal before the script
body_part = body_part.replace('</body></html>', popup_modal + '\n' + js_logic + '\n</body></html>')

# Fix a small bug in original JS logic where it searches for btnText and btnLoading
js_logic_fixed = js_logic.replace("btnLoading.style.display = 'inline';", "btnLoading.style.display = 'inline-block';")

final_html = head_part + body_part

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Merged successfully!")
