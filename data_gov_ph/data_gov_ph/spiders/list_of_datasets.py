from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector

from data_gov_ph.items import DataSet


class PhilippinesSpider(CrawlSpider):
    name = "DataSetList"
    baseurl = "http://data.gov.ph/catalogue/dataset?page="
    allowed_domains = ['data.gov.ph']
    start_urls = [baseurl + str(x) for x in range(1, 54)]

    def parse(self, response):
        items = []
        sel = Selector(response)
        datasets = sel.css('.org')
        for dataset in datasets:
            item = DataSet()
            item['title'] = dataset.css('h1::text').extract()[0]
            item['link'] = dataset.css('.downlad::attr(href)').extract()[0]
            item['description'] = dataset.css('.package-description::text').extract()[0]
            items.append(item)
        return items
