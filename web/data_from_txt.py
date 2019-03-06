#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '86706'
__mtime__ = '2019/3/3'
# qq:2456056533

佛祖保佑  永无bug!

"""
from  web.vcoding import *


lines=None
with open('vcoding_txt',encoding='utf8') as f:
    lines=f.readlines()

for line in lines:
    u=line.split(',')[0]
    p=line.split(',')[1].rsplit()
    login(u,p)

logout()

