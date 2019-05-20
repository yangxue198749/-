
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class orderextract(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_orderextract0(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.extract", "version": "v1.1", "customer_id": "C6538261", "detail_id": "35346993", "random_code": "f619b07c-e6c5-49a2-a224-586930909176", "sign": "486c19764835eacc0e6b053c67725707"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_orderextract1(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "None", "version": "v1.1", "customer_id": "C6538261", "detail_id": "35346993", "random_code": "f619b07c-e6c5-49a2-a224-586930909176", "sign": "909fd68d79862da186fb29d28f4e4a6a"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_orderextract2(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.extract", "version": "None", "customer_id": "C6538261", "detail_id": "35346993", "random_code": "f619b07c-e6c5-49a2-a224-586930909176", "sign": "3cabff7c5e53f88bbd3b40a79aa87375"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_orderextract3(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.extract", "version": "v1.1", "customer_id": "None", "detail_id": "35346993", "random_code": "f619b07c-e6c5-49a2-a224-586930909176", "sign": "f3c64615675c455ead8ecf8df08584ed"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_orderextract4(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "order.extract", "version": "v1.1", "customer_id": "C6538261", "detail_id": "None", "random_code": "f619b07c-e6c5-49a2-a224-586930909176", "sign": "e2d66f55309c89155499f776c6f820cb"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

