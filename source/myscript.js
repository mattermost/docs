$(document).ready(function(){
	// Init GTM dataLayer for Analytics
	var dataLayer = window.dataLayer || [];

	var thermometerHtml =
		"<div class='c-thermometer'> \
			<div class='c-thermometer__trigger'> \
				<div>🙂</div> \
			</div> \
			<div class='c-thermometer__popup'> \
				<div class='c-thermometer__close'>×</div> \
				<p class='c-thermometer__paragraph'>How would you rate this page?</p> \
				<div class='c-thermometer__emojis'> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='Excellent'> \
						<span class='c-thermometer__emoji'>😀</span> \
						<p>Excellent</p> \
					</a> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='Average'> \
						<span class='c-thermometer__emoji'>😐</span> \
						<p>Average</p> \
					</a> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='Poor'> \
						<span class='c-thermometer__emoji'>🙁</span> \
						<p>Poor</p> \
					</a> \
				</div> \
			</div> \
		</div>";

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

	$('body').on('click', '.notification-bar__close', function(){
		$(this).parents('.notification-bar').remove();
		$('header').removeClass('with-notification');
		$('.wy-grid-for-nav').addClass('no-notification');
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

	// Click Event for Ratings
    $('body').on('click', '.c-thermometer__emojis a.rate-this-page-action', function(){
		var click_elem = $(this);

		// UX Update
		$('.c-thermometer__paragraph').text('Thank you for submitting your rating.');
		setTimeout(() => {
			$('.c-thermometer').fadeOut(() => {
				$('.c-thermometer').remove();
			});
		}, 3000);

		// Prepare DataLayer Vars
		var rating = click_elem.attr('data-rating');
		var event_value = 0;
		switch (rating) {
			case 'Excellent':
				event_value = 3;
				break;
			case 'Average':
				event_value = 2;
				break;
			case 'Poor':
				event_value = 1;
				break;
		}

		if (event_value > 0) {
			// Submit DataLayer Event
			dataLayer.push({
				event: 'rateThisPage',
				eventLabel: rating,
				eventValue: event_value
			});
		}
	});

});
