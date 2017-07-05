#coding: utf-8
import unittest
from django.template.defaultfilters import length
class Test(unittest.TestCase):
    def setUp(self):
        print 'setup...'
    def tearDown(self):
        print 'tearDown...'
    def test_first(self):
        d = {}
        print 'programm...'