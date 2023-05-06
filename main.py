from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/home')
  pw = request.form['pw']
  if pw == 'vjsg':
    return render_template('home.html')
  return render_template('index.html')

if '__main__' == __name__:
	app.run()
