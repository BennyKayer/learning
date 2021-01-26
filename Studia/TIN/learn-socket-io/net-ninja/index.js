const express = require("express");
const socket = require("socket.io");

// Setup
const app = express();
const portNumber = 3000;
const server = app.listen(portNumber, () => {
    console.log(`App is running on port ${portNumber}`);
});

// Static files
app.use(express.static("public"));

//Socket Setup
const io = socket(server);

// backend listen
io.on("connection", socket => {
    socket.on("chat", data => {
        io.sockets.emit("chat", data);
    });

    socket.on("typing", userName => {
        socket.broadcast.emit("typing", userName);
    });
});
