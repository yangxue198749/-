#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : createtest.py
@Author: yangxue
@Date  : 2019/4/29 9:50
@Desc  : 
'''
from xlrd import open_workbook
from core import ReadCofig
import os
from xlutils.copy import copy

r=ReadCofig.ReadConfig()
TestCasePath=r.get_item('testdata')

class testcaseread:

    def get_xls(self,xls_name,sheet_name):
        cls=[]
        self.xls_path=os.path.join(TestCasePath['base_dir'],xls_name)
        self.p=open_workbook(self.xls_path)
        self.sheet=self.p.sheet_by_name(sheet_name)
        for i in range(self.sheet.nrows):
            if self.sheet.row_values(i)[0] != 'case_name':
                cls.append(self.sheet.row_values(i))

        return cls

    def write_xls(self,xls_name,sheet_name,row,result):
        xls_path = os.path.join(TestCasePath['base_dir'], xls_name)
        contentold=open_workbook(xls_path)
        # print(contentold)
        contentnew=copy(contentold)
        # print(contentnew)
        newws=contentnew.get_sheet(sheet_name)
        newws.write(row+1,6,result)
        contentnew.save(xls_path)






#
# t=testcaseread()
# r=t.get_xls('testcase.xls','createorder')
# print(r)
# t.write_xls('D:\\python\\interfacetest\\testfile\\testcase.xls','createorder',1,'ok')

