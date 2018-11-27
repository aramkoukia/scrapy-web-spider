import scrapy

filename = 'potinfo.txt'

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
        with open(filename, 'a+') as f:
            for product in product_list:
                title = product.css('.product-tile__title::text').extract_first().strip()
                vendor = product.css('.product-tile__vendor::text').extract_first().strip()
                price = product.css('.product-tile__price::text').extract_first().strip()
                #properties = product.css('.product-tile__properties::text').extract_first()
                image = product.css('img::attr(src)').extract_first().strip()
                
                f.write(
                    title + ',' +
                    vendor + ',' +                    
                    price + ',' +
                    #properties + ',' +
                    image + '\n')