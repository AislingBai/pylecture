# coding=utf8

from flask import render_template, json, request, redirect, url_for
from flask.json import jsonify
from flask_bootstrap import Bootstrap

def create_app(app):

    Bootstrap(app)

    @app.route('/')
    def index():
        return jsonify(a='sdfghj')

    @app.route('/new')
    def new():
        return render_template('new.html')

    return app
