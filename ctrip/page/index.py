#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong

from ctrip.Base.base import WEB
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time as t


class CtripIndex(WEB):
	place_loc=(By.XPATH,'//*[@id="HD_CityName"]')
	roomnumber_loc=(By.ID,'J_roomCountList]')
	peoplecount_loc=(By.ID,'J_RoomGuestInfoTxt')
	click_icon_loc=(By.CLASS_NAME,'icon_numplus')
	click_confirm_loc=(By.ID,'J_RoomGuestInfoBtnOK')
	CheckINData_loc=(By.ID,'HD_CheckIn')
	click_Hotel_loc=(By.XPATH,'/html/body/div[12]/div/ul/li[1]/b')
	checkOutData_loc=(By.ID,'HD_CheckOut')
	Input_keyword_loc=(By.XPATH,'//*[@id="HD_TxtKeyword"]')
	search_button_loc=(By.XPATH,'//*[@id="HD_Btn"]')
	Hotel_select_loc=(By.ID,'searchHotelLevelSelect')

	def place(self,placename):
		u'''目的地'''
		self.find_element(*self.place_loc).clear()
		self.wait
		self.find_element(*self.place_loc).send_keys(placename)

	def getplacekeyword(self):
		u'''获取目的地输入关键字'''
		return self.find_element(*self.place_loc).get_attribute('value')

	def peoplecount(self):
		u'''住客数'''
		self.find_element(*self.peoplecount_loc).click()

	def click_icon(self):
		u'''点击加号按钮'''
		self.find_element(*self.click_icon_loc).click()

	def click_confirmButton(self):
		u'''点击确认按钮'''
		self.find_element(*self.click_confirm_loc).click()

	def do_people_count(self):
		u'''执行住客数的方法'''
		self.peoplecount()
		self.wait
		self.click_icon()
		self.wait
		self.click_confirmButton()

	def get_peoplecount_value(self):
		u'''获取输入的住客数的人数'''
		return self.find_element(*self.peoplecount_loc).get_attribute('value')

	def CheckINData(self,checkIndate):
		u'''入住日期'''
		self.wait
		self.find_element(*self.CheckINData_loc).clear()
		self.wait
		self.find_element(*self.CheckINData_loc).send_keys(checkIndate)

	def Click_Hotel(self):
		u'''点击酒店'''
		self.find_element(*self.click_Hotel_loc).click()

	def get_CheckINData_Value(self):
		u'''获取入住日期'''
		return self.find_element(*self.CheckINData_loc).get_attribute('value')

	def CheckOutData(self,checkOutdate):
		u'''退房日期'''
		self.wait
		self.find_element(*self.checkOutData_loc).clear()
		self.wait
		self.find_element(*self.checkOutData_loc).send_keys(checkOutdate)
		self.wait
		self.Click_Hotel()

	def get_CheckOutData_Value(self):
		u'''获取退房日期'''
		return self.find_element(*self.checkOutData_loc).get_attribute('value')

	def Input_keyword(self,keyword):
		self.find_element(*self.Input_keyword_loc).clear()
		u'''输入关键字'''
		self.find_element(*self.Input_keyword_loc).send_keys(keyword)

	def get_Input_keyword_value(self):
		u'''获取输入关键字'''
		return self.find_element(*self.Input_keyword_loc).get_attribute('value')

	def hotel_select(self,level):
		u'''定位到酒店级别：下拉选框'''
		HL=self.find_element(*self.Hotel_select_loc)
		select = Select(HL)
		self.wait
		select.select_by_visible_text(level)

	def get_hotel_select_value(self):
		u'''获取酒店级别'''
		return self.find_element(*self.Hotel_select_loc).get_attribute('value')

	def search(self):
		u'''点击search按钮'''
		self.find_element(*self.search_button_loc).click()









