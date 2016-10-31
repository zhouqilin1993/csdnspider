#encoding=utf-8
import os
import scrapy
import json
from csdnspider.items import ForumQuestionItem

class ForumSpider(scrapy.Spider):
	name = "forum_spider"
	allowed_domains = ["bbs.csdn.net"]
	start_urls = []
	curdir = os.path.abspath('.')
	jsonfile = file(curdir + "/args/urlnum.json")
	urlnum_json = json.load(jsonfile)
	for url_item in urlnum_json:
		url_head = url_item['url_base'][0]
		url_num = url_item['url_num'][0]
		for i in range(1,int(url_num)):
			url_link = url_head + str(i)
			start_urls.append(url_link)
	# print start_urls
	
	def parse(self, response):
		for sel in response.xpath('//tr'):
			question_item = ForumQuestionItem()
			question_item['forum_topic'] = sel.xpath('td[1]/span[@class = "parent"]/a/@href').extract()
			question_item['forum_title'] = sel.xpath('td[1]/a/@title').extract()
			question_item['forum_url'] = sel.xpath('td[1]/a/@href').extract()
			question_item['forum_point'] = sel.xpath('td[2]/text()').extract()
			question_item['forum_question_user'] = sel.xpath('td[3]/a/@href').extract()
			question_item['forum_question_time'] = sel.xpath('td[3]/span[@class = "time"]/text()').extract()
			question_item['forum_answer_number'] = sel.xpath('td[4]/text()').extract()
			question_item['forum_update_user'] = sel.xpath('td[5]/a/@href').extract()
			question_item['forum_update_time'] = sel.xpath('td[5]/span[@class = "time"]/text()').extract()
			yield question_item
