from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/Home/', methods = ["POST"])
def home():
	pw = request.form['pw']
	if pw == 'vjsg'
		return render_template('home.html')

if __name__ == '__main__':
	app.run()
