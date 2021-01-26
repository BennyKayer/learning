window.onload = event => {
    const lis = document.querySelectorAll("li");

    lis.forEach(li => {
        li.addEventListener("click", event => {
            // Change individual
            if (event.ctrlKey) {
                li.classList.toggle("selected");
            }
            // Check exclusively
            else {
                lis.forEach(li => {
                    li.classList.remove("selected");
                });
                li.classList.add("selected");
            }
        });
    });
};
