const express = require("express");
const app = express();
const fs = require("fs");

app.use(express.json());

app.get("/api", (req, res) => {
    console.log("here");
    const a = req.body;
    // console.log(JSON.stringify(a));

    var ans = fs.readFileSync("output.json");
    let fans = JSON.parse(ans);
    console.log("working-get");
    res.json({ fans });
    fs.writeFileSync("input.json", JSON.stringify(a), (err) => {
        if (err) {
            console.error(err);
            return;
        }
    });
});

let port = process.env.PORT || 3001;
app.listen(port, () => {
    console.log(`listining on port:${port}`);
});
