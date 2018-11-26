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
        pot_list = response.css('div.product-tile__info > h4 *::text').extract()

        with open(filename, 'a+') as f:
            for pot_title in pot_list:
                f.write(pot_title + '\n')