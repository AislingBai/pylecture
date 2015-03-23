# coding=utf8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, BooleanField, TextAreaField
from wtforms.validators import Required


class EditForm(Form):
    name = StringField(u'任务名（英文）', validators=[Required()])
    domain = StringField(u'允许的域', validators=[Required()])
    spider_dscription = TextField(u'描述',
                                  validators=[Required()])
    start_url = StringField(u'订阅页面', validators=[Required()])
    url_rules = StringField(u'匹配URL规则', validators=[Required()])
    info_script = TextAreaField(u'抓取信息脚本')
    location = StringField(u'地区', validators=[Required()])

    title = StringField(u'主题提取规则',
                        validators=[Required()])
    processor = StringField(u'主讲者提取规则',
                            validators=[Required()])
    processor_intro = StringField(u'主讲者简介提取规则',
                                  validators=[Required()])
    datetime = StringField(u'时间日期提取规则',
                           validators=[Required()])
    description = StringField(u'描述提取规则',
                              validators=[Required()])
    position = StringField(u'位置提取规则',
                           validators=[Required()])
    suborg = StringField(u'子单位提取规则',
                         validators=[Required()])
    submit = SubmitField()
