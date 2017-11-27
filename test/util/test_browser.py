# -*- coding: utf-8 -*-
"""
    File Name : test_browser
    Author : livid
    Email: livid.xh@foxmail.com
    Create Time : 17/11/26 下午5:16
    Description : description what the main function of this file
    Change Activity:
         version0 : 17/11/26 下午5:16 by livid init 
    
"""
import unittest

from src.util.browser_util import BrowserUtil


class MyTestCase(unittest.TestCase):
    def test_something(self):
        browser = BrowserUtil()

        content = browser.get_url_content("http://npm.taobao.org/mirrors/chromedriver/2.33/")

        print(content)


if __name__ == '__main__':
    unittest.main()
