import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Philosophy
philosophy_html = """
<!-- Philosophy Section -->
<section class="bg-surface-container py-section-gap fade-in-section">
    <div class="px-margin-mobile md:px-margin-desktop max-w-3xl mx-auto text-center">
        <h2 class="font-headline-lg-mobile md:font-headline-lg text-primary mb-6">Why We Exist</h2>
        <p class="font-body-lg text-on-surface-variant mb-6">
            For generations, men have been told to "man up," suppress their emotions, and carry their burdens in silence. This isolation leads to stress, burnout, and a deep sense of loneliness, even in a crowded room.
        </p>
        <p class="font-body-lg text-on-surface-variant">
            MANTALKS was created to break that cycle. We are not a clinical therapy service—we are a sanctuary of brotherhood. A place to put the armor down, speak your truth without judgment, and realize you are never walking alone.
        </p>
    </div>
</section>
"""
# Insert after Stats Strip, before About
content = content.replace('<!-- About Section -->', philosophy_html + '\n<!-- About Section -->')


# 2. Power of Brotherhood and 3. Who is this for?
brotherhood_html = """
<!-- Power of Brotherhood Section -->
<section class="bg-surface py-section-gap fade-in-section">
    <div class="px-margin-mobile md:px-margin-desktop max-w-container-max-width mx-auto">
        <div class="text-center mb-16">
            <h2 class="font-headline-lg-mobile md:font-headline-lg text-primary mb-4">The Power of Brotherhood</h2>
            <p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto">There is a unique, biological, and psychological relief that happens when men open up to other men.</p>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-surface-container-low p-8 rounded-[24px] border border-outline-variant/30 text-center soft-glow">
                <span class="material-symbols-outlined text-secondary text-5xl mb-4 icon-fill">handshake</span>
                <h3 class="font-headline-md text-on-surface mb-3">Shared Lived Experience</h3>
                <p class="font-body-md text-on-surface-variant">Only a man truly understands the invisible societal pressures placed on men. Speak with someone who inherently "gets it."</p>
            </div>
            <div class="bg-surface-container-low p-8 rounded-[24px] border border-outline-variant/30 text-center soft-glow">
                <span class="material-symbols-outlined text-secondary text-5xl mb-4 icon-fill">water_drop</span>
                <h3 class="font-headline-md text-on-surface mb-3">Emotional Unburdening</h3>
                <p class="font-body-md text-on-surface-variant">Venting lowers cortisol (the stress hormone). Releasing pent-up frustration directly improves focus, sleep, and physical health.</p>
            </div>
            <div class="bg-surface-container-low p-8 rounded-[24px] border border-outline-variant/30 text-center soft-glow">
                <span class="material-symbols-outlined text-secondary text-5xl mb-4 icon-fill">balance</span>
                <h3 class="font-headline-md text-on-surface mb-3">Zero Judgment</h3>
                <p class="font-body-md text-on-surface-variant">No diagnosing. No unsolicited advice. Just a raw, respectful environment where your thoughts are validated and kept strictly confidential.</p>
            </div>
        </div>
    </div>
</section>

<!-- Who Is This For Section -->
<section class="bg-primary-container text-on-primary-container py-section-gap fade-in-section">
    <div class="px-margin-mobile md:px-margin-desktop max-w-4xl mx-auto">
        <div class="text-center mb-12">
            <h2 class="font-headline-lg-mobile md:font-headline-lg text-primary-fixed mb-4">Is MANTALKS for you?</h2>
        </div>
        <div class="grid md:grid-cols-2 gap-6">
            <div class="flex items-start gap-4">
                <span class="material-symbols-outlined text-secondary mt-1">check_box</span>
                <p class="font-body-lg">You feel overwhelmed by responsibilities but have no one to safely vent to.</p>
            </div>
            <div class="flex items-start gap-4">
                <span class="material-symbols-outlined text-secondary mt-1">check_box</span>
                <p class="font-body-lg">You feel isolated or lonely, even when surrounded by friends and family.</p>
            </div>
            <div class="flex items-start gap-4">
                <span class="material-symbols-outlined text-secondary mt-1">check_box</span>
                <p class="font-body-lg">You want an unbiased, non-judgmental perspective on a tough situation.</p>
            </div>
            <div class="flex items-start gap-4">
                <span class="material-symbols-outlined text-secondary mt-1">check_box</span>
                <p class="font-body-lg">You just need someone to listen to you, without trying to "fix" your problems.</p>
            </div>
        </div>
    </div>
</section>
"""
# Insert after About Section end, before How It Works
content = content.replace('<!-- How It Works Section -->', brotherhood_html + '\n<!-- How It Works Section -->')

