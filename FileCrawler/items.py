# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    file_urls = scrapy.Field()
    publish_date = scrapy.Field()
    title = scrapy.Field()
    file_name = scrapy.Field()
    pass
