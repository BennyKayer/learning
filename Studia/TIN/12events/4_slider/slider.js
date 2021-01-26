window.onload = event => {
    const slider = document.querySelector(".slider");
    const thumb = document.querySelector(".thumb");

    const updatePosition = event => {
        // 15px body padding and 15px thumb width - divides into 2
        const newPosition =
            event.clientX - 22.5 > 310
                ? 310
                : event.clientX - 22.5 < 0
                ? 0
                : event.clientX - 22.5;
        thumb.style.left = `${newPosition}px`;
    };

    slider.addEventListener("click", updatePosition);

    thumb.addEventListener("mousedown", event => {
        slider.addEventListener("mousemove", updatePosition);
    });

    // attached to window in case user leaves slider area while dragging
    window.addEventListener("mouseup", event => {
        slider.removeEventListener("mousemove", updatePosition, false);
    });
};
