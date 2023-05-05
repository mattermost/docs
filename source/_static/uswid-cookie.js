// USWID Cookie
// In-product link-outs have u/sids in the URL
// This cookie will be used to track those click identifiers
// So they can be attached to form submissions
// A cookie of the same name is set on mm.com

const mm_id_cookie = 'mm_uswid';
	
const uswid_controller = {
    enabled: false,
    testing_local: true, //set this to true if you are testing locally with no https protocol
    root_domain: window.location.hostname, 
    // root_domain: 'mattermost.com', 

    ACCEPTED_PARAM_KEYS: [
        'uid',
        'sid',
    ],

    Init: () => {
        // console.log('Init - ' + uswid_controller.root_domain);
        uswid_controller.enabled = true; 
        uswid_controller.SetMMUSWIDCookie();
    },

    DeleteMMUSWIDCookie: () => {
        if (uswid_controller.enabled) {
            document.cookie = `${mm_id_cookie}=; Expires=Thu, 01 Jan 1970 00:00:00 GMT; Domain=.${uswid_controller.root_domain}; Path=/;`;
        }
    },

    SetMMUSWIDCookie: () => {
        // console.info('Setting USWID cookie');
        const queryString = window.location.search;
        if (queryString) {
            // check if the query string contains uid/sid
            const queryObj = new URLSearchParams(queryString);
            if (queryObj.has('uid') && queryObj.has('sid')) {
                const entries = queryObj.entries();
                const entriesObj = Object.fromEntries(entries);
                let cleanObj = {};

                uswid_controller.ACCEPTED_PARAM_KEYS.forEach(key => {
                    if (entriesObj[key]) {
                        cleanObj[key] = entriesObj[key];
                    }
                });

                // Logic to flag as SH (s)/Cloud (c)
                if (queryObj.has('utm_medium')) {
                    const utm_medium = queryObj.get('utm_medium');
                    if (utm_medium === 'in-product-cloud') {
                        cleanObj.mm_d = 'c';
                    } else {
                        cleanObj.mm_d = 's';
                    }
                } else {
                    cleanObj.mm_d = 's';
                }

                // Cookie string info
                const cookieValue = JSON.stringify(cleanObj);
                let expirationTime = 31536000; // 1 year in seconds
                expirationTime = expirationTime * 1000; // Converts expiration time to milliseconds
                let date = new Date(); 
                let dateTimeNow = date.getTime(); 
                date.setTime(dateTimeNow + expirationTime); // Sets expiration time (Time now + one month)
                let dateString = date.toUTCString(); // Converts milliseconds to UTC time string

                let secure_flag = ' Secure;';

                if (uswid_controller.testing_local) {
                    secure_flag = '';
                }

                const cookieString = `${mm_id_cookie}=${cookieValue}; SameSite=Lax; Expires=${dateString}; Path=/;${secure_flag} Domain=.${uswid_controller.root_domain}`;
                
                document.cookie = cookieString; // Sets cookie for all subdomains
            }
        }
        
    }

};

$(document).ready(function () {
    // Initialize the USWID Cookie logic
    console.log('uswid cookie - v1.6');	
	uswid_controller.Init();
});
