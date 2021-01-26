window.onload = event => {
    const imgs = document.querySelectorAll("img");
    const display = document.querySelector("#largeImg");

    imgs.forEach(img => {
        img.addEventListener("click", event => {
            event.preventDefault();
            display.src = event.target.src;
            display.title = event.target.parentNode.title;
        });
    });
};
