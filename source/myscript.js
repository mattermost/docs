$(document).ready(function(){
	var thermometerHtml = "<div class='c-thermometer'><div class='c-thermometer__trigger'><div>🙂</div></div><div class='c-thermometer__popup'><div class='c-thermometer__close'>×</div><p class='c-thermometer__paragraph'>How would you rate this page?</p> <div class='c-thermometer__emojis'> <a href='javascript:void(0)' onClick=\"ga('send', 'event', {'sendTo':'UA-67846571-2', eventCategory: 'Feedback', eventAction: 'Click', eventLabel: 'Excellent', eventValue: 3});\"> <span class='c-thermometer__emoji'>😀</span> <p>Excellent</p> </a> <a href='javascript:void(0)' onClick=\"ga('send', 'event', {'sendTo':'UA-67846571-2', eventCategory: 'Feedback', eventAction: 'Click', eventLabel: 'Average', eventValue: 2});\"> <span class='c-thermometer__emoji'>😐</span> <p>Average</p> </a> <a href='javascript:void(0)' onClick=\"ga('send', 'event', {'sendTo':'UA-67846571-2', eventCategory: 'Feedback', eventAction: 'Click', eventLabel: 'Poor', eventValue: 1});\"> <span class='c-thermometer__emoji'>🙁</span> <p>Poor</p> </a> </div></div></div>";
	$('body').append(thermometerHtml);

	$('header .links__icon').on('click', function (){
		$("header .header__searchbar").hide();
		$("header .header__links").slideToggle();
	});

	$('header .search__icon').on('click', function (){
		$("header .header__links").hide();
		$("header .header__searchbar").slideToggle(400, function() {
			if($(this).is(':visible')) {
				$(this).find("input[type=text]").focus();
			}
		});
	});

	if($('.wy-menu-vertical li.current>a').length){
		var sidebarScrollPosition = $('.wy-menu-vertical li.current>a').offset().top;
		$('.wy-side-scroll').scrollTop(sidebarScrollPosition-120);
	}

	$('body').on('click', '.c-thermometer__emojis a', function(){
		$(this).parent().hide();
	});

	$('body').on('click', function(){
		$('.c-thermometer__popup').hide();
	});

	$('body').on('click', '.c-thermometer__close', function(){
		$(this).parent().hide();
	});

	$('body').on('click', '.c-thermometer__popup', function(e){
		e.stopImmediatePropagation();
	});

	$('body').on('click', '.c-thermometer__trigger', function(e){
		e.stopImmediatePropagation();
		$('.c-thermometer__popup').fadeToggle();
	});

    $('body').on('click', '.c-thermometer__emojis a', function(){
		$('.c-thermometer__paragraph').text('Thank you for submitting your rating.');
		setTimeout(() => {
			$('.c-thermometer').fadeOut(() => {
				$('.c-thermometer').remove();
			});
		}, 3000);
	});

});
