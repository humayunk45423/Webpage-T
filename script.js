/**
 * Mobile Express - Enterprise Commercial Core Engine
 * Features: Light/Dark Mode, Bilingual (EN/BN) i18n, 3D Crossing Bands Parallax, Real-Time Catalog & Estimator
 */

document.addEventListener('DOMContentLoaded', () => {
    initThemeManager();
    initLanguageManager();
    initCrossingBandsParallax();
    initGlassNavbar();
    initNavPillSelector();
    initMobileDrawer();
    initDiagnosticCalculator();
    initInventoryCatalog();
});

/* ==========================================================================
   1. Theme Manager (Dark / Light "White" Mode)
   ========================================================================== */
function initThemeManager() {
    const savedTheme = localStorage.getItem('me_theme') || 'light';
    applyTheme(savedTheme);

    const themeToggles = document.querySelectorAll('.theme-segmented-toggle, #themeToggleBtn, .theme-toggle-btn');
    themeToggles.forEach(btn => {
        btn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            applyTheme(newTheme);
            localStorage.setItem('me_theme', newTheme);
        });
    });
}

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    const themeToggles = document.querySelectorAll('.theme-segmented-toggle, #themeToggleBtn, .theme-toggle-btn');
    themeToggles.forEach(btn => {
        const isDark = theme === 'dark';
        btn.setAttribute('data-state', isDark ? 'right' : 'left');
        btn.setAttribute('aria-label', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');
        btn.setAttribute('title', isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode');
    });

    const themeIcons = document.querySelectorAll('.theme-icon');
    themeIcons.forEach(icon => {
        if (theme === 'light') {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        } else {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    });
}

/* ==========================================================================
   2. Bilingual Manager (English & Bengali / বাংলা)
   ========================================================================== */
const I18N_DICTIONARY = {
    en: {
        'nav-home': 'Home',
        'nav-diagnostics': 'Diagnostics',
        'nav-estimator': 'Estimator',
        'nav-inventory': 'Inventory',
        'nav-contact': 'Contact',
        'nav-support': 'Support',
        'theme-lbl': 'Theme',
        'lang-lbl': 'Language',
        'call-line': '+88 01834 254875',
        'apple-badge': 'Apple & Android Expert Service Center',
        'hero-title-1': 'Flawless Security',
        'hero-title-2': 'Bypass & Fixation.',
        'hero-desc': 'Permanent iCloud unlocking, instant FRP removal, and deep software restoration alongside a premium selection of BD\'s favorite smartphones.',
        'btn-browse': 'Browse Devices',
        'btn-protocols': 'View Protocols',
        'stat-restored-num': '100+',
        'stat-restored-lbl': 'Devices Restored',
        'stat-success-num': '99.4%',
        'stat-success-lbl': 'Bypass Success Rate',
        'stat-turnaround-num': '15 Mins',
        'stat-turnaround-lbl': 'Express Turnaround',
        'services-tag': 'Diagnostic',
        'services-tag-hi': 'Expertise',
        'services-sub': 'Advanced hardware benches and proprietary diagnostic algorithms engineered to safely restore locked, disabled, and bricked devices.',
        'srv-icloud-title': 'iCloud & Security Bypass',
        'srv-icloud-desc': 'Hardware and Ramdisk-tethered bypass solutions for all iOS architectures, disabled screens, and activation locked iPhones & iPads.',
        'srv-icloud-time': '15 - 45 Mins',
        'srv-frp-title': 'FRP Account Removal',
        'srv-frp-desc': 'Instantaneous Factory Reset Protection (FRP) unlocking for Samsung, Xiaomi, Oppo, Vivo, Realme, and Infinix with zero data risk.',
        'srv-frp-time': '10 - 25 Mins',
        'srv-deadboot-title': 'Dead Boot & Board Fix',
        'srv-deadboot-desc': 'Motherboard flashing, Qualcomm 9008 EDL revival, direct ISP memory reconstruction, and deeply bricked device resurrection.',
        'srv-deadboot-time': 'Same Day Turnaround',
        'btn-inquire': 'Inquire',
        'est-title-1': 'Instant Diagnostic',
        'est-title-2': 'Estimator',
        'est-sub': 'Select your device platform and failure type for an immediate cost range and procedure estimate.',
        'est-lbl-plat': 'Platform',
        'est-lbl-issue': 'Failure / Symptom',
        'est-lbl-model': 'Model (Optional)',
        'btn-calc': 'Calculate',
        'contact-title-1': 'Establish',
        'contact-title-2': 'Connection',
        'contact-sub': 'Direct communication channels and shop location for proprietor Tanvir Iqbal.',
        'contact-pill-1-sub': 'Direct Line',
        'contact-pill-2-sub': 'Official WhatsApp Desk',
        'contact-pill-3-sub': 'Email Support',
        'contact-pill-4-sub': 'Shop Location',
        'contact-pill-4-val': 'Mita Cinema Hall Adjacent, Zilla Parishad Market, Badarganj, Rangpur',
        'qr-scan-label': 'Scan to Connect on WhatsApp',
        'ethics-text': '"The honest and trustworthy merchant will be with the prophets, the truthful ones, and the martyrs on the Day of Resurrection."',
        'ethics-ref': '[Sunan At-Tirmidhi, Hadith No. 1209]',
        'inv-header-1': 'Mid & Budget Range',
        'inv-header-2': 'Handsets',
        'inv-header-sub': 'Handpicked, highly popular devices for the Bangladeshi market. All units pass rigorous software, battery health, and hardware motherboard bench testing.',
        'inv-search-placeholder': 'Search by name, brand, processor, camera (e.g. Note 13, 108MP, G99)...',
        'filter-all': 'All Brands',
        'filter-xiaomi': 'Xiaomi & Poco',
        'filter-samsung': 'Samsung',
        'filter-realme': 'Realme',
        'filter-vivo': 'Vivo',
        'filter-oppo': 'Oppo',
        'filter-infinix': 'Infinix & Tecno',
        'filter-oneplus': 'OnePlus',
        'filter-motorola': 'Motorola',
        'guarantee-badge': '7-Day Replacement Guarantee Included',
        'btn-order': 'Acquire Device',
        'footer-copy': '© 2026 Mobile Express. System architecture & diagnostics by Tanvir Iqbal.',
        'footer-loc': 'Mita Road, Zilla Parishad Market, Badarganj, Rangpur • Bangladesh'
    },
    bn: {
        'nav-home': 'হোম',
        'nav-diagnostics': 'ডায়াগনস্টিক',
        'nav-estimator': 'খরচ হিসাব',
        'nav-inventory': 'স্মার্টফোন কালেকশন',
        'nav-contact': 'যোগাযোগ',
        'nav-support': 'সাপোর্ট',
        'theme-lbl': 'থিম মোড',
        'lang-lbl': 'ভাষা নির্বাচন',
        'call-line': '+৮৮ ০১৮৩৪ ২৫৪৮৭৫',
        'apple-badge': 'অ্যাপল ও অ্যান্ড্রয়েড এক্সপার্ট সার্ভিস সেন্টার',
        'hero-title-1': 'নিখুঁত সিকিউরিটি',
        'hero-title-2': 'বাইপাস ও সমাধান।',
        'hero-desc': 'আইক্লাউড আনলকিং, এফআরপি রিমুভাল, ডেড বুট রিকভারি এবং বাংলাদেশের জনপ্রিয় সেরা স্মার্টফোনের প্রিমিয়াম সম্ভার।',
        'btn-browse': 'স্মার্টফোন দেখুন',
        'btn-protocols': 'সার্ভিস প্রটোকল',
        'stat-restored-num': '১০০+',
        'stat-restored-lbl': 'সফল ডিভাইস মেরামত',
        'stat-success-num': '৯৯.৪%',
        'stat-success-lbl': 'বাইপাস সাফল্য হার',
        'stat-turnaround-num': '১৫ মিনিট',
        'stat-turnaround-lbl': 'এক্সপ্রেস সার্ভিস',
        'services-tag': 'ডায়াগনস্টিক',
        'services-tag-hi': 'অভিজ্ঞতা ও দক্ষতা',
        'services-sub': 'অত্যাধুনিক হার্ডওয়্যার ডায়াগনস্টিক ও আধুনিক সফটওয়্যার সল্যুশনের মাধ্যমে লক ও ডেড ডিভাইস পুনরুজ্জীবন।',
        'srv-icloud-title': 'আইক্লাউড ও সিকিউরিটি বাইপাস',
        'srv-icloud-desc': 'আইওএস ডিভাইস, ডিসেবল স্ক্রিন এবং অ্যাক্টিভেশন লক করা আইফোনের রামডিস্ক ও হার্ডওয়্যার বাইপাস পদ্ধতি।',
        'srv-icloud-time': '১৫ - ৪৫ মিনিট',
        'srv-frp-title': 'এফআরপি অ্যাকাউন্ট রিমুভাল',
        'srv-frp-desc': 'স্যামসাং, শাওমি, অপ্পো, ভিভো, রিয়েলমি এবং ইনফিনিক্সের গুগল এফআরপি ও অ্যাকাউন্ট ইনস্ট্যান্ট রিমুভ।',
        'srv-frp-time': '১০ - ২৫ মিনিট',
        'srv-deadboot-title': 'ডেড বুট ও মাদারবোর্ড ফিক্স',
        'srv-deadboot-desc': 'কোয়ালকম ৯০০৮ EDL ফ্ল্যাশিং, ডিরেক্ট ISP মেমোরি রিকভারি এবং হার্ড ব্রিক ডিভাইস সচলকরণ।',
        'srv-deadboot-time': 'সেম ডে সার্ভিস',
        'btn-inquire': 'তথ্য জানুন',
        'est-title-1': 'ইনস্ট্যান্ট ডায়াগনস্টিক',
        'est-title-2': 'খরচ ক্যালকুলেটর',
        'est-sub': 'আপনার ফোনের ব্র্যান্ড ও সমস্যার ধরন নির্বাচন করে সাথে সাথে খরচের রেঞ্জ ও আনুমানিক সময় জেনে নিন।',
        'est-lbl-plat': 'প্ল্যাটফর্ম',
        'est-lbl-issue': 'সমস্যার ধরন',
        'est-lbl-model': 'মডেল (ঐচ্ছিক)',
        'btn-calc': 'হিসাব করুন',
        'contact-title-1': 'সরাসরি',
        'contact-title-2': 'যোগাযোগ ও ঠিকানা',
        'contact-sub': 'স্বত্বাধিকারী তানভীর ইকবালের শোরুম ও সার্ভিস সেন্টারে যোগাযোগের ঠিকানা।',
        'contact-pill-1-sub': 'সরাসরি কল',
        'contact-pill-2-sub': 'অফিসিয়াল হোয়াটসঅ্যাপ ডেস্ক',
        'contact-pill-3-sub': 'ইমেইল সাপোর্ট',
        'contact-pill-4-sub': 'দোকানের ঠিকানা',
        'contact-pill-4-val': 'মিতা সিনেমা হল সংলগ্ন, জেলা পরিষদ মার্কেট, বদরগঞ্জ, রংপুর',
        'qr-scan-label': 'হোয়াটসঅ্যাপে কানেক্ট করতে স্ক্যান করুন',
        'ethics-text': '"রাসূলুল্লাহ (সা.) বলেছেন, \'সত্যবাদী ও আমানতদার (বিশ্বস্ত) ব্যবসায়ী কিয়ামতের দিন নবীগণ, সিদ্দিকগণ এবং শহীদগণের সাথে থাকবেন।\'"',
        'ethics-ref': '[সুনান আত-তিরমিজি, হাদিস নং ১২০৯]',
        'inv-header-1': 'বাজেট ও মিড-রেঞ্জ',
        'inv-header-2': 'স্মার্টফোন সম্ভার',
        'inv-header-sub': 'বাংলাদেশি বাজারের সবচেয়ে জনপ্রিয় ও বিশ্বস্ত হ্যান্ডসেট। প্রতিটি ইউনিট মাদারবোর্ড, ব্যাটারি ও ডিসপ্লে চেকিং পাসকৃত।',
        'inv-search-placeholder': 'মডেল, ব্র্যান্ড, প্রসেসর বা ক্যামেরা দিয়ে সার্চ করুন (যেমন: Note 13, 108MP, G99)...',
        'filter-all': 'সকল ব্র্যান্ড',
        'filter-xiaomi': 'শাওমি ও পোকো',
        'filter-samsung': 'স্যামসাং',
        'filter-realme': 'রিয়েলমি',
        'filter-vivo': 'ভিভো',
        'filter-oppo': 'অপ্পো',
        'filter-infinix': 'ইনফিনিক্স ও টেকনো',
        'filter-oneplus': 'ওয়ানপ্লাস',
        'filter-motorola': 'মটোরোলা',
        'guarantee-badge': '৭ দিনের রিপ্লেসমেন্ট গ্যারান্টি অন্তর্ভুক্ত',
        'btn-order': 'অর্ডার / তথ্য জানুন',
        'footer-copy': '© ২০২৬ মোবাইল এক্সপ্রেস। সিস্টেম আর্কিটেকচার ও ডায়াগনস্টিক: তানভীর ইকবাল।',
        'footer-loc': 'মিতা রোড, জেলা পরিষদ মার্কেট, বদরগঞ্জ, রংপুর • বাংলাদেশ'
    }
};

let currentLanguage = 'bn';

function initLanguageManager() {
    currentLanguage = localStorage.getItem('me_lang') || 'bn';
    applyLanguage(currentLanguage);

    const langToggles = document.querySelectorAll('.lang-segmented-toggle, #langToggleBtn, .lang-toggle-btn');
    langToggles.forEach(btn => {
        btn.addEventListener('click', () => {
            currentLanguage = currentLanguage === 'en' ? 'bn' : 'en';
            applyLanguage(currentLanguage);
            localStorage.setItem('me_lang', currentLanguage);
            
            // Re-render catalog if present
            if (typeof window.reRenderInventory === 'function') {
                window.reRenderInventory();
            }
        });
    });
}

function applyLanguage(lang) {
    document.body.classList.toggle('lang-bn', lang === 'bn');
    
    // Update segmented toggle state (BN on left, EN on right)
    const langToggles = document.querySelectorAll('.lang-segmented-toggle, #langToggleBtn, .lang-toggle-btn');
    langToggles.forEach(btn => {
        btn.setAttribute('data-state', lang === 'en' ? 'right' : 'left');
        btn.setAttribute('aria-label', lang === 'en' ? 'Switch to Bengali (বাংলা)' : 'Switch to English');
        btn.setAttribute('title', lang === 'en' ? 'Switch to Bengali (বাংলা)' : 'Switch to English');
    });

    const langLabels = document.querySelectorAll('.lang-label');
    langLabels.forEach(lbl => {
        lbl.textContent = lang === 'en' ? 'বাং' : 'EN';
    });

    const dict = I18N_DICTIONARY[lang] || I18N_DICTIONARY['en'];
    const elements = document.querySelectorAll('[data-i18n]');
    
    elements.forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
            el.textContent = dict[key];
        }
    });

    // Update search inputs placeholders
    const searchInputs = document.querySelectorAll('#inv-search');
    searchInputs.forEach(input => {
        input.placeholder = dict['inv-search-placeholder'] || input.placeholder;
    });

    // Refresh nav pill position for updated text widths
    if (typeof window.refreshNavPill === 'function') {
        window.refreshNavPill();
    }
}

