# -*- coding: utf-8 -*-
# @Time    : 3/18/21 1:35 PM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : __init__.py
# @Software: PyCharm

import unittest


def get_tests():
    from .models_test import ModelsTestCase
    # from .serializer import ResourceTestCase as SerializerTestCase
    # from .utils import UtilsTestCase
    #
    modelssuite = unittest.TestLoader().loadTestsFromTestCase(ModelsTestCase)
    # serializersuite = unittest.TestLoader().loadTestsFromTestCase(SerializerTestCase)
    # utilssuite = unittest.TestLoader().loadTestsFromTestCase(UtilsTestCase)
    #
    return unittest.TestSuite([modelssuite])
