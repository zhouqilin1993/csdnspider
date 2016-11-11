# This is a program for IP limit using picture recognition.
# URL:    http://bbs.csdn.net/human_validations/new
# Input: human validations page
# Get the jpeg from the url.
# use picture recognition to get the string from the picture.
# Authentication pass!
import os
import sys
import time
import urllib2
import cookielib
import urllib
from cookielib import CookieJar

import pytesseract
from selenium import webdriver
from PIL import Image,ImageFilter,ImageEnhance
from selenium.webdriver.common import action_chains, keys

class Validate:

	def imageToString(self,picname):
		image = Image.open(picname)
		# image = spacFilter("median",image)
		image = image.filter(ImageFilter.EDGE_ENHANCE)
		image = image.convert('L')
		image = ImageEnhance.Contrast(image)
		image = image.enhance(2.0)
		ValidCode = pytesseract.image_to_string(image)
		image.save('valid.png')
		return ValidCode

	def validlogin(self,driver,cookie,validcode):
		# use the validcode to authentication
		PostUrl = "http://bbs.csdn.net/human_validations"		
		elem = driver.find_element_by_id("captcha")
		elem.send_keys(validcode)
		elem.send_keys(Keys.TAB)
		submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
		submit_button.click()
		cur_url = driver.current_url
		print (cur_url)
		if cur_url == PostUrl:
			return True
		else:
			return False

	def validpost(self,cookie,auth_token,captcha,captcha_key):
		cj = CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		formdata = { "authenticity_token" : auth_token, "captcha": captcha, "captcha_key" : captcha_key }
		data_encoded = urllib.urlencode(formdata)
		response = opener.open("http://bbs.csdn.net/human_validations", data_encoded)
		content = response.read()

		return True

	
	def validImageGet(self):
		AuthUrl = "http://bbs.csdn.net/human_validations/new"
		picname = 'captcha.png'
		# cookie = 
		# curdir = os.path.abspath('.')
					
		sel = webdriver.Chrome()
		sel.get(AuthUrl)
		cookie = sel.get_cookies()
		auth_token = sel.find_element_by_xpath('//input[@name="authenticity_token"]')
		captcha_key = sel.find_element_by_xpath('//input[@id="captcha_key"]')
		print (cookie)
		print (auth_token)
		print (captcha_key)

		# submit_button = sel.find_element_by_xpath('//button[@type="submit"]')
		# submit_button.submit()		
		time.sleep(0.3)
		# get te picture
		while True:
			picItem = sel.find_element_by_xpath('//img[@alt="captcha"]')
			submit_button = sel.find_element_by_xpath('//button[@type="submit"]')
			sel.save_screenshot(picname)
			left = picItem.location['x']
			top = picItem.location['y']
			right = picItem.location['x'] + picItem.size['width']
			bottom = picItem.location['y'] + picItem.size['height']
			im = Image.open(picname) 
			im = im.crop((left, top, right, bottom))
			im.save(picname)
			# validcode picture recognize
			time.sleep(1)
			validcode = self.imageToString(picname)
			print (validcode)

			validcode = input("please input:")
			if True: # if (len(validcode) == 6) & validcode.isalnum():
				if self.validpost(cookie,auth_token,validcode,captcha_key):# if self.validlogin(sel,cookie,validcode):
					print ('Authentication Pass!')
					break
			else:
				submit_button.click()
		
		time.sleep(10)
		sel.quit()




if __name__ == '__main__':
	ValidTest = Validate()
	ValidTest.validImageGet()


