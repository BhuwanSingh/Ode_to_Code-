const express = require("express");
const app = express();
const fs = require("fs");
const PythonShell = require("python-shell").PythonShell;

app.use(express.json());

app.get("/api", (req, res) => {
    console.log("here");
    const a = req.body;

    fs.writeFileSync("input.json", JSON.stringify(a), (err) => {
        if (err) {
            console.error(err);
            return;
        }
    });

    PythonShell.run("main.py", null, function (err) {
        if (err) throw err;
        console.log("finished");
        var ans = fs.readFileSync("output.json");
        let fans = JSON.parse(ans);
        console.log("working-get");
        res.json({ fans });
    });

});

let port = process.env.PORT || 3001;
app.listen(port, () => {
    console.log(`listining on port:${port}`);
});
