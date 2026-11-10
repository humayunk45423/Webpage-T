import os
from playwright.sync_api import sync_playwright

prototype_html = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hero Phone Prototype Test</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=Noto+Sans+Bengali:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
    <style>
        /* Prototype-specific styles to test two-column hero */
        .hero-section {
            overflow: visible !important;
            padding: 54px 50px 48px !important;
            text-align: left !important;
        }

        .hero-layout {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 36px;
            align-items: center;
            position: relative;
        }

        .hero-content-col {
            position: relative;
            z-index: 2;
        }

        .hero-badges-cluster {
            justify-content: flex-start !important;
            margin-bottom: 20px !important;
        }

        .hero-title {
            text-align: left !important;
            margin-bottom: 20px !important;
            font-size: clamp(2.3rem, 4.4vw, 3.8rem) !important;
        }

        .hero-desc {
            text-align: left !important;
            margin: 0 0 28px 0 !important;
            max-width: 560px !important;
            font-size: 1.12rem !important;
        }

        .hero-actions {
            justify-content: flex-start !important;
            margin-bottom: 32px !important;
        }

        .hero-stats-row {
            margin: 0 !important;
            max-width: 520px !important;
        }

        .stat-box {
            text-align: left !important;
        }

        /* Phone Stage & Visual Styles */
        .hero-visual-col {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2;
        }

        .hero-phone-stage {
            position: relative;
            width: 100%;
            max-width: 480px;
            aspect-ratio: 520 / 480;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: -15px;
        }

        .phone-stage-glow {
            position: absolute;
            width: 420px;
            height: 420px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(230, 57, 70, 0.28) 0%, rgba(230, 57, 70, 0.08) 55%, transparent 72%);
            filter: blur(36px);
            z-index: 0;
            pointer-events: none;
            animation: glowPulse 8s ease-in-out infinite alternate;
        }

        [data-theme="light"] .phone-stage-glow {
            background: radial-gradient(circle, rgba(217, 4, 41, 0.22) 0%, rgba(217, 4, 41, 0.06) 55%, transparent 72%);
            filter: blur(32px);
        }

        @keyframes glowPulse {
            0% { transform: scale(0.92); opacity: 0.75; }
            100% { transform: scale(1.08); opacity: 1; }
        }

        .hero-phone-svg {
            width: 100%;
            height: 100%;
            position: relative;
            z-index: 1;
            filter: drop-shadow(0 20px 35px rgba(0, 0, 0, 0.45));
            overflow: visible;
        }

        [data-theme="light"] .hero-phone-svg {
            filter: drop-shadow(0 18px 30px rgba(0, 0, 0, 0.12));
        }

        /* SVG Internal Themes */
        .hero-phone-svg .phone-screen-bg {
            fill: #0c0e14;
        }
        [data-theme="light"] .hero-phone-svg .phone-screen-bg {
            fill: #ffffff;
        }

        .hero-phone-svg .phone-card-bg {
            fill: rgba(255, 255, 255, 0.06);
            stroke: rgba(255, 255, 255, 0.12);
        }
        [data-theme="light"] .hero-phone-svg .phone-card-bg {
            fill: rgba(15, 23, 42, 0.04);
            stroke: rgba(15, 23, 42, 0.10);
        }

        .hero-phone-svg .phone-text-pri {
            fill: #ffffff;
        }
        [data-theme="light"] .hero-phone-svg .phone-text-pri {
            fill: #0f172a;
        }

        .hero-phone-svg .phone-text-sec {
            fill: #94a3b8;
        }
        [data-theme="light"] .hero-phone-svg .phone-text-sec {
            fill: #64748b;
        }

        .hero-phone-svg .phone-back-body {
            fill: url(#backPhoneGradDark);
        }
        [data-theme="light"] .hero-phone-svg .phone-back-body {
            fill: url(#backPhoneGradLight);
        }

        .hero-phone-svg .phone-back-left-body {
            fill: url(#leftPhoneGradDark);
        }
        [data-theme="light"] .hero-phone-svg .phone-back-left-body {
            fill: url(#leftPhoneGradLight);
        }

        /* Floating Info Chips */
        .hero-chip {
            position: absolute;
            z-index: 10;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 999px;
            background: rgba(18, 20, 28, 0.82);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35), 0 0 12px rgba(230, 57, 70, 0.15);
            font-size: 0.82rem;
            font-weight: 700;
            color: #f8fafc;
            white-space: nowrap;
            user-select: none;
            pointer-events: auto;
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
        }

        [data-theme="light"] .hero-chip {
            background: rgba(255, 255, 255, 0.88);
            border: 1px solid rgba(217, 4, 41, 0.18);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 0 10px rgba(217, 4, 41, 0.08);
            color: #0f172a;
        }

        .hero-chip:hover {
            transform: translateY(-3px) scale(1.04);
            border-color: var(--red-main);
            box-shadow: 0 14px 30px var(--red-glow);
        }

        .hero-chip i {
            color: var(--red-main);
            font-size: 0.95rem;
        }

        /* Chip Placements */
        .chip-1 { top: 6%; left: -2%; animation: chipFloat1 6.2s ease-in-out infinite; }
        .chip-2 { top: 28%; right: -6%; animation: chipFloat2 7.1s ease-in-out infinite 0.8s; }
        .chip-3 { bottom: 14%; left: 0%; animation: chipFloat3 6.6s ease-in-out infinite 1.4s; }
        .chip-4 { bottom: 4%; right: 2%; animation: chipFloat4 7.4s ease-in-out infinite 2.1s; }

        @keyframes chipFloat1 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-7px); } }
        @keyframes chipFloat2 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
        @keyframes chipFloat3 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
        @keyframes chipFloat4 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-7px); } }

        /* Gentle Phone Floating Motions */
        .phone-group-front {
            animation: phoneFloatFront 6.8s ease-in-out infinite;
        }
        .phone-group-right {
            animation: phoneFloatRight 7.6s ease-in-out infinite 0.6s;
        }
        .phone-group-left {
            animation: phoneFloatLeft 8.2s ease-in-out infinite 1.2s;
        }

        @keyframes phoneFloatFront { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
        @keyframes phoneFloatRight { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(5px); } }
        @keyframes phoneFloatLeft { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(4px); } }

        @media (prefers-reduced-motion: reduce) {
            .phone-group-front, .phone-group-right, .phone-group-left, .hero-chip, .phone-stage-glow {
                animation: none !important;
                transform: none !important;
            }
        }

        /* Responsive Breakpoints */
        @media (max-width: 991px) {
            .hero-section {
                padding: 40px 28px !important;
                text-align: center !important;
            }
            .hero-layout {
                grid-template-columns: 1fr;
                gap: 32px;
            }
            .hero-badges-cluster,
            .hero-title,
            .hero-desc,
            .hero-actions {
                text-align: center !important;
                justify-content: center !important;
            }
            .hero-desc {
                margin: 0 auto 24px !important;
            }
            .hero-stats-row {
                margin: 0 auto !important;
            }
            .stat-box {
                text-align: center !important;
            }
            .hero-phone-stage {
                max-width: 380px;
                margin: 0 auto;
            }
            .chip-1 { top: 4%; left: 0%; }
            .chip-2 { top: 25%; right: -2%; }
            .chip-3 { bottom: 12%; left: 2%; }
            .chip-4 { bottom: 2%; right: 4%; }
        }

        @media (max-width: 640px) {
            .hero-section {
                padding: 24px 14px 20px !important;
            }
            .hero-title {
                font-size: clamp(1.65rem, 7vw, 2.15rem) !important;
            }
            .hero-phone-stage {
                max-width: 320px;
                aspect-ratio: 520 / 440;
            }
            .hero-chip {
                padding: 5px 11px;
                font-size: 0.72rem;
                gap: 6px;
            }
            .hero-chip i {
                font-size: 0.8rem;
            }
        }
    </style>
