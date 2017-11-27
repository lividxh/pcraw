# -*- coding: utf-8 -*-
"""
    File Name : browser_util.py
    Author : livid
    Email: livid.xh@foxmail.com
    Create Time : 17/11/26 下午5:14
    Description : selenium 打开chrome获取html
    Change Activity:
         version0 : 17/11/26 下午5:14 by livid init 
    
"""
from selenium import webdriver


class BrowserUtil:
    """
    版本与驱动的对应关系: http://blog.csdn.net/huilan_same/article/details/51896672
    驱动下载地址: http://npm.taobao.org/mirrors/chromedriver/
    """

    def __init__(self):
        self.browser = webdriver.Chrome('/Users/livid/code/person/python/selnium-driver/chromedriver')

    def get_url_content(self, url):
        self.browser.get(url)
        return self.browser.page_source

    def close(self):
        self.browser.close()
