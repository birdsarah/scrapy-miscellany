from scrapy.item import Item, Field


class DataSet(Item):
    title = Field()
    description = Field()
    link = Field()
