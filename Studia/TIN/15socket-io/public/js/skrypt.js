/* jshint browser: true, globalstrict: true, devel: true */
/* global io: false */
"use strict";

// Inicjalizacja
document.addEventListener("DOMContentLoaded", function(event) {
    var statusImg = document.getElementById("status");
    var openConnection = document.getElementById("open");
    var closeConnection = document.getElementById("close");
    var sendBtn = document.getElementById("send");
    var msgInput = document.getElementById("text");
    var messageContainer = document.getElementById("message-container");
    var socket;
    const logged = document.getElementById("logged");
    const typing = document.getElementById("typing");

    const appendMessage = message => {
        const newMsg = document.createElement("div");
        newMsg.innerText = message;
        messageContainer.append(newMsg);
    };

    statusImg.textContent = "Brak połącznia";
    closeConnection.disabled = true;
    sendBtn.disabled = true;

    // Po kliknięciu guzika „Połącz” tworzymy nowe połączenie WS
    openConnection.addEventListener("click", event => {
        openConnection.disabled = true;
        logged.hidden = false;
        if (!socket || !socket.connected) {
            socket = io({ forceNew: true });
        }

        socket.on("connect", function() {
            closeConnection.disabled = false;
            sendBtn.disabled = false;
            statusImg.src = "img/bullet_green.png";
            console.log("Nawiązano połączenie przez Socket.io");
            //  new-user
            let user = null;
            while (!user) {
                user = prompt("Jak się nazywasz?");
            }
            appendMessage("Dołączasz do czatu");
            socket.emit("new-user", user);
        });
        socket.on("disconnect", function() {
            openConnection.disabled = false;
            statusImg.src = "img/bullet_red.png";
            console.log("Połączenie przez Socket.io zostało zakończone");
        });
        socket.on("error", err => {
            messageContainer.textContent =
                "Błąd połączenia z serwerem: '" + JSON.stringify(err) + "'";
        });
        socket.on("echo", function(data) {
            messageContainer.textContent =
                "Serwer twierdzi, że otrzymał od Ciebie: '" + data + "'";
        });

        socket.on("message", pos => {
            appendMessage(`${pos.name}: ${pos.msg}`);
            typing.innerText = "";
        });

        socket.on("user-connected", name => {
            appendMessage(`${name} dołączył do czatu`);
            socket.emit("users-change", null);
        });

        socket.on("user-disconnected", name => {
            appendMessage(`${name} opuścił czat`);
            socket.emit("users-change", null);
        });

        socket.on("update-list", users => {
            logged.innerHTML = "<ul id='logged'></ul>";
            Object.values(users).map(name => {
                const li = document.createElement("li");
                li.textContent = name;
                logged.append(li);
            });
        });

        socket.on("typing", userName => {
            typing.innerText = `${userName} pisze...`;
        });
    });

    // Zamknij połączenie po kliknięciu guzika „Rozłącz”
    closeConnection.addEventListener("click", function(event) {
        closeConnection.disabled = true;
        sendBtn.disabled = true;
        openConnection.disabled = false;
        logged.hidden = true;
        messageContainer.textContent = "";
        socket.emit("disconnect", null);
        socket.io.disconnect();
        console.dir(socket);
    });

    // Wyślij komunikat do serwera po naciśnięciu guzika „Wyślij”
    sendBtn.addEventListener("click", event => {
        event.preventDefault();
        const message = msgInput.value;
        socket.emit("sent-message", message);
        msgInput.value = "";
    });

    // Wyświetl pisze...
    msgInput.addEventListener("keypress", event => {
        socket.emit("typing", socket.id);
    });
});
