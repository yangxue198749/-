#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : creatorderDemo.py
@Author: yangxue
@Date  : 2019/5/14 16:50
@Desc  : 
'''

from core import createtest
from core import SingHandler
import json

templat="""
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class mytest(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass
"""

tempcase="""
    def test_creatorder%s(self):
        self.url=''.join(self.baseurl+'%s')
        self.data='%s'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'%s')
"""
sing=SingHandler.Singhadler()
def write_templet():
    with open('TestCreateOrder.py','a+') as f:
        f.write(templat)
        rec_obj = createtest.testcaseread()
        rec = rec_obj.get_xls('testcase.xls', 'createorder')
        for i in range(len(rec)-1):
            data=json.dumps(sing.sing(rec[i][3]))
            if rec[i][1] == 'post':
                f.write(tempcase%(i,rec[i][2],data,rec[i][4]))
                
write_templet()
