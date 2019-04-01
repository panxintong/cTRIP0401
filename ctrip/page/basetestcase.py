#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong

import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Firefox()
		cls.driver.maximize_window()
		cls.driver.get('http://www.ctrip.com')
		cls.driver.implicitly_wait(30)

	@classmethod
	def tearDownClass(cls):
		# cls.driver.quit()
		pass
