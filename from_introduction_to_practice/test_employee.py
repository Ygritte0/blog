#-*-coding:utf-8-*-
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.andy = Employee('andy','green',150000)

    def test_give_default_raise(self):
        self.andy.give_raise()
        self.assertEqual(self.andy.annual_salary,155000)

    def test_give_custom_raise(self):
        self.andy.give_raise(10000)
        self.assertEqual(self.andy.annual_salary,160000)