// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Crecer Website Initialized');

    const menuToggle = document.getElementById('menu-toggle');
    const mainNav = document.getElementById('main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            console.log('📱 Mobile Menu Toggle clicked');
            mainNav.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!menuToggle.contains(e.target) && !mainNav.contains(e.target)) {
            mainNav.classList.remove('active');
            menuToggle.classList.remove('active');
        }
    });

    // Contact Card Click Handler
    const clickableCards = document.querySelectorAll('.clickable-card');
    console.log(`🔍 Found ${clickableCards.length} clickable contact cards`);

    clickableCards.forEach(card => {
        card.addEventListener('click', (e) => {
            const link = card.querySelector('.contact-card__link');
            if (link) {
                console.log(`🖱️ Contact card clicked. Triggering link: ${link.href}`);
                if (e.target !== link) {
                    // Using window.location.href for more robust protocol handling (mailto/tel)
                    window.location.href = link.href;
                }
            } else {
                console.warn('⚠️ No link found inside the contact card');
            }
        });
    });
});
