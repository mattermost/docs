$(document).ready(function(){

	$('header .links__icon').on('click', function (){
		$(this).next().slideToggle();
	});

	if($('.wy-menu-vertical .toctree-l3.current').length){
		var sidebarScrollPosition = $('.wy-menu-vertical .toctree-l3.current').offset().top;
		$('.wy-side-scroll').scrollTop(sidebarScrollPosition-120);
	}

	var centerScroll = function(position){
		setTimeout(function(){
			var centerScrollPosition = $('.wy-nav-content-wrap').scrollTop();
			$('.wy-nav-content-wrap').scrollTop(centerScrollPosition-position);
		},100);
	};

	$('.wy-menu-vertical li.current li').on('click', function(){
		centerScroll(80);
	});

	centerScroll(75);

	if(!$('.toctree-l1').hasClass('current')){
		$('.wy-body-for-nav').addClass('hidden-nav');
	}

});