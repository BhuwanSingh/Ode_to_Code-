const express = require("express");
const app = express();
const fs = require("fs");

app.use(express.json());

app.get("/api", (req, res) => {
    console.log("here");
    const { a } = req.body;
    console.log(a);
    console.log(a['audio'])
    // fs.writeFileSync("input.txt", JSON.stringify(a), err => {
    //     if (err) {
    //         console.error(err);
    //         return;
    //     }
    // });
    // app.get("/api", (req, res) => {
        var ans = fs.readFileSync("output.json");
        let fans = JSON.parse(ans);
        console.log("working-get");
        res.json({ fans });
    // })
});

app.listen(3001, () => {
    console.log("listining");
});

// process.on('exit' , () => {
//     console.log("exiting1");
// })

// process.on('uncaughtException', () => {
//     console.log("exiting2");
// })

// process.on('SIGTERM', () => {
//     console.log("exiting3");
// })