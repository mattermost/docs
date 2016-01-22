$(document).ready(function(){

	$('header .links__icon').on('click', function (){
		$(this).next().slideToggle();
	});

	var scrollPosition;

	var scrollFunction = function(){
		scrollPosition = $(window).scrollTop();
		if(scrollPosition > 60){
			$('.wy-side-nav-search').addClass('scrolled');
		}
		else {
			$('.wy-side-nav-search').removeClass('scrolled');
		}
	}

	scrollFunction();

	$(window).scroll(function(){
		scrollFunction();
	});


});