# coding=utf8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, BooleanField
from wtforms.validators import Required


class EditForm(Form):
    name = StringField(u'抓去任务名', validators=[Required()])
    domain = StringField('domain', validators=[Required()])
    spider_dscription = TextField('spider_description',
                                  validators=[Required()])
    start_url = StringField('start_url', validators=[Required()])
    url_rules = StringField('url_rules', validators=[Required()])
    info_script = TextField('info_script')
    location = StringField('location', validators=[Required()])

    title = StringField('title', description=u'主题提取规则',
                        validators=[Required()])
    processor = StringField('processor', description=u'主讲者提取规则',
                            validators=[Required()])
    processor_intro = StringField('processor_intro', description=u'主讲者简介提取规则',
                                  validators=[Required()])
    datetime = StringField('datetime', description=u'时间日期提取规则',
                           validators=[Required()])
    description = StringField('description', description=u'描述提取规则',
                              validators=[Required()])
    position = StringField('position', description=u'位置提取规则',
                           validators=[Required()])
    suborg = StringField('suborg', description=u'子单位提取规则',
                         validators=[Required()])
