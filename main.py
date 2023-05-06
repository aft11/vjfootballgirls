from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
  if request.method == "GET":
	  return render_template('index.html')
  
	pw = request.form['pw']
	if pw == 'vjsg':
		return render_template('home.html')

if __name__ == '__main__':
	app.run()
