// Navigation Scroll Effect
const navbar = document.querySelector('.apple-nav');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(0, 0, 0, 0.85)';
        navbar.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.5)';
    } else {
        navbar.style.background = 'rgba(0, 0, 0, 0.7)';
        navbar.style.boxShadow = 'none';
    }
});

// Smooth reveal for cards
const cards = document.querySelectorAll('.apple-card');

const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    cards.forEach(card => {
        const elementTop = card.getBoundingClientRect().top;
        if (elementTop < windowHeight - 100) {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }
    });
};

// Initial state for animation
cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(40px)';
    card.style.transition = 'all 0.6s cubic-bezier(0.25, 1, 0.5, 1)';
});

window.addEventListener('scroll', revealOnScroll);
// Trigger once on load
setTimeout(revealOnScroll, 100);
