const express =  require("express");
const app = express();
const fs = require("fs");

app.get( '/json' , function(req, res , next) {
    console.log("working");
    res.json({"one" : "two"});
})

app.listen(3000 , () =>{
    console.log("working");
})