/* Helper to convert numbers to Bengali numeral digits */
function toBengaliDigits(number) {
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return number.toString().replace(/\d/g, d => bnDigits[d]);
}

/* ==========================================================================
   3. 3D Architectural Parallax Kinetic Ribbons Engine
   ========================================================================== */
function initCrossingBandsParallax() {
    const elements = document.querySelectorAll('.card-band, .band-beam');
    if (!elements.length) return;

    let ticking = false;

    const updateParallax = () => {
        const scrolled = window.scrollY;

        elements.forEach(el => {
            const speed = parseFloat(el.getAttribute('data-speed') || '0.35');
            const yMove = scrolled * speed;

            const isLeft = el.classList.contains('band-left-outer') || 
                           el.classList.contains('band-left-main') || 
                           el.classList.contains('band-left-beam') ||
                           el.classList.contains('band-left-1') || 
                           el.classList.contains('band-left-2');
                           
            const baseRotate = isLeft ? 24 : -24;
            const dynamicRotate = baseRotate + (isLeft ? (scrolled * 0.004) : -(scrolled * 0.004));
            
            let zDepth = -90;
            if (el.classList.contains('band-outer') || el.classList.contains('band-left-2') || el.classList.contains('band-right-2')) {
                zDepth = -200;
            } else if (el.classList.contains('band-beam')) {
                zDepth = -40;
            }

            el.style.transform = `translate3d(0, ${yMove}px, ${zDepth}px) rotateZ(${dynamicRotate}deg)`;
        });

        ticking = false;
    };

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(updateParallax);
            ticking = true;
        }
    }, { passive: true });

    updateParallax();
}

