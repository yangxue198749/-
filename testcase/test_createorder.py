#!/usr/bin/python
#coding=utf-8
'''
@File  : test_createorder.py
@Author: yangxue
@Date  : 2019/4/29 11:01
@Desc  : 
'''

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

    def test_creat_order1(self):
        rec_obj=createtest.testcaseread()
        rec=rec_obj.get_xls('testcase.xls','createorder')
        for i in range(len(rec)):
            if rec[i][1]=='post':
                self.url=''.join(self.baseurl+rec[i][2])
                self.data=rec[i][3]
                res=self.post_obj.post(url=self.url,data=self.data)
                res=res.json()
                if res['return_code']==rec[i][4]:
                    rec_obj.write_xls('testcase.xls','createorder',i,'pass')
                else:
                    rec_obj.write_xls('testcase.xls', 'createorder',i, 'fail')
                # return res
            elif rec[i][1] =='get':
                # self.url=''.join(self.baseurl+rec[i][2])
                self.url = rec[i][2]
                res=obj.get(url=self.url)
                # res=res.json()
                print(res,type(res))
                if res.status_code==200:
                    rec_obj.write_xls('testcase.xls', 'createorder', i, 'pass')
                else:
                    rec_obj.write_xls('testcase.xls', 'createorder', i, 'fail')

#



if __name__== "__main__":
    # testunit=unittest.TestSuite()
    # testunit.addTest(mytest('test1'))
    test_dir='D:\\python\\interfacetest\\testcase'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    f=open('D:\\python\\interfacetest\\result\\res.html','wb')
    runer=HTMLTestRunner(stream=f,title='testreport',description='no')
    runer.run(discover)
    f.close()