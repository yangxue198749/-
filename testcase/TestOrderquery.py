
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class orderquery(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_orderquery0(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.query", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "order_seq": "35336438", "sku_id": "3083", "sign": "d7aaada74a144de7a6536aba32963198"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_orderquery1(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "None", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "order_seq": "35336438", "sku_id": "3083", "sign": "5deeb7355e9ff41d2f36352379d34d78"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_orderquery2(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.query", "version": "None", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "order_seq": "35336438", "sku_id": "3083", "sign": "3db9510193002cfea9183ce504024557"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_orderquery3(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.query", "version": "v1", "customer_id": "None", "order_seq": "35336438", "sku_id": "3083", "sign": "c4f024330cd7ac28cbb8f7fe86614577"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_orderquery4(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.query", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "order_seq": "None", "sku_id": "3083", "sign": "961ded332a9202d34f6427961a10aca4"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_orderquery5(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.query", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "order_seq": "35336438", "sku_id": "None", "sign": "f6213e49904615f78a26d87a58828118"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

