# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem



class lianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["lianjia.com"]
    start_urls = ['https://nj.lianjia.com/ershoufang/']

    def parse(self,response):
        url = response.url
        for page in range(1,101):
            all_page_url = url+'pg'+str(page)
            request = scrapy.Request(all_page_url,callback=self.allpage)
            yield request

    def allpage(self,response):
        a_page_list = response.xpath('//li[@class="clear"]//a//@data-housecode')
        for a_page_url in a_page_list:
            b_page_url = a_page_url.extract()
            all_page_url = 'https://nj.lianjia.com/ershoufang/'+b_page_url+'.html'
            request = scrapy.Request(all_page_url,callback=self.parse_nj_price)
            yield request


    def parse_nj_price(self, response):
        item = LianjiaItem()
        item['unitprice'] = response.xpath('.//div[@class="unitPrice"]//span/text()').extract()
        item['price'] = response.xpath('.//div[@class="price"]//span/text()').extract()
        item['room'] = response.xpath('.//div[@class="room"]//div/text()').extract()
        item['communityName'] = response.xpath('.//div[@class="communityName"]//a/text()').extract()
        item['info'] = response.xpath('.//span[@class="info"]//a/text()').extract()
        item['allinfo'] = response.xpath('.//div[@class="content"]//li/text()').extract()
        item['url'] = response.url
           
        yield item
















