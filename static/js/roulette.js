document.addEventListener('DOMContentLoaded', () => {
    const hacerPedidoBtn = document.getElementById('hacerPedidoBtn');
    const ruletaModal = new bootstrap.Modal(document.getElementById('ruletaModal'));
    const ruleta = document.getElementById('ruleta');
    const resultado = document.getElementById('resultado');
    const btnGirar = document.getElementById('btnGirar');
    const cerrarModal = document.getElementById('cerrarModal');
    const pedidoForm = document.getElementById('pedidoForm');

    // Al hacer clic en "Hacer pedido", abre el modal con la ruleta
    hacerPedidoBtn.addEventListener('click', (event) => {
        event.preventDefault();
        ruletaModal.show();
    });

    // Función para reiniciar la posición de la ruleta a 0°
    const reiniciarRuleta = () => {
        ruleta.style.transition = 'none';
        ruleta.style.transform = 'rotate(0deg)';
    };

    btnGirar.addEventListener('click', () => {
        btnGirar.disabled = true; // Desactiva el botón mientras gira
        reiniciarRuleta(); // Reinicia la posición inicial de la ruleta

        const premios = [
            { texto: 'Compra gratis', angulo: 0 },            // Primer segmento
            { texto: 'Gratis para un amigo', angulo: 30 },    // Segundo segmento
            { texto: 'Casi ganas!', angulo: 60 },             // Tercer segmento
            { texto: 'Sigue intentando', angulo: 90 },        // Cuarto segmento
            { texto: '20% descuento', angulo: 120 },          // Quinto segmento
            { texto: 'Un mes gratis para ti', angulo: 150 },  // Sexto segmento
            { texto: 'Compra gratis', angulo: 180 },          // Séptimo segmento
            { texto: 'Sigue intentando', angulo: 210 },       // Octavo segmento
            { texto: '2 por precio de 1', angulo: 240 },      // Noveno segmento
            { texto: 'Ups! sigue intentando', angulo: 270 },  // Décimo segmento
            { texto: '10% descuento', angulo: 300 },          // Undécimo segmento
            { texto: 'Sigue intentando', angulo: 330 }        // Duodécimo segmento
        ];

        // Selecciona un premio aleatorio
        const premioSeleccionado = premios[Math.floor(Math.random() * premios.length)];
        const vueltas = 15; // Número de vueltas completas antes de frenar
        const anguloFinal = 360 * vueltas + premioSeleccionado.angulo;

        // Aplicar la animación de giro
        setTimeout(() => {
            ruleta.style.transition = 'transform 12s cubic-bezier(0.1, 0.9, 0.1, 1)';
            ruleta.style.transform = `rotate(${anguloFinal}deg)`;
        }, 50);

        // Mostrar resultado después de la animación
        setTimeout(() => {
            resultado.textContent = `¡Tu premio es: ${premioSeleccionado.texto}!`;
            resultado.style.display = 'block';
            cerrarModal.style.display = 'inline-block';
            btnGirar.disabled = false; // Reactivar el botón después del giro
        }, 12000);
    });

    // Al hacer clic en "Aceptar", enviar el formulario
    cerrarModal.addEventListener('click', () => {
        ruletaModal.hide();
        pedidoForm.submit();
    });
});
