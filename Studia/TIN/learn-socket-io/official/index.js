const app = require("express")();
const http = require("http").createServer(app);
const io = require("socket.io")(http);

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

io.on("connection", socket => {
    socket.on("chat message", msg => {
        console.log("message" + msg);
    });
    // socket.on("disconnect", () => {
    //     console.log("user disconnected");
    // });
});

http.listen(4000, () => {
    console.log("Listening on port 4000");
});
