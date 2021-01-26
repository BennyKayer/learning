var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");

function inputLength() {
	return input.value.length;
}

function createListElement() {
	var li = document.createElement("li");
	li.appendChild(document.createTextNode(input.value));
	ul.appendChild(li);
	createDeleteButtons(li);
	input.value = "";
}

function createDeleteButtons(li){
	var button = document.createElement("button");
	button.appendChild(document.createTextNode("Delete"));
	li.appendChild(button);
}

function addListAfterClick() {
	if (inputLength() > 0) {
		createListElement();
	}
}

function addListAfterKeypress(event) {
	if (inputLength() > 0 && event.keyCode === 13) {
		createListElement();
	}
}

function toggleDone(event){
	if (event.target && event.target.tagName == "LI"){
		event.target.classList.toggle("done");
	}
}

function deleteItem(event){
	if(event.target && event.target.tagName == "BUTTON"){
		event.target.previousSibling.remove();
		event.target.parentElement.remove();
	}
}

button.addEventListener("click", addListAfterClick);
input.addEventListener("keypress", addListAfterKeypress);
ul.addEventListener("click", toggleDone);
ul.addEventListener("click", deleteItem);
