#!/usr/bin/env python

import os
import sys
import unittest

_HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, os.pardir)))

import ZakPackage._nani
from ZakPackage._numeric import Float32


_PY2 = sys.version_info[0] == 2


class NaniTest(unittest.TestCase):

    def test_basics(self):
        data_type = ZakPackage._nani.Bool(default=True)
        self.assertIsNotNone(ZakPackage._nani.resolve(data_type))

        data_type = ZakPackage._nani.Object(default=[])
        self.assertIsNotNone(ZakPackage._nani.resolve(data_type))

        data_type = ZakPackage._nani.Number(type=Float32, default=1.23)
        self.assertIsNotNone(ZakPackage._nani.resolve(data_type))

        if _PY2:
            data_type = ZakPackage._nani.String(length=8, default='abc')
            self.assertIsNotNone(ZakPackage._nani.resolve(data_type))
        else:
            data_type = ZakPackage._nani.Unicode(length=8, default='abc')
            self.assertIsNotNone(ZakPackage._nani.resolve(data_type))

        data_type = ZakPackage._nani.String(length=8, default=b'abc')
        self.assertIsNotNone(ZakPackage._nani.resolve(data_type))

        data_type = ZakPackage._nani.Unicode(length=8, default=u'abc')
        self.assertIsNotNone(ZakPackage._nani.resolve(data_type))

        data_type = ZakPackage._nani.Array(element_type=ZakPackage._nani.Number(), shape=1)
        self.assertIsNotNone(ZakPackage._nani.resolve(data_type))

        data_type = ZakPackage._nani.Structure(
            fields=(
                ('number', ZakPackage._nani.Number()),
            )
        )
        self.assertIsNotNone(ZakPackage._nani.resolve(data_type))


if __name__ == '__main__':
    from tests.run import run
    run('__main__')
