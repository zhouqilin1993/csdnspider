#encoding=utf-8
import os
import scrapy
from csdnspider.items import UrlItem

class UrlgetSpider(scrapy.Spider):
	name = "urlget_spider"
	allowed_domains = ["bbs.csdn.net"]
	start_urls = []
	curdir = os.path.abspath('.')
	forums_urls_file = open(curdir + "/args/forums_urls")
	for forum_url in forums_urls_file:
		forum_url_link = forum_url[0:-1]
		start_urls.append(forum_url_link)
	
	def parse(self, response):
		url_item = UrlItem()
		url_item['url_base'] = response.xpath('//div[@class = "bread_nav"]/a[last()]/@href').extract()
		url_item['url_num'] = response.xpath('//div[@class = "page_nav"]/ul/li[last()]/span[2]/text()').extract()
		yield url_item

