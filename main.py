import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('form.html')
	
@app.route('/result/', methods = ["POST"])
def results():
	conn = sqlite3.connect('database.db')
	
	info = request.form['info']
	data = {}
	
	for info in conn.execute("SELECT * FROM table WHERE info = ?", (info,)):
		data[info] = info
		
	return render_template('result.html', info = info, data = data)


if __name__ == '__main__':
	app.run()