# -*- coding: latin-1 -*-
import unittest

from tablereader import Xls
from base_test import BaseReaderTest

class TestXlsFunctions(unittest.TestCase, BaseReaderTest):

    def setUp(self):
        self.data = Xls("data/nobel.xls")
        i = self.data.read()
        self.r1 = i.next()
        self.r2 = i.next()
        self.r3 = i.next()
        self.r4 = i.next()


if __name__ == '__main__':
    unittest.main()
