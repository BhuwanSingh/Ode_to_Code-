const express =  require("express");
const app = express();
const fs = require("fs");

var ans = fs.readFileSync('output.json');
let fans = JSON.parse(ans);
// console.log(fans);

app.use( express.urlencoded({
    extended : true
}))

app.use(express.json())

app.post('/api' , (req, res) => {
    for(const a of req.body ){
        console.log(a);
    }
})

app.get( '/api' , function(req, res , next) {
    console.log("working-get");
    res.json({fans});
})

app.listen(3000 , () =>{
    console.log("listining");
})