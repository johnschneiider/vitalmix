
  document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".animated-button");
    setInterval(() => {
      button.style.animation = "none"; // Reinicia la animación
      setTimeout(() => {
        button.style.animation = "attention 1s ease-in-out";
      }, 10); // Espera un poco para reiniciar
    }, 5000); // Repite cada 5 segundos
  });
