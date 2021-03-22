var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");
var button = document.getElementById("randomButton");
setGradient();

function setGradient() {
	body.style.background =
	"linear-gradient(to right, "
	+ color1.value
	+ ", "
	+ color2.value
	+ ")";

	css.textContent = body.style.background + ";";
}

function rc() {
	let num = Math.floor(Math.random() * (+255 - +0));
	return num.toString(16);
}

function randColors(){
	color1.value = "#" + rc() + rc() + rc() ;
	color2.value = "#" + rc() + rc() + rc() ;
	setGradient();
}

color1.addEventListener("input", setGradient);
color2.addEventListener("input", setGradient);
button.addEventListener("click", randColors);
