/* jshint node: true */
var express = require("express");
var app = express();
var httpServer = require("http").Server(app);
var io = require("socket.io")(httpServer);

var path = require("path");

app.use(express.static(path.join(__dirname, "public")));

const users = {};

io.on("connection", function(socket) {
    socket.on("new-user", name => {
        users[socket.id] = name;
        io.emit("user-connected", name);
        console.log(users);
    });

    socket.on("sent-message", msg => {
        io.emit("message", {
            msg: msg,
            name: users[socket.id]
        });
        console.log(users[socket.id], msg);
    });

    socket.on("disconnect", () => {
        io.emit("user-disconnected", users[socket.id]);
        delete users[socket.id];
        console.log(users);
    });

    socket.on("error", function(err) {
        console.dir(err);
    });

    socket.on("users-change", () => {
        io.emit("update-list", users);
    });

    socket.on("typing", id => {
        socket.broadcast.emit("typing", users[id]);
    });
});

httpServer.listen(3000, function() {
    console.log("Serwer HTTP działa na porcie " + 3000);
});
