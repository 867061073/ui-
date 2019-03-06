#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '86706'
__mtime__ = '2019/2/27'
# qq:2456056533

佛祖保佑  永无bug!

"""


from HTMLTestRunner import  HTMLTestRunner
from datetime import datetime
import unittest
import os
#加载测试用例
from seng_email import send_email

case_dir='./test_case'
cases=unittest.defaultTestLoader.discover(case_dir,pattern='*.py')
if __name__ == '__main__':
    #send_email()
    report_file=open('./report/report{}.html'.format(datetime.now().strftime('%Y%m%d%H%M')),'w',encoding='utf8')
    runner=HTMLTestRunner(stream=report_file,title='测试报告')
    runner.run(cases)