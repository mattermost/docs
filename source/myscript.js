$(document).ready(function(){

	$('header .links__icon').on('click', function (){
		$(this).next().slideToggle();
	});

	var sidebarScrollPosition = $('.wy-menu-vertical li.current>a').offset().top;
	$('.wy-side-scroll').scrollTop(sidebarScrollPosition-100);


});