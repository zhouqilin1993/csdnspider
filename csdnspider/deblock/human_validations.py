# This is a program for IP limit using picture recognition.
# URL:    http://bbs.csdn.net/human_validations/new
# Input: human validations page
# Get the jpeg from the url.
# use picture recognition to get the string from the picture.
# Authentication pass!


import urllib2
import cookielib
import urllib
import re
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

AuthUrl = "http://bbs.csdn.net/human_validations/new"
PostUrl = "http://bbs.csdn.net/human_validations"

cookie = cookielib.MozillaCookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

# req = urllib2.Request(AuthUrl)
# response = urllib2.urlopen(req)
# print ("response: "+response)
print ("cookie: "+str(cookie))
html = opener.open(AuthUrl).read()
print ("html: "+html)
print ("cookie: "+str(cookie))
# CaptchaUrl 
curdir = os.path.abspath('.')
picpath = curdir + "/args/pic/simple_captcha.jpg"
local = open(picpath, 'wb')
local.write(picture)
local.close()
