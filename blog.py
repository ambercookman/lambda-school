from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/birthday')
def birthday():
	return 'September 25 1988'

@app.route('/greeting/<name>')
def greeting(name):
	return 'Hello ' + name

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
	return str( a + b )

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a,b):
	return str( a * b )

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a,b):
	return str( a - b )

@app.route('/favoritefoods')
def favoritefoods():
	favoritefoods = ['coffee', 'pineapple curry', 'tiger butter caramel apples']
	return jsonify(favoritefoods)