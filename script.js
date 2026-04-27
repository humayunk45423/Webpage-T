// --- 3D Background Parallax Effect (Card Chevrons) ---
const bands = document.querySelectorAll('.card-band');

window.addEventListener('scroll', () => {
    requestAnimationFrame(() => {
        const scrolled = window.scrollY;
        
        bands.forEach(band => {
            const speed = parseFloat(band.getAttribute('data-speed') || '0.5');
            const yMove = scrolled * speed;
            
            // Determine if it's left or right to maintain correct rotation
            let baseRotate = band.classList.contains('band-left-1') || band.classList.contains('band-left-2') ? 25 : -25;
            
            // Add a slight dynamic rotation based on scroll for extra 3D feel
            const dynamicRotate = baseRotate + (scrolled * 0.01);
            
            // Read Z-translation from CSS logic (hardcoded here to maintain depth)
            let zTrans = -100;
            if (band.classList.contains('band-left-2') || band.classList.contains('band-right-2')) {
                zTrans = -200;
            }
            
            band.style.transform = `translateY(${yMove}px) rotateZ(${dynamicRotate}deg) translateZ(${zTrans}px)`;
        });
    });
});


// --- Dynamic Inventory Generation (Mid-to-Budget BD Market) ---
const inventoryGrid = document.getElementById('inventory-grid');

if (inventoryGrid) {
    const products = [
        { brand: 'Xiaomi', name: 'Redmi Note 13', price: '22,999', specs: 'AMOLED 120Hz | Snapdragon 685 | 108MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-4g.jpg' },
        { brand: 'Xiaomi', name: 'Redmi Note 12', price: '19,500', specs: 'AMOLED 120Hz | Snapdragon 685 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-12-4g.jpg' },
        { brand: 'Xiaomi', name: 'Redmi 12', price: '16,999', specs: '90Hz LCD | Helio G88 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-12.jpg' },
        { brand: 'Poco', name: 'Poco X5 Pro', price: '32,000', specs: 'AMOLED 120Hz | Snapdragon 778G | 108MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-x5-pro-5g.jpg' },
        { brand: 'Poco', name: 'Poco M5', price: '15,500', specs: '90Hz LCD | Helio G99 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-m5-.jpg' },
        
        { brand: 'Realme', name: 'Realme C55', price: '18,999', specs: '90Hz LCD | Helio G88 | 64MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-c55.jpg' },
        { brand: 'Realme', name: 'Realme C53', price: '14,999', specs: '90Hz LCD | Unisoc T612 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-c53.jpg' },
        { brand: 'Realme', name: 'Realme 11 Pro', price: '35,000', specs: 'Curved AMOLED | Dimensity 7050 | 100MP OIS', img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-11-pro.jpg' },
        { brand: 'Realme', name: 'Realme 10', price: '20,000', specs: 'Super AMOLED 90Hz | Helio G99 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/realme-10-4g.jpg' },
        
        { brand: 'Samsung', name: 'Galaxy A24', price: '24,500', specs: 'Super AMOLED 90Hz | Helio G99 | 50MP OIS', img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a24-4g.jpg' },
        { brand: 'Samsung', name: 'Galaxy A14', price: '18,500', specs: 'PLS LCD | Exynos 850 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a14-4g.jpg' },
        { brand: 'Samsung', name: 'Galaxy M14 5G', price: '21,000', specs: '90Hz LCD | Exynos 1330 | 6000mAh Battery', img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-m14-5g.jpg' },
        { brand: 'Samsung', name: 'Galaxy A04s', price: '13,500', specs: '90Hz LCD | Exynos 850 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a04s.jpg' },
        
        { brand: 'Vivo', name: 'Vivo Y22', price: '17,500', specs: 'LCD | Helio G85 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/vivo-y22.jpg' },
        { brand: 'Vivo', name: 'Vivo Y16', price: '14,000', specs: 'LCD | Helio P35 | 13MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/vivo-y16.jpg' },
        { brand: 'Vivo', name: 'Vivo V27e', price: '32,999', specs: 'AMOLED 120Hz | Helio G99 | 64MP OIS', img: 'https://fdn2.gsmarena.com/vv/bigpic/vivo-v27e.jpg' },
        
        { brand: 'Oppo', name: 'Oppo A78', price: '26,500', specs: 'AMOLED 90Hz | Snapdragon 680 | 67W Fast Charge', img: 'https://fdn2.gsmarena.com/vv/bigpic/oppo-a78-4g.jpg' },
        { brand: 'Oppo', name: 'Oppo A17', price: '14,500', specs: 'LCD | Helio G35 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/oppo-a17.jpg' },
        
        { brand: 'Infinix', name: 'Infinix Note 30', price: '18,500', specs: '120Hz LCD | Helio G99 | 64MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/infinix-note-30.jpg' },
        { brand: 'Infinix', name: 'Infinix Hot 30', price: '15,000', specs: '90Hz LCD | Helio G88 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/infinix-hot-30.jpg' },
        
        { brand: 'Tecno', name: 'Tecno Spark 10 Pro', price: '15,500', specs: '90Hz LCD | Helio G88 | 32MP Selfie', img: 'https://fdn2.gsmarena.com/vv/bigpic/tecno-spark-10-pro.jpg' },
        { brand: 'Tecno', name: 'Tecno Camon 20', price: '19,999', specs: 'AMOLED | Helio G85 | 64MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/tecno-camon-20.jpg' },
        
        { brand: 'Motorola', name: 'Moto G32', price: '17,000', specs: '90Hz LCD | Snapdragon 680 | 50MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/motorola-moto-g32.jpg' },
        { brand: 'OnePlus', name: 'Nord CE 3 Lite', price: '28,000', specs: '120Hz LCD | Snapdragon 695 | 108MP Camera', img: 'https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-ce-3-lite-5g.jpg' }
    ];

    products.forEach((prod) => {
        // Split specs
        const specList = prod.specs.split('|').map(s => `<li><i class="fa-solid fa-microchip" style="margin-right:8px; opacity:0.5;"></i> <span>${s.trim()}</span></li>`).join('');
        
        const cardHTML = `
            <div class="inv-card glass-panel" data-tilt data-tilt-max="5" data-tilt-glare="true" data-tilt-max-glare="0.2">
                <div class="inv-img">
                    <img src="${prod.img}" alt="${prod.name}" loading="lazy">
                </div>
                <h3>${prod.name}</h3>
                <div class="inv-price">৳ ${prod.price}</div>
                <ul class="inv-specs">
                    ${specList}
                </ul>
                <a href="https://wa.me/8801834254875?text=I'm%20interested%20in%20the%20${encodeURIComponent(prod.name)}" class="btn-primary btn-full">
                    Acquire Device <i class="fa-brands fa-whatsapp"></i>
                </a>
            </div>
        `;
        inventoryGrid.insertAdjacentHTML('beforeend', cardHTML);
    });
}
