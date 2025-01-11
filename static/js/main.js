/* =====================================
Template Name: 	Mediplus.
Author Name: Naimur Rahman
Website: http://wpthemesgrid.com/
Description: Mediplus - Doctor HTML Template.
Version:	1.1
========================================*/   
/*=======================================
[Start Activation Code]
=========================================
* Sticky Header JS
* Search JS
* Mobile Menu JS
* Hero Slider JS
* Testimonial Slider JS
* Portfolio Slider JS
* Clients Slider JS
* Single Portfolio Slider JS
* Accordion JS
* Nice Select JS
* Date Picker JS
* Counter Up JS
* Checkbox JS
* Right Bar JS
* Video Popup JS
* Wow JS
* Scroll Up JS
* Animate Scroll JS
* Stellar JS
* Google Maps JS
* Preloader JS
=========================================
[End Activation Code]
=========================================*/ 
(function($) {
    "use strict";
     $(document).on('ready', function() {
	
        jQuery(window).on('scroll', function() {
			if ($(this).scrollTop() > 200) {
				$('#header .header-inner').addClass("sticky");
			} else {
				$('#header .header-inner').removeClass("sticky");
			}
		});
		
		/*====================================
			Sticky Header JS
		======================================*/ 
		jQuery(window).on('scroll', function() {
			if ($(this).scrollTop() > 100) {
				$('.header').addClass("sticky");
			} else {
				$('.header').removeClass("sticky");
			}
		});
		
		$('.pro-features .get-pro').on( "click", function(){
			$('.pro-features').toggleClass('active');
		});
		
		/*====================================
			Search JS
		======================================*/ 
		$('.search a').on( "click", function(){
			$('.search-top').toggleClass('active');
		});
		
		/*====================================
			Mobile Menu
		======================================*/ 	
		$('.menu').slicknav({
			prependTo:".mobile-nav",
			duration: 300,
			closeOnClick:true,
		});
		
		/*===============================
			Hero Slider JS
		=================================*/ 
		$(".hero-slider").owlCarousel({
			loop:true,
			autoplay:true,
			smartSpeed: 500,
			autoplayTimeout:3500,
			singleItem: true,
			autoplayHoverPause:true,
			items:1,
			nav:true,
			navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
			dots:false,
		});

		/*===============================
			Testimonial Slider JS
		=================================*/ 
		$('.testimonial-slider').owlCarousel({
			items:3,
			autoplay:true,
			autoplayTimeout:4500,
			smartSpeed:300,
			autoplayHoverPause:true,
			loop:true,
			merge:true,
			nav:false,
			dots:true,
			responsive:{
				1: {
					items:1,
				},
				300: {
					items:1,
				},
				480: {
					items:1,
				},
				768: {
					items:2,
				},
				1170: {
					items:3,
				},
			}
		});
		
		/*===============================
			Portfolio Slider JS
		=================================*/ 
		$('.portfolio-slider').owlCarousel({
			autoplay:true,
			autoplayTimeout:4000,
			margin:15,
			smartSpeed:300,
			autoplayHoverPause:true,
			loop:true,
			nav:true,
			dots:false,
			responsive:{
				300: {
					items:1,
				},
				480: {
					items:2,
				},
				768: {
					items:2,
				},
				1170: {
					items:4,
				},
			}
		});
		
		/*=====================================
			Counter Up JS
		======================================*/
		$('.counter').counterUp({
			delay:20,
			time:2000
		});
		
		/*===============================
			Clients Slider JS
		=================================*/ 
		$('.clients-slider').owlCarousel({
			items:5,
			autoplay:true,
			autoplayTimeout:3500,
			margin:15,
			smartSpeed: 400,
			autoplayHoverPause:true,
			loop:true,
			nav:false,
			dots:false,
			responsive:{
				300: {
					items:1,
				},
				480: {
					items:2,
				},
				768: {
					items:3,
				},
				1170: {
					items:5,
				},
			}
		});
		
		/*====================================
			Single Portfolio Slider JS
		======================================*/ 
		$('.pf-details-slider').owlCarousel({
			items:1,
			autoplay:false,
			autoplayTimeout:5000,
			smartSpeed: 400,
			autoplayHoverPause:true,
			loop:true,
			merge:true,
			nav:true,
			dots:false,
			navText: ['<i class="icofont-rounded-left"></i>', '<i class="icofont-rounded-right"></i>'],
		});
		
		/*===================
			Accordion JS
		=====================*/ 
		$('.accordion > li:eq(0) a').addClass('active').next().slideDown();
		$('.accordion a').on('click', function(j) {
			var dropDown = $(this).closest('li').find('p');
			$(this).closest('.accordion').find('p').not(dropDown).slideUp(300);
			if ($(this).hasClass('active')) {
				$(this).removeClass('active');
			} else {
				$(this).closest('.accordion').find('a.active').removeClass('active');
				$(this).addClass('active');
			}
			dropDown.stop(false, true).slideToggle(300);
			j.preventDefault();
		});
		
		/*====================================
			Nice Select JS
		======================================*/ 	
		$('select').niceSelect();
		
		/*=====================================
			Date Picker JS
		======================================*/ 
		$( function() {
			$( "#datepicker" ).datepicker();
		} );
		
		
		
		/*===============================
			Checkbox JS
		=================================*/  
		$('input[type="checkbox"]').change(function(){
			if($(this).is(':checked')){
				$(this).parent("label").addClass("checked");
			} else {
				$(this).parent("label").removeClass("checked");
			}
		});
		
		/*===============================
			Right Bar JS
		=================================*/ 
		$('.right-bar .bar').on( "click", function(){
			$('.sidebar-menu').addClass('active');
		});
		$('.sidebar-menu .cross').on( "click", function(){
			$('.sidebar-menu').removeClass('active');
		});
		
		/*=====================
			Video Popup JS
		=======================*/ 
		$('.video-popup').magnificPopup({
			type: 'video',	
		});
		
		/*================
			Wow JS
		==================*/		
		var window_width = $(window).width();   
			if(window_width > 767){
            new WOW().init();
		}
	
		/*===================
			Scroll Up JS
		=====================*/
		$.scrollUp({
			scrollText: '<span><i class="fa fa-angle-up"></i></span>',
			easingType: 'easeInOutExpo',
			scrollSpeed: 900,
			animation: 'fade'
		}); 

		/*=======================
			Animate Scroll JS
		=========================*/
		$('.scroll').on("click", function (e) {
			var anchor = $(this);
				$('html, body').stop().animate({
					scrollTop: $(anchor.attr('href')).offset().top - 100
				}, 1000);
			e.preventDefault();
		});
		
		/*=======================
			Stellar JS
		=========================*/
		$.stellar({
		  horizontalOffset: 0,
		  verticalOffset: 0
		});

		/*====================
			Google Maps JS
		======================*/
		var map = new GMaps({
				el: '#map',
				lat: 23.011245,
				lng: 90.884780,
				scrollwheel: false,
			});
			map.addMarker({
				lat: 23.011245,
				lng: 90.884780,
				title: 'Marker with InfoWindow',
				infoWindow: {
				content: '<p>welcome to Medipro</p>'
			}
		
		});
	});
	
	/*====================
		Preloader JS
	======================*/
	$(window).on('load', function() {
		$('.preloader').addClass('preloader-deactivate');
	});
	
	
})(jQuery);


