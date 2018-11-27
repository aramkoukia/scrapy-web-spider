import scrapy

filename = 'potinfo.txt'

class PotSpider(scrapy.Spider):
    name = "pot_spider"

    def start_requests(self):
        urls= [
            'https://ocs.ca/collections/bongs?page=1',
            'https://ocs.ca/collections/bongs?page=2',
        ]

        for url in urls:
            yield scrapy.Request(url= url, callback=self.parse)

    def parse(self, response):
        # product_list = response.css('div.product-tile__info > h4 *::text').extract()
        product_list = response.css('.product-tile')
        with open(filename, 'a+') as f:
            for product in product_list:
                title = product.css('.product-tile__title::text').extract_first()
                vendor = product.css('.product-tile__vendor::text').extract_first()
                price = product.css('.product-tile__price::text').extract_first()
                image = product.css('img::attr(src)').extract_first()
                
                f.write(
                    title + ',' +
                    vendor + ',' +                    
                    price + ',' +
                    image + '\n')