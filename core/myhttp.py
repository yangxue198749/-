#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : myhttp.py
@Author: yangxue
@Date  : 2019/4/29 9:19
@Desc  : 
'''

import requests
from core import ReadCofig
from log import log


h=ReadCofig.ReadConfig()
d=h.get_item('http')

class myhttp:
    def __init__(self):
        host=d['baseurl']
        port=d['port']
        self.timeout=d['timeout']
        self.log=log.log('myhttp','httplog.txt')
        self.header={}
        self.params={}
        self.data={}
        self.url=None
        self.files={}

    def set_url(self,url):
        self.url=host+self.url

    def set_header(self,header):
        self.header=header

    def set_header(self,params):
        self.params=params

    def set_data(self,data):
        self.data=data

    def set_files(self,file):
        self.files=file


    def get(self,**kwargs):
        try:
            res=requests.get(**kwargs)
            return res
        except TimeoutError:
            self.log.error('timeout')
            return None


    def post(self,**kwargs):
        try:
            # res=requests.post(self.url,data=self.data,header=self.header,files=self.files,timeout=self.timeout)
            res = requests.post(**kwargs)
            return res
        except TimeoutError:
            self.log.error('timeout')
            return None
