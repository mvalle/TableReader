# -*- coding: latin-1 -*-
from reader.csv import Csv
import unittest

class TestCsvFunctions(unittest.TestCase):

    def setUp(self):
        self.csv = Csv("data/nobel.csv")

        self.r1 = self.csv.read().next()
        self.r2 = self.csv.read().next()
        self.r3 = self.csv.read().next()
        self.r4 = self.csv.read().next()
        
    def test_value_class(self):
        self.assertRaises(AttributeError, lambda : self.csv.Value.not_a_field == "")
        
        self.assertTrue('Chemistry' in dir(self.csv.Value))
        self.assertTrue('Economics' in dir(self.csv.Value))
        self.assertTrue('Literature' in dir(self.csv.Value))
        self.assertTrue('Peace' in dir(self.csv.Value))
        self.assertTrue('Physiology_or_Medicine' in dir(self.csv.Value))
        self.assertTrue('Year' in dir(self.csv.Value))

    def test_read_year(self):
        self.assertEqual(self.r1.Year, u"1901")
        self.assertEqual(self.r2.Year, u"1902")
        self.assertEqual(self.r3.Year, u"1903")
        self.assertEqual(self.r4.Year, u"1904")

    def test_read_physics(self):
        self.assertEqual(self.r1.Physics, u"Wilhelm Röntgen")
        self.assertEqual(self.r2.Physics, u"Hendrik Lorentz; Pieter Zeeman")
        self.assertEqual(self.r3.Physics, u"Henri Becquerel; Pierre Curie; Marie Curie")
        self.assertEqual(self.r4.Physics, u"The Lord Rayleigh")

    def test_read_chemistry(self):
        self.assertEqual(self.r1.Chemistry, u"Jacobus Henricus van 't Hoff")
        self.assertEqual(self.r2.Chemistry, u"Hermann Emil Fischer")
        self.assertEqual(self.r3.Chemistry, u"Svante Arrhenius")
        self.assertEqual(self.r4.Chemistry, u"William Ramsay")

    def test_physiology_or_medicine(self):
        self.assertEqual(self.r1.Physiology_or_Medicine, u"Emil Adolf von Behring")
        self.assertEqual(self.r2.Physiology_or_Medicine, u"Ronald Ross")
        self.assertEqual(self.r3.Physiology_or_Medicine, u"Niels Ryberg Finsen")
        self.assertEqual(self.r4.Physiology_or_Medicine, u"Ivan Pavlov")
        

if __name__ == '__main__':
    unittest.main()
