// 1. Scroll suave a secciones
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }

    // Si el menú móvil está abierto, ciérralo al hacer clic
    const navMenu = document.getElementById('nav-menu');
    if (navMenu && navMenu.classList.contains('active')) {
      navMenu.classList.remove('active');
    }
  });
});

// 2. Scroll Reveal (animación al aparecer)
const revealElements = document.querySelectorAll('.reveal');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target); // solo una vez
    }
  });
}, {
  threshold: 0.1
});

revealElements.forEach(el => observer.observe(el));

// 3. Menú hamburguesa
const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.getElementById('nav-menu');

if (menuToggle && navMenu) {
  menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
  });
}

// 4. Validación del formulario
const form = document.getElementById('contact-form');

if (form) {
  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const nombre = form.nombre.value.trim();
    const email = form.email.value.trim();

    if (!nombre || !email) {
      alert('Por favor completa los campos requeridos.');
      return;
    }

    alert(`¡Gracias por tu mensaje, ${nombre}! Pronto nos pondremos en contacto contigo ☕`);
    form.reset();
  });
}
