#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '86706'
__mtime__ = '2019/3/3'
# qq:2456056533

佛祖保佑  永无bug!

"""
from web.vcoding import *
from web.vcoding_dict import user

for u in user:
    login(u.get('username'),u.get('password'))

logout()
