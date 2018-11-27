from scrapy.item import Item, Field


class ProductItem(Item):
    title = Field()
    vendor = Field()
    price = Field()
    properties = Field()
    image = Field()
    url = Field()
