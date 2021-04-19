// Executed as soon as extension is loaded or refreshed
console.log("from background");

let activeTabId = 0;
chrome.tabs.onActivated.addListener((tab) => {
    console.log(tab);
    chrome.tabs.get(tab.tabId, (current_tab_info) => {
        activeTabId = tab.tabId;
        console.log(current_tab_info);
        console.log(current_tab_info.url);
        if (/^https:\/\/www\.google/.test(current_tab_info.url)) {
            chrome.tabs.insertCSS(null, { file: "./mystyles.css" });
            chrome.tabs.executeScript(null, { file: "./foreground.js" }, () =>
                console.log("I have injected")
            );
        }
    });
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === "yo check the storage") {
        chrome.tabs.sendMessage(activeTabId, {
            message: "Yo I got your message 2",
        });
        sendResponse({ message: "yo I got your message" });
        chrome.storage.local.get("password", (value) => {
            console.log(value);
        });
    }
});

// Will error bcs we cannot inject into chrome://extensions/
// chrome.tabs.executeScript(null, { file: "./foreground.js" }, () =>
//     console.log("I injected")
// );
