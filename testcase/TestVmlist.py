
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class vmlist(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_vmlist0(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.list", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "sign": "0bd77c1f268d41bd6aec9f43ac037dd3"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_vmlist1(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "None", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "sign": "5b1211c8db186022c51a934ce3930b44"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmlist2(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.list", "version": "None", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "sign": "32e3c5d1f0d87a36773e85bcdc97df41"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmlist3(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.list", "version": "v1", "customer_id": "None", "sign": "143d5c97fe5fff1ee36df250cc83be1b"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