// Selección de elementos del DOM
// Selección de elementos del DOM
const areaDeslizable = document.getElementById("slider");
const manejadorDeslizable = areaDeslizable.querySelector(".manejador-deslizable");
const enlaceRedireccion = document.getElementById("redirect-link");

let deslizamientoActivo = false;
let anchoArea, anchoManejador, inicioX, posicionInicial, maxDesplazamiento;
let porcentajeRedireccion = 0.5; // 80% del recorrido
let intervaloAnimacion;

// Configura el deslizador y sus dimensiones
function inicializarDeslizador() {
  const dimensionesArea = areaDeslizable.getBoundingClientRect();
  anchoArea = dimensionesArea.width;
  anchoManejador = manejadorDeslizable.offsetWidth;
  maxDesplazamiento = anchoArea - anchoManejador; // Límite máximo de movimiento
  manejadorDeslizable.style.left = "5px"; // Restablece la posición inicial del manejador
}

// Inicia el deslizamiento (mousedown o touchstart)
function iniciarDeslizamiento(event) {
  deslizamientoActivo = true;
  inicioX = event.touches ? event.touches[0].clientX : event.clientX; // Posición inicial del dedo/mouse
  posicionInicial = parseInt(manejadorDeslizable.style.left || 5); // Guarda la posición actual
  manejadorDeslizable.style.transition = "none"; // Deshabilita la transición para el arrastre
  detenerAnimacion(); // Detén la animación automática mientras se arrastra
}

