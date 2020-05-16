from flask import Flask


# app.static_folder = 'static'

app = Flask(__name__) 
from gra_w_tysiaca import views

