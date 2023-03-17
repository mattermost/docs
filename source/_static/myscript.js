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
				<h3>Tell us more!</h3> \
				<p>Your feedback helps us improve the Mattermost product documentation.</br> \
				<p><b>How can we make this page more helpful? </b></br> \
				</br> \
				<textarea maxlength='186' rows='4' placeholder='Share your feedback here'></textarea> \
					<div class='c-thermometer-modal__textarea-footer'> \
						<div></div> \
						<div class='c-thermometer-modal__counter'> \
							<span>0</span>/186	\
						</div> \
					</div> \
					<p>Have a feature request? <a href='https://mattermost.com/suggestions' target='blank'> Share it here.</a></p> \
					<p>Having issues? <a href='https://community.mattermost.com' target='blank'> Join our Community server. </a></p> \
					<div class='c-thermometer-modal__footer'> \
						<button class='btn btn-link'>Cancel</button> \
						<button class='btn btn-primary'>Submit</button> \
					</div> \
				</div> \
			</div> \
		</div> \
		<div class='c-thermometer'> \
			<div class='c-thermometer__trigger'> \
				<p class='c-thermometer__paragraph'>Did you find what you were looking for?</p> \
				<div class='c-thermometer__emojis'> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='Yes'> \
						<span class='c-thermometer__emoji'>😀</span> \
						<p>Yes</p> \
					</a> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='Somewhat'> \
						<span class='c-thermometer__emoji'>😐</span> \
						<p>Mostly</p> \
					</a> \
					<a href='javascript:void(0);' class='rate-this-page-action' data-rating='No'> \
						<span class='c-thermometer__emoji'>🙁</span> \
						<p>No!</p> \
					</a> \
				</div> \
			</div> \
		</div>";

	$('body footer').append(thermometerHtml);

	$('header .links__icon').on('click', function () {
		$("header .header__searchbar").hide();
		$("header .header__links").slideToggle();
	});

	$('.search__icon').on('click', function () {
		$("header .header__links").hide();
		$("header .header__searchbar").slideToggle(400, function () {
			if ($(this).is(':visible')) {
				$(this).find("input[type=text]").focus();
			}
		});
		// document.getElementById('hamburger').classList.remove('is-active');
        // document.body.classList.remove('nav-open');
        // document.getElementById('navigation').classList.remove('active');
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

				if (typeof (rudderanalytics) !== 'undefined') {
					rudderanalytics.track("feedback_submitted", { label: rating, rating: eventValue, feedback: currentString });
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
	
	// Notification Banner

	// NOTE: Change the notification_banner_key to something unique everytime it changes
	// So it will show up for new announcements
	// Keep "mm_notification_banner__" at the beginning of the key
	// Add system to clean out storage items that are no longer needed
	const notification_banner_key = 'mm_notification_banner__mst';

	if (localStorage.getItem(notification_banner_key) === null) {
		localStorage.setItem(notification_banner_key, true);
		$('.notification-bar').addClass('flex');
		$('body').addClass('with-notification');
	} else {
		const banner_state = localStorage.getItem(notification_banner_key);

		if (banner_state == 'false') {
			$('.notification-bar').remove();
			$('body').removeClass('with-notification');
		} else {
			$('body').addClass('with-notification');
		}
	}

	$('body').on('click', '.notification-bar__close', function(){
		$('.notification-bar').remove();
		$('body').removeClass('with-notification');
		localStorage.setItem(notification_banner_key, false);
	});

	// Installation Copy Buttons
	Array.from(
		document.querySelectorAll('.mm-code-copy')
	).map(clicker => {
		const clickerInput = clicker.querySelector('.mm-code-copy__text');
		const clickerTrigger = clicker.querySelector('.mm-code-copy__copy-trigger');
		const copyText = clickerInput.innerText;
		clickerTrigger.addEventListener('click', (e) => {
			e.preventDefault();
			navigator.clipboard.writeText(copyText).then(() => {
				clicker.querySelector('.mm-code-copy-copied').classList.add('show');

				const copyCommand = clicker.dataset.clickCommand;
				const copyMethod = clicker.dataset.clickMethod;
				dataLayer.push({
					event: 'copy.installation',
					installMethod: copyMethod,
					installCommand: copyCommand
				});

				setTimeout(function () {
					clicker.querySelector('.mm-code-copy-copied').classList.remove("show");
				}, 1000);
			});
		});
	});

});

// Redesign - Navigation
document.addEventListener("DOMContentLoaded", function(event) {     
    const hamburger = document.getElementById('hamburger');
    const subMenus = document.querySelectorAll('.site-nav__hassubnav a');

    let multiEventSingleHandler = (elem, events, handler, use_capture) => {
        events.forEach(ev => {
            elem.addEventListener(ev, handler, typeof(use_capture) === 'undefined' ? false : use_capture);
        });
    }

    let clickTouch = (elem, handler, use_capture) => {
        multiEventSingleHandler(elem, ['click', 'touch'], handler, typeof(use_capture) === 'undefined' ? false : use_capture);
    }

    subMenus.forEach(snav => {
        clickTouch(snav, () => {
            snav.parentElement.classList.toggle('is-active');
        }, false);
    });

    clickTouch(hamburger, () => {
        hamburger.classList.toggle('is-active');
        document.body.classList.toggle('nav-open');
        document.getElementById('navigation').classList.toggle('active');
    });
});
