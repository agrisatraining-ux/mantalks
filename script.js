// ── Scroll Reveal ────────────────────────────────────────────────────────────
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  },
  { threshold: 0.1, rootMargin: '0px 0px -60px 0px' }
);
reveals.forEach((el) => observer.observe(el));

// ── Navbar Transparency on Scroll ────────────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ── Smooth Scroll for all anchor links ───────────────────────────────────────
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
      // Close mobile menu if open
      mobileMenu.classList.remove('open');
      hamburger.classList.remove('active');
    }
  });
});

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  mobileMenu.classList.toggle('open');
});

// ── Modal Logic ──────────────────────────────────────────────────────────────
const modalOverlay = document.getElementById('modalOverlay');
const closeModalBtn = document.getElementById('closeModal');
const openModalBtns = document.querySelectorAll('.open-modal');

function openModal() {
  modalOverlay.classList.add('active');
  document.body.style.overflow = 'hidden'; // Prevent scroll
}

function closeModal() {
  modalOverlay.classList.remove('active');
  document.body.style.overflow = ''; // Restore scroll
}

openModalBtns.forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    openModal();
  });
});

closeModalBtn.addEventListener('click', closeModal);

modalOverlay.addEventListener('click', (e) => {
  if (e.target === modalOverlay) closeModal();
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
    closeModal();
  }
});

// ── Form Submission ───────────────────────────────────────────────────────────
const joinForm = document.getElementById('joinForm');
const submitBtn = document.getElementById('submit-btn');
const btnText = submitBtn.querySelector('.btn-text');
const btnLoading = submitBtn.querySelector('.btn-loading');
const formSuccess = document.getElementById('formSuccess');

// Google Sheets Web App URL — replace with your deployed script URL
const GOOGLE_SHEET_URL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';

joinForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  // Basic validation
  const consent = document.getElementById('consent');
  if (!consent.checked) {
    shakeElement(consent.closest('.form-consent'));
    return;
  }

  const requiredFields = joinForm.querySelectorAll('[required]');
  let valid = true;
  requiredFields.forEach((field) => {
    if (!field.value.trim() || (field.type === 'checkbox' && !field.checked)) {
      field.classList.add('error');
      valid = false;
    } else {
      field.classList.remove('error');
    }
  });

  if (!valid) return;

  // Collect data
  const formData = {
    displayName: joinForm.displayName.value.trim(),
    email: joinForm.email.value.trim(),
    phone: joinForm.phone.value.trim(),
    language: joinForm.language.value,
    sessionType: joinForm.sessionType.value,
    date: joinForm.date.value,
    timePref: joinForm.timePref.value,
    timestamp: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }),
  };

  // Show loading
  btnText.style.display = 'none';
  btnLoading.style.display = 'inline';
  submitBtn.disabled = true;

  try {
    if (GOOGLE_SHEET_URL !== 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE') {
      await fetch(GOOGLE_SHEET_URL, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
    } else {
      // Simulate network delay for demo
      await new Promise((r) => setTimeout(r, 1200));
    }

    // Success
    joinForm.style.display = 'none';
    formSuccess.style.display = 'flex';
    formSuccess.classList.add('visible');

    // Keep modal open for a moment so they see success, then maybe close?
    // For now just show success.
  } catch (err) {
    console.error('Submission error:', err);
    btnText.style.display = 'inline';
    btnLoading.style.display = 'none';
    submitBtn.disabled = false;
    alert('Something went wrong. Please try again or contact us directly.');
  }
});

// Remove error class on input
joinForm.querySelectorAll('input, select, textarea').forEach((el) => {
  el.addEventListener('input', () => el.classList.remove('error'));
});

// ── Shake Animation Helper ────────────────────────────────────────────────────
function shakeElement(el) {
  el.classList.add('shake');
  setTimeout(() => el.classList.remove('shake'), 600);
}

// ── Animated Counter (stats strip) ───────────────────────────────────────────
function animateStats() {
  const statsSection = document.querySelector('.stats-strip');
  if (!statsSection) return;

  const statsObserver = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        statsSection.classList.add('animated');
        statsObserver.disconnect();
      }
    },
    { threshold: 0.5 }
  );
  statsObserver.observe(statsSection);
}
animateStats();

function initHeroCarousel() {
  const images = document.querySelectorAll('.hero-carousel-img');
  if (images.length < 2) return;
  
  let currentIndex = 0;
  setInterval(() => {
    images[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].classList.add('active');
  }, 4500); // Smooth change every 4.5s
}
initHeroCarousel();

// ── Floating card stagger animation  ─────────────────────────────────────────
const floatingCards = document.querySelectorAll('.f-card');
floatingCards.forEach((card, i) => {
  card.style.animationDelay = `${i * 0.7}s`;
});
