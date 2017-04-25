from flask import Flask, render_template
from flask import request
from blah import valid_name
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        #just loading a poge
        lol = ""
        return render_template('index.html', templateData=lol)
    else:
        #POSTs when form with action to this address is pressed
        # valid name is simple method right now checks for empty string
        if valid_name(request.form['username'],request.form['password']):
            lol = "It is valid";
        else:
            lol = "not valid";
        return render_template('index.html', templateData=lol)
