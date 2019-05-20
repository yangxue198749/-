
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class vmstatus(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_vmstatus0(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.status", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "01000214", "sign": "790494468a93c84cc5881ad3e6dc9f27"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_vmstatus1(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "None", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "01000214", "sign": "f18b2d5078bf84b2f84229d482cc738f"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmstatus2(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.status", "version": "None", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "01000214", "sign": "2331ac0f1ab9330f52469c66b09b55b3"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmstatus3(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.status", "version": "v1", "customer_id": "None", "vm_code": "01000214", "sign": "f09be0f80566f222186d769271171143"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')


    def test_vmstatus4(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "vm.status", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "vm_code": "None", "sign": "4a2b282f1b9a9942efec8882428adc11"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

