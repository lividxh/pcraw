# -*- coding: utf-8 -*-
"""
    File Name : test_craw_index
    Author : livid
    Email: livid.xh@foxmail.com
    Create Time : 17/11/26 下午5:36
    Description : description what the main function of this file
    Change Activity:
         version0 : 17/11/26 下午5:36 by livid init 
    
"""
import socket
import unittest
from datetime import datetime

import requests
import socks


class MyTestCase(unittest.TestCase):
    headers = {
        "Host": "t66y.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://t66y.com/",
        "Cookie": "__cfduid=dc59a61b87ddb7aa9bb2ba3e1a356a7bb1511689275",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    proxy = 'SOCKS5://127.0.0.1:1080'

    def test_index(self):
        proxy = dict(all=self.proxy) if self.proxy else None

        # socks.set_default_proxy(socks.SOCKS5, "localhost", 1080)
        # socket.socket = socks.socksocket

        response = requests.get("http://t66y.com/index.php", proxies=proxy, headers=self.headers)
        print(response.content)


if __name__ == '__main__':
    unittest.main()
