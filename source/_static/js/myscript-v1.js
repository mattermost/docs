$(document).ready(function () {
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

	// Notification Banner

	// Fallback for when a notification CTA expires - ie. webinar happens
	const dateInFuture = (value) => new Date().getTime() <= new Date(value).getTime();
    const expiryDate = '2024-11-01T00:00:00-0500';
    // 2023-11-01 @ 12am EST
    const fallback_url = 'https://mattermost.com/solutions/mattermost-for-microsoft-teams/';
    const fallback_text = 'Learn more about Mattermost for Microsoft Teams »';

    if (!dateInFuture(expiryDate)) {
        if ($(".notification-bar").length) {
            // $('.notification-bar').remove();
            // $('body').removeClass('with-notification');
            $('.notification-bar__link').attr('href', fallback_url);
            $('.notification-bar__link').text(fallback_text);
        }
    }

	// NOTE: Change the notification_banner_key to something unique everytime it changes
	// So it will show up for new announcements
	// Keep "mm_notification_banner__" at the beginning of the key
	// Add system to clean out storage items that are no longer needed
	let notification_banner_key = 'mm_notification_banner__inc-23';
	if (!dateInFuture(expiryDate)) {
		notification_banner_key = 'mm_notification_banner__fallback-mst';
	}

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

	// Navigation
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
