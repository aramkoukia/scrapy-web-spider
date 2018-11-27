import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrappots.items import ProductItem

class PotSpider(scrapy.Spider):
    name = "pot_spider"

    def start_requests(self):
        urls= [
            'https://ocs.ca/collections/bongs?page=1',
            'https://ocs.ca/collections/bongs?page=2',
            'https://ocs.ca/collections/dried-flower-cannabis?page=1',
            'https://ocs.ca/collections/dried-flower-cannabis?page=2',
            'https://ocs.ca/collections/dried-flower-cannabis?page=3',
            'https://ocs.ca/collections/dried-flower-cannabis?page=4',
            'https://ocs.ca/collections/dried-flower-cannabis?page=5',
            'https://ocs.ca/collections/dried-flower-cannabis?page=6',
            'https://ocs.ca/collections/dried-flower-cannabis?page=7'
            'https://ocs.ca/collections/pre-rolled?page=1',
            'https://ocs.ca/collections/pre-rolled?page=2',
            'https://ocs.ca/collections/oils-and-capsules?page=1',
            'https://ocs.ca/collections/oils-and-capsules?page=2'
        ]

        for url in urls:
            yield scrapy.Request(url= url, callback=self.parse)

    def parse(self, response):
        # product_list = response.css('div.product-tile__info > h4 *::text').extract()
        product_list = response.css('.product-tile')
        for product in product_list:
            item = ProductItem()
            item['title'] = product.css('.product-tile__title::text').extract_first().strip()
            item['vendor'] = product.css('.product-tile__vendor::text').extract_first().strip()
            item['price'] = product.css('.product-tile__price::text').extract_first().strip()
            #item['properties'] = product.css('.product-tile__properties::text').extract_first()
            item['image'] = product.css('img::attr(src)').extract_first().strip()
            yield item