// --- Theme Toggle Logic ---
const themeToggle = document.getElementById('themeToggle');
const htmlTag = document.documentElement;
const themeLabel = document.querySelector('.toggle-label');

// Check for saved theme
const savedTheme = localStorage.getItem('mobile_express_theme') || 'dark';
htmlTag.setAttribute('data-theme', savedTheme);
if(themeLabel) themeLabel.textContent = savedTheme === 'dark' ? 'Dark Mode' : 'Light Mode';

themeToggle.addEventListener('click', () => {
    const currentTheme = htmlTag.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    htmlTag.setAttribute('data-theme', newTheme);
    localStorage.setItem('mobile_express_theme', newTheme);
    
    if(themeLabel) {
        themeLabel.textContent = newTheme === 'dark' ? 'Dark Mode' : 'Light Mode';
    }
});


// --- Reveal Animations ---
const reveals = document.querySelectorAll('.reveal');
const scrollContainer = document.getElementById('scroll-container');

const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    reveals.forEach(el => {
        const elementTop = el.getBoundingClientRect().top;
        if (elementTop < windowHeight - 50) {
            el.classList.add('active');
        }
    });
};

// Listen on the scrolling pane
if (scrollContainer) {
    scrollContainer.addEventListener('scroll', revealOnScroll);
} else {
    window.addEventListener('scroll', revealOnScroll);
}

// Trigger once on load
setTimeout(revealOnScroll, 100);


// --- Navigation Active State Sync ---
const panels = document.querySelectorAll('.panel');
const navItems = document.querySelectorAll('.nav-item[data-target]');

if (scrollContainer && panels.length > 0) {
    scrollContainer.addEventListener('scroll', () => {
        let current = '';
        const scrollY = scrollContainer.scrollTop;
        
        panels.forEach(panel => {
            const panelTop = panel.offsetTop;
            const panelHeight = panel.clientHeight;
            if (scrollY >= (panelTop - panelHeight / 3)) {
                current = panel.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('data-target') === current) {
                item.classList.add('active');
            }
        });
    });
}
