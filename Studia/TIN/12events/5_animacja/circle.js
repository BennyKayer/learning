window.onload = event => {
    const circle = document.querySelector(".circle");
    circle.addEventListener("click", event => {
        circle.style.transition = "width 3s, height 3s";

        // Zrób, aby po kliknięciu na okręgu jego średnica w ciągu 3 sekund płynnie powiększyła się do 600 pikseli.
        // na obrazku wyglada bardziej na 300 x 300 niz na 600 x 600
        circle.style.width = "300px";
        circle.style.height = "300px";
    });
    circle.addEventListener("transitionend", event => {
        // Both will trigger need only 1
        if (event.propertyName === "width") {
            // Centering
            circle.style.display = "flex";
            circle.style.alignItems = "center";
            circle.style.justifyContent = "center";
            // Text
            const lotr = document.createElement("p");
            // Fennas nogothrim...
            lotr.textContent = "Lasto beth lammen";
            lotr.style.fontWeight = "bold";
            lotr.style.fontSize = "24px";
            circle.appendChild(lotr);
        }
    });
};
