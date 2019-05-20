
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class vendout(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_vendout0(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "order.vendout", "pay_amount": "999", "pay_type": "k\u652f\u4ed8", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "sign": "440660dd5a30e736ae0389905e2bf2e2", "order_seq": "35346902", "version": "v1", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_vendout1(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "None", "pay_amount": "999", "pay_type": "k\u652f\u4ed8", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "sign": "5017c5719c44915f9c1ed1983a23d1b6", "order_seq": "35346902", "version": "v1", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vendout2(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "order.vendout", "pay_amount": "None", "pay_type": "k\u652f\u4ed8", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "sign": "88741f1c48c6a9c234159b962ba7c1e4", "order_seq": "35346902", "version": "v1", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vendout3(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "order.vendout", "pay_amount": "999", "pay_type": "None", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "sign": "6c6feff49dc1cd9e7f1311bbbe97ad63", "order_seq": "35346902", "version": "v1", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vendout4(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "order.vendout", "pay_amount": "999", "pay_type": "k\u652f\u4ed8", "customer_id": "None", "sign": "bb7a6351f2ea26e991f1c4139dfc14aa", "order_seq": "35346902", "version": "v1", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vendout5(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "order.vendout", "pay_amount": "999", "pay_type": "k\u652f\u4ed8", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "sign": "440660dd5a30e736ae0389905e2bf2e2", "order_seq": "35346902", "version": "v1", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vendout6(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "order.vendout", "pay_amount": "999", "pay_type": "k\u652f\u4ed8", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "sign": "6b02c579141473bc42e13a605aaa6e26", "order_seq": "None", "version": "v1", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vendout7(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"service": "order.vendout", "pay_amount": "999", "pay_type": "k\u652f\u4ed8", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "sign": "3125045d6f0b18fa424e2b8085a4dd02", "order_seq": "35346902", "version": "None", "notify_url": "http://xxxxxxxxx/xxx"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

