# -*- coding: latin-1 -*-
import unittest

from tablereader import Ods
from base_test import BaseReaderTest

class TestOdsFunctions(unittest.TestCase, BaseReaderTest):

    def setUp(self):
        self.data = Ods("test/data/nobel.ods")
        i = self.data.read()
        self.r1 = i.next()
        self.r2 = i.next()
        self.r3 = i.next()
        self.r4 = i.next()


if __name__ == '__main__':
    unittest.main()
