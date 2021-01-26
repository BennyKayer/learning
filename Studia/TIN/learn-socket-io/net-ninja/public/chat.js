// make connection
const socket = io.connect("http://localhost:3000");

// DOM
const message = document.getElementById("message");
const handle = document.getElementById("handle");
const send = document.getElementById("send");
const output = document.getElementById("output");
const feedback = document.getElementById("feedback");

// Emit events
send.addEventListener("click", event => {
    socket.emit("chat", {
        msg: message.value,
        handle: handle.value
    });
});

message.addEventListener("keypress", event => {
    socket.emit("typing", handle.value);
});

// Listen for events
socket.on("chat", data => {
    output.innerHTML += `<p><strong>${data.handle}</strong>: ${data.msg}</p>`;
    feedback.innerHTML = "";
});

socket.on("typing", userName => {
    feedback.innerHTML = `<p><em>${userName} is typing...</em></p>`;
});
