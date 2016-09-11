var http = require("http");
var express = require('express');
var app = express();

app.get('/', function(req, res) {
    res.send('Hello World!');;
});

app.listen(5000, function() {
    console.log('Listening on port 5000'); //Listening on port 5000
});
