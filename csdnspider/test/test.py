#encoding=utf-8
import os
import json

start_urls = []
curdir = os.path.abspath('..')
jsonfile = file(curdir + "/args/urlnum.json")
urlnum_json = json.load(jsonfile)
# print (urlnum_json)
for url_item in urlnum_json:
	url_head = url_item['url_base'][0]
	url_num = url_item['url_num'][0]
	for i in range(1,int(url_num)):
		url_link = url_head + str(i)
		start_urls.append(url_link)
print start_urls