

import scrapy


class XiaoSpider(scrapy.Spider):
    name = "xiao"
    allowed_domains = ["4399.com"]
    start_urls = ["https://4399.com/flash/"]

    def parse(self, response):
        li_list = response.xpath("//ul[@class='n-game cf']/li")  # 提取数据
        for li in li_list:
            #xpath默认返回的是selector对象
            #想要返回需要#extract()返回列表
            # name = li.xpath("./a/b/text()").extract_first()  #extract_first() 返回一个数据，如果没有，返回None
            date = li.xpath("./em/text()").extract_first()


            dic = {
                "date":date
            }
            #用yield 将字典数据传送给管道，返回数据，把数据传给pipelines,进行数据化存取
            yield dic
