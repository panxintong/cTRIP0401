#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong


from ctrip.Base.base import WEB
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Ctrip(WEB):
	click_loc=(By.XPATH,'/html/body/div[5]/div/ul[2]/li[1]/a/span/span')
	userName_loc = (By.XPATH, '//*[@id="nloginname"]')
	password_loc = (By.XPATH, '//*[@id="npwd"]')
	clickButton_loc = (By.ID, 'nsubmit')
	error_loc = (By.ID, "personErr")
	swipe_tag_loc=(By.CLASS_NAME,'cpt-drop-btn')

	def click(self):
		u'''点击您好请登录'''
		self.find_element(*self.click_loc).click()

	def getUserTextField(self, username):
		u'''输入用户名'''
		self.wait
		self.find_element(*self.userName_loc).send_keys(username)

	def getPasswordField(self, password):
		u'''输入密码'''
		self.wait
		self.find_element(*self.password_loc).send_keys(password)

	def getSubmitButton(self):
		u'''点击确认按钮'''
		self.wait
		self.find_element(*self.clickButton_loc).click()

	def getLoginErrorDiv(self):
		u'''提示错误信息'''
		self.wait
		return self.find_element(*self.error_loc).text

	def doLogin(self, username, password):
		self.click()
		self.getUserTextField(username)
		self.getPasswordField(password)
		self.getSubmitButton()

	# def swipe_tag(self):
	# 	u'''测试如果用户登录过程中出现滑动模块'''
	# 	try:
	# 		button = self.find_element(*self.swipe_tag_loc)  # 找到“滑块”
	# 		action = ActionChains(self.driver)  # 实例化一个action对象
	# 		action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
	# 		action.reset_actions()
	# 		action.move_by_offset(0, 20).perform()  # 移动滑块
	#
	# 	except Exception as e:
	# 		e.args[0]


