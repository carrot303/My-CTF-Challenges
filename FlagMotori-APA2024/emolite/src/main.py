import sqlite3
import os

from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

FLAG = os.environ.get("FLAG", "flag{fake_flag}")
emojies_list = [
	("\U0001F601", "grinning face with smiling eyes"),
	("\U0001F602", "face with tears of joy"),
	("\U0001F603", "smiling face with open mouth"),
	("\U0001F604", "smiling face with open mouth and smiling eyes"),
	("\U0001F605", "smiling face with open mouth and cold sweat"),
	("\U0001F606", "smiling face with open mouth and tightly-closed eyes"),
	("\U0001F609", "winking face"),
	("\U0001F60A", "smiling face with smiling eyes"),
	("\U0001F60B", "face savouring delicious food"),
	("\U0001F60C", "relieved face"),
	("\U0001F60D", "smiling face with heart-shaped eyes"),
	("\U0001F60F", "smirking face"),
	("\U0001F612", "unamused face"),
	("\U0001F613", "face with cold sweat"),
	("\U0001F614", "pensive face"),
	("\U0001F616", "confounded face"),
	("\U0001F618", "face throwing a kiss"),
	("\U0001F61A", "kissing face with closed eyes"),
	("\U0001F61C", "face with stuck-out tongue and winking eye"),
	("\U0001F61D", "face with stuck-out tongue and tightly-closed eyes"),
	("\U0001F61E", "disappointed face"),
	("\U0001F620", "angry face"),
	("\U0001F621", "pouting face"),
	("\U0001F622", "crying face"),
	("\U0001F623", "persevering face"),
	("\U0001F624", "face with look of triumph"),
	("\U0001F625", "disappointed but relieved face"),
]


def get_connection():
	return sqlite3.connect("db.sqlite3")


def init_sql():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("DROP TABLE IF EXISTS emoji;")
	cur.execute("DROP TABLE IF EXISTS flag;")
	cur.execute("CREATE TABLE flag (name CHAR(24), description TEXT)")
	cur.execute("CREATE TABLE emoji (description TEXT, value BLOB)")

	cur.execute("INSERT INTO flag (name, description) VALUES (?, ?);", ("flag", FLAG))
	cur.executemany("INSERT INTO emoji (value, description) VALUES (?, ?)", emojies_list)

	conn.commit()
	cur.close()


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/emojies")
def emojies():
	conn = get_connection()
	try:
		cur = conn.cursor()
		cur.execute("SELECT value,description FROM emoji;")
		records = cur.fetchall()
		return render_template("emojies.html", emoji_list=records, title="List")
	finally:
		cur.close()

@app.route("/search")
def search():
	query = request.args.get("q")
	if not query:
		return redirect(url_for("index"))
	conn = get_connection()
	try:
		cur = conn.cursor()
		records = cur.execute(f"""
			SELECT value, description FROM emoji
			WHERE description LIKE "%{query}%";
		""")
		return render_template("emojies.html", emoji_list=records, title="Search")
	finally:
		cur.close()

if __name__ == "__main__":
	init_sql()
	app.run("0.0.0.0", 1337)
