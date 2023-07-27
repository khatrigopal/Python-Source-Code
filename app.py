from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> -------Welcome BAck //// Cloud & Devops is Good practice.................... </h1>'
