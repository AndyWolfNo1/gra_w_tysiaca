from gra_w_tysiaca import app 	
from gra_w_tysiaca import mysql
from flask import render_template
from flask import request
#from gra_w_tysiaca.klass.Table import *
#from gra_w_tysiaca.klass.Card import *
from gra_w_tysiaca.klass.Player import *
#from gra_w_tysiaca.klass.Deck import *
#from gra_w_tysiaca.klass.Tactics import *
#from gra_w_tysiaca.klass.test import *
from random import shuffle
from flask_table import Table, Col
import jinja2
from flask import url_for, session, redirect, escape
from hashlib import md5


env = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates/'])) 


@app.route('/',methods = ['POST', 'GET'])
def start():
    if request.method == 'POST':
        if request.form["add_table"] == "true":
            conn = mysql.connect()
            cur = conn.cursor()
            to_db = session['username']
            cur.execute("""INSERT INTO `tables`(`author`, `stan`) VALUES ( %s ,0)""", session['username'].capitalize())
            data = cur.fetchall()
            conn.commit()
            return "Dodano stół"
    else:
        return render_template( 'start.html' )


@app.route('/table/<int:table_id>',methods = ['POST', 'GET'])
def table(table_id):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("""SELECT `chair` FROM `t_p` WHERE table_ID = %s """, table_id )
    chairs = cur.fetchall()
    int_chairs = len(chairs)
    cur.execute("""SELECT * FROM `t_p` WHERE table_ID = %s """, table_id )
    gracze = cur.fetchall()
    cur.execute("""SELECT `author` FROM `tables` WHERE ID = %s  """, table_id )
    author = cur.fetchall()
    author = author[0][0]
    cur.execute("""SELECT * FROM `t_p` WHERE table_ID = %s  """, table_id )
    table_players = cur.fetchall()
    buff = []
    gracze_ogolem = gracze
    for i in gracze:
        buff.append(i[1])
    gracze = buff
    
    if request.method == 'POST':
        if request.form["run_table"]:
            list_playesrs = []
            return render_template('test2.html', gracze_ogolem=gracze_ogolem)
            
    if request.method == 'POST':
        if request.form["sit_down"]:
            chair = request.form['sit_down']
            conn = mysql.connect()
            cur = conn.cursor()
            table_id = table_id
            to_db = (session['username'], chair, table_id)
            cur.execute("""INSERT INTO `t_p`(`name`, `chair`,`table_ID`) VALUES ( %s , %s, %s)""", to_db )
            conn.commit()
            return "dodano"
    else:
        return render_template('table.html', table_id = table_id,
                               chairs=chairs,
                               gracze=gracze,
                               author=author,
                               table_players=table_players,
                               int_chairs=int_chairs,
                               gracze_ogolem=gracze_ogolem,
                               )


@app.route('/klasyfikacja')
def klasyfikacja():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from gracze")
    data = cursor.fetchall()
    return render_template('klasyfikacja.html', data = data, ile = len(data))
   

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if 'username' in session:
        return render_template( 'start.html' )
 
    error = None
    error_register = None
    success_register = None
    class ServerError(Exception):pass
 
    if request.method == 'POST':
        if request.form["action"] == "login":
            try:
                conn = mysql.connect()
                cur = conn.cursor()
                username_form  = request.form['username']
                cur.execute("SELECT COUNT(1) FROM gracze WHERE login = '" + username_form +"'")
 
                if not cur.fetchone()[0]:
                    raise ServerError('Błędna nazwa użytkownika')
 
                password_form  = request.form['password']
                cur.execute("SELECT passwd FROM gracze WHERE login = '" + username_form +"'")
 
                for row in cur.fetchall():
                    if md5(password_form.encode('utf-8')).hexdigest() == row[0]:
                        session['username'] = request.form['username']
                        return render_template( 'start.html' )
 
                raise ServerError('Błędne hasło')
 
            except ServerError as e:
                error = str(e)
 
        if request.form["action"] == "register":
            try:
                conn = mysql.connect()
                cur = conn.cursor()
                name_form = request.form['name']
                username_form  = request.form['user']
                password_form  = request.form['pass']
                hash_password = md5(password_form.encode('utf-8')).hexdigest()
                to_db = ("", username_form, hash_password, name_form, 0)
                cur.execute("SELECT COUNT(1) FROM gracze WHERE login = '" + username_form +"'")
 
                if cur.fetchone()[0]:
                    raise ServerError('Nazwa uzytkownika zajęta')
 
                else:
                    cur.execute("INSERT INTO gracze VALUES (%s, %s, %s, %s, %s)", to_db)
                    conn.commit()
                    success_register = "Zarejestrowałeś się!"
 
            except ServerError as e:
                error_register = str(e)
 
    return render_template('login.html', error=error, error_register=error_register, success_register=success_register)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template( 'start.html' )


@app.context_processor
def inject_variables():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from gracze")
    users = cursor.fetchall()
    cursor.execute("SELECT * from tables")
    tables = cursor.fetchall()
    return dict(
        session = session,
        tables = tables,
        users = users,
        navigation = [
            {
                'href': '/',
                'caption': 'Główna'
            },
            {
                'href': 'klasyfikacja',
                'caption': 'Punktacja'
            },
            {
                'href': 'login',
                'caption': 'Logowanie'
            }
        ])

