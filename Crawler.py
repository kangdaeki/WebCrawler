#!/Users/user/AppData/Local/Microsoft/WindowsApps/python3.exe
# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    start_urls = ["https://quotes.toscrape.com/tag/humor/",]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

"""
#####!/usr/bin/env python
"""

