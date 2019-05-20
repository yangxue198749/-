#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : ReadCofig.py
@Author: yangxue
@Date  : 2019/4/28 9:31
@Desc  : 
'''
import os
import configparser
from log import log


# pro_path=os.path.split(os.path.realpath(__file__))[0]
# cofig_path=os.path.join(pro_path,'\\config\\config.ini')
cofig_path='D:\\python\\interfacetest\\config\\config.ini'

l=log.log('redcofig','config.txt')

class ReadConfig:
    def __init__(self):
        self.conf=configparser.ConfigParser()
        # self.data=con.read(cofig_path)
        self.conf.read(cofig_path)

    def get_selection(self):
        try:
            self.selection=self.conf.sections()
        except Exception as e:
            print(e)
        return self.selection

    def get_opthion(self,name):
        try:
            self.opthions=self.conf.options(name)
        except Exception as e:
            print('get config opthion fail :',e)
        return self.opthions

    def get_item(self,name):
        self.data_dict={}
        try:
            self.items=self.conf.items(name)
            for k in self.items:
                self.data_dict[k[0]]=k[1]
            # l.info('get config item:%s'%self.data_dict)
        except Exception as e:
            l.error('get config fail :',e)
            print('get config fail :',e)
        return self.data_dict


# c=ReadConfig()
# data=c.get_item('socket')
# data1={}
# for k in data:
#     data1[k[0]]=k[1]
#     print(data1)
# # print([k for x in data for k in x])

