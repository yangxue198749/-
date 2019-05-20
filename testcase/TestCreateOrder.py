

from core import myhttp
from core import ReadCofig
import unittest




class mytest(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_creatorder0(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "136098ca85d33a393a28bfc3d6ce021b", "start_day": "2019-04-17", "end_day": "2019-04-17", "version": "v1", "skus": [{"sku_id": "3418", "sku_count": "1"}], "vm_id": "01000002", "service": "order.create", "customer_id": "C6538261", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')

    def test_creatorder1(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "136098ca85d33a393a28bfc3d6ce021b", "start_day": "2019-04-17", "end_day": "2019-04-17", "version": "v1", "skus": [{"sku_id": "34180", "sku_count": "1"}], "vm_id": "01000002", "service": "order.create", "customer_id": "C6538261", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder2(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "66b94b5dd2478d90fd871e9f2253fc50", "start_day": "None", "end_day": "2018-12-03", "version": "v1", "skus": [{"sku_id": "3427", "sku_count": "1"}], "vm_id": "01000287", "service": "order.create", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder3(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "f224aa8b59253a752a098d1cd4e64269", "start_day": "2018-12-03", "end_day": "None", "version": "v1", "skus": [{"sku_id": "3427", "sku_count": "1"}], "vm_id": "01000287", "service": "order.create", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder4(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "e987090237397fe2536bf7e6d82977d7", "start_day": "2018-12-03", "end_day": "2018-12-03", "version": "None", "skus": [{"sku_id": "3427", "sku_count": "1"}], "vm_id": "01000287", "service": "order.create", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder5(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "e987090237397fe2536bf7e6d82977d7", "start_day": "2018-12-03", "end_day": "2018-12-03", "version": "None", "skus": [{"sku_id": "3427", "sku_count": "1"}], "vm_id": "01000287", "service": "order.create", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder6(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "6186200d642674ee3cf4d3b26497fee9", "start_day": "2018-12-03", "end_day": "2018-12-03", "version": "v1", "skus": "None", "vm_id": "01000287", "service": "order.create", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder7(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "d2776d170af0acd229ad7e17728e5a89", "start_day": "2018-12-03", "end_day": "2018-12-03", "version": "v1", "skus": [{"sku_id": "3427", "sku_count": "1"}], "vm_id": "None", "service": "order.create", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder8(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "74981757719b7556757031a8ed84b370", "start_day": "2018-12-03", "end_day": "2018-12-03", "version": "v1", "skus": [{"sku_id": "3427", "sku_count": "1"}], "vm_id": "01000287", "service": "None", "customer_id": "uH7eAtKmGNZ1Ngr0vWmh", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')

    def test_creatorder9(self):
        self.url=''.join(self.baseurl+'service')
        self.data='{"sign": "cf3b4a14549a6a9c609848e7acb25aeb", "start_day": "2018-12-03", "end_day": "2018-12-03", "version": "v1", "skus": [{"sku_id": "3427", "sku_count": "1"}], "vm_id": "01000287", "service": "order.create", "customer_id": "None", "order_type": "immediate"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'FAIL')
