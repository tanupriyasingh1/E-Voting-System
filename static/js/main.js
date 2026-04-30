document.addEventListener('DOMContentLoaded', () => {
    // Dark Mode Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlEl = document.documentElement;
    
    // Check local storage for theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlEl.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
    }

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = htmlEl.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        htmlEl.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        themeToggleBtn.textContent = theme === 'dark' ? '☀️' : '🌓';
    }

    // Biometric Simulation
    const biometricBtns = document.querySelectorAll('.biometric-btn');
    
    biometricBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent form submission immediately
            const form = this.closest('form');
            
            // Add scanning animation class
            this.classList.add('scanning');
            this.innerHTML = '<div class="fingerprint-icon">🌀</div><span>Scanning Fingerprint...</span>';
            
            // Simulate 2 seconds of biometric scanning
            setTimeout(() => {
                this.classList.remove('scanning');
                this.style.backgroundColor = 'rgba(34, 197, 94, 0.2)'; // Success green
                this.style.borderColor = 'var(--success-color)';
                this.innerHTML = '<div class="fingerprint-icon">✅</div><span>Verified! Casting Vote...</span>';
                
                // Submit the form after short delay
                setTimeout(() => {
                    form.submit();
                }, 800);
                
            }, 2000);
        });
    });
});
