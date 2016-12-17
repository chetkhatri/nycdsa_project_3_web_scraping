# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem

class ValidateItemPipeline(object):
	def process_item(self, item, spider):
		if not all(item.values()):
			raise DropItem("Missing values!")
		else:
			return item

class WriteItemPipeline(object):
	def __init__(self):
		self.file_name = open('test_name.txt', 'w')
		self.file_state = open('test_state.txt', 'w')
		self.file_date = open('test_date.txt', 'w')
		self.file_visitor = open('test_visitor.txt', 'w')

	def process_item(self, item, spider):
		line_name = str(str(item['name'][0]) + '\n')
		line_state = str(str(item['state'][0]) + '\n')
		line_date = str(str(item['date'][0]) + '\n')
		#line = str(str(item['area'][0]) + '\n')
		line_visitor = str(str(item['visitor'][0]) + '\n')
		#line = str(str(item['description'][0]) + '\n')
		#line = str(str(item['link'][0]) + '\n')
		self.file_name.write(line_name)
		self.file_state.write(line_state)
		self.file_date.write(line_date)
		self.file_visitor.write(line_visitor)
		return item