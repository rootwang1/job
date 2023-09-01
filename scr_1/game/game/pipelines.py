#数据存储

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GamePipeline:#随意定义一个类
    def process_item(self, item, spider):  #处理数据的专用方法  item数据 spider爬虫
        return item#必须返回一个数据，否则下一个管道不能拿到数据
