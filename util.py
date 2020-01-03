#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class AlgorithmTest(unittest.TestCase):
    def something(self, value, true_value):
        self.assertEqual(value, true_value)
