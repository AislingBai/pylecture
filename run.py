# coding=utf8

from optparse import OptionParser
from flask import Flask, render_template, json, request, redirect, url_for
from flask.json import jsonify
from flask_bootstrap import Bootstrap
# from gevent.pywsgi import WSGIServer

from pylecture import app
from pylecture.utils import gen_spider
from pylecture.models import init_db, reset_db

__version__ = '0.0.0'

def cmd():
    usage = "usage: %prog command [option] arg"
    parser = OptionParser(usage=usage, version="%prog " + __version__)
    parser.add_option('-p', '--port', help="Specifically port number.")

    (options, args) = parser.parse_args()

    if len(args) == 0:
        app.run(host='localhost', port=8000)
    elif args[0] == 'gen':
        print gen_spider(1, dest='pylecture/spiders/sues.py')
    elif args[0] == 'build':
        init_db()
    elif args[0] == 'rebuild':
        reset_db()
    elif args[0] == 'cli':
        pass

if __name__ == '__main__':
    cmd()
