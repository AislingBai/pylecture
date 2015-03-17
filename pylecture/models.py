# coding=utf8

import os
from flask_sqlalchemy import SQLAlchemy
from pylecture import app
from settings import DB_SAVE_PATH 

app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + DB_SAVE_PATH,
})
db = SQLAlchemy(app)


class Spider(db.Model):
    """ 爬虫基本信息管理 """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, doc=u'名字')
    domain = db.Column(db.String(100), doc=u'允许的域')
    description = db.Column(db.Text, doc=u'描述')

    start_url = db.Column(db.String(200), doc=u'Feed 订阅页面')
    url_rules = db.Column(db.String(80), doc=u'匹配URL规则')
    info_script = db.Column(db.Text, doc=u'抓取信息脚本')

    location = db.Column(db.String(20), doc=u'地区')
    org = db.Column(db.String(20), doc=u'承办机构')

    @property
    def rules(self):
        rules = LectureRules.query.filter_by(spider_id=self.id).first()
        fields = ['title', 'processor', 'processor_intro', 'datetime',
                  'description', 'position', 'suborg']
        return {k: getattr(rules, k) for k in fields}


class LectureRules(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(80), doc=u'主题提取规则')
    processor = db.Column(db.String(80), doc=u'主讲者提取规则')
    processor_intro = db.Column(db.String(80), doc=u'主讲者简介提取规则')
    datetime = db.Column(db.String(80), doc=u'时间日期提取规则')
    description = db.Column(db.String(80), doc=u'描述提取规则')
    position = db.Column(db.String(80), doc=u'位置提取规则')
    suborg = db.Column(db.String(80), doc=u'子单位提取规则')

    spider_id = db.Column(db.ForeignKey('spider.id'), unique=True)
    spider = db.relationship('Spider')


class Lecture(db.Model):
    """ 讲座信息持久化数据模型 """
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), doc=u'来源页URL')

    title = db.Column(db.String(80), doc=u'讲座主题')
    processor = db.Column(db.String(40), doc=u'演讲者')
    processor_intro = db.Column(db.Text, doc=u'演讲者简介')
    datetime = db.Column(db.String(40), doc=u'日期和时间')
    description = db.Column(db.Text, doc=u'演讲描述')
    position = db.Column(db.String(100), doc=u'具体位置')
    suborg = db.Column(db.String(100), doc=u'承办子单位')

    spider_id = db.Column(db.Integer, db.ForeignKey('spider.id'),
                          doc=u'使用哪个爬虫')
    spider = db.relationship('Spider')


def reset_db():
    db.drop_all()
    init_db()


def init_db():
    if not os.path.exists(DB_SAVE_PATH):
        db.create_all()

        spider = Spider(
            name='sues',
            description=u'上海工程技术大学，一所神奇的学校',
            domain='http://www.sues.edu.cn',
            start_url='http://www.sues.edu.cn/',
            url_rules='//li[@class="t4"]//a/@href',
            info_script="""
            """,
            location='310000',
            org=u'上海工程技术大学',
        )
        try:
            db.session.add(spider)
            db.session.commit()
        except:
            db.session.callback()

        lecture_rules = LectureRules(
            title='//div[@class="readinfo"]/p[1]',
            processor='//div[@class="readinfo"]/p[2]',
            processor_intro='//div[@class="readinfo"]/p[3]',
            datetime='//div[@class="readinfo"]/p[4]',
            description='//div[@class="readinfo"]/p[7]',
            position='//div[@class="readinfo"]/p[5]',
            suborg='//div[@class="readinfo"]/p[6]',
            spider_id=spider.id,
        )

        db.session.add(lecture_rules)
        db.session.commit()

if __name__ == '__main__':
    init_db()
