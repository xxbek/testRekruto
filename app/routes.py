from app import app
from flask import render_template, request
from app.forms import HelloForm


@app.route('/')
@app.route('/index')
def index():
    args = request.args
    name = args.get('name')
    message = args.get('message')
    form = HelloForm()
    return render_template('index.html', name=name, message=message, form=form)

