# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from models import Lecture, db

class PylecturePipeline(object):
    def process_item(self, item, spider):
        myitem = dict(**item)
        myitem.update({'spider_id': spider.sid})
        lecture = Lecture(**myitem)
        db.session.add(lecture)
        db.session.commit()
        return myitem
