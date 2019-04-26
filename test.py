#coding=utf8

import requests
from lxml import etree
import json
import re
import time
import pymysql

url = 'http://test-admin.linlangmao.cn/Comm_plat_linlang/userAccountInfoOld'

l = requests.get(url).json()

print(l)


exit()




url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'v=Am4uPhDVvuaOX8r9yCaZ157Nuc8zbzJpRDPmTZg32nEsewB5AP-CeRTDNlxr',
    'Host': 'q.10jqka.com.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',

}

detail1 = requests.get(url=url, headers=headers).content.decode('gbk')
tree1 = etree.HTML(detail1)
good_url = tree1.xpath('/html/body/table/tbody/tr[1]/text()')

print(good_url)


