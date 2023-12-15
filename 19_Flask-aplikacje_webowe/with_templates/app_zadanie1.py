# flask --app app2 run
#
from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    return render_template('form_zadanko.html', imie="")

@app.route('/add')
def add():
    args = request.args
    print(args)
    imie = args["name"]
    data.append(args["name"])
    print(imie)
    return render_template('form_zadanko.html', name=imie)
