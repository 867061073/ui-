#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '86706'
__mtime__ = '2019/2/27'
# qq:2456056533

佛祖保佑  永无bug!

"""


import unittest
from web.add import add

class Test_Cul(unittest.TestCase):


    def test_add(self):
        self.assertEqual(3,add(2,1))



if __name__ == '__main__':
    unittest.main()
