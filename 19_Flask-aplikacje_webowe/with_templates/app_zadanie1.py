# flask --app app2 run
#
from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    name = ""
    args = request.args
    print(args)
    params = [{"key": k, "value": v} for k, v in args.items()]
    if "name" in args.keys():
        name = args["name"]
    print(params)
    return render_template('form_zadanko.html', params=params, name=name)

@app.route('/add')
def add():
    args = request.args
    print(args)
    data.append(args["name"])

    return render_template('form_zadanko.html', data=data, tytul="Dodano pozycję do listy")
