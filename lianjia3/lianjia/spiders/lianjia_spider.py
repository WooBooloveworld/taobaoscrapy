# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem



class lianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["lianjia.com"]
    start_urls = ['https://nj.lianjia.com/xiaoqu/']

    def parse(self,response):
        url = response.url
        for page in range(1,101):
            all_page_url = url+'pg'+str(page)
            request = scrapy.Request(all_page_url,callback=self.allpage)
            yield request

    def allpage(self,response):
        a_page_list = response.xpath('//ul[@class="listContent"]//li//@data-housecode')
        for a_page_url in a_page_list:
            b_page_url = a_page_url.extract()
            all_page_url = 'https://nj.lianjia.com/xiaoqu/'+b_page_url
            request = scrapy.Request(all_page_url,callback=self.parse_nj_price)
            yield request


    def parse_nj_price(self, response):
        item = LianjiaItem()
        item['detailTitle'] = response.xpath('.//div[@class="detailHeader fl"]//h1/text()').extract()
        item['detailDesc'] = response.xpath('.//div[@class="detailHeader fl"]//div/text()').extract()
        item['price'] = response.xpath('.//span[@class="xiaoquUnitPrice"]/text()').extract()
        item['allinfo'] = response.xpath('.//span[@class="xiaoquInfoContent"]/text()').extract()
        item['url'] = response.url
           
        yield item
















