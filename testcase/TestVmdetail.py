
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class vmdetail(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_vmdetail0(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.detail", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "01000214", "sign": "720b4e4598db0be7f56041721f5bfd7f"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_vmdetail1(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "None", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "01000214", "sign": "f18b2d5078bf84b2f84229d482cc738f"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmdetail2(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.detail", "version": "None", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "01000214", "sign": "8b1d98771571801abcbdf8d3247c32a0"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmdetail3(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.detail", "version": "v1", "customer_id": "None", "vm_code": "01000214", "sign": "a81e5944ef242ad29b5c0a24e526b84f"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmdetail4(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.detail", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "None", "sign": "14090971185a947e32838f55e2de00ff"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

