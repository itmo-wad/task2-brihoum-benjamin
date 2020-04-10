from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/img')
def img():
    return '<h1>Nothing to see here folk</h1>', 404
