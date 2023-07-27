from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> This is Testing Environment with some functionality................... </h1>'
