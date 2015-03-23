# coding=utf8

" Package Init "

import os
import sys
from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'

from views import create_app
app = create_app(app)