</head>
<body class="lang-bn">
    <div class="app-content">
        <section id="hero" class="hero-section glass-panel">
            <div class="hero-layout">
                <!-- Left Column: Copy & Actions -->
                <div class="hero-content-col">
                    <div class="hero-badges-cluster">
                        <div class="hero-badge apple-specialist-badge">
                            <i class="fa-brands fa-apple"></i> <span>অ্যাপল এক্সপার্ট তানভীর ইকবাল • মোবাইল এক্সপ্রেস</span>
                        </div>
                    </div>

                    <h1 class="hero-title">
                        <span>মোবাইল এক্সপ্রেস</span> <br>
                        <span class="red-gradient-text">ক্রয় • বিনিময় • বিক্রয়।</span>
                    </h1>
                    <p class="hero-desc">
                        তানভীর ইকবালের বিশ্বস্ত অ্যাপল ও স্মার্টফোন হাব — আইক্লাউড অ্যাকাউন্ট তৈরি, পাসকোড/লক রিকভারি ও বাইপাস সমাধান এবং <a href="https://maps.app.goo.gl/1e6A4LQxwAeqnt4p8" target="_blank" rel="noopener noreferrer" class="location-highlight" title="গুগল ম্যাপে শপের লোকেশন ও ডিরেকশন দেখুন"><i class="fa-solid fa-location-dot"></i> বদরগঞ্জ, রংপুরে</a> ৭ দিনের গ্যারান্টি সহ স্মার্টফোন ক্রয় • বিনিময় • বিক্রয় সুবিধা।
                    </p>
                    <div class="hero-actions">
                        <a href="inventory.html" class="btn-primary">
                            <i class="fa-solid fa-mobile-screen"></i> <span>স্মার্টফোন দেখুন ও এক্সচেঞ্জ (২৪+)</span>
                        </a>
                        <a href="#services" class="btn-secondary">
                            <i class="fa-brands fa-apple"></i> <span>অ্যাপল ও আইক্লাউড ল্যাব</span>
                        </a>
                    </div>

                    <!-- Key Metric Highlights -->
                    <div class="hero-stats-row">
                        <div class="stat-box">
                            <strong>১০০+</strong>
                            <span>সফল ডিভাইস মেরামত</span>
                        </div>
                        <div class="stat-box">
                            <strong>৯৯.৪%</strong>
                            <span>বাইপাস সাফল্য হার</span>
                        </div>
                        <div class="stat-box">
                            <strong>১৫ মিনিট</strong>
                            <span>এক্সপ্রেস সার্ভিস</span>
                        </div>
                    </div>
                </div>

                <!-- Right Column: Smartphone Stack Visual -->
                <div class="hero-visual-col" aria-label="Used smartphones for sale, exchange, repair and iCloud unlock">
                    <div class="hero-phone-stage">
                        <div class="phone-stage-glow" aria-hidden="true"></div>

                        <!-- Vector Smartphone Cluster SVG -->
                        <svg class="hero-phone-svg" viewBox="0 0 520 480" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Smartphone cluster featuring verified devices and diagnostic service">
                            <defs>
                                <!-- Gradients for Depth & Realism -->
                                <linearGradient id="frontFrameGrad" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#4a5060"/>
                                    <stop offset="30%" stop-color="#1e222b"/>
                                    <stop offset="70%" stop-color="#0f1116"/>
                                    <stop offset="100%" stop-color="#2d3340"/>
                                </linearGradient>

                                <linearGradient id="frontRedRim" x1="0" y1="0" x2="0" y2="1">
                                    <stop offset="0%" stop-color="#ff4d5e" stop-opacity="0.9"/>
                                    <stop offset="45%" stop-color="#e63946" stop-opacity="0.6"/>
                                    <stop offset="100%" stop-color="#8b1e28" stop-opacity="0.2"/>
                                </linearGradient>

                                <linearGradient id="screenGradMesh" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#141724"/>
                                    <stop offset="40%" stop-color="#0e1017"/>
                                    <stop offset="85%" stop-color="#1b090c"/>
                                    <stop offset="100%" stop-color="#3b080f"/>
                                </linearGradient>

                                <linearGradient id="backPhoneGradDark" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#242834"/>
                                    <stop offset="50%" stop-color="#15171e"/>
                                    <stop offset="100%" stop-color="#0a0c10"/>
                                </linearGradient>

                                <linearGradient id="backPhoneGradLight" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#f1f5f9"/>
                                    <stop offset="50%" stop-color="#e2e8f0"/>
                                    <stop offset="100%" stop-color="#cbd5e1"/>
                                </linearGradient>

                                <linearGradient id="leftPhoneGradDark" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#1e222b"/>
                                    <stop offset="100%" stop-color="#08090d"/>
                                </linearGradient>

                                <linearGradient id="leftPhoneGradLight" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#e2e8f0"/>
                                    <stop offset="100%" stop-color="#94a3b8"/>
                                </linearGradient>

                                <linearGradient id="cameraGlassGrad" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#1a202c"/>
                                    <stop offset="50%" stop-color="#0b0e14"/>
                                    <stop offset="100%" stop-color="#030712"/>
                                </linearGradient>

                                <linearGradient id="lensRingGrad" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#64748b"/>
                                    <stop offset="50%" stop-color="#334155"/>
                                    <stop offset="100%" stop-color="#0f172a"/>
                                </linearGradient>

                                <linearGradient id="glassSweep" x1="0" y1="0" x2="1" y2="1">
                                    <stop offset="0%" stop-color="#ffffff" stop-opacity="0.14"/>
                                    <stop offset="28%" stop-color="#ffffff" stop-opacity="0.04"/>
                                    <stop offset="55%" stop-color="#ffffff" stop-opacity="0"/>
                                </linearGradient>
                            </defs>

                            <!-- ============================================== -->
                            <!-- PHONE 1: LEFT PHONE (BEHIND, TILT -14 DEG) -->
                            <!-- ============================================== -->
                            <g class="phone-group-left">
                                <g transform="translate(130, 240) rotate(-14) translate(-130, -240)">
                                    <!-- Shadow -->
                                    <rect x="42" y="66" width="180" height="370" rx="34" fill="rgba(0,0,0,0.55)" filter="blur(16px)"/>
                                    <!-- Outer Metal Frame -->
                                    <rect x="40" y="60" width="180" height="370" rx="34" fill="url(#leftPhoneGradDark)" class="phone-back-left-body" stroke="rgba(255,255,255,0.18)" stroke-width="1.5"/>
                                    <!-- Red Accent Highlight on Left Edge -->
                                    <rect x="40" y="60" width="180" height="370" rx="34" fill="none" stroke="url(#frontRedRim)" stroke-width="2" opacity="0.65"/>
                                    <!-- Screen / Glimpse -->
                                    <rect x="46" y="66" width="168" height="358" rx="28" fill="#07090d"/>
                                    <!-- Diagnostic code / lock aesthetic subtle lines -->
                                    <circle cx="130" cy="180" r="28" fill="none" stroke="rgba(230,57,70,0.4)" stroke-width="2" stroke-dasharray="4 4"/>
                                    <path d="M124 180L129 185L138 175" stroke="#e63946" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    <rect x="90" y="224" width="80" height="8" rx="4" fill="rgba(255,255,255,0.12)"/>
                                    <rect x="100" y="240" width="60" height="6" rx="3" fill="rgba(255,255,255,0.08)"/>
                                </g>
                            </g>

                            <!-- ============================================== -->
                            <!-- PHONE 2: RIGHT PHONE (BEHIND, BACK VIEW, TILT +11 DEG) -->
                            <!-- ============================================== -->
                            <g class="phone-group-right">
                                <g transform="translate(365, 230) rotate(11) translate(-365, -230)">
                                    <!-- Shadow -->
                                    <rect x="272" y="56" width="190" height="390" rx="36" fill="rgba(0,0,0,0.55)" filter="blur(18px)"/>
                                    <!-- Phone Body (Back Glass) -->
                                    <rect x="270" y="50" width="190" height="390" rx="36" fill="url(#backPhoneGradDark)" class="phone-back-body" stroke="rgba(255,255,255,0.16)" stroke-width="1.5"/>
                                    <!-- Red Rim Light on Right Edge -->
                                    <rect x="270" y="50" width="190" height="390" rx="36" fill="none" stroke="#e63946" stroke-width="2" opacity="0.5"/>

                                    <!-- Modern Triple Camera Module (Squircle Island) -->
                                    <rect x="286" y="66" width="76" height="84" rx="22" fill="url(#cameraGlassGrad)" stroke="rgba(255,255,255,0.22)" stroke-width="1.5"/>
                                    <!-- Camera 1: Top-Left (Primary 50MP) -->
                                    <circle cx="308" cy="88" r="14" fill="url(#lensRingGrad)"/>
                                    <circle cx="308" cy="88" r="10" fill="#05070a"/>
                                    <circle cx="308" cy="88" r="6" fill="#0f172a"/>
                                    <circle cx="306" cy="86" r="2.5" fill="#38bdf8" opacity="0.8"/>

                                    <!-- Camera 2: Bottom-Left (Ultra-Wide) -->
                                    <circle cx="308" cy="126" r="14" fill="url(#lensRingGrad)"/>
                                    <circle cx="308" cy="126" r="10" fill="#05070a"/>
                                    <circle cx="308" cy="126" r="6" fill="#0f172a"/>
                                    <circle cx="306" cy="124" r="2.5" fill="#ec4899" opacity="0.7"/>

                                    <!-- Camera 3: Center-Right (Telephoto) -->
                                    <circle cx="342" cy="107" r="14" fill="url(#lensRingGrad)"/>
                                    <circle cx="342" cy="107" r="10" fill="#05070a"/>
                                    <circle cx="342" cy="107" r="6" fill="#0f172a"/>
                                    <circle cx="340" cy="105" r="2.5" fill="#38bdf8" opacity="0.8"/>

                                    <!-- True Tone Dual-LED Flash -->
                                    <circle cx="342" cy="76" r="5" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>
                                    <circle cx="342" cy="76" r="2" fill="#ffffff"/>

                                    <!-- LiDAR / Mic Dot -->
                                    <circle cx="342" cy="136" r="2.5" fill="#1e293b" stroke="rgba(255,255,255,0.2)" stroke-width="0.5"/>
                                </g>
                            </g>

                            <!-- ============================================== -->
                            <!-- PHONE 3: MAIN FRONT PHONE (FLAGSHIP, TILT -5.5 DEG) -->
                            <!-- ============================================== -->
                            <g class="phone-group-front">
                                <g transform="translate(245, 245) rotate(-5.5) translate(-245, -245)">
                                    <!-- Soft Ground Contact Shadow -->
                                    <rect x="135" y="38" width="220" height="440" rx="40" fill="rgba(0,0,0,0.65)" filter="blur(22px)"/>
                                    
                                    <!-- Outer Titanium Chasis Frame -->
                                    <rect x="135" y="30" width="220" height="440" rx="40" fill="url(#frontFrameGrad)" stroke="rgba(255,255,255,0.22)" stroke-width="1.5"/>
                                    <!-- High-impact Red Precision Rim Light -->
                                    <rect x="135" y="30" width="220" height="440" rx="40" fill="none" stroke="url(#frontRedRim)" stroke-width="2.5"/>

                                    <!-- Ultra-Thin Bezel Interior -->
                                    <rect x="140" y="35" width="210" height="430" rx="36" fill="#000000"/>

                                    <!-- Active OLED Screen Surface -->
                                    <rect x="142" y="37" width="206" height="426" rx="34" fill="url(#screenGradMesh)" class="phone-screen-bg"/>

                                    <!-- Dynamic Island Cutout -->
                                    <rect x="217" y="44" width="56" height="15" rx="7.5" fill="#000000"/>
                                    <circle cx="261" cy="51.5" r="3" fill="#111827"/>
                                    <circle cx="261" cy="51.5" r="1.2" fill="#1e3a8a"/>

                                    <!-- Status Bar: Time & Connectivity -->
                                    <text x="160" y="56" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="800" fill="currentColor" class="phone-text-pri">9:41</text>
                                    
                                    <!-- 5G Bars -->
                                    <rect x="312" y="53" width="2" height="3" rx="0.5" fill="currentColor" class="phone-text-pri"/>
                                    <rect x="316" y="51" width="2" height="5" rx="0.5" fill="currentColor" class="phone-text-pri"/>
                                    <rect x="320" y="49" width="2" height="7" rx="0.5" fill="currentColor" class="phone-text-pri"/>
                                    <rect x="324" y="47" width="2" height="9" rx="0.5" fill="currentColor" class="phone-text-pri"/>

                                    <!-- Battery -->
                                    <rect x="330" y="48" width="16" height="8" rx="2.5" fill="none" stroke="currentColor" stroke-width="1" class="phone-text-pri"/>
                                    <rect x="332" y="50" width="11" height="4" rx="1.5" fill="#22c55e"/>
                                    <path d="M347 50.5V53.5" stroke="currentColor" stroke-width="1" stroke-linecap="round" class="phone-text-pri"/>

                                    <!-- ==================================== -->
                                    <!-- SCREEN UI: Mobile Express In-Shop App -->
                                    <!-- ==================================== -->
                                    
                                    <!-- Brand Verified Badge Pill -->
                                    <rect x="162" y="72" width="166" height="24" rx="12" fill="rgba(230,57,70,0.14)" stroke="rgba(230,57,70,0.35)" stroke-width="1"/>
                                    <circle cx="175" cy="84" r="5" fill="#22c55e"/>
                                    <path d="M172.5 84L174.5 86L178 82" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <text x="186" y="87.5" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.8" font-weight="800" fill="#e63946" letter-spacing="0.3">MOBILE EXPRESS VERIFIED</text>

                                    <!-- Core Feature Showcase Card -->
                                    <rect x="152" y="106" width="186" height="156" rx="20" class="phone-card-bg"/>

                                    <!-- Dual Device Exchange Graphic Inside Card -->
                                    <g transform="translate(245, 142)">
                                        <!-- Mini Phone 1 -->
                                        <rect x="-38" y="-22" width="28" height="44" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
                                        <rect x="-35" y="-19" width="22" height="38" rx="4" fill="#0f172a"/>
                                        <circle cx="-24" cy="-17" r="1.5" fill="#64748b"/>
                                        
                                        <!-- Mini Phone 2 -->
                                        <rect x="10" y="-22" width="28" height="44" rx="6" fill="#e63946" stroke="#ff4d5e" stroke-width="1"/>
                                        <rect x="13" y="-19" width="22" height="38" rx="4" fill="#8b1e28"/>
                                        <circle cx="24" cy="-17" r="1.5" fill="#fca5a5"/>

                                        <!-- Circular Exchange Arrow Icons -->
                                        <path d="M-5 -8C0 -14 5 -14 8 -8" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"/>
                                        <path d="M6 -10L8 -8L5 -6" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"/>
                                        <path d="M5 8C0 14 -5 14 -8 8" stroke="#e63946" stroke-width="1.5" stroke-linecap="round"/>
                                        <path d="M-6 10L-8 8L-5 6" fill="none" stroke="#e63946" stroke-width="1.5" stroke-linecap="round"/>
                                    </g>

                                    <!-- Card Headline -->
                                    <text x="245" y="184" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5" font-weight="900" fill="#e63946" letter-spacing="0.5">BUY • EXCHANGE • SELL</text>
                                    <text x="245" y="198" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="700" fill="currentColor" class="phone-text-pri">Certified Handsets In Stock</text>
                                    <text x="245" y="210" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="500" fill="currentColor" class="phone-text-sec">Motherboard-Tested & Diagnostics Passed</text>

                                    <!-- Rating / Test Score Bar -->
                                    <rect x="166" y="222" width="158" height="22" rx="11" fill="rgba(34,197,94,0.12)" stroke="rgba(34,197,94,0.25)" stroke-width="1"/>
                                    <path d="M178 233L181 236L187 230" stroke="#22c55e" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    <text x="194" y="236.5" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="800" fill="#22c55e">100% HARDWARE VERIFIED</text>

                                    <!-- Service Micro-Pills Row -->
                                    <rect x="152" y="272" width="58" height="20" rx="10" class="phone-card-bg"/>
                                    <text x="181" y="285" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.2" font-weight="700" fill="currentColor" class="phone-text-pri">Apple Lab</text>

                                    <rect x="216" y="272" width="58" height="20" rx="10" class="phone-card-bg"/>
                                    <text x="245" y="285" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.2" font-weight="700" fill="currentColor" class="phone-text-pri">iCloud Fix</text>

                                    <rect x="280" y="272" width="58" height="20" rx="10" class="phone-card-bg"/>
                                    <text x="309" y="285" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.2" font-weight="700" fill="currentColor" class="phone-text-pri">24+ Phones</text>

                                    <!-- Trust Guarantee Banner -->
                                    <rect x="152" y="302" width="186" height="38" rx="14" fill="rgba(230,57,70,0.08)" stroke="rgba(230,57,70,0.25)" stroke-width="1"/>
                                    <circle cx="170" cy="321" r="9" fill="var(--red-main)"/>
                                    <path d="M167 321L169 323L173 319" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
                                    <text x="185" y="318" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="800" fill="currentColor" class="phone-text-pri">7-Day Replacement</text>
                                    <text x="185" y="329" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.2" font-weight="600" fill="#e63946">Official Warranty Included</text>

                                    <!-- Quick Call-to-Action Bar -->
                                    <rect x="160" y="352" width="170" height="32" rx="16" fill="#e63946"/>
                                    <text x="245" y="372" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="800" fill="#ffffff" letter-spacing="0.3">BROWSE HANDSETS →</text>

                                    <!-- Home Indicator Bar -->
                                    <rect x="200" y="448" width="90" height="4" rx="2" fill="currentColor" class="phone-text-pri" opacity="0.4"/>

                                    <!-- Diagonal Glass Glare Sweep -->
                                    <path d="M142 37L348 37L280 240L142 160Z" fill="url(#glassSweep)"/>
                                </g>
                            </g>
                        </svg>

                        <!-- Floating Info Chips -->
                        <div class="hero-chip chip-1">
                            <i class="fa-solid fa-mobile-screen"></i>
                            <span data-i18n="hero-chip-verified">ব্যবহৃত • যাচাইকৃত</span>
                        </div>
                        <div class="hero-chip chip-2">
                            <i class="fa-solid fa-arrow-right-arrow-left"></i>
                            <span data-i18n="hero-chip-exchange">এক্সচেঞ্জ সুবিধা</span>
                        </div>
                        <div class="hero-chip chip-3">
                            <i class="fa-solid fa-screwdriver-wrench"></i>
                            <span data-i18n="hero-chip-repair">রিপেয়ার ও আনলক</span>
                        </div>
                        <div class="hero-chip chip-4">
                            <i class="fa-solid fa-shield-halved"></i>
                            <span data-i18n="hero-chip-warranty">৭ দিনের গ্যারান্টি</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</body>
</html>
"""

with open('tests/prototype.html', 'w', encoding='utf-8') as f:
    f.write(prototype_html)

os.makedirs('tests/prototype_shots', exist_ok=True)
url = 'file:///' + os.path.abspath('tests/prototype.html').replace('\\\\', '/')

with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, w, h in [('desktop', 1440, 900), ('tablet', 820, 1180), ('mobile', 390, 844)]:
        for theme in ['dark', 'light']:
            page = browser.new_page(viewport={'width': w, 'height': h})
            page.goto(url)
            page.evaluate(f"document.documentElement.setAttribute('data-theme', '{theme}')")
            page.wait_for_timeout(400)
            hero = page.locator('#hero')
            hero.screenshot(path=f'tests/prototype_shots/{name}_{theme}.png')
            page.close()
    browser.close()

print("Prototype screenshots captured!")

