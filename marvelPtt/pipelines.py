# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class MarvelpttPipeline(object):
    def process_item(self, item, spider):
    	print('==================================')
    	print(item['title'],item['postUser'],item['time'],item['push'],sep=',')
    	print('==================================')
        # with open('marvel.csv','a+') as f:
        #     writer = csv.writer(f)
        #     print(item['title'],item['postUser'],item['time'],item['push'],sep=',')
        #     L = [item['title'],item['postUser'],item['time'],item['push']]
        #     writer.writerow(L)
       	#     return item 
        # print('儲存成功')
