#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong

from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time as t


class WEB(object):
	def __init__(self,driver):
		self.driver=driver

	def find_element(self,*loc):
		try:
			return WebDriverWait(self.driver,20).until(
				lambda x:x.find_element(*loc))

		except (NoSuchElementException,KeyError,ValueError,Exception)as e:
			print('Error details:%s'%(e.args[0]))

	@property
	def wait(self):
		t.sleep(2)
