# -*- coding: utf-8 -*-

# Scrapy settings for pylecture project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os

BOT_NAME = 'pylecture'

SPIDER_MODULES = ['pylecture.spiders']
NEWSPIDER_MODULE = 'pylecture.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pylecture (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'pylecture.pipelines.PylecturePipeline': 300,
}

LOG_LEVEL = 'DEBUG'

SPIDER_TEMPLATE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                    'spiders', 'lecture.tmpl')
DB_SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'db.sqlite')
