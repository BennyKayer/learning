"use strict";

// 1
function getshowAbstract(show, brief) {
    return function() {
        show = !show;
        //console.log(show);
        this.innerText = show ? "Hide Abstract" : "Show Abstract";
        brief.style.display = show ? "block" : "none";
    };
}
// 2
function filterArticles(input) {
    return function() {
        var lis = document.getElementsByTagName("li");

        for (var li of lis) {
            //console.log(li.innerText);
            if (
                li.innerText.toLowerCase().includes(input.value.toLowerCase())
            ) {
                //console.log("block");
                li.style.display = "block";
            } else {
                //console.log("none");
                li.style.display = "none";
            }
        }

        var uls = document.getElementsByTagName("ul");

        for (var ul of uls) {
            var h4 = document.getElementById(`H4${ul.id}`);
            h4.style.display = "none";
            for (var li of ul.children) {
                if (li.style.display == "block") {
                    h4.style.display = "block";
                }
            }
        }
    };
    // Zrealizuj możliwość przywrócenia pierwotnej postaci dokumentu - wyczyścić input
}

function prepare() {
    // 1
    var lis = document.getElementsByTagName("li");
    for (var li of lis) {
        // Buttons
        var button = document.createElement("button");
        button.appendChild(document.createTextNode("Show Abstract "));
        li.appendChild(button);
        // Briefs
        var title = li.firstElementChild.firstElementChild.title;
        var brief = document.createElement("div");
        brief.innerHTML = title;
        brief.style.padding = "1em";
        brief.style.margin = "0.5em";
        brief.style.border = "1px solid black";
        brief.style.display = "none";
        li.appendChild(brief);
        // Toggles
        var show = false;
        button.onclick = getshowAbstract(show, brief);
    }
    // 2
    var input = document.createElement("input");
    input.style.position = "fixed";
    input.style.top = "15px";
    input.style.right = "15px";
    document.body.appendChild(input);
    input.onchange = filterArticles(input);
}

window.onload = prepare;