/* ==========================================================================
   4. Floating Glass Navbar Dynamics
   ========================================================================== */
function initGlassNavbar() {
    const header = document.querySelector('.glass-header');
    if (!header) return;

    const handleScroll = () => {
        if (window.scrollY > 30) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
}

/* ==========================================================================
   4.1 Buttery Smooth Top Navbar Pill Selector Indicator
   ========================================================================== */
function initNavPillSelector() {
    const navLinksContainer = document.querySelector('.nav-links');
    if (!navLinksContainer) return;

    let indicator = navLinksContainer.querySelector('.nav-pill-indicator');
    if (!indicator) {
        indicator = document.createElement('div');
        indicator.className = 'nav-pill-indicator';
        indicator.setAttribute('aria-hidden', 'true');
        navLinksContainer.prepend(indicator);
    }

    const links = Array.from(navLinksContainer.querySelectorAll('a'));
    if (!links.length) return;

    let currentActiveLink = navLinksContainer.querySelector('a.active') || links[0];
    let isClickScrolling = false;
    let clickScrollTimer = null;

    const updatePillPosition = (targetLink, animate = true) => {
        if (!targetLink) return;

        const targetRect = targetLink.getBoundingClientRect();
        const containerRect = navLinksContainer.getBoundingClientRect();

        // Subpixel precision coordinate math
        const left = Math.round((targetRect.left - containerRect.left) * 10) / 10;
        const width = Math.round(targetRect.width * 10) / 10;

        if (!animate) {
            indicator.style.transition = 'none';
        } else {
            indicator.style.transition = 'transform 0.35s cubic-bezier(0.25, 1, 0.35, 1), width 0.35s cubic-bezier(0.25, 1, 0.35, 1), opacity 0.2s ease';
        }

        indicator.style.transform = `translate3d(${left}px, 0, 0)`;
        indicator.style.width = `${width}px`;
        indicator.style.opacity = '1';

        if (!animate) {
            indicator.offsetHeight; // force reflow
            indicator.style.transition = 'transform 0.35s cubic-bezier(0.25, 1, 0.35, 1), width 0.35s cubic-bezier(0.25, 1, 0.35, 1), opacity 0.2s ease';
        }
    };

    // Position indicator once layout and fonts are ready
    const initPosition = () => updatePillPosition(currentActiveLink, false);
    requestAnimationFrame(initPosition);
    if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(initPosition);
    }

    // Helper for buttery smooth scrolling with header offset
    const smoothScrollTo = (targetId) => {
        if (targetId === 'hero') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
            return;
        }
        const targetEl = document.getElementById(targetId);
        if (!targetEl) return;
        const isMobile = window.innerWidth <= 960;
        const headerOffset = isMobile ? 80 : 105;
        const targetPosition = targetEl.getBoundingClientRect().top + window.pageYOffset;
        const offsetPosition = Math.max(0, targetPosition - headerOffset);
        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    };

    // Handle clicks: smoothly glide the indicator to clicked tab and lock scroll spy during travel
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href && (href.startsWith('#') || (href.includes('index.html#') && isIndexPage))) {
                const targetId = href.replace(/^.*#/, '');
                const targetEl = document.getElementById(targetId);
                if (targetEl) {
                    e.preventDefault();
                    links.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                    currentActiveLink = link;
                    updatePillPosition(link, true);

                    isClickScrolling = true;
                    clearTimeout(clickScrollTimer);
                    clickScrollTimer = setTimeout(() => {
                        isClickScrolling = false;
                    }, 800);

                    smoothScrollTo(targetId);
                    if (history.pushState) {
                        history.pushState(null, null, `#${targetId}`);
                    }
                }
            }
        });
    });

    // Also bind generic anchor links like .btn-secondary (#services)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        if (!anchor.closest('.nav-links') && !anchor.closest('.drawer-links')) {
            anchor.addEventListener('click', (e) => {
                const targetId = anchor.getAttribute('href').replace(/^#/, '');
                const targetEl = document.getElementById(targetId);
                if (targetEl) {
                    e.preventDefault();
                    smoothScrollTo(targetId);
                    if (history.pushState) {
                        history.pushState(null, null, `#${targetId}`);
                    }
                }
            });
        }
    });

    // Scroll spy for in-page sections on index.html
    const isIndexPage = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || !window.location.pathname.includes('.html');
    if (isIndexPage) {
        const sectionIds = ['hero', 'services', 'estimator', 'contact'];
        const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);

        let scrollTicking = false;
        const handleScrollSpy = () => {
            if (isClickScrolling) {
                scrollTicking = false;
                return;
            }

            const scrollPos = window.scrollY + 180;
            let activeSection = null;

            for (let i = sections.length - 1; i >= 0; i--) {
                const section = sections[i];
                if (section.offsetTop <= scrollPos) {
                    activeSection = section;
                    break;
                }
            }

            if (!activeSection && sections.length > 0) {
                activeSection = sections[0];
            }

            if (activeSection) {
                const activeHref = `#${activeSection.id}`;
                const matchingLink = links.find(l => l.getAttribute('href') === activeHref);
                if (matchingLink && matchingLink !== currentActiveLink) {
                    links.forEach(l => l.classList.remove('active'));
                    matchingLink.classList.add('active');
                    currentActiveLink = matchingLink;
                    updatePillPosition(matchingLink, true);
                }
            }
            scrollTicking = false;
        };

        window.addEventListener('scroll', () => {
            if (!scrollTicking) {
                window.requestAnimationFrame(handleScrollSpy);
                scrollTicking = true;
            }
        }, { passive: true });
    }

    // Check if page was loaded with a hash (e.g. user clicked Diagnostics, Estimator, Contact from inventory.html)
    if (isIndexPage && window.location.hash) {
        const targetId = window.location.hash.replace(/^#/, '');
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
            const matchingLink = links.find(l => {
                const h = l.getAttribute('href') || '';
                return h === `#${targetId}` || h.endsWith(`#${targetId}`);
            });
            if (matchingLink) {
                links.forEach(l => l.classList.remove('active'));
                matchingLink.classList.add('active');
                currentActiveLink = matchingLink;
                updatePillPosition(matchingLink, false);
            }

            isClickScrolling = true;
            clearTimeout(clickScrollTimer);
            clickScrollTimer = setTimeout(() => {
                isClickScrolling = false;
            }, 1200);

            const executeInitialScroll = () => {
                smoothScrollTo(targetId);
            };

            // Run at multiple frames to ensure fonts and layout have stabilized
            setTimeout(executeInitialScroll, 50);
            setTimeout(executeInitialScroll, 250);
            if (document.fonts && document.fonts.ready) {
                document.fonts.ready.then(() => setTimeout(executeInitialScroll, 100));
            }
        }
    }

    // Handle window resize
    window.addEventListener('resize', () => {
        const active = navLinksContainer.querySelector('a.active') || currentActiveLink;
        updatePillPosition(active, false);
    });

    // Language / dynamic refresh hook
    window.refreshNavPill = () => {
        setTimeout(() => {
            const active = navLinksContainer.querySelector('a.active') || currentActiveLink;
            updatePillPosition(active, false);
        }, 50);
    };
}

