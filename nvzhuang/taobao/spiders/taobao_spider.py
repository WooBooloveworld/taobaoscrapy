# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem



class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = ['https://shopsearch.taobao.com/search?app=shopsearch&spm=a230r.7195193.0.0.Qx5BDv&q=%E5%A5%B3%E8%A3%85&tracelog=shopsearchnoqcat&shop_type=&ratesum=huang&isb=0&goodrate=9900%2C&fs=1&special=yes&loc=&s=']


    
    def parse(self,response):
        url = response.url
        for page in range(1,2000,20):
            all_page_url = url+str(page)
            request = scrapy.Request(all_page_url,callback=self.allnvzhuang)
            yield request


    def allnvzhuang(self, response):
        item = TaobaoItem()
        x = response.xpath('//div[@class="count count5"]//em')
        item['city'] = x.xpath('text()').extract()
        item['url'] = response.url

        yield item
















