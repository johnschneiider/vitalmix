document.addEventListener('DOMContentLoaded', function() {
    const barraInferior = document.querySelector('.barra-inferior');
    const fireworksContainer = document.getElementById('fireworks-container');
    let isPressed = false;
    let interval;

    barraInferior.addEventListener('click', function() {
      createFireworks();
    });

    barraInferior.addEventListener('mousedown', function(event) {
      isPressed = true;
      interval = setInterval(() => createFireworksFromPointer(event), 100); // Crea fuegos artificiales cada 100ms
    });

    barraInferior.addEventListener('mouseup', function() {
      isPressed = false;
      clearInterval(interval);
    });

    barraInferior.addEventListener('mouseleave', function() {
      isPressed = false;
      clearInterval(interval);
    });

    function createFireworks() {
      for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'firework-particle';
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.backgroundColor = getRandomColor();
        particle.style.animationDuration = `${Math.random() * 2 + 1}s`;
        fireworksContainer.appendChild(particle);

        particle.addEventListener('animationend', function() {
          particle.remove();
        });
      }
    }

    function createFireworksFromPointer(event) {
      if (!isPressed) return;

      for (let i = 0; i < 10; i++) {
        const particle = document.createElement('div');
        particle.className = 'firework-particle';
        particle.style.left = `${event.clientX}px`;
        particle.style.top = `${event.clientY}px`;
        particle.style.backgroundColor = getRandomColor();
        particle.style.animationDuration = `${Math.random() * 2 + 1}s`;
        fireworksContainer.appendChild(particle);

        particle.addEventListener('animationend', function() {
          particle.remove();
        });
      }
    }

    function getRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
  });