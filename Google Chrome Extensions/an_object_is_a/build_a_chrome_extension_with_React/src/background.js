chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === "complete" && tab.url.includes("http")) {
        chrome.tabs.executeScript(
            tabId,
            { file: "./inject_script.js" },
            () => {
                chrome.tabs.executeScript(
                    tabId,
                    { file: "./foreground.bundle.js" },
                    () => {
                        console.log("INJECTED AND EXECUTED");
                    }
                );
            }
        );
    }
});