# 4. Testimonials
testimonials_html = """
<!-- Testimonials Section -->
<section class="bg-surface py-section-gap fade-in-section">
    <div class="px-margin-mobile md:px-margin-desktop max-w-container-max-width mx-auto">
        <div class="text-center mb-16">
            <h2 class="font-headline-lg-mobile md:font-headline-lg text-primary mb-4">Voices of the Brotherhood</h2>
            <p class="font-body-lg text-on-surface-variant max-w-2xl mx-auto">Real experiences from men who decided to open up.</p>
        </div>
        <div class="grid md:grid-cols-2 gap-8">
            <div class="bg-surface-container p-8 rounded-tr-[40px] rounded-bl-[40px] border-l-4 border-secondary">
                <p class="font-body-lg italic text-on-surface mb-6">"I didn't think talking would do much, but the sheer relief of saying things out loud to another guy who didn't judge me was incredible. I slept like a baby that night."</p>
                <div class="font-label-md text-on-surface-variant">— Anonymous, 34</div>
            </div>
            <div class="bg-surface-container p-8 rounded-tl-[40px] rounded-br-[40px] border-r-4 border-secondary text-right">
                <p class="font-body-lg italic text-on-surface mb-6">"It's hard to talk to my partner because I don't want to stress her out. This gave me the exact outlet I needed to process my career anxiety."</p>
                <div class="font-label-md text-on-surface-variant">— Anonymous, 29</div>
            </div>
        </div>
    </div>
</section>
"""
# Insert after How It Works end, before Guidelines
content = content.replace('<!-- Session Guidelines Section -->', testimonials_html + '\n<!-- Session Guidelines Section -->')

# 5. FAQ
faq_html = """
<!-- FAQ Section -->
<section class="bg-surface-container-low py-section-gap fade-in-section border-t border-surface-variant">
    <div class="px-margin-mobile md:px-margin-desktop max-w-3xl mx-auto">
        <div class="text-center mb-12">
            <h2 class="font-headline-lg-mobile md:font-headline-lg text-primary mb-4">Frequently Asked Questions</h2>
        </div>
        <div class="space-y-4">
            <details class="group bg-surface-container p-6 rounded-2xl cursor-pointer [&_summary::-webkit-details-marker]:hidden">
                <summary class="flex justify-between items-center font-headline-md text-on-surface">
                    Is this a substitute for clinical therapy?
                    <span class="material-symbols-outlined transition duration-300 group-open:-rotate-180">expand_more</span>
                </summary>
                <p class="mt-4 font-body-md text-on-surface-variant leading-relaxed">No, MANTALKS is a peer-support listening space, not a medical or psychiatric service. We provide a space for venting, connection, and brotherhood. If you are experiencing a severe mental health crisis, please seek professional clinical help.</p>
            </details>
            <details class="group bg-surface-container p-6 rounded-2xl cursor-pointer [&_summary::-webkit-details-marker]:hidden">
                <summary class="flex justify-between items-center font-headline-md text-on-surface">
                    Is my identity really safe?
                    <span class="material-symbols-outlined transition duration-300 group-open:-rotate-180">expand_more</span>
                </summary>
                <p class="mt-4 font-body-md text-on-surface-variant leading-relaxed">Absolutely. You are welcome to use an alias during booking, and our sessions are entirely confidential. What happens in the circle stays in the circle.</p>
            </details>
            <details class="group bg-surface-container p-6 rounded-2xl cursor-pointer [&_summary::-webkit-details-marker]:hidden">
                <summary class="flex justify-between items-center font-headline-md text-on-surface">
                    Who am I talking to?
                    <span class="material-symbols-outlined transition duration-300 group-open:-rotate-180">expand_more</span>
                </summary>
                <p class="mt-4 font-body-md text-on-surface-variant leading-relaxed">You will be speaking with empathetic, trained peers who understand the male experience. They are there to listen, validate, and support you—not to lecture or judge.</p>
            </details>
            <details class="group bg-surface-container p-6 rounded-2xl cursor-pointer [&_summary::-webkit-details-marker]:hidden">
                <summary class="flex justify-between items-center font-headline-md text-on-surface">
                    What if I just want to listen and not speak much?
                    <span class="material-symbols-outlined transition duration-300 group-open:-rotate-180">expand_more</span>
                </summary>
                <p class="mt-4 font-body-md text-on-surface-variant leading-relaxed">That is completely fine. There is no pressure to perform or speak. Sometimes just being present in a safe, understanding environment is exactly what you need.</p>
            </details>
        </div>
    </div>
</section>
"""
content = content.replace('<!-- CTA Section -->', faq_html + '\n<!-- CTA Section -->')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Content sections successfully injected.")
