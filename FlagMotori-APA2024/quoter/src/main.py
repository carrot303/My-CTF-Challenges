import os
import re
from flask import Flask, render_template, request, Response, make_response
import threading
import time

app = Flask(__name__)

quote_file = None
image_file = None


def plain_response(stream):
	resp = Response(stream.read())
	resp.headers["Content-type"] = "text/plain"
	return resp


def display_image(stream):
	response = make_response(stream.read())
	response.headers.set('Content-Type', 'image/jpeg')
	return response


@app.route("/")
def quote_page():
	global quote_file
	filename = request.args.get("filename")
	if filename:
		filename = filename.replace("../", "")
		filename = os.path.abspath("./static/qoutes/" + filename)
		try:
			quote_file = open(filename)
		except:
			return "Invalid filename given!"

		if os.path.basename(filename) == "flag.txt":
			return "No way!"

		with open(filename) as file:
			return plain_response(file)

	return render_template("index.html")


@app.route("/image")
def image_page():
	global image_file
	filename = request.args.get("filename")
	if filename:
		filename = filename.replace("../", "")
		filename = os.path.abspath("./static/images/" + filename)
		try:
			image_file = open(filename, "rb")
		except:
			return "Invalid filename given!"

		if os.path.basename(filename) == "flag.txt":
			return "No way!"

		with open(filename, "rb") as file:
			return display_image(file)

	return render_template("index.html")

if __name__ == "__main__":
	app.run("0.0.0.0", 1337)