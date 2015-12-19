# -*- coding: latin-1 -*-
import unittest

from tablereader import Excel
from base_test import BaseReaderTest

class TestXlsxFunctions(unittest.TestCase, BaseReaderTest):

    def setUp(self):
        self.data = Excel("test/data/nobel.xlsx")
        i = self.data.read()
        self.r1 = i.next()
        self.r2 = i.next()
        self.r3 = i.next()
        self.r4 = i.next()


if __name__ == '__main__':
    unittest.main()
