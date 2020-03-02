# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MarvelpttItem(scrapy.Item):
	# 標題
	title = scrapy.Field()
	# 作者
	postUser = scrapy.Field()
	# 時間
	time = scrapy.Field() 
	# 推文數
	push = scrapy.Field()
