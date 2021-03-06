# coding=utf8

from models import Spider
from jinja2 import Template
from settings import SPIDER_TEMPLATE_PATH
from sqlalchemy.orm.attributes import InstrumentedAttribute


def gen_spider(i, tpl=None, dest=None):
    spider = Spider.query.get(i)
    if not tpl:
        tpl = SPIDER_TEMPLATE_PATH
    with open(tpl) as f:
        t = Template(f.read())
    if dest:
        with open(dest, 'w') as f:
            f.write(t.render(spider=spider).encode('utf8'))
    return t.render(spider=spider)


def scandb(model):
    d = model.__dict__
    return filter(lambda k: isinstance(d[k], InstrumentedAttribute), d)
