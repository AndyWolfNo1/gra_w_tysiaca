from gra_w_tysiaca import app
from flask import render_template
from gra_w_tysiaca.klass.Table import *
from gra_w_tysiaca.klass.Card import *
from gra_w_tysiaca.klass.Player import *
from gra_w_tysiaca.klass.Deck import *
from gra_w_tysiaca.klass.Tactics import *
from gra_w_tysiaca.klass.test import *
from random import shuffle
from flask_table import Table, Col
import jinja2


env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates/'])) 
@app.context_processor
def inject_variables():
    return dict(
        the_title = table,
        data = table,
        navigation = [
            {
                'href': '/',
                'caption': 'Główna'
            },
            {
                'href': 'test',
                'caption': 'Test'
            }
        ])


@app.route('/')
def start():
    ready()
    return render_template( 'start.html' )


@app.route('/test')
def test():
    return render_template( 'test.html' )



