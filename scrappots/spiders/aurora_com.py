import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrappots.items import ProductItem

class PotSpider(scrapy.Spider):
    name = "pot_spider"

    def start_requests(self):
        urls= [
            'https://www.auroramj.com/strains/'
        ]

        for url in urls:
            yield scrapy.Request(url= url, callback=self.parse)

 # data-name="Aurora Cloud CBD" data-thc="~20" data-cbd="~550" data-category="Cannabis Oil" data-type="Hybrid"

    def parse(self, response):
        # product_list = response.css('div.product-tile__info > h4 *::text').extract()
        product_list = response.css('#container')
        for product in product_list:
            item = ProductItem()
            item['title'] = product.css('.product-tile__title::text').extract_first().strip()
            item['vendor'] = product.css('.product-tile__vendor::text').extract_first().strip()
            item['price'] = product.css('.product-tile__price::text').extract_first().strip()
            #item['properties'] = product.css('.product-tile__properties::text').extract_first()
            item['image'] = product.css('img::attr(src)').extract_first().strip()
            yield item