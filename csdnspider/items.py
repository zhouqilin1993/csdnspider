# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ForumQuestionItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    forum_topic = scrapy.Field()
    forum_title = scrapy.Field()
    forum_url = scrapy.Field()
    forum_point = scrapy.Field()
    forum_question_user = scrapy.Field()
    forum_question_time = scrapy.Field()
    forum_answer_number = scrapy.Field()
    forum_update_user = scrapy.Field()
    forum_update_time = scrapy.Field()
    pass

class UrlItem(Item):
    url_base = scrapy.Field()
    url_num = scrapy.Field()
    pass


# class ForumCommentsItem(Item):
#     comments_floor = scrapy.Field()
#     comments_time = scrapy.Field()
#     comments_up_num = scrapy.Field()
#     comments_down_num = scrapy.Field()
#     comments_point = scrapy.Field()
#     comments_body_url = scrapy.Field()
#     comments_body_text = scrapy.Field()
#     comments_body_jpeg = scrapy.Field()
#     pass