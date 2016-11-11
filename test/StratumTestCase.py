"""
PyStratum

Copyright 2015-2016 Set Based IT Consultancy

Licence MIT
"""
import sys
import unittest
from io import StringIO

from test.TestDataLayer import TestDataLayer


class StratumTestCase(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def setUp(self):
        TestDataLayer.connect('localhost', 'test', 'test', 'test', 'test')

        self.held, sys.stdout = sys.stdout, StringIO()

    # ------------------------------------------------------------------------------------------------------------------
    def tearDown(self):
        sys.stdout = self.held
        TestDataLayer.disconnect()

# ----------------------------------------------------------------------------------------------------------------------
