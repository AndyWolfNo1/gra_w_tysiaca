from gra_w_tysiaca import app 	
from gra_w_tysiaca import mysql
from flask import render_template
from flask import request
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


@app.route('/')
def start():
    ready()
    return render_template( 'start.html' )

@app.route('/register')
def register():
    ready()
    return render_template( 'register.html' )


@app.route('/player')
def gracz():
    return render_template( 'player.html' )


@app.route('/klasyfikacja')
def klasyfikacja():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from gracze")
    data = cursor.fetchall()
    return render_template('klasyfikacja.html', data = data, ile = len(data))


@app.route('/test',methods = ['POST', 'GET'])
def test():
    if request.method == 'POST':  
      table.players[0].name = 'Marek'
      return render_template("test.html")
    else:
        return render_template( 'test.html' )


@app.route('/register',methods = ['POST', 'GET'])  
def print_data():
    if request.method == 'POST':  
      result = request.form  
      return render_template("test2.html",result = result)  



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
            },
            {
                'href': 'player',
                'caption': 'Gra'
            },
            {
                'href': 'klasyfikacja',
                'caption': 'Punktacja'
            },
            {
                'href': 'register',
                'caption': 'Rejestracja'
            },
            {
                'href': 'test2',
                'caption': 'test2'
            }
        ])