// Maneja el movimiento del deslizador
function moverDeslizador(event) {
  if (!deslizamientoActivo) return;

  const posicionActualX = event.touches ? event.touches[0].clientX : event.clientX;
  const desplazamiento = posicionActualX - inicioX; // Distancia movida desde el inicio
  let nuevaPosicion = posicionInicial + desplazamiento; // Calcula la nueva posición del manejador

  // Limitar el movimiento del manejador al área verde
  nuevaPosicion = Math.max(0, Math.min(nuevaPosicion, maxDesplazamiento));
  manejadorDeslizable.style.left = nuevaPosicion + "px";
}

// Finaliza el deslizamiento y verifica si se completó
function finalizarDeslizamiento() {
  if (!deslizamientoActivo) return;

  deslizamientoActivo = false;
  const posicionActual = parseInt(manejadorDeslizable.style.left || 0);

  // Calcula el límite del 80% del recorrido
  const limiteRedireccion = maxDesplazamiento * porcentajeRedireccion;

  // Si el manejador alcanza o supera el 80% del recorrido
  if (posicionActual >= limiteRedireccion) {
    areaDeslizable.classList.add("deslizado");
    manejadorDeslizable.style.left = maxDesplazamiento + "px"; // Asegura que el manejador quede al final
    setTimeout(() => {
      // Redirige usando el enlace de redirección
      enlaceRedireccion.click();
    }, 200); // Añade un pequeño retraso para una mejor experiencia visual
  } else {
    // Regresa el deslizador al inicio si no se completó
    manejadorDeslizable.style.transition = "left 0.3s ease";
    manejadorDeslizable.style.left = "5px";
    iniciarAnimacion(); // Reanuda la animación automática
  }
}

// Animación automática para incitar al usuario a deslizar
function animarManejador() {
  if (!deslizamientoActivo && !areaDeslizable.classList.contains("deslizado")) {
    manejadorDeslizable.style.transition = "left 0.5s ease-in-out";
    manejadorDeslizable.style.left = "10%";
    setTimeout(() => {
      manejadorDeslizable.style.left = "5px";
    }, 500); // Regresar después de 500ms
  }
}

// Iniciar la animación automática cada 7 segundos
function iniciarAnimacion() {
  detenerAnimacion(); // Evita duplicar intervalos
  intervaloAnimacion = setInterval(animarManejador, 2000);
}

// Detener la animación automática
function detenerAnimacion() {
  clearInterval(intervaloAnimacion);
}

// Agrega eventos al manejador
function agregarEventos() {
  manejadorDeslizable.addEventListener("mousedown", iniciarDeslizamiento);
  manejadorDeslizable.addEventListener("touchstart", iniciarDeslizamiento);

  document.addEventListener("mousemove", moverDeslizador);
  document.addEventListener("touchmove", moverDeslizador);

  document.addEventListener("mouseup", finalizarDeslizamiento);
  document.addEventListener("touchend", finalizarDeslizamiento);
}

// Inicializar el deslizador
inicializarDeslizador();
agregarEventos();
iniciarAnimacion(); // Comenzar la animación automática

// Recalcular dimensiones si se cambia el tamaño de la ventana
window.addEventListener("resize", inicializarDeslizador);


/* ESTA CHAMBONADA ES PARA POCISIONAR MEJOR EL LOGO */
