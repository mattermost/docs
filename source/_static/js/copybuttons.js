// Installation Copy Buttons
Array.from(
    document.querySelectorAll('.mm-code-copy')
).map(clicker => {
    const clickerInput = clicker.querySelector('.mm-code-copy__text');
    const clickerTriggers = clicker.querySelectorAll('.mm-code-copy__trigger');
    const clickerNotice = clicker.querySelector('.mm-code-copy__copied-notice');
    const copyText = clickerInput.innerText;

    clickerTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            // The Clipboard API is only available in secure contexts (HTTPS), in some or all supporting browsers.
            // https://developer.mozilla.org/en-US/docs/Web/API/Clipboard
            // So this will not work on our current preview sites
            // Building locally with `make livehtml` will work
            clickerNotice.classList.add('show');

            const copyCommand = clicker.dataset.clickCommand;
            const copyMethod = clicker.dataset.clickMethod;
            const copyEl = trigger.dataset.clickEl;

            setTimeout(function () {
                clickerNotice.classList.remove("show");
            }, 1000);

            navigator.clipboard.writeText(copyText).then(() => {

                dataLayer.push({
                    event: 'copy.installation',
                    installLabel: `${copyMethod} - ${copyCommand}`,
                    copyAction: copyEl
                });

            });
        });
    });

});
