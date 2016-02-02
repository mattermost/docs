$(document).ready(function(){

	$('header .links__icon').on('click', function (){
		$(this).next().slideToggle();
	});

	var sidebarScrollPosition = $('.wy-menu-vertical li.current>a').offset().top;
	$('.wy-side-scroll').scrollTop(sidebarScrollPosition-100);

	var centerScroll = function(){
		setTimeout(function(){
			var centerScrollPosition = $('.wy-nav-content-wrap').scrollTop();
			$('.wy-nav-content-wrap').scrollTop(centerScrollPosition-70);
		},100);
	};

	$('.wy-menu-vertical li.current li').on('click', function(){
		centerScroll();
	});

	centerScroll();

});