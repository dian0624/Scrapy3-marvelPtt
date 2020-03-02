# -*- coding: utf-8 -*-
import scrapy
from marvelPtt.items import MarvelpttItem

class MyspiderSpider(scrapy.Spider):
    name = 'marvelCrawl'
    page = int(input("請輸入頁數:"))
    urla = 'https://www.ptt.cc/bbs/marvel/index'
    urlb = '.html'
    start_urls = []
    for i in range(1,page+1):
    	start_urls.append(urla+str(i)+urlb)

    def parse(self, response):
        data = response.body.decode()
        selector = scrapy.Selector(text=data)
        total = selector.xpath('//*[@id="main-container"]/div[2]/div')
        
        for article in total:
            item = MarvelpttItem()
            x1 = article.xpath('./div[2]/a/text()').extract()
            if len(x1) == 0:
                continue
            else:
                item['title'] = x1[0]
                item['postUser'] = article.xpath('./div[3]/div[1]/text()').extract()[0]
                item['time'] = article.xpath('./div[3]/div[3]/text()').extract()[0]

                x2 = article.xpath('./div/span/text()').extract()
                if len(x2) == 0:
                	item['push'] = '0'
                else:
                	item['push'] = x2[0]
                yield item
