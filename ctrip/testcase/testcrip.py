#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong

from ctrip.page.ctrip import  Ctrip
from ctrip.page.basetestcase import *
from ctrip.page.index import *


class CtripTest(BaseTestCase,Ctrip,CtripIndex):
	def test_Alogin(self):
		self.doLogin('15804256691','1qazxsw!')

	def test_bplace(self):
		self.place('三亚')

		self.assertEqual((self.getplacekeyword()),'三亚')

	def test_peoplecount(self):
		self.do_people_count()
		self.assertEqual((self.get_peoplecount_value()),'2成人 ')

	def test_checkIn_date(self):
		self.CheckINData('2019-05-01')
		self.Click_Hotel()
		self.assertEqual(self.get_CheckINData_Value(), '2019-05-01')

	def test_checkOut_date(self):
		self.CheckOutData('2019-05-04')
		self.assertEqual(self.get_CheckOutData_Value(), '2019-05-04')

	def test_input_keyword(self):
		self.Input_keyword('海棠湾')
		self.assertEqual(self.get_Input_keyword_value(), '海棠湾')

	def test_hotel_select(self):
		self.hotel_select('五星级/豪华')
		self.assertEqual(self.get_hotel_select_value(), '5')

	def test_search(self):
		self.search()


if __name__ == '__main__':
	unittest.main(verbosity=2)


