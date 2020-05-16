from flask import Flask, render_template, url_for
from Table import *
from Card import *
from Player import *
from Deck import *
from Tactics import *
from test import *
from random import shuffle
from flask_table import Table, Col
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates/'])) 

app = Flask(__name__)


@app.route('/')

def hello():
    ready()
    template = env.get_template('start.html')
    return template.render( the_title = table,
                            data = table )
    
@app.route('/test', methods=['GET', 'POST'])

##def index():
##    return 'Hello World'
##
##
##def start():
##    template = env.get_template('test.html')
##    return template.render( data = table )
##

def contact():
    form = ContactForm()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            template = env.get_template('test.html')
            return template.render( data2 = "tekst" )


app.run(debug=True)
