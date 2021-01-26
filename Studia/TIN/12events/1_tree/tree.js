window.onload = event => {
    const lis = document.querySelectorAll("li");
    lis.forEach(li => {
        // Determine collapsible
        const target = li.childNodes.length > 1;
        // Wrap text in span
        if (target) {
            const s = document.createElement("span");
            s.appendChild(document.createTextNode(li.firstChild.nodeValue));
            li.replaceChild(s, li.firstChild);
        }
    });

    const spans = document.querySelectorAll("span");

    spans.forEach(span => {
        // By default it's empty, added to avoid first click "do nothing"
        span.nextElementSibling.style.display = "block";
        // Toggle collapse
        span.addEventListener("click", event => {
            event.target.nextElementSibling.style.display === "block"
                ? (event.target.nextElementSibling.style.display = "none")
                : (event.target.nextElementSibling.style.display = "block");
        });
    });
};
