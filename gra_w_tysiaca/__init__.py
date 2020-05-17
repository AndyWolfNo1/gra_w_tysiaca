from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL


# app.static_folder = 'static'

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'tysiac'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
from gra_w_tysiaca import views

