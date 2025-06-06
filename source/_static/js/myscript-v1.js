// Function to sort version numbers in descending order (newer versions first)
function sortVersions(versions) {
    return versions.sort((a, b) => {
        const [majorA, minorA] = a.split('.').map(Number);
        const [majorB, minorB] = b.split('.').map(Number);

        if (majorA !== majorB) {
            return majorB - majorA;
        }
        return minorB - minorA;
    });
}

// Function to parse a version string to an object with major and minor properties
function parseVersion(v) {
    if (v === 'all') return { major: 0, minor: 0 };
    const [major, minor] = v.split('.').map(Number);
    return { major, minor };
}

$(document).ready(function () {
    // Function to set the custom theme attribute based on the current theme
    function setCustomTheme(theme) {
        $('body').attr('data-custom-theme', theme);
    }

    // Check for a manually set theme
    var manualTheme = $('body').attr('data-theme');
    if (manualTheme === 'dark' || manualTheme === 'light') {
        // If manually set to 'dark' or 'light', use that value
        setCustomTheme(manualTheme);
    } else {
        // If 'data-theme' is 'auto' or not set, use prefers-color-scheme to determine the theme
        if (
            window.matchMedia &&
            window.matchMedia('(prefers-color-scheme: dark)').matches
        ) {
            setCustomTheme('dark');
        } else {
            setCustomTheme('light');
        }
    }

    // Listen for changes in the theme preference
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
        // Only update the theme based on prefers-color-scheme if 'data-theme' is 'auto' or not set
        if (
            !$('body').attr('data-theme') ||
            $('body').attr('data-theme') === 'auto'
        ) {
            setCustomTheme(e.matches ? 'dark' : 'light');
        }
    });

    // Optional: Listen for manual changes to the data-theme attribute, e.g., through a theme switcher
    $('.theme-toggle').on('click', function () {
        var currentTheme = $('body').attr('data-theme');
        // Toggle theme only if not set to 'auto'
        if (currentTheme !== 'auto') {
            var newTheme = currentTheme === 'dark' ? 'dark' : 'light';
            $('body').attr('data-theme', newTheme); // Update the data-theme attribute
            setCustomTheme(newTheme); // Update the data-custom-theme attribute
        }
    });

    $('header .links__icon').on('click', function () {
        $('header .header__searchbar').hide();
        $('header .header__links').slideToggle();
    });

    $('.search__icon').on('click', function () {
        $('header .header__links').hide();
        $('header .header__searchbar').slideToggle(400, function () {
            if ($(this).is(':visible')) {
                $(this).find('input[type=text]').focus();
            }
        });
    });

    if ($('.wy-menu-vertical li.current>a').length) {
        var sidebarScrollPosition = $('.wy-menu-vertical li.current>a').offset()
            .top;
        $('.wy-side-scroll').scrollTop(sidebarScrollPosition - 120);
    }

    // Notification Banner

    // Fallback for when a notification CTA expires
    const dateInFuture = (value) =>
        new Date().getTime() <= new Date(value).getTime();
    const expiryDate = '2024-10-31T00:00:00-0500';
    // 12am EST
    const fallback_url =
        'https://docs.mattermost.com/about/maximize-microsoft-investments.html';
    const fallback_text = 'Maximize your Microsoft investments  »';

    if (!dateInFuture(expiryDate)) {
        if ($('.notification-bar').length) {
            $('.notification-bar__link').attr('href', fallback_url);
            $('.notification-bar__link').text(fallback_text);
        }
    }

    // NOTE: Change the notification_banner_key to something unique everytime it changes
    // So it will show up for new announcements
    // Keep "mm_notification_banner__" at the beginning of the key
    // Add system to clean out storage items that are no longer needed
    let notification_banner_key = 'mm_notification_banner__v10-mst-sept';
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

    $('body').on('click', '.notification-bar__close', function () {
        $('.notification-bar').remove();
        $('body').removeClass('with-notification');
        localStorage.setItem(notification_banner_key, false);
    });

    // Navigation
    const hamburger = document.getElementById('hamburger');
    const subMenus = document.querySelectorAll('.site-nav__hassubnav a');

    let multiEventSingleHandler = (elem, events, handler, use_capture) => {
        events.forEach((ev) => {
            elem.addEventListener(
                ev,
                handler,
                typeof use_capture === 'undefined' ? false : use_capture
            );
        });
    };

    let clickTouch = (elem, handler, use_capture) => {
        multiEventSingleHandler(
            elem,
            ['click', 'touch'],
            handler,
            typeof use_capture === 'undefined' ? false : use_capture
        );
    };

    subMenus.forEach((snav) => {
        clickTouch(
            snav,
            () => {
                snav.parentElement.classList.toggle('is-active');
            },
            false
        );
    });

    clickTouch(hamburger, () => {
        hamburger.classList.toggle('is-active');
        document.body.classList.toggle('nav-open');
        document.getElementById('navigation').classList.toggle('nav-is-active');
    });

    // Remove classes to close the nav if screen size is larger than 992px
    function closeNav() {
        if (window.innerWidth > 992) {
            document.body.classList.remove('nav-open');
            document.getElementById('navigation').classList.remove('nav-is-active');
            hamburger.classList.remove('is-active');
        }
    }

    closeNav();

    $(window).on('resize', closeNav);

});
