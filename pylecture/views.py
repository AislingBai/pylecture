# coding=utf8

from flask import render_template, json, request, redirect, url_for, request
from flask.json import jsonify
from flask_bootstrap import Bootstrap
from forms import EditForm
from .models import Spider, LectureRules, db
from utils import scandb


def create_app(app):

    Bootstrap(app)

    @app.route('/')
    def index():
        return jsonify(a='sdfghj')

    @app.route('/new')
    def new():
        return render_template('new.html')

    @app.route('/edit', methods=['GET', 'POST'])
    def edit():
        form = EditForm()
        if form.validate_on_submit():
            spider_fields = scandb(Spider)
            lecturerules_fields = scandb(LectureRules)
            spider_data = {k: form.data.get(k) for k in spider_fields}
            spider = Spider(**spider_data)

            lecturerules_data = {k: form.data.get(k) for k in lecturerules_fields}
            lecturerules = LectureRules(**lecturerules_data)

            try:
                db.session.add(spider)
                db.session.add(lecturerules)
                # 将数据写入数据库
                db.session.commit()
            except Exception as e:
                print(e.message)
                db.session.callback()
        return render_template("edit.html", form=form)

    return app
