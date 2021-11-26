from flask import Flask
from flask import render_template
import os
from mangayabu import getTitulos, getPage
from neox import pegarneox
app = Flask(__name__)


@app.route('/')
def basePage():
	return f'{getTitulos()}'
@app.route('/neox')
def mostarta():
	return '<h1>Itadaki seiki, assiste-se tomando vinho<h1/>'

@app.route('/index')
def indexPage():
	name = getTitulos()
	return render_template('index.html', name=name)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run(  # Starts the site
	    host=
	    '0.0.0.0',  # EStablishes the host, required for repl to detect the site
	    port=5000  # Randomly select the port the machine hosts on.
	)
