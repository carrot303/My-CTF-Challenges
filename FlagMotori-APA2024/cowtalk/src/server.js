const express = require("express");
const path = require("path");
const child_process = require("child_process");

const PORT = 1337;
const HOST = "localhost";

const app = express();

app.set("view engine", "ejs");


app.get("/", (req, res) => {
	let text = req.query.text;
	if (!text) {
		res.render("index", {result: undefined});
		return;
	}
	let command = `echo "${text}";`
	try {
		result = child_process.execSync(command).toString();
	} catch {
		result = "Invalid input given!";		
	}
	res.render("index", {result});
})


app.listen(PORT, () => {
	console.log(`Server listening at post ${HOST}:${PORT}`);
});