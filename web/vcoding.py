#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '86706'
__mtime__ = '2019/3/2'
# qq:2456056533

佛祖保佑  永无bug!

"""


from  selenium import  webdriver
import time

url='http://test.vcoding.com/login/'
deiver=webdriver.Chrome()
time.sleep(3)



def login(username,password):
    deiver.get(url)
    deiver.find_element_by_id('username').send_keys(username)
    deiver.find_element_by_id('password').send_keys(password)
    deiver.find_element_by_id('submit').click()
    print(deiver.title)
    if '用户中心'==deiver.title:
        print('{}用密码{}登录成功'.format(username,password))
    else:
        print('{}用密码{}登录失败'.format(username, password))

def logout():
    time.sleep(2)
    deiver.find_element_by_partial_link_text('管理').click()
    time.sleep(2)
    deiver.find_element_by_partial_link_text('退出').click()




if __name__ == '__main__':
    login()
    logout()