
from core import createtest
from core import myhttp
from core import ReadCofig
import unittest
from HTMLTestRunner import HTMLTestRunner



class nodedetail(unittest.TestCase):

    def setUp(self):
        obj = ReadCofig.ReadConfig()
        self.config=obj.get_item('http')
        self.baseurl=self.config['baseurl']
        self.post_obj=myhttp.myhttp()

    def tearDown(self):
        pass

    def test_nodedetail0(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "node.detail", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "node_id": "30240", "sign": "de2d9ebd360552991a80dfd01d7b2729"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'SUCCESS')


    def test_nodedetail1(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "None", "version": "v1", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "node_id": "30240", "sign": "6324c0bc7bb6f2d348ce43845003fd36"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'')


    def test_nodedetail2(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "node.detail", "version": "None", "customer_id": "v2dDGKGNn8pkoLcgUbWJ", "node_id": "30240", "sign": "b4c4569d9fe1c46f09b177126b02f47d"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'')


    def test_nodedetail3(self):
        self.url=''.join(self.baseurl+'server')
        self.data='{"service": "node.detail", "version": "v1", "customer_id": "None", "node_id": "30240", "sign": "2d2b4b249999fc18c61401d3a0fddb7a"}'
        res=self.post_obj.post(url=self.url,data=self.data)
        res=res.json()
        self.assertEqual(res['return_code'],'')

