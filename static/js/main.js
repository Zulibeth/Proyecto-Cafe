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

// Flip cards en móvil con clic
const flipCards = document.querySelectorAll('.flip-card');

flipCards.forEach(card => {
  card.addEventListener('click', () => {
    // Cerrar otras
    flipCards.forEach(other => {
      if (other !== card) other.classList.remove('flipped');
    });

    // Alternar esta
    card.classList.toggle('flipped');
  });
});

//Actualización de precios
async function fetchPrices() {
      try {
        const res = await fetch("/api/precios");
        const data = await res.json();
        document.getElementById("precio-altura").textContent = data["Café Altura - Brasil Peru (250g)"];
        document.getElementById("precio-mandrake").textContent = data["Café Mandrake - Blend Espresso (1kg)"];
        document.getElementById("precio-dLara").textContent = data["D'Lara - Blend Saphire El Salvador (250g)"];
      } catch (e) {
        console.error("Error al obtener los precios", e);
      }
    }

    fetchPrices();
    setInterval(fetchPrices, 300000); // cada 5 minutos


//Logica Boton volver arriba
const boton = document.getElementById("btnVolverArriba");

    // Mostrar el botón al hacer scroll hacia abajo
    window.onscroll = function() {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            boton.style.display = "block";
        } else {
            boton.style.display = "none";
        }
    };

    // Volver arriba con scroll suave
    boton.addEventListener("click", function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });