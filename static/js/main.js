function createCosmicBackground() {
    const cosmicBackground = document.getElementById('cosmicBackground');
    
    for(let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 3}s`;
        cosmicBackground.appendChild(star);
    }

    setInterval(() => {
        const shootingStar = document.createElement('div');
        shootingStar.className = 'shooting-star';
        shootingStar.style.left = `${Math.random() * 20}%`;
        shootingStar.style.top = `${Math.random() * 20}%`;
        cosmicBackground.appendChild(shootingStar);
        
        setTimeout(() => shootingStar.remove(), 3000);
    }, 5000);
}

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelectorAll('.nav-link, .content-section').forEach(el => {
            el.classList.remove('active');
        });
        this.classList.add('active');
        const sectionId = this.getAttribute('href').substring(1);
        document.getElementById(sectionId).classList.add('active');
    });
});

createCosmicBackground();
