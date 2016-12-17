# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from demo.items import DemoItem

class DemoSpider(Spider):
	name = 'demo'
	allowed_urls = ['en.wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States']

	def parse(self, response):
		rows = response.xpath('//*[@id="mw-content-text"]/table[1]/tr').extract()

		for row in rows:
			name = Selector(text=row).xpath('//th/a/text()').extract()
			state = Selector(text=row).xpath('//td/a/text()').extract()
			date = Selector(text=row).xpath('//td[3]/span[2]/text()').extract()
			# area = Selector(text=row).xpath('//td[4]/span/text()').extract()
			visitor = Selector(text=row).xpath('//td[5]/text()').extract()
			description = Selector(text=row).xpath('//td[6]/text()').extract()
			link = Selector(text=row).xpath('//th/a/@href').extract()
			 

			item = DemoItem()
			item['name'] = name
			item['state'] = state
			item['date'] = date
			# item['area'] = area
			item['visitor'] = visitor
			item['description'] = description
			item['link'] = link
			 

			yield item 
			 

