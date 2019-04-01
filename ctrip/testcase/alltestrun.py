#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong

import time

import unittest
from HTMLTestRunner import HTMLTestRunner


if __name__ == "__main__":
    # 测试用例目录
    test_dir = r"E:\PycharmProject\testpractice\ctrip\testcase"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, 'test*.py')
    # 测试报告路径
    report_path = r"E:\PycharmProject\testpractice\ctrip\report\report.html"

    with open(report_path,"wb") as report:
        runner = HTMLTestRunner(stream = report,
                                title = "Ctrip test report",
                                description = "Ctrip auto test report ")
        runner.run(discover)




