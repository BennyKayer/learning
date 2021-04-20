document.addEventListener("click", () => {
    // Hey background fetch for me
    chrome.runtime.sendMessage({ message: "fetch_for_me" }, () =>
        console.log("cool")
    );

    // Ok I'll do it myself
    // fetch("https://www.yahoo.com")
    //     .then((res) => console.log(res))
    //     .catch((err) => console.log("Could not fetch"));
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {});
