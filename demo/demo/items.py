# -*- coding: utf-8 -*-
from scrapy import Item, Field

class DemoItem(Item):
	name = Field()
	state = Field()
	date = Field()
	# area = Field()
	visitor = Field()
	description = Field()
	link = Field()
	 
	 