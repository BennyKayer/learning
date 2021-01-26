/*jshint node: true */
'use strict';

var express = require('express');
var app = express();
var session = require('express-session');
var path = require('path');
var bodyParser = require('body-parser');
var favicon = require('serve-favicon');
var morgan = require('morgan');
var baza = require('./db/books');

app.use(session({
    secret: 'xxxyyyzzz',
    resave: false,
  saveUninitialized: true
}));
app.use(morgan('dev'));
app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'node_modules/jquery/dist')));

app.post('/login', function (req, res) {
    if(req.session.user !== 'admin'){
        if(req.body.login === "admin" && req.body.password === "nimda") {
            req.session.user = "admin";
        } else {
            res.sendStatus(401);
        }
    }
    res.sendStatus(200);
});

app.post('/logout', function (req, res) {
    if(req.session.user === 'admin'){
        req.session.destroy();
        res.sendStatus(200);
    }
});

app.post('/checkLogin', function (req, res) {
    if(req.session.user === 'admin'){
        res.sendStatus(200);
    } else {
        res.sendStatus(401);
    }
});

app.get('/genres', function (req, res) {
    var genres = baza().distinct("genre");
    res.json(genres);
});

app.get('/genre/:gen', function (req, res) {
    var books = baza({genre: req.params.gen}).select("title", "author");
    res.json(books);
});

app.post('/genre/:gen', function (req, res) {
    if(req.session && req.session.user === "admin") {
        var newAuthor=req.body.newAuthor;
        var newTitle=req.body.newTitle;
        var genre = req.params.gen;
        baza.insert({'genre':genre,'title':newTitle,'author':newAuthor});
        res.end();
    } else {
        res.sendStatus(401);
    }
    
});

app.listen(3000, function () {
    console.log('Serwer działa na porcie 3000');
});


