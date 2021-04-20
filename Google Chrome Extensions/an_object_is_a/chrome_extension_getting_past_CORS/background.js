let active_tab_id = 0;

chrome.tabs.onActivated.addListener((tab) => {
    chrome.tabs.get(tab.tabId, (current_tab_info) => {
        active_tab_id = tab.tabId;

        if (/^https:\/\/www\.google/.test(current_tab_info.url)) {
            chrome.tabs.insertCSS(null, { file: "./mystyles.css" });
            chrome.tabs.executeScript(null, { file: "./foreground.js" }, () =>
                console.log("I've injected")
            );
        }
    });
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === "fetch_for_me") {
        // Call using jquery
        // $.ajax({
        //     url: "https://www.yahoo.com",
        //     method: "GET",
        //     success: function (data, status, jqxhr) {
        //         console.log("Successfully fetched...");
        //         console.log(data);
        //     },
        //     error: function (jqxhr, status, error) {
        //         console.log("There was a problem fetching...");
        //         console.log(error);
        //     },
        // });

        // Call using fetchAPI
        fetch("https://www.yahoo.com")
            .then((res) => console.log(res))
            .catch((err) => console.log("Could not fetch..."));
    }
});
