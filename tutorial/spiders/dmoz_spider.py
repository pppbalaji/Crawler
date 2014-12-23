
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name = "gigstart"
	allowed_domains = ["gigstart.com"]
	start_urls = [
        "http://www.gigstart.com/"
       
	]

	def parse(self, response):
		for sel in response.xpath('//noscript'):
			item=DmozItem()
			item['name'] = sel.xpath('a/text()').extract()
			yield item