/* ==========================================================================
   5. Mobile Responsive Drawer Navigation
   ========================================================================== */
function initMobileDrawer() {
    const toggleBtn = document.getElementById('menu-toggle');
    const closeBtn = document.getElementById('drawer-close');
    const drawer = document.getElementById('mobile-drawer');
    const overlay = document.getElementById('drawer-overlay');
    const links = document.querySelectorAll('.drawer-links a');

    if (!toggleBtn || !drawer || !overlay) return;

    const openDrawer = () => {
        drawer.classList.add('open');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    const closeDrawer = () => {
        drawer.classList.remove('open');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    };

    toggleBtn.addEventListener('click', openDrawer);
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    overlay.addEventListener('click', closeDrawer);

    links.forEach(l => {
        l.addEventListener('click', (e) => {
            const href = l.getAttribute('href');
            if (href && (href.startsWith('#') || (href.includes('index.html#') && isIndexPage))) {
                const targetId = href.replace(/^.*#/, '');
                const targetEl = document.getElementById(targetId);
                if (targetEl) {
                    e.preventDefault();
                    closeDrawer();
                    setTimeout(() => {
                        if (targetId === 'hero') {
                            window.scrollTo({ top: 0, behavior: 'smooth' });
                        } else {
                            const isMobile = window.innerWidth <= 960;
                            const headerOffset = isMobile ? 80 : 105;
                            const targetPosition = targetEl.getBoundingClientRect().top + window.pageYOffset;
                            const offsetPosition = Math.max(0, targetPosition - headerOffset);
                            window.scrollTo({
                                top: offsetPosition,
                                behavior: 'smooth'
                            });
                        }
                        if (history.pushState) {
                            history.pushState(null, null, `#${targetId}`);
                        }
                    }, 120);
                } else {
                    closeDrawer();
                }
            } else {
                closeDrawer();
            }
        });
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && drawer.classList.contains('open')) {
            closeDrawer();
        }
    });
}

/* ==========================================================================
   6. Diagnostic Feasibility & Cost Calculator
   ========================================================================== */
function initDiagnosticCalculator() {
    const brandSelect = document.getElementById('calc-brand');
    const issueSelect = document.getElementById('calc-issue');
    const btn = document.getElementById('calc-btn');
    const resultBox = document.getElementById('calc-result');
    const resultTitle = document.getElementById('calc-result-title');
    const resultDesc = document.getElementById('calc-result-desc');
    const resultBtn = document.getElementById('calc-wa-btn');

    if (!btn || !brandSelect || !issueSelect) return;

    const database = {
        'apple': {
            'icloud': {
                en: { title: 'Apple iCloud Activation Lock Resolution', time: '15 - 45 Mins', cost: '৳ 1,500 - ৳ 4,500', note: 'Hardware / Ramdisk method with signal support based on iOS & baseband.' },
                bn: { title: 'অ্যাপল আইক্লাউড অ্যাক্টিভেশন লক রিমুভাল', time: '১৫ - ৪৫ মিনিট', cost: '৳ ১,৫০০ - ৳ ৪,৫০০', note: 'আইওএস সংস্করণ ও বেসব্যান্ড অনুযায়ী ফুল সিগন্যাল সহ রামডিস্ক সল্যুশন।' }
            },
            'disabled': {
                en: { title: 'iPhone Disabled / Unavailable Recovery', time: '20 - 40 Mins', cost: '৳ 800 - ৳ 1,800', note: 'Safe restore and DFU firmware flash without board damage.' },
                bn: { title: 'আইফোন ডিসেবল / আনঅ্যাভেইলেবল স্ক্রিন রিকভারি', time: '২০ - ৪০ মিনিট', cost: '৳ ৮০০ - ৳ ১,৮০০', note: 'নিরাপদ ফার্মওয়্যার ফ্ল্যাশ ও ডেটা লস ছাড়া সফল রিস্টোর।' }
            },
            'restore': {
                en: { title: '"Unable to Activate" & Baseband Repair', time: '30 - 60 Mins', cost: '৳ 1,000 - ৳ 2,500', note: 'EEPROM & baseband IC diagnostic with Apple IPSW official signed restore.' },
                bn: { title: 'Unable to Activate ও বেসব্যান্ড আইসি মেরামত', time: '৩০ - ৬০ মিনিট', cost: '৳ ১,০০০ - ৳ ২,৫০০', note: 'বেসব্যান্ড চিপসেট ডায়াগনস্টিক ও অফিশিয়াল ফার্মওয়্যার ফ্ল্যাশ।' }
            },
            'hardware': {
                en: { title: 'Apple Motherboard & Chip Repair', time: 'Same Day Service', cost: 'Diagnosis Required', note: 'Microscope multimeter inspection, short circuit removal and BGA reballing.' },
                bn: { title: 'আইফোন মাদারবোর্ড ও চিপ লেভেল রিপেয়ার', time: 'সেম ডে সার্ভিস', cost: 'চেক করে জানানো হবে', note: 'মাইক্রোস্কোপ ইন্সপেকশন, শর্ট সার্কিট রিমুভ ও বিজিএ রিবলিং।' }
            }
        },
        'android': {
            'frp': {
                en: { title: 'Instant Android FRP Account Removal', time: '10 - 25 Mins', cost: '৳ 500 - ৳ 1,500', note: 'Samsung, Xiaomi, Vivo, Oppo, Realme authorized server & EDL testpoint bypass.' },
                bn: { title: 'ইনস্ট্যান্ট গুগল এফআরপি অ্যাকাউন্ট রিমুভাল', time: '১০ - ২৫ মিনিট', cost: '৳ ৫০০ - ৳ ১,৫০০', note: 'স্যামসাং, শাওমি, ভিভো, অপ্পো, রিয়েলমি ও ইনফিনিক্সের অথরাইজড সার্ভার আনলক।' }
            },
            'deadboot': {
                en: { title: 'Dead Boot & Deep Brick Revival', time: '1 - 3 Hours', cost: '৳ 1,200 - ৳ 3,000', note: 'Qualcomm EDL 9008, MTK DA, and direct ISP / JTAG memory flashing.' },
                bn: { title: 'ডেড বুট ও হার্ড ব্রিক পুনরুজ্জীবন', time: '১ - ৩ ঘণ্টা', cost: '৳ ১,২০০ - ৳ ৩,০০০', note: 'কোয়ালকম ৯০০৮ EDL, MTK DA ও ডিরেক্ট ISP পিনআউট মেমোরি ফ্ল্যাশিং।' }
            },
            'network': {
                en: { title: 'SIM Network & Region Carrier Unlock', time: '20 - 45 Mins', cost: '৳ 800 - ৳ 2,000', note: 'Permanent CSC and regional firmware unlocking.' },
                bn: { title: 'সিম নেটওয়ার্ক ও রিজিয়ন ক্যারিয়ার আনলক', time: '২০ - ৪৫ মিনিট', cost: '৳ ৮০০ - ৳ ২,০০০', note: 'স্থায়ী CSC ও রিজিওনাল কান্ট্রি কোড আনলকিং।' }
            },
            'hardware': {
                en: { title: 'Android Motherboard & Power IC Fix', time: 'Same Day Service', cost: 'Diagnosis Required', note: 'Board level power IC replacement and short removal.' },
                bn: { title: 'অ্যান্ড্রয়েড মাদারবোর্ড ও পাওয়ার আইসি ফিক্স', time: 'সেম ডে সার্ভিস', cost: 'চেক করে জানানো হবে', note: 'পাওয়ার আইসি প্রতিস্থাপন ও ডেড সার্কিট মেরামত।' }
            }
        }
    };

    btn.addEventListener('click', () => {
        const brand = brandSelect.value;
        const issue = issueSelect.value;

        if (!brand || !issue) {
            alert(currentLanguage === 'bn' ? 'দয়া করে প্ল্যাটফর্ম ও সমস্যার ধরন নির্বাচন করুন।' : 'Please select both the platform and the failure type.');
            return;
        }

        const category = brand === 'apple' ? 'apple' : 'android';
        const rawData = database[category] && database[category][issue];
        const data = (rawData && rawData[currentLanguage]) || (rawData && rawData['en']) || {
            title: currentLanguage === 'bn' ? 'কাস্টম প্রিসিশন ডায়াগনস্টিক' : 'Custom Precision Diagnostics',
            time: currentLanguage === 'bn' ? '৩০ - ৬০ মিনিট' : '30 - 60 Mins',
            cost: currentLanguage === 'bn' ? 'চেক করে জানানো হবে' : 'Estimate upon inspection',
            note: currentLanguage === 'bn' ? 'দোকানে ফুল হার্ডওয়্যার ও সফটওয়্যার টেস্টের পর সমাধান দেওয়া হবে।' : 'Full hardware and software bench diagnostic at store.'
        };

        if (resultBox && resultTitle && resultDesc && resultBtn) {
            resultTitle.textContent = `${data.title} (${data.time})`;
            resultDesc.textContent = `${currentLanguage === 'bn' ? 'আনুমানিক ডায়াগনস্টিক খরচ' : 'Diagnostic Cost Range'}: ${data.cost}. ${data.note}`;

            const text = encodeURIComponent(currentLanguage === 'bn' 
                ? `আসসালামু আলাইকুম মোবাইল এক্সপ্রেস, আমি ${brand.toUpperCase()} - ${data.title} সম্পর্কিত সার্ভিস নিতে চাচ্ছি।`
                : `Hello Mobile Express, I would like to consult about ${brand.toUpperCase()} - ${data.title}. Issue: ${issue}`);
            resultBtn.href = `https://wa.me/8801834254875?text=${text}`;

            resultBox.classList.add('visible');
            resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    });
}

/* ==========================================================================
   7. Dynamic Inventory Catalog (24+ Devices) with Bilingual Support
   ========================================================================== */
const INVENTORY_DATA = [
    { id: 1, brand: 'Xiaomi', name: 'Redmi Note 13', price: 22999, tag: { en: 'Bestseller', bn: 'বেস্টসেলার' }, specs: ['AMOLED 120Hz 6.67"', 'Snapdragon 685 (6nm)', '108MP Triple Camera', '5000mAh | 33W Fast'], img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-4g.jpg' },
    { id: 2, brand: 'Xiaomi', name: 'Redmi Note 12', price: 19500, tag: { en: 'Popular', bn: 'জনপ্রিয়' }, specs: ['AMOLED 120Hz Display', 'Snapdragon 685 Chip', '50MP AI Triple Cam', '5000mAh Battery'], img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-12.jpg' },
    { id: 3, brand: 'Xiaomi', name: 'Redmi 12', price: 16999, tag: { en: 'Budget King', bn: 'বাজেট কিং' }, specs: ['90Hz FHD+ IPS Display', 'MediaTek Helio G88', '50MP Triple Camera', 'Glass Back Finish'], img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-12.jpg' },
    { id: 4, brand: 'Poco', name: 'Poco X5 Pro 5G', price: 32000, tag: { en: 'Performance', bn: 'হাই স্পিড' }, specs: ['120Hz Flow AMOLED', 'Snapdragon 778G 5G', '108MP Pro Camera', '67W Turbo Charge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-x5-pro-5g.jpg' },
    { id: 5, brand: 'Poco', name: 'Poco M5', price: 15500, tag: { en: 'Gaming Entry', bn: 'গেমিং চয়েস' }, specs: ['90Hz DynamicSwitch', 'Helio G99 (6nm)', '50MP AI Camera', '5000mAh Long-Life'], img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-m5-.jpg' },
    
    { id: 6, brand: 'Realme', name: 'Realme 11 Pro 5G', price: 35000, tag: { en: 'Curved OLED', bn: 'কার্ভড ওলেড' }, specs: ['120Hz Curved AMOLED', 'Dimensity 7050 5G', '100MP OIS Camera', '67W SuperVOOC'], img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-11-pro.jpg' },
    { id: 7, brand: 'Realme', name: 'Realme C55', price: 18999, tag: { en: 'Mini Capsule', bn: 'মিনি ক্যাপসুল' }, specs: ['90Hz FHD+ Screen', 'Helio G88 Gaming Chip', '64MP AI Main Cam', '33W Dart Charge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-c55.jpg' },
    { id: 8, brand: 'Realme', name: 'Realme 10', price: 20000, tag: { en: 'Super AMOLED', bn: 'সুপার অ্যামোলেড' }, specs: ['Super AMOLED 90Hz', 'Helio G99 6nm', '50MP Color AI Cam', 'Ultra-Slim 7.9mm'], img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-10-4g.jpg' },
    { id: 9, brand: 'Realme', name: 'Realme C53', price: 14999, tag: { en: 'Budget Pick', bn: 'বাজেট পিক' }, specs: ['90Hz Display', 'Unisoc T612 Octa-Core', '50MP Dual Camera', '33W Fast Charge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-c53.jpg' },
    
    { id: 10, brand: 'Samsung', name: 'Galaxy A24', price: 24500, tag: { en: 'OIS Camera', bn: 'OIS ক্যামেরা' }, specs: ['Super AMOLED 90Hz', 'Helio G99 Processor', '50MP Main with OIS', '5000mAh Battery'], img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a24-4g.jpg' },
    { id: 11, brand: 'Samsung', name: 'Galaxy M14 5G', price: 21000, tag: { en: '6000mAh Monster', bn: '৬০০০mAh ব্যাটারি' }, specs: ['90Hz FHD+ Display', 'Exynos 1330 (5nm)', '50MP Triple Camera', '6000mAh Massive Bat'], img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m14-5g.jpg' },
    { id: 12, brand: 'Samsung', name: 'Galaxy A14', price: 18500, tag: { en: 'Reliable', bn: 'দীর্ঘস্থায়ী' }, specs: ['6.6" FHD+ Large Screen', 'Octa-core Processor', '50MP Triple Camera', '13MP High-res Selfie'], img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a14-4g.jpg' },
    { id: 13, brand: 'Samsung', name: 'Galaxy A04s', price: 13500, tag: { en: 'Entry Level', bn: 'এন্ট্রি লেভেল' }, specs: ['90Hz Smooth Display', 'Exynos 850 Stable', '50MP Triple Camera', 'Dolby Atmos Audio'], img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a04s.jpg' },
    
    { id: 14, brand: 'Vivo', name: 'Vivo V27e', price: 32999, tag: { en: 'Aura Light', bn: 'অরা লাইট' }, specs: ['120Hz AMOLED Panel', 'Helio G99 High Speed', '64MP OIS Aura Portrait', '66W FlashCharge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/vivo-v27e.jpg' },
    { id: 15, brand: 'Vivo', name: 'Vivo Y22', price: 17500, tag: { en: 'Design', bn: 'স্লিক ডিজাইন' }, specs: ['6.55" Sunlight Screen', 'Helio G85 Processor', '50MP Night Camera', '18W Fast Charge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/vivo-y22.jpg' },
    { id: 16, brand: 'Vivo', name: 'Vivo Y16', price: 14000, tag: { en: 'Slim', bn: 'স্লিম বিল্ড' }, specs: ['2.5D Curved Design', 'Helio P35 Octa-Core', 'AI Dual Camera', '5000mAh All-day'], img: 'https://fdn2.gsmarena.com/vv/bigpic/vivo-y16.jpg' },
    
    { id: 17, brand: 'Oppo', name: 'Oppo A78', price: 26500, tag: { en: '67W Flash', bn: '৬৭W ফাস্ট চার্জ' }, specs: ['FHD+ AMOLED 90Hz', 'Snapdragon 680', '50MP AI Dual Camera', '67W SUPERVOOC'], img: 'https://fdn2.gsmarena.com/vv/bigpic/oppo-a78-4g.jpg' },
    { id: 18, brand: 'Oppo', name: 'Oppo A17', price: 14500, tag: { en: 'Leather Feel', bn: 'লেদার ফিনিশ' }, specs: ['Premium Leather Design', 'Helio G35 Processor', '50MP AI Camera', '5000mAh Battery'], img: 'https://fdn2.gsmarena.com/vv/bigpic/oppo-a17.jpg' },
    
    { id: 19, brand: 'Infinix', name: 'Infinix Note 30', price: 18500, tag: { en: '45W Fast', bn: '৪৫W ফাস্ট চার্জ' }, specs: ['120Hz FHD+ Display', 'Helio G99 6nm', '64MP Ultra Clear Cam', '45W Bypass Charge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/infinix-note-30.jpg' },
    { id: 20, brand: 'Infinix', name: 'Infinix Hot 30', price: 15000, tag: { en: 'Gaming', bn: 'গেমিং ডিসপ্লে' }, specs: ['90Hz 1080P Screen', 'Helio G88 Processor', '50MP Night Camera', '33W Fast Charge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-30.jpg' },
    
    { id: 21, brand: 'Tecno', name: 'Tecno Camon 20', price: 19999, tag: { en: 'AMOLED Portrait', bn: 'অ্যামোলেড পোর্ট্রেট' }, specs: ['FHD+ AMOLED Screen', 'Helio G85 Processor', '64MP RGBW Sensor', '33W Flash Charge'], img: 'https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-20.jpg' },
    { id: 22, brand: 'Tecno', name: 'Tecno Spark 10 Pro', price: 15500, tag: { en: '32MP Selfie', bn: '৩২MP সেলফি' }, specs: ['90Hz FHD+ Big Screen', 'Helio G88 Gaming Chip', '50MP Ultra Clear', 'Glass Starry Design'], img: 'https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-10-pro.jpg' },
    
    { id: 23, brand: 'OnePlus', name: 'OnePlus Nord CE 3 Lite', price: 28000, tag: { en: '108MP Master', bn: '১০৮MP ক্যামেরা' }, specs: ['120Hz Smooth Display', 'Snapdragon 695 5G', '108MP 3x Lossless Zoom', '67W SUPERVOOC'], img: 'https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-ce-3-lite-5g.jpg' },
    { id: 24, brand: 'Motorola', name: 'Moto G32', price: 17000, tag: { en: 'Stereo Dolby', bn: 'ডলবি স্পিকার' }, specs: ['90Hz FHD+ Display', 'Snapdragon 680', '50MP Quad Pixel Cam', 'Dual Stereo Speakers'], img: 'https://fdn2.gsmarena.com/vv/bigpic/motorola-moto-g32.jpg' }
];

function initInventoryCatalog() {
    const grid = document.getElementById('inventory-grid');
    if (!grid) return;

    const searchInput = document.getElementById('inv-search');
    const sortSelect = document.getElementById('inv-sort');
    const filterChips = document.querySelectorAll('.chip-btn');
    const countDisplay = document.getElementById('inv-count');

    let currentFilter = 'all';
    let currentSearch = '';
    let currentSort = 'featured';

    const render = () => {
        let filtered = INVENTORY_DATA.filter(item => {
            const matchesFilter = (currentFilter === 'all') || 
                                  (item.brand.toLowerCase() === currentFilter.toLowerCase()) ||
                                  (currentFilter === 'xiaomi' && item.brand.toLowerCase() === 'poco') ||
                                  (currentFilter === 'infinix' && item.brand.toLowerCase() === 'tecno');

            const matchesSearch = item.name.toLowerCase().includes(currentSearch.toLowerCase()) ||
                                  item.brand.toLowerCase().includes(currentSearch.toLowerCase()) ||
                                  item.specs.some(s => s.toLowerCase().includes(currentSearch.toLowerCase()));

            return matchesFilter && matchesSearch;
        });

        if (currentSort === 'price-low') {
            filtered.sort((a, b) => a.price - b.price);
        } else if (currentSort === 'price-high') {
            filtered.sort((a, b) => b.price - a.price);
        } else if (currentSort === 'name') {
            filtered.sort((a, b) => a.name.localeCompare(b.name));
        }

        if (countDisplay) {
            const countNum = currentLanguage === 'bn' ? toBengaliDigits(filtered.length) : filtered.length;
            countDisplay.textContent = currentLanguage === 'bn' ? `${countNum} টি হ্যান্ডসেট স্টকে রয়েছে` : `${countNum} Handsets Available`;
        }

        if (filtered.length === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; color: var(--text-secondary);">
                    <i class="fa-solid fa-mobile-screen-button" style="font-size: 3rem; color: var(--text-dim); margin-bottom: 16px; display:block;"></i>
                    <h3 style="margin-bottom:8px;">${currentLanguage === 'bn' ? 'কোনো হ্যান্ডসেট পাওয়া যায়নি' : 'No smartphones match your filter'}</h3>
                    <p>${currentLanguage === 'bn' ? 'অন্য কোনো মডেল সার্চ করুন অথবা ব্র্যান্ড ফিল্টার পরিবর্তন করুন।' : 'Try searching for a different model or clearing your active brand filter.'}</p>
                </div>
            `;
            return;
        }

        grid.innerHTML = filtered.map(item => {
            const formattedPrice = currentLanguage === 'bn' ? toBengaliDigits(item.price.toLocaleString('en-BD')) : item.price.toLocaleString('en-BD');
            const itemTag = (typeof item.tag === 'object') ? (item.tag[currentLanguage] || item.tag.en) : item.tag;
            const btnText = currentLanguage === 'bn' ? 'অর্ডার করুন' : 'Order Now';
            const waText = encodeURIComponent(currentLanguage === 'bn'
                ? `আসসালামু আলাইকুম মোবাইল এক্সপ্রেস, আমি ${item.brand} ${item.name} (৳${formattedPrice}) ক্রয় করতে আগ্রহী। এটি কি স্টকে আছে?`
                : `Assalamu Alaikum Mobile Express, I am interested in purchasing the ${item.brand} ${item.name} (৳${formattedPrice}). Is it available in store?`);
            
            const specsList = item.specs.map(s => `<li><i class="fa-solid fa-microchip"></i> <span>${s}</span></li>`).join('');

            return `
                <div class="inv-card">
                    <div class="inv-card-top">
                        <span class="inv-badge-top">${itemTag}</span>
                        <span class="inv-brand">${item.brand}</span>
                    </div>
                    <div class="inv-img">
                        <img src="${item.img}" alt="${item.name}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src='Mobile Express.svg';">
                    </div>
                    <h3>${item.name}</h3>
                    <div class="inv-price">৳ ${formattedPrice}</div>
                    <ul class="inv-specs">
                        ${specsList}
                    </ul>
                    <a href="https://wa.me/8801834254875?text=${waText}" target="_blank" rel="noopener noreferrer" class="btn-primary btn-full">
                        <i class="fa-brands fa-whatsapp"></i> <span>${btnText}</span>
                    </a>
                </div>
            `;
        }).join('');
    };

    window.reRenderInventory = render;

    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            currentSearch = e.target.value.trim();
            render();
        });
    }

    if (sortSelect) {
        sortSelect.addEventListener('change', (e) => {
            currentSort = e.target.value;
            render();
        });
    }

    filterChips.forEach(chip => {
        chip.addEventListener('click', () => {
            filterChips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            currentFilter = chip.getAttribute('data-filter') || 'all';
            render();
        });
    });

    render();
}
