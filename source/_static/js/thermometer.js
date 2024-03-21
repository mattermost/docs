/* Mattermost documentation feedback widget */

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
// Adapted from https://youmightnotneedjquery.com/#parents
const jqueryParents = (el, selector) => {
    const parents = [];
    while ((el = el.parentNode) && el !== document) {
        if (!selector || el.matches(selector)) parents.push(el);
    }
    return parents;
};
// Adapted from https://youmightnotneedjquery.com/#val
const jqueryVal = (el) => {
    if (el.options && el.multiple) {
        return el.options
            .filter((option) => option.selected)
            .map((option) => option.value);
    } else {
        return el.value;
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

    jqueryOn(
        document.body,
        'click',
        (evt) => {
            if (evt.target) {
                console.debug('set selected from emoji anchor');
                evt.target.classList.add('selected');
            }
        },
        '.c-thermometer__emojis a'
    );

    jqueryOn(
        document.body,
        'click',
        (evt) => {
            if (evt.target) {
                let targetEl = evt.target;
                console.debug('clicked a rating');
                if (
                    targetEl.classList.contains('c-thermometer__emoji') ||
                    targetEl.classList.contains('c-thermometer__emoji_action')
                ) {
                    targetEl = targetEl.parentElement;
                }
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
                } else {
                    eventValue = 0;
                    console.debug('dataRating was null');
                }
                document
                    .querySelectorAll('.c-thermometer-modal__container')
                    .forEach((elt) => {
                        console.debug('show container');
                        elt.style.visibility = 'visible';
                    });
            }
        },
        '.c-thermometer__emojis a.rate-this-page-action'
    );

    jqueryOn(
        document.body,
        'click',
        (evt) => {
            if (evt.target) {
                if (evt.target.classList.contains('btn-link')) {
                    console.debug('target has class "btn-link"');
                    jqueryParents(
                        evt.target,
                        '.c-thermometer-modal__container'
                    ).forEach((parentElt) => {
                        console.debug('hide container');
                        parentElt.style.visibility = 'hidden';
                    });
                    document
                        .querySelectorAll('a.rate-this-page-action')
                        .forEach((elt) => {
                            console.debug('remove selected from links');
                            elt.classList.remove('selected');
                        });
                    document
                        .querySelectorAll(
                            '.c-thermometer-modal__container textarea'
                        )
                        .forEach((elt) => {
                            console.debug('set value to empty');
                            elt.value = '';
                        });
                    document
                        .querySelectorAll('.c-thermometer-modal__counter span')
                        .forEach((elt) => {
                            elt.innerHTML = '0';
                        });
                    return;
                }
                let currentValue = '';
                const textareas = document.querySelectorAll(
                    '.c-thermometer-modal__container textarea'
                );
                if (textareas && textareas[0]) {
                    currentValue = jqueryVal(textareas[0]);
                }
                console.debug(
                    `eventValue=${eventValue}, currentValue=${currentValue}`
                );
                if (currentValue !== '' && eventValue > 0) {
                    // Google Analytics event
                    const dataLayer = window.dataLayer || [];
                    dataLayer.push({
                        event: 'rateThisPage',
                        eventLabel: rating,
                        eventValue: eventValue,
                        eventFeedback: currentValue,
                    });
                    // Rudderstack event
                    if (typeof rudderanalytics !== 'undefined') {
                        rudderanalytics.track('feedback_submitted', {
                            label: rating,
                            rating: eventValue,
                            feedback: currentValue,
                        });
                    }
                }
                jqueryParents(
                    evt.target,
                    '.c-thermometer-modal__container'
                ).forEach((parentElt) => {
                    console.debug('hide container');
                    parentElt.style.visibility = 'hidden';
                });
                document
                    .querySelectorAll(
                        '.c-thermometer-modal__container textarea'
                    )
                    .forEach((elt) => {
                        console.debug('set value to empty');
                        elt.value = '';
                    });
                document
                    .querySelectorAll('.c-thermometer-modal__counter span')
                    .forEach((elt) => {
                        elt.innerHTML = '0';
                    });
                document
                    .querySelectorAll('a.rate-this-page-action')
                    .forEach((elt) => {
                        console.debug('remove selected from links');
                        elt.classList.remove('selected');
                    });
                document
                    .querySelectorAll('.c-thermometer-popup')
                    .forEach((elt) => {
                        console.debug('show popup');
                        elt.style.display = 'block';
                    });
                setTimeout(() => {
                    document
                        .querySelectorAll('.c-thermometer-popup')
                        .forEach((elt) => {
                            console.debug('hide popup');
                            elt.style.display = 'none';
                        });
                }, 3000);
            }
        },
        '.c-thermometer-modal__footer .btn'
    );

    document
        .querySelectorAll('.c-thermometer-modal__container textarea')
        .forEach((elt) => {
            jqueryOn(elt, 'keyup', (evt) => {
                if (evt.target) {
                    const currentVal = String(jqueryVal(evt.target));
                    document
                        .querySelectorAll('.c-thermometer-modal__counter span')
                        .forEach((elt) => {
                            elt.innerHTML = currentVal.length.toString();
                        });
                }
            });
        });

    // document.body.addEventListener('click', evt => {
    //     document.querySelectorAll('.c-thermometer-popup').forEach(elt => {
    //         console.debug('hide popup from body click');
    //         elt.style.visibility = 'hidden';
    //     });
    // });

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

    jqueryOn(
        document.body,
        'click',
        (evt) => {
            console.debug('stop event prop from popup');
            evt.stopImmediatePropagation();
        },
        '.c-thermometer__popup'
    );

    jqueryOn(
        document.body,
        'click',
        (evt) => {
            console.debug('stop event prop from trigger');
            evt.stopImmediatePropagation();
        },
        '.c-thermometer__trigger'
    );

    console.debug('jqueryReady finished');
});
