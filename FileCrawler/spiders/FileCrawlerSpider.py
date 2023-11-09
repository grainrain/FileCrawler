import os

import scrapy
from scrapy import Selector

from FileCrawler.items import FilecrawlerItem


class FilecrawlerspiderSpider(scrapy.Spider):
    name = "FileCrawlerSpider"
    allowed_domains = ["xmu.edu.cn"]

    def start_requests(self):
        urls = [
            'https://dblab.xmu.edu.cn/topic/teaching/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        records = response.xpath("//div[contains(@class,'page-list')]")
        for record in records:
            title = record.xpath("./ul/li/span[1]/a/@title").extract_first()
            url = record.xpath("./ul/li/span[1]/a/@href").extract_first()
            publish_date = record.xpath("./ul/li/span[2]/text()").extract_first()
            yield scrapy.Request(url=url, callback=self.parse_content,
                                 meta={'title': title,
                                       'url': url,
                                       'publish_date': publish_date
                                       })
        next_page = response.xpath("//a[contains(@class,'nextpostslink')]/@href").extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
        pass

    def parse_content(self, response):
        title = response.meta['title']
        url = response.meta['url']
        publish_date = response.meta['publish_date']
        docs = response.xpath("//a[contains(@href,'.pdf')]/@href "
                              "| //a[contains(@href,'.ppt')]/@href"
                              "| //a[contains(@href,'.pptx')]/@href"
                              "| //a[contains(@href,'.pptx')]/@href"
                              "| //a[contains(@href,'.doc')]/@href"
                              "| //a[contains(@href,'.docx')]/@href"
                              "| //a[contains(@href,'.xls')]/@href"
                              "| //a[contains(@href,'.xlsx')]/@href").extract()
        if len(docs) > 0:
            for doc in docs:
                file_urls = list()
                file_url = str(doc)
                file_name = os.path.basename(file_url)
                file_urls.append(file_url)
                filecrawlerItem = FilecrawlerItem()
                filecrawlerItem["file_urls"] = file_urls
                filecrawlerItem["title"] = str(title)
                filecrawlerItem["publish_date"] = str(publish_date)
                filecrawlerItem["file_name"] = str(file_name)
                print(title[0:30], '/', file_name)
                yield filecrawlerItem
