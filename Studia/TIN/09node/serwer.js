/*jshint globalstrict: true, devel: true, node: true */
'use strict';

var express = require('express');
var app = express();
var path = require('path');
var bodyParser = require('body-parser');
var favicon = require('serve-favicon');
var morgan = require('morgan');
var baza = require('./db/books');

app.set('view engine', 'ejs');

app.use(morgan('dev'));
app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function (req, res) {
    var genres = baza().distinct("genre");
    res.render('index.ejs', {genres: genres});
});

app.get('/:gen', function (req, res) {
    var genres = baza().distinct("genre");
    var books = baza({genre: req.params.gen}).select("title", "author");
    var genre = req.params.gen;
    res.render('index.ejs', {genres: genres, books: books, genre: genre});
});

app.post('/:gen', function (req, res) {
    var newAuthor=req.body.author;
    var newTitle=req.body.title;
    var genre = req.params.gen;
    console.log(newAuthor, newTitle);
    if (req.body.login === 'admin' && req.body.password === 'nimda') {
        var record = {title: newTitle, author: newAuthor, genre: genre};
        addToDB(record);
    } else { console.log('\nNiewlasciwy login lub haslo'); };
    var genres = baza().distinct("genre");
    var books = baza({genre: genre}).select("title", "author");
    res.render('index.ejs', {genres: genres, books: books, genre: genre});
});

var addToDB = function(record) {
    baza.insert(record);
}


app.listen(3000, function () {
    console.log('Serwer działa na porcie 3000');
});


process.on('SIGINT',function() {
    console.log('\nZapisywanie do pliku.');
    var books = baza().select("title", "author", "genre");
    var fs = require('fs');
    var data = JSON.stringify(books);
    fs.writeFile('database.csv', data, function (err) {
                 if (err) {
        return console.error(err);
    } else { console.log('\nshutting down');
  process.exit();
           }
    });
});