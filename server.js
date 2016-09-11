var http = require("http");
var express = require('express');
var app = express();

app.get('/', function(req, res) {
    res.end();
});

app.listen(8023, function() {
    console.log('Listening on port 8023'); //Listening on port 8888
});
