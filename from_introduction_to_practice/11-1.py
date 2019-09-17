#-*-coding:utf-8-*-
import unittest
from city_functions import city_country
class CityTestCase(unittest.TestCase):

    def test_cities(self):
        santiago_chile = city_country('santiago','chile','50000')
        self.assertEqual(santiago_chile,'Santiago, Chile - population 50000')
