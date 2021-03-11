document.addEventListener(
  "DOMContentLoaded",
  function () {
    var checkPageButton = document.getElementById("clickIt");
    checkPageButton.addEventListener(
      "click",
      function () {
        chrome.tabs.getSelected(null, function (tab) {
          var xpath = "//h3[text()='Gamitude']";
          var matchingEl = document.evaluate(
            xpath,
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
          ).singleNodeValue;

          alert(matchingEl);
          // matchingEl.click();
        });
      },
      false
    );
  },
  false
);
