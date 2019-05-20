
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class nodelist(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_nodelist0(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "node.list", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "sign": "f1a1c30871d7558d7eaf493eb2466531"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_nodelist1(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "None", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "sign": "5b1211c8db186022c51a934ce3930b44"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_nodelist2(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "node.list", "version": "None", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "sign": "69b653b296a00ca80399b07690abf172"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_nodelist3(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "node.list", "version": "v1", "customer_id": "None", "sign": "6a0408865336707eacffb7743098092c"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

