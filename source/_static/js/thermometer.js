/* Mattermost documentation feedback widget */
/* Modified to remove Rudderstack integration and freeform feedback modal */

// Adapted from https://youmightnotneedjquery.com/#on
const jqueryOn = (el, eventName, eventHandler, selector) => {
    if (selector) {
        const wrappedHandler = (e) => {
            if (!e.target) return;
            const el = e.target.closest(selector);
            if (el) {
                eventHandler.call(el, e);
            }
        };
        el.addEventListener(eventName, wrappedHandler);
        return wrappedHandler;
    } else {
        const wrappedHandler = (e) => {
            eventHandler.call(el, e);
        };
        el.addEventListener(eventName, wrappedHandler);
        return wrappedHandler;
    }
};

// Adapted from https://youmightnotneedjquery.com/#ready
const jqueryReady = (fn) => {
    if (document.readyState !== 'loading') {
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
};

jqueryReady(() => {
    let eventValue = 0;
    let rating = '';

    // Handle rating selection - now sends analytics immediately
    jqueryOn(
        document.body,
        'click',
        (evt) => {
            if (evt.target) {
                // Prevent default anchor behavior (jumping to top of page)
                evt.preventDefault();
                
                let targetEl = evt.target;
                console.debug('clicked a rating');
                if (
                    targetEl.classList.contains('c-thermometer__emoji') ||
                    targetEl.classList.contains('c-thermometer__emoji_action')
                ) {
                    targetEl = targetEl.parentElement;
                }
                
                // Remove previous selection
                document.querySelectorAll('a.rate-this-page-action').forEach((elt) => {
                    elt.classList.remove('selected');
                });
                
                // Add selection to current element
                targetEl.classList.add('selected');
                
                const dataRating = targetEl.getAttribute('data-rating');
                if (dataRating !== null) {
                    rating = dataRating;
                    console.debug(`rating=${rating}`);
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
                    
                    // Send Google Analytics event immediately (no modal required)
                    if (eventValue > 0) {
                        console.debug(`Sending GA event: ${rating} (${eventValue})`);
                        const dataLayer = window.dataLayer || [];
                        dataLayer.push({
                            event: 'rateThisPage',
                            eventLabel: rating,
                            eventValue: eventValue,
                            // No eventFeedback since freeform feedback is disabled
                        });
                    }
                    
                    // Show thank you popup
                    document.querySelectorAll('.c-thermometer-popup').forEach((elt) => {
                        console.debug('show popup');
                        elt.style.display = 'block';
                    });
                    
                    // Hide popup after 3 seconds
                    setTimeout(() => {
                        document.querySelectorAll('.c-thermometer-popup').forEach((elt) => {
                            console.debug('hide popup');
                            elt.style.display = 'none';
                        });
                    }, 3000);
                } else {
                    eventValue = 0;
                    console.debug('dataRating was null');
                }
            }
        },
        '.c-thermometer__emojis a.rate-this-page-action'
    );

    // All modal-related code removed due to Rudderstack decommissioning

    jqueryOn(
        document.body,
        'click',
        (evt) => {
            if (evt.target) {
                console.debug('hide popup from close button');
                evt.target.parentNode.style.display = 'none';
            }
        },
        '.c-thermometer-popup__close'
    );

    // Prevent event propagation for popup
    jqueryOn(
        document.body,
        'click',
        (evt) => {
            console.debug('stop event prop from popup');
            evt.stopImmediatePropagation();
        },
        '.c-thermometer-popup'
    );

    // Prevent event propagation for trigger
    jqueryOn(
        document.body,
        'click',
        (evt) => {
            console.debug('stop event prop from trigger');
            evt.stopImmediatePropagation();
        },
        '.c-thermometer__trigger'
    );

    console.debug('thermometer.js loaded - freeform feedback disabled, GA-only ratings enabled');
});
