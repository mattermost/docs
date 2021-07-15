$(document).ready(function () {
	// Init GTM dataLayer for Analytics
	var dataLayer = window.dataLayer || [];
	var eventValue = 0;
	var rating = '';


	var thermometerHtml =
		" <div class='c-thermometer-popup'> \
			<div class='c-thermometer-popup__close'>×</div> \
			<svg width='19' height='19' viewBox='0 0 19 19' fill='none' xmlns='http://www.w3.org/2000/svg'><circle cx='9.5' cy='9.5' r='9.5' fill='#166DE0' fill-opacity='0.08'/><g clip-path='url(#clip0)'><path d='M15.0172 6.43306L7.81719 13.6331L4.51959 10.3211L5.36919 9.48586L7.81719 11.9339L14.1676 5.58346L15.0172 6.43306Z' fill='#166DE0'/></g><defs><clipPath id='clip0'><rect width='13.4118' height='11.1765' fill='white' transform='translate(2.79395 3.35303)'/></clipPath></defs></svg> \
			<h5>Thank you!</h5> \
			<p>We appreciate your feedback.</p> \
		</div> \
		<div class='c-thermometer-modal__container'> \
			<div> \
				<div class='c-thermometer-modal__content'> \
					<h3>Share your thoughts</h3> \
					<p>Your feedback helps us improve. Share your thoughts with us here or join the DGW - Documentation Working Group channel on our Community server.</p> \
					<textarea maxlength='186' rows='4' placeholder='Leave your feedback here'></textarea> \
					<div class='c-thermometer-modal__textarea-footer'> \
						<div></div> \
						<div class='c-thermometer-modal__counter'> \
							<span>0</span>/186	\
						</div> \
					</div> \
					<div class='c-thermometer-modal__footer'> \
						<button class='btn btn-link'>Cancel</button> \
						<button class='btn btn-primary'>Submit</button> \
					</div> \
				</div> \
			</div> \
		</div> \
		<div class='c-thermometer'> \
			<div class='c-thermometer__trigger'> \
				<p class='c-thermometer__paragraph'>Was this page helpful?</p> \
				<div class='c-thermometer__emojis'> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='Yes'> \
						<span class='c-thermometer__emoji'>😀</span> \
						<p>Yes</p> \
					</a> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='Somewhat'> \
						<span class='c-thermometer__emoji'>😐</span> \
						<p>Somewhat</p> \
					</a> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='No'> \
						<span class='c-thermometer__emoji'>🙁</span> \
						<p>No</p> \
					</a> \
				</div> \
			</div> \
		</div>";

	$('body footer').append(thermometerHtml);

	$('header .links__icon').on('click', function () {
		$("header .header__searchbar").hide();
		$("header .header__links").slideToggle();
	});

	$('header .search__icon').on('click', function () {
		$("header .header__links").hide();
		$("header .header__searchbar").slideToggle(400, function () {
			if ($(this).is(':visible')) {
				$(this).find("input[type=text]").focus();
			}
		});
	});

	if ($('.wy-menu-vertical li.current>a').length) {
		var sidebarScrollPosition = $('.wy-menu-vertical li.current>a').offset().top;
		$('.wy-side-scroll').scrollTop(sidebarScrollPosition - 120);
	}

	$('body').on('click', '.c-thermometer__emojis a', function () {
		$(this).addClass('selected');
	});

	$('body').on('click', '.c-thermometer-modal__footer .btn', function () {
		if ($(this).hasClass('btn-link')) {
			$(this).parents('.c-thermometer-modal__container').fadeOut();
			$('a.rate-this-page-action').removeClass('selected');
			$('.c-thermometer-modal__container textarea').val('');
		} else {
			var currentString = $(".c-thermometer-modal__container textarea").val()

			if (eventValue > 0) {
				// Submit DataLayer Event
				dataLayer.push({
					event: 'rateThisPage',
					eventLabel: rating,
					eventValue: eventValue,
					eventFeedback: currentString
				});

				if (typeof(rudderanalytics) !== 'undefined') {
					rudderanalytics.track("feedback_submitted", { label: rating, rating: eventValue, feedback: currentString});
				}

				$(this).parents('.c-thermometer-modal__container').fadeOut(() => {
					$('.c-thermometer-modal__container').remove();
				});
				$('.c-thermometer__emojis').addClass('pointer-events-none');

				$('.c-thermometer-popup').fadeIn();

				setTimeout(() => {
					$('.c-thermometer-popup').fadeOut('fast');
				}, 3000)
			}
		}
	});

	$(".c-thermometer-modal__container textarea").on('keyup', function (event) {
		var currentString = $(this).val();
		$(".c-thermometer-modal__counter span").html(currentString.length);
	});

	$('body').on('click', function () {
		$('.c-thermometer__popup').hide();
	});

	$('body').on('click', '.c-thermometer-popup__close', function () {
		$(this).parent().fadeOut('fast');
	});

	$('body').on('click', '.c-thermometer__popup', function (e) {
		e.stopImmediatePropagation();
	});

	$('body').on('click', '.c-thermometer__trigger', function (e) {
		e.stopImmediatePropagation();
	});

	// Click Event for Ratings
	$('body').on('click', '.c-thermometer__emojis a.rate-this-page-action', function () {
		var click_elem = $(this);
		click_elem.addClass('selected');

		// UX Update

		$('.c-thermometer-modal__container').fadeIn();

		setTimeout(() => {
			// $('.c-thermometer').fadeOut(() => {
			// 	$('.c-thermometer').remove();
			// });
		}, 3000);

		// Prepare DataLayer Vars
		rating = click_elem.attr('data-rating');

		console.log(rating);

		switch (rating) {
			case 'Yes':
				eventValue = 3;
				break;
			case 'Somewhat':
				eventValue = 2;
				break;
			case 'No':
				eventValue = 1;
				break;
		}
	});

});
