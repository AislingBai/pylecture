# coding=utf8

" Package Init "

from flask import Flask
from views import create_app

app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'
app = create_app(app)
