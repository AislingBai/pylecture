# coding=utf8

import scrapy
from datetime import datetime
from pylecture.items import PylectureItem
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request


class suesSpider(CrawlSpider):
    """
        上海工程技术大学，一所神奇的学校
    """
    sid = 1
    name = 'sues'
    domain = 'http://www.sues.edu.cn'
    start_urls = ['http://www.sues.edu.cn/']

    def parse(self, response):
        log.msg('URL')
        for url in response.xpath('//li[@class="t4"]//a/@href').extract():
            if self.domain not in url:
                url = self.domain + url
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        log.msg("Print")
        i = PylectureItem()
        
        i['description'] = ''.join(response.xpath('//div[@class="readinfo"]/p[7]').css('::text').extract())
        
        i['title'] = ''.join(response.xpath('//div[@class="readinfo"]/p[1]').css('::text').extract())
        
        i['suborg'] = ''.join(response.xpath('//div[@class="readinfo"]/p[6]').css('::text').extract())
        
        i['datetime'] = ''.join(response.xpath('//div[@class="readinfo"]/p[4]').css('::text').extract())
        
        i['processor_intro'] = ''.join(response.xpath('//div[@class="readinfo"]/p[3]').css('::text').extract())
        
        i['position'] = ''.join(response.xpath('//div[@class="readinfo"]/p[5]').css('::text').extract())
        
        i['processor'] = ''.join(response.xpath('//div[@class="readinfo"]/p[2]').css('::text').extract())
        
        return i