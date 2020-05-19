from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL
from flask import url_for, session, redirect, escape
from hashlib import md5


# app.static_folder = 'static'

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'tysiac'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = 'asd1d4w9f21d13dlo6zd1f4lb6j2vne6la5'
mysql.init_app(app)
from gra_w_tysiaca import